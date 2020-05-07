#!/usr/bin/env python3
import time
import sys
import random

from AppKit import NSSpeechSynthesizer

notes = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
]

modifiers = [
    "", "sharp", "flat"
]

qualities = [
    "major", "minor", "diminished", "augmented"
]

interval = 5
if len(sys.argv) > 1:
    try: 
        interval = int(sys.argv[1])
    except ValueError:
        print("interval {} is not a number, using default.".format(sys.argv[1]))
        pass

ss = NSSpeechSynthesizer.alloc().init()

while True:
    note = random.choice(notes)
    modifier = random.choice(modifiers)
    quality = random.choice(qualities)
    triad = "[[char LTRL]] " + note + " [[char NORM]] " + modifier + " " + quality
    ss.startSpeakingString_(triad)
    time.sleep(interval)