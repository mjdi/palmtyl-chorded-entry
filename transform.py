from enum import Enum

class Hand (Enum):
    LEFT = 0
    RIGHT = 1

class ChordPart (Enum):
    FINGER = 0
    THUMB = 1
    PALM = 2

HAND_KEY = "hand"
CHORD_PART_KEY = "chord_part"
CHORD_KEY = "chord_key"

PALM_SHIFT_KEY = "palm shift"
PALM_NO_SPACE_KEY = "palm no space"
PALM_DISAMGUATE_KEY = "palm disambiguate"
PALM_PLURAL_KEY = "palm plural"


convert_uppercase_punctuation_to_lowercase = {
    '_' : '-',
    '+' : '=',
    '"' : "'",
    '|' : '\\',
    '<' : ',',
    '>' : '.',
    '?' : '/',
    ':' : ';',
}
    

transform = {
    "tab" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "j"},
    "q" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "k"},
    "w" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "d"},
    "f" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "l"},
    "p" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "f"},
    "b" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "b"},
    "j" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "b"},
    "l" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "f"},
    "u" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "l"},
    "y" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "d"},
    "-" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "k"},
    "=" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "j"},
    "esc" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "v"},
    "a" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "s"},
    "r" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "n"},
    "s" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "r"},
    "t" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "t"},
    "g" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "p"},
    "m" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "p"},
    "n" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "t"},
    "e" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "r"},
    "i" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "n"},
    "o" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "s"},
    "'" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "v"},
    "\\" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "x"},
    "z" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "c"},
    "x" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "w"},
    "c" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "m"},
    "d" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "h"},
    "v" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "g"},
    "k" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "g"},
    "h" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "h"},
    "," : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "m"},
    "." : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "w"},
    "/" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "c"},
    ";" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.FINGER, CHORD_KEY : "x"},
    "backspace" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.THUMB, CHORD_KEY : "e"},
    "insert" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.THUMB, CHORD_KEY : "a"},
    "delete" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.THUMB, CHORD_KEY : "o"},
    "caps lock" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.THUMB, CHORD_KEY : "a"},
    "space" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.THUMB, CHORD_KEY : "e"},
    "enter" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.THUMB, CHORD_KEY : "o"},
    "ctrl" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.PALM, CHORD_KEY : PALM_SHIFT_KEY},
    "shift" : { HAND_KEY : Hand.LEFT, CHORD_PART_KEY: ChordPart.PALM, CHORD_KEY : PALM_NO_SPACE_KEY},
    "right shift" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.PALM, CHORD_KEY : PALM_DISAMGUATE_KEY},
    "right ctrl" : { HAND_KEY : Hand.RIGHT, CHORD_PART_KEY: ChordPart.PALM, CHORD_KEY : PALM_PLURAL_KEY},
}
