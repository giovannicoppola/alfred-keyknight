# Thursday, October 10, 2024
import json
import sys
import os

MY_INPUT = sys.argv[2] if len(sys.argv) > 2 else None
MYMODE = sys.argv[1]
SPACING = int(os.path.expanduser(os.getenv('SPACING', '')))
LEFT_PAD = int(os.path.expanduser(os.getenv('LEFT_PAD', '')))
WF_PATH = os.getenv('alfred_preferences')
WF_BUNDLE = os.getenv('alfred_workflow_bundleid')
SYMBOL_SET = "keycap"



def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)



def format_string(myString, target_char=None):
    # Define the string 'qwerty'
    chars = list(myString)
    
    # If the user has provided a target character, add '|' around it
    if target_char in chars:
        chars = [f"|{char}|" if char == target_char else char for char in chars]
    
    # Join the characters with two spaces
    return '  '.join(chars)


def addItem (myString, myResults):

    myResults["items"].append ({
            "title": myString.upper(),
            'subtitle': "",
            'valid': True,
            "quicklookurl": f'{WF_PATH}/workflows/{WF_BUNDLE}/touch-typing-keyboard.png',
            "mods": {
                    "alt": {
                        "valid": False,
                        "arg": "",
                        "subtitle": ""
                        },
                     "ctrl": {
                        "valid": False,
                        "arg": "",
                        "subtitle":""
                        },
                    "cmd": {
                        "valid": True,
                        "arg": "",
                        "subtitle": ""
                            },
                    "cmd+alt": {
                            "valid": True,
                            "arg": "",
                            "subtitle": ""
                    }
                },
                "icon": {
                    "path": 'icons/none.png'
                },
                'arg': "resultString"
            }) 
    return myResults

def defineDict ():
    keysDict = {
        "row0": {"`": 5,
                 "1": 5, "2": 4, "3": 3, "4": 2, "5": 2, "6": 2, "7": 2, "8": 3, "9": 4, "0": 5, "-": 5, "=": 5},
        "row1": {"q": 5, "w": 4, "e": 3, "r": 2, "t": 2, "y": 2, "u": 2, "i": 3, "o": 4, "p": 5, "[": 5, "]": 5},
        "row2": {"a": 5, "s": 4, "d": 3, "f": 2, "g": 2, "h": 2, "j": 2, "k": 3, "l": 4, ";": 5, "'": 5},
        "row3": {"z": 5, "x": 4, "c": 3, "v": 2, "b": 2, "n": 2, "m": 2, ",": 3, ".": 4, "/": 5}
    }

    dvorakDict = {
        'row0': {"1":5,"2":4,"3":3,"4":2,"5":2,"6":2,"7":2,"8":3,"9":4,"0":5,"'":5,",":5,".":5},
        'row1': {"p":2,"y":2,"f":2,"g":2,"c":3,"r":4,"l":5},
        'row2': {"/":2,"=":3,"a":4,"o":3,"e":2,"u":2,"i":2,"d":2,"h":3,"t":4,"n":5,"s":5,"-":5},
        'row4': {";":5,"q":5,"j":5,"k":5,"x":5,"b":5,"m":5,"w":5,"v":5,"z":5}
    }


    return keysDict


def format_keycap_for_character(keysDict, character):
    result = []
    
   
    for row, key_values in keysDict.items():
        if character in key_values:
            num = key_values[character]
            emoji = keycap_emoji[num]
            result.append(f"{emoji}{character}")  # Add emoji next to character
        else:
            # Add the key without the emoji
            result.append(character)
    
    return '  '.join(result)

# def format_rows(keysDict):
#     keycap_emoji = {
#     1: "1️⃣", 2: "2️⃣", 3: "③", 4: "4️⃣", 5: "5️⃣", 6: "⑤"
#     #1: "1️⃣", 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣", 6: "6️⃣"
#     }
    
#     formatted_output = {}
    
#     for row, key_values in keysDict.items():
#         formatted_output[row] = '  '.join(f"{keycap_emoji[num]}{key}{keycap_emoji[num]}" for key, num in key_values.items())
#         # Add the emoji only before the character
#         formatted_output[row] = '    '.join(f"{keycap_emoji[num]}{key}" for key, num in key_values.items())
#         # Create the left and right hand portions
#         left_hand = '  '.join(f"{keycap_emoji[num]}{key}" for key, num in key_values.items() if key in "`qwertasdfgzxcvb12345")
#         right_hand = '  '.join(f"{keycap_emoji[num]}{key}" for key, num in key_values.items() if key in "yuiophjklnm67890-=[];'./")
        
#         # Add extra space between the two hands
#         formatted_output[row] = left_hand + "              " + right_hand  # Extra spaces between the hands
    
    
#     return formatted_output

def chooseEmoj (EMOJI_SET):
    keycap_emoji = {
    1: "1️⃣", 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣"
    }
    keycap_circled = {
    1: "️⓵", 2: "⓶", 3: "③", 4: "️⓸", 5: "️⑤"
    }
     
    keycap_full = {
    1: "️⓵", 2: "⓶", 3: "③", 4: "️⓸", 5: "️⑤"
    }
    return keycap_emoji

def format_rows_with_emoji(keysDict, myMode, keycap_emoji, character=None):
    formatted_output = {}
 
    for row, key_values in keysDict.items():
        # Create the left and right hand portions
        left_hand = []
        right_hand = []
        if row != "row0":
            extraSpace = (' '* SPACING*2)
        else:
            extraSpace = ''
        if character or myMode == 'hidden':
            
            for key, num in key_values.items():
                if key in list(character):  # Check if the key matches the user input
                    formatted_key = f"{key}{keycap_emoji[num]}"  # Add emoji next to the character
                else:
                    formatted_key = f"{key}"  # Just add the key normally
                # Separate keys into left and right hands
                if key in "`qwertasdfgzxcvb12345":
                    left_hand.append(formatted_key)
                else:
                    right_hand.append(formatted_key)
        elif myMode == 'map':
            for key, num in key_values.items():
                formatted_key = f"{key}{keycap_emoji[num]}"  # Add emoji next to the character
                  # Separate keys into left and right hands
                if key in "`qwertasdfgzxcvb12345":
                    left_hand.append(formatted_key)
                else:
                    right_hand.append(formatted_key)

        # Join hands with appropriate spacing
        formatted_output[row] = (' ' * LEFT_PAD) + extraSpace + (' '* SPACING).join(left_hand) + (" " * SPACING*3) + (' '* SPACING).join(right_hand)  # Extra spaces between hands
    
    return formatted_output

def main():
    result = {"items": []}

    keysDict = defineDict()
    keycap_emoji = chooseEmoj(SYMBOL_SET)
    # Get the formatted rows
    # if MYMODE == "map":
    #     formatted_rows = format_rows(keysDict)
    # elif MYMODE == "hidden":

        # formatted_rows = format_rows(keysDict)
    formatted_rows = format_rows_with_emoji(keysDict, MYMODE, keycap_emoji, MY_INPUT)

    # Print the output for each row
    for row, formatted_string in formatted_rows.items():
        result = addItem(formatted_string, result)

    print(json.dumps(result))

if __name__ == "__main__":
    main()


