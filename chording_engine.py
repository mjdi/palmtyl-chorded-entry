import keyboard
from transform import *
from enum import Enum

class State (Enum):
    CHORDING_OFF = 0
    CHORDING_ON = 1

LEFT_HAND_CHORDING_TOGGLE_KEY = "insert"
RIGHT_HAND_CHORDING_TOGGLE_KEY = "caps lock"

SUPER_VOWELS_LIST = [
    'you',
    'eye',
    'aye',
    'eau',
    'eou',
    'iou',
    'uou',
    'eue',
]

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


    def determine_beginning_consonants(self):
        
        if 'k' in self.biggest_left_hand_finger_keys_set and 'd' in self.biggest_left_hand_finger_keys_set:
            self.biggest_left_hand_finger_keys_set.remove('k')
            self.biggest_left_hand_finger_keys_set.remove('d')
            self.biggest_left_hand_finger_keys_set.add('q')

        if 'c' in self.biggest_left_hand_finger_keys_set and 'w' in self.biggest_left_hand_finger_keys_set:
            self.biggest_left_hand_finger_keys_set.remove('c')
            self.biggest_left_hand_finger_keys_set.remove('w')
            self.biggest_left_hand_finger_keys_set.add('z')

        if len(self.biggest_left_hand_finger_keys_set) == 0:
            return ''

        expected_order = 'jdsvxpmgkncqzwthbflr'

        for key in expected_order:
            if key not in self.biggest_left_hand_finger_keys_set:
                expected_order = expected_order.replace(key, '')

        return expected_order
    

    def determine_left_vowels(self):

        if len(self.biggest_left_hand_thumb_keys_set) == 3:
            return SUPER_VOWELS_LIST[0]

        elif len(self.biggest_left_hand_thumb_keys_set) == 2:
            if 'e' in self.biggest_left_hand_thumb_keys_set and 'a' in self.biggest_left_hand_thumb_keys_set:
                return 'i'
            elif 'e' in self.biggest_left_hand_thumb_keys_set and 'o' in self.biggest_left_hand_thumb_keys_set:
                return 'u'
            elif 'a' in self.biggest_left_hand_thumb_keys_set and 'o' in self.biggest_left_hand_thumb_keys_set:
                return 'y'
        elif len(self.biggest_left_hand_thumb_keys_set) == 1:
            return self.biggest_left_hand_thumb_keys_set.pop()
        
        else: # this will mean some shorthand likely
            return '' 
    

    def determine_right_vowels(self):
            
        if len(self.biggest_right_hand_thumb_keys_set) == 3:
            return SUPER_VOWELS_LIST[0]

        elif len(self.biggest_right_hand_thumb_keys_set) == 2:
            if 'e' in self.biggest_right_hand_thumb_keys_set and 'a' in self.biggest_right_hand_thumb_keys_set:
                return 'i'
            elif 'e' in self.biggest_right_hand_thumb_keys_set and 'o' in self.biggest_right_hand_thumb_keys_set:
                return 'u'
            elif 'a' in self.biggest_right_hand_thumb_keys_set and 'o' in self.biggest_right_hand_thumb_keys_set:
                return 'y'
        elif len(self.biggest_right_hand_thumb_keys_set) == 1:
            return self.biggest_right_hand_thumb_keys_set.pop()
        
        else: # this will mean some shorthand likely
            return ''

    def determine_ending_consonants(self):

        if 'k' in self.biggest_right_hand_finger_keys_set and 'd' in self.biggest_right_hand_finger_keys_set:
            self.biggest_right_hand_finger_keys_set.remove('k')
            self.biggest_right_hand_finger_keys_set.remove('d')
            self.biggest_right_hand_finger_keys_set.add('q')

        if 'c' in self.biggest_right_hand_finger_keys_set and 'w' in self.biggest_right_hand_finger_keys_set:
            self.biggest_right_hand_finger_keys_set.remove('c')
            self.biggest_right_hand_finger_keys_set.remove('w')
            self.biggest_right_hand_finger_keys_set.add('z')

        
        if len(self.biggest_right_hand_finger_keys_set) == 0:
            return ''

        expected_order = 'rlmpbwnsvfdgckxthzjq'

        for key in expected_order:
            if key not in self.biggest_right_hand_finger_keys_set:
                expected_order = expected_order.replace(key, '')

        return expected_order
    


    def translate_biggest_sets_to_chorded_entry(self):
        
        word_part = self.determine_beginning_consonants() + self.determine_left_vowels()

        if PALM_DISAMGUATE_KEY in self.biggest_right_hand_palm_keys_set:
            # TODO: disambiguate
            word_part = word_part + self.determine_ending_consonants() + self.determine_right_vowels()
        else:
            word_part = word_part + self.determine_right_vowels() + self.determine_ending_consonants()

        if PALM_SHIFT_KEY in self.biggest_left_hand_palm_keys_set:
            word_part = word_part[0].upper() + word_part[1:]

        if PALM_PLURAL_KEY in self.biggest_right_hand_palm_keys_set:
            if word_part[-1] == 's' or word_part[-1] == 'x' or word_part[-1] == 'z' or word_part[-2:] == 'ch' or \
                word_part[-2:] == 'sh' or word_part[-1] == 'o': 
                word_part = word_part + 'es'
            else:
                word_part = word_part + 's' 

        if PALM_NO_SPACE_KEY not in self.biggest_left_hand_palm_keys_set:
            word_part = word_part + ' '

        return word_part


    def reset_biggest_sets(self):
        self.biggest_left_hand_finger_keys_set = set()
        self.biggest_right_hand_finger_keys_set = set()
        self.biggest_left_hand_thumb_keys_set = set()
        self.biggest_right_hand_thumb_keys_set = set()
        self.biggest_left_hand_palm_keys_set = set()
        self.biggest_right_hand_palm_keys_set = set()


    def handle_chording_and_return_state(self, event):

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
            
            word_part = self.translate_biggest_sets_to_chorded_entry()

            print(word_part)
            keyboard.write(word_part)

            self.reset_biggest_sets()

        elif len(self.biggest_left_hand_thumb_keys_set) == 1 and len(self.biggest_right_hand_thumb_keys_set) == 1:
            if list(self.biggest_left_hand_thumb_keys_set)[0] == LEFT_HAND_CHORDING_TOGGLE_KEY and \
                list(self.biggest_right_hand_thumb_keys_set)[0] == RIGHT_HAND_CHORDING_TOGGLE_KEY:
                self.reset_biggest_sets()
                print("CHORDING OFF") 
                return State.CHORDING_OFF

        return State.CHORDING_ON


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
            if event.name in non_chording_keys_pressed:
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
            state = chordparser.handle_chording_and_return_state(event)
            #print(repr(chordparser))
        else:
            if event.event_type == 'down':
                keyboard.send(event.name, event.event_type)


if __name__ == '__main__':

    keyboard.hook(on_key, suppress=True)
    
    keyboard.wait(100000)
   