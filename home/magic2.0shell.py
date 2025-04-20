#!/usr/bin/env python3
import cmd
import shlex
import time
import sys

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

class MagicShell(cmd.Cmd):
    intro = f"{CYAN}Atlantis Magic Shell v1.0 – Type 'help' for commands.{RESET}"
    prompt = f"{YELLOW}≫ {RESET}"

    def do_levi(self, arg):
        """levi <objekto>  – Levitate an object."""
        args = shlex.split(arg)
        if args:
            print(f"{GREEN}✨ Levating '{args[0]}' into the air! ✨{RESET}")
        else:
            print(f"{YELLOW}Error: Missing object to levitate.{RESET}")

    def do_flugi(self, arg):
        """flugi – Fly through the air."""
        print(f"{GREEN}🕊️ You rise off the ground and soar! 🕊️{RESET}")

    def do_radi​on(self, arg):
        """radion de <ruĝa|varmo> – Project a ray of light or heat."""
        args = shlex.split(arg)
        if args:
            print(f"{GREEN}🔥 Casting ray of '{' '.join(args)}'! 🔥{RESET}")
        else:
            print(f"{YELLOW}Error: Specify ray type ('ruĝa lumo' or 'varmo').{RESET}")

    def do_persona(self, arg):
        """persona ŝildo – Erect a personal shield."""
        if arg.strip().startswith("ŝildo"):
            print(f"{GREEN}🛡️ A shimmering shield surrounds you! 🛡️{RESET}")
        else:
            print(f"{YELLOW}Unknown persona command.{RESET}")

    def do_bamf(self, arg):
        """bamf – Teleport with nightcrawler-style effect."""
        print(f"{GREEN}💨 *BAMF*! You vanish and reappear instantly! 💨{RESET}")

    def default(self, line):
        print(f"{YELLOW}Error: Unknown command '{line.split()[0]}'.{RESET}")

    def do_exit(self, arg):
        """exit – Leave the Magic Shell."""
        print("Farewell, wizard.")
        return True

if __name__ == "__main__":
    try:
        MagicShell().cmdloop()
    except KeyboardInterrupt:
        sys.exit("\nInterrupted. Goodbye.")
