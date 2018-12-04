# ----------------------------------------------------------------------
#  eliza.py
#
#  a cheezy little Eliza knock-off by Joe Strout
#  with some updates by Jeff Epler
#  hacked into a module and updated by Jez Higgins
#
#  Available under MIT licence from https://github.com/jezhiggins/eliza.py
#  This version further tweaked by Zac Hatfield-Dodds.
# ----------------------------------------------------------------------

import json
import re
import random
import string
import time


with open("simpledoctor.json") as f:
    # PATERNS is a list of (regex, [several responses]) pairs.
    PATTERNS = json.load(f)


def translate(str_):
    """Replace any words found in the reflections dict with their
    corresponding value, e.g. 'I am' --> 'you are'."""
    reflections = {
        "am": "are",
        "was": "were",
        "i": "you",
        "i'd": "you would",
        "i've": "you have",
        "i'll": "you will",
        "my": "your",
        "are": "am",
        "you've": "I have",
        "you'll": "I will",
        "your": "my",
        "yours": "mine",
        "you": "me",
        "me": "you",
    }
    return " ".join(reflections.get(word, word) for word in str_.lower().split())


def respond(str_):
    """Take a string input, match it against one of the PATTERNS,
    and complete then return one of the corresponding responses.
    """
    # find a match among keys
    for pattern, responses in PATTERNS:
        match = re.match(pattern, str_)
        if match:
            # found a match ... stuff with corresponding value
            # chosen randomly from among the available options
            resp = random.choice(responses)
            # we've got a response... stuff in reflected text where indicated
            pos = resp.find("%")
            while pos > -1:
                num = int(resp[pos + 1 : pos + 2])
                resp = resp[:pos] + translate(match.group(num)) + resp[pos + 2 :]
                pos = resp.find("%")
            # fix munged punctuation at the end
            if resp[-2:] == "?.":
                resp = resp[:-2] + "."
            if resp[-2:] == "??":
                resp = resp[:-2] + "?"
            return resp


# ----------------------------------------------------------------------
#  command_interface
# ----------------------------------------------------------------------
def command_interface():
    print("Therapist\n---------")
    print("Talk to the program by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.  Enter "quit" when done.')
    print("=" * 72)
    print("Hello.  How are you feeling today?")

    s = ""
    while s != "quit":
        try:
            s = input("> ")
        except EOFError:
            s = "quit"
        time.sleep(random.uniform(0.1, 0.4))
        print(respond(s.rstrip("!.")))


if __name__ == "__main__":
    command_interface()
