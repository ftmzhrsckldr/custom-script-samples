#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]

    if not args:
        print("No arguments received.")
        sys.exit(1)

    print(f"Received {len(args)} arguments.")
    for i, arg in enumerate(args, start=1):
        print(f"Arg {i}: '{arg}'")

    print("All arguments processed successfully.")

if __name__ == "__main__":
    main()
