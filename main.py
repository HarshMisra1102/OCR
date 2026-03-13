"""
SmartChessAI
Pure UCI Entry Point

This file starts the engine in UCI mode.
Compatible with Arena, CuteChess, Banksia GUI, etc.
"""

from engine.uci import uci_loop


def main():
    uci_loop()


if __name__ == "__main__":
    main()