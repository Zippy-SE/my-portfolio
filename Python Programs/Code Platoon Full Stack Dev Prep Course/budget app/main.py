#!/usr/bin/env python3
import sys
import os

# Ensure imports resolve when running from any directory
sys.path.insert(0, os.path.dirname(__file__))

from cli import CLI


def main():
    try:
        CLI().run()
    except KeyboardInterrupt:
        print("\n\nExiting. Budget saved.")
        sys.exit(0)


if __name__ == "__main__":
    main()
