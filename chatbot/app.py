import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load pretrained DialoGPT model & tokenizer
model_name = "microsoft/DialoGPT-medium"          # you can also try "-small" (faster) or "-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Keep chat history (simple list of strings)
chat_history_ids = None

def chat_with_bot(user_message, history):
    global chat_history_ids

    # Encode the new user input + add end-of-sentence token
    new_input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors='pt')

    # Append to history if exists
    bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids

    # Generate reply (greedy for simplicity; can add sampling later)
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,          # ← makes replies more varied
        top_p=0.95,
        top_k=60,
        temperature=0.75
    )

    # Decode only the new reply (skip input part)
    reply_ids = chat_history_ids[:, bot_input_ids.shape[-1]:][0]
    reply = tokenizer.decode(reply_ids, skip_special_tokens=True)

    # Update Gradio history format
    history.append((user_message, reply))
    return "", history   # clear input box, return updated history


# Gradio interface
with gr.Blocks(title="Simple DialoGPT Chatbot") as demo:
    gr.Markdown("# Basic Pretrained Chatbot (DialoGPT-medium)")
    gr.Markdown("Just type and press Enter. Type 'quit' or 'bye' to stop.")

    chatbot = gr.Chatbot(height=500)
    msg = gr.Textbox(placeholder="Type your message here...", label="You")
    clear = gr.Button("Clear Chat")

    msg.submit(chat_with_bot, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()