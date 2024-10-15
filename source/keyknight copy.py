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
SYMBOL_SET = os.path.expanduser(os.getenv('SYM_SERIES', ''))
LAYOUT = os.path.expanduser(os.getenv('LAYOUT', ''))



def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)




def addItem (myString, myResults):

    myResults["items"].append ({
            "title": myString.upper(),
            'subtitle': "",
            'valid': True,
            "quicklookurl": f'{WF_PATH}/workflows/{WF_BUNDLE}/icons/{LAYOUT}.png',
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

def chooseKeyboard (LAYOUT):
    if LAYOUT == "qwerty":
        keybLayout = {
            "layout" : {
                "row0": {"`": 5,
                        "1": 5, "2": 4, "3": 3, "4": 2, "5": 2, "6": 2, "7": 2, "8": 3, "9": 4, "0": 5, "-": 5, "=": 5},
                "row1": {"q": 5, "w": 4, "e": 3, "r": 2, "t": 2, "y": 2, "u": 2, "i": 3, "o": 4, "p": 5, "[": 5, "]": 5},
                "row2": {"a": 5, "s": 4, "d": 3, "f": 2, "g": 2, "h": 2, "j": 2, "k": 3, "l": 4, ";": 5, "'": 5},
                "row3": {"z": 5, "x": 4, "c": 3, "v": 2, "b": 2, "n": 2, "m": 2, ",": 3, ".": 4, "/": 5}},
            "lefthand": "`12345qwertasdfgzxcvb",
            "righthand": "567890-=yuioph"
        }
    elif LAYOUT == "dvorak":
        keybLayout = {
            "layout": {
                'row0': {"1":5,"2":4,"3":3,"4":2,"5":2,"6":2,"7":2,"8":3,"9":4,"0":5,"[":5,"]":5},
                'row1': {"'":5,",":4,".":3,"p":2,"y":2,"f":2,"g":2,"c":3,"r":4,"l":5,"/":5,"=":5},
                'row2': {"a":5,"o":4,"e":3,"u":2,"i":2,"d":2,"h":2,"t":3,"n":4,"s":5,"-":5},
                'row4': {";":5,"q":4,"j":3,"k":2,"x":2,"b":2,"m":2,"w":3,"v":4,"z":5}},
            "lefthand": "12345',.pyaoeui;qjkx",
            "righthand": "67890[]fgcrl/=dhtns-vzbmw"
        }

    return keybLayout


def chooseEmoj (EMOJI_SET):
    if EMOJI_SET == "keycaps":
        keycap_emoji = {
        1: "1️⃣", 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣"
        }
    elif EMOJI_SET == "circled":
        keycap_emoji = {
        1: "️⓵", 2: "⓶", 3: "③", 4: "️⓸", 5: "️⑤"
        }
    elif EMOJI_SET == "full":
        keycap_emoji = {
        1: "️❶", 2: "❷", 3: "❸", 4: "️❹", 5: "️❺"
        }
    return keycap_emoji
    
def format_rows_with_emoji(keysDict, myMode, keycap_emoji, character=None):
    formatted_output = {}
 
    for row, key_values in keysDict['layout'].items():
        # Create the left and right hand portions
        left_hand = []
        right_hand = []
        if row != "row0":
            extraSpace = (' '* SPACING*2)
        else:
            extraSpace = ''
        log(f"row: {row}")
        log(f"key_values: {key_values}")
        if character or myMode == 'hidden':
            
            for key, num in key_values.items():
                if character and key in list(character):  # Check if the key matches the user input
                    formatted_key = f"{key}{keycap_emoji[num]}"  # Add emoji next to the character
                else:
                    formatted_key = f"{key}"  # Just add the key normally
                # Separate keys into left and right hands
                if key in keysDict['lefthand']:
                    left_hand.append(formatted_key)
                else:
                    right_hand.append(formatted_key)
        elif myMode == 'map':
            for key, num in key_values.items():
                formatted_key = f"{key}{keycap_emoji[num]}"  # Add emoji next to the character
                  # Separate keys into left and right hands
                if key in keysDict['lefthand']:
                    left_hand.append(formatted_key)
                else:
                    right_hand.append(formatted_key)

        # Join hands with appropriate spacing
        formatted_output[row] = (' ' * LEFT_PAD) + extraSpace + (' '* SPACING).join(left_hand) + (" " * SPACING*3) + (' '* SPACING).join(right_hand)  # Extra spaces between hands
    
    return formatted_output

def main():
    result = {"items": []}

    keysDict = chooseKeyboard(LAYOUT)
    keycap_emoji = chooseEmoj(SYMBOL_SET)
    
    formatted_rows = format_rows_with_emoji(keysDict, MYMODE, keycap_emoji, MY_INPUT)

    # Print the output for each row
    for row, formatted_string in formatted_rows.items():
        result = addItem(formatted_string, result)

    print(json.dumps(result))

if __name__ == "__main__":
    main()


