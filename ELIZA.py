#! python3
"""
A simple program similar to the famous ELIZA.
"""

import argparse
import re
import string


def respond_to(script, statement):
    """Return the response to a single input from the user."""
    return statement + "?"


def main(script_file):
    """The algorithm that *is* ELIZA."""
    with open(script_file) as f:
        script = f.read()
    print("HOW DO YOU DO. PLEASE TELL ME YOUR PROBLEM")
    while True:
        # Get capitalised input, then keep only letters and spaces
        from_user = input("> ").upper()
        from_user = re.sub(r"[^\s\w]", "", from_user, 999).strip()
        if from_user in ("", "EXIT", "QUIT"):
            print("GOODBYE")
            break
        print(respond_to(script, from_user))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(allow_abbrev=False, description=__doc__)
    parser.add_argument("--script", help="The filename of an ELIZA script file.")
    script = parser.parse_args().script or "DOCTOR.txt"
    main(script)
