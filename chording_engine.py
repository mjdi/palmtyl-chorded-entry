import keyboard
from transform import *
from enum import Enum

class State (Enum):
    CHORDING_OFF = 0
    CHORDING_ON = 1

LEFT_HAND_CHORDING_TOGGLE_KEY = "insert"
RIGHT_HAND_CHORDING_TOGGLE_KEY = "caps lock"

state = State.CHORDING_OFF
non_chording_keys_pressed = set()

class ChordParser():

    def __init__(self):
        self.left_hand_finger_keys_pressed = set()
        self.biggest_left_hand_finger_keys_set = set()
        self.right_hand_finger_keys_pressed = set()
        self.biggest_right_hand_finger_keys_set = set()
        self.left_hand_palm_keys_pressed = set()
        self.biggest_left_hand_thumb_keys_set = set()
        self.right_hand_palm_keys_pressed = set()
        self.biggest_right_hand_thumb_keys_set = set()
        self.left_hand_thumb_keys_pressed = set()
        self.biggest_left_hand_palm_keys_set = set()
        self.right_hand_thumb_keys_pressed = set()
        self.biggest_right_hand_palm_keys_set = set()

    def __repr__(self):
        return "left hand finger: " + str(self.left_hand_finger_keys_pressed) + "\n" + \
            "biggest left hand finger: " + str(self.biggest_left_hand_finger_keys_set) + "\n" + \
            "right hand finger: " + str(self.right_hand_finger_keys_pressed) + "\n" + \
            "biggest right hand finger: " + str(self.biggest_right_hand_finger_keys_set) + "\n" + \
            "left hand thumb: " + str(self.left_hand_thumb_keys_pressed) + "\n" + \
            "biggest left hand thumb: " + str(self.biggest_left_hand_thumb_keys_set) + "\n" + \
            "right hand thumb: " + str(self.right_hand_thumb_keys_pressed) + "\n" + \
            "biggest right hand thumb: " + str(self.biggest_right_hand_thumb_keys_set) + "\n" + \
            "left hand palm: " + str(self.left_hand_palm_keys_pressed) + "\n" + \
            "biggest left hand palm: " + str(self.biggest_left_hand_palm_keys_set) + "\n" + \
            "right hand palm: " + str(self.right_hand_palm_keys_pressed) + "\n" + \
            "biggest right hand palm: " + str(self.biggest_right_hand_palm_keys_set)

    def reset_biggest_sets(self):
        self.biggest_left_hand_finger_keys_set = set()
        self.biggest_right_hand_finger_keys_set = set()
        self.biggest_left_hand_thumb_keys_set = set()
        self.biggest_right_hand_thumb_keys_set = set()
        self.biggest_left_hand_palm_keys_set = set()
        self.biggest_right_hand_palm_keys_set = set()

    def handle_chording(self, event):

        transform_info = transform[event.name]

        if event.event_type == 'down':
            if transform_info[HAND_KEY] == Hand.LEFT:
                if transform_info[CHORD_PART_KEY] == ChordPart.FINGER:
                    self.left_hand_finger_keys_pressed.add(transform_info[CHORD_KEY])
                    self.biggest_left_hand_finger_keys_set.add(transform_info[CHORD_KEY])
                elif transform_info[CHORD_PART_KEY] == ChordPart.THUMB:
                    self.left_hand_thumb_keys_pressed.add(transform_info[CHORD_KEY])
                    self.biggest_left_hand_thumb_keys_set.add(transform_info[CHORD_KEY])
                elif transform_info[CHORD_PART_KEY] == ChordPart.PALM:
                    self.left_hand_palm_keys_pressed.add(transform_info[CHORD_KEY])
                    self.biggest_left_hand_palm_keys_set.add(transform_info[CHORD_KEY])
            elif transform_info[HAND_KEY] == Hand.RIGHT:
                if transform_info[CHORD_PART_KEY] == ChordPart.FINGER:
                    self.right_hand_finger_keys_pressed.add(transform_info[CHORD_KEY])
                    self.biggest_right_hand_finger_keys_set.add(transform_info[CHORD_KEY])
                elif transform_info[CHORD_PART_KEY] == ChordPart.THUMB:
                    self.right_hand_thumb_keys_pressed.add(transform_info[CHORD_KEY])
                    self.biggest_right_hand_thumb_keys_set.add(transform_info[CHORD_KEY])
                elif transform_info[CHORD_PART_KEY] == ChordPart.PALM:
                    self.right_hand_palm_keys_pressed.add(transform_info[CHORD_KEY])
                    self.biggest_right_hand_palm_keys_set.add(transform_info[CHORD_KEY])
        else:
            if transform_info[HAND_KEY] == Hand.LEFT:
                if transform_info[CHORD_PART_KEY] == ChordPart.FINGER:
                    self.left_hand_finger_keys_pressed.remove(transform_info[CHORD_KEY])
                elif transform_info[CHORD_PART_KEY] == ChordPart.THUMB:
                    self.left_hand_thumb_keys_pressed.remove(transform_info[CHORD_KEY])
                elif transform_info[CHORD_PART_KEY] == ChordPart.PALM:
                    self.left_hand_palm_keys_pressed.remove(transform_info[CHORD_KEY])
            elif transform_info[HAND_KEY] == Hand.RIGHT:
                if transform_info[CHORD_PART_KEY] == ChordPart.FINGER:
                    self.right_hand_finger_keys_pressed.remove(transform_info[CHORD_KEY])
                elif transform_info[CHORD_PART_KEY] == ChordPart.THUMB:
                    self.right_hand_thumb_keys_pressed.remove(transform_info[CHORD_KEY])
                elif transform_info[CHORD_PART_KEY] == ChordPart.PALM:
                    self.right_hand_palm_keys_pressed.remove(transform_info[CHORD_KEY])

        if len(self.left_hand_finger_keys_pressed) == 0 and len(self.right_hand_finger_keys_pressed) == 0 and \
            len(self.left_hand_thumb_keys_pressed) == 0 and len(self.right_hand_thumb_keys_pressed) == 0 and \
            len(self.left_hand_palm_keys_pressed) == 0 and len(self.right_hand_palm_keys_pressed) == 0:
            
            print(self.biggest_left_hand_palm_keys_set, self.biggest_right_hand_palm_keys_set, \
                  self.biggest_left_hand_finger_keys_set, self.biggest_left_hand_thumb_keys_set, \
                  self.biggest_right_hand_thumb_keys_set, self.biggest_right_hand_finger_keys_set \
            )
            
            self.reset_biggest_sets()


chordparser = ChordParser()

# main callback
def on_key(event):

    global state
    global non_chording_keys_pressed
    global chordparser

    if state == State.CHORDING_OFF:
        if event.event_type == 'down':
            non_chording_keys_pressed.add(event.name)
        else:
            non_chording_keys_pressed.remove(event.name)

        # insert + caps lock = chording on
        if LEFT_HAND_CHORDING_TOGGLE_KEY in non_chording_keys_pressed and \
            RIGHT_HAND_CHORDING_TOGGLE_KEY in non_chording_keys_pressed:
            non_chording_keys_pressed.remove(LEFT_HAND_CHORDING_TOGGLE_KEY)
            non_chording_keys_pressed.remove(RIGHT_HAND_CHORDING_TOGGLE_KEY)

            left_transform_info = transform[LEFT_HAND_CHORDING_TOGGLE_KEY]
            chordparser.left_hand_thumb_keys_pressed.add(left_transform_info[CHORD_KEY])
            right_transform_info = transform[RIGHT_HAND_CHORDING_TOGGLE_KEY]
            chordparser.right_hand_thumb_keys_pressed.add(right_transform_info[CHORD_KEY])

            state = State.CHORDING_ON
            print("CHORDING ON")
            return
        
        # otherwise, just send the key
        if event.event_type == 'down':
           keyboard.send(event.name, event.event_type)
    else:

        # account for shifted alphas by
        key_name = event.name 

        if len(key_name) == 1:
            if key_name in convert_uppercase_punctuation_to_lowercase:
                key_name = convert_uppercase_punctuation_to_lowercase[key_name]
            else:
                key_name = key_name.lower()

        if key_name in transform:
            event.name = key_name
            chordparser.handle_chording(event)
            #print(repr(chordparser))
        else:
            if event.event_type == 'down':
                keyboard.send(event.name, event.event_type)


if __name__ == '__main__':

    keyboard.hook(on_key, suppress=True)
    
    keyboard.wait(100000)
   