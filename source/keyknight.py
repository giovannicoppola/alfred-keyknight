# Thursday, October 10, 2024
import json
import sys

if len(sys.argv) > 1:
    MY_INPUT = sys.argv[1]
else:
    MY_INPUT = ''


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
            
            "mods": {
                    "alt": {
                        "valid": True,
                        "arg": "alfredapp.com/powerpack/",
                        "subtitle": "https://www.alfredapp.com/powerpack/"
                        },
                    "cmd": {
                        "valid": True,
                        "arg": "alfredapp.com/shop/",
                        "subtitle": "https://www.alfredapp.com/shop/"
                            },
                    "cmd+alt": {
                            "valid": True,
                            "arg": "alfredapp.com/blog/",
                            "subtitle": "https://www.alfredapp.com/blog/"
                    }
                },
                # "icon": {
                #     "path": 'icons/icon.png'
                # },
                'arg': "resultString"
            }) 
    return myResults

def defineDict ():
    keysDict = {
        "row1": {"q": 5, "w": 4, "e": 3, "r": 2, "t": 1, "y": 1, "u": 2, "i": 3, "o": 4, "p": 5, "[": 6, "]": 6},
        "row2": {"a": 4, "s": 3, "d": 2, "f": 1, "g": 1, "h": 2, "j": 3, "k": 4, "l": 5, ";": 6, "'": 6},
        "row3": {"z": 5, "x": 4, "c": 3, "v": 2, "b": 1, "n": 1, "m": 2, ",": 3, ".": 4, "/": 5},
        "row0": {"1": 5, "2": 4, "3": 3, "4": 2, "5": 1, "6": 1, "7": 2, "8": 3, "9": 4, "0": 5, "-": 6, "=": 6}
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

def format_rows(keysDict):
    keycap_emoji = {
    1: "1️⃣", 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣", 6: "6️⃣"
    }
    
    formatted_output = {}
    
    for row, key_values in keysDict.items():
        formatted_output[row] = '  '.join(f"{keycap_emoji[num]}{key}{keycap_emoji[num]}" for key, num in key_values.items())
        # Add the emoji only before the character
        formatted_output[row] = '    '.join(f"{keycap_emoji[num]}{key}" for key, num in key_values.items())
        # Create the left and right hand portions
        left_hand = '  '.join(f"{keycap_emoji[num]}{key}" for key, num in key_values.items() if key in "qwertasdfgzxcvb12345")
        right_hand = '  '.join(f"{keycap_emoji[num]}{key}" for key, num in key_values.items() if key in "yuiophjklnm67890-=[];'./")
        
        # Add extra space between the two hands
        formatted_output[row] = left_hand + "        " + right_hand  # Extra spaces between the hands
    
    
    return formatted_output

        

def main():
    result = {"items": []}
    # row1 = format_string("qwertyuiop[]", MY_INPUT)
    # result = addItem(row1, result)
    # row2 = format_string("asdfghjkl;'", MY_INPUT)
    # result = addItem(row2, result) 
    #print(json.dumps(result))

    keysDict = defineDict()
    # Get the formatted rows
    formatted_rows = format_rows(keysDict)
    # Get the character from command line arguments
    if len(sys.argv) > 1:
        user_character = sys.argv[1]
        # Get the formatted output for the specified character
        keycap_output = format_keycap_for_character(keysDict, user_character)

    # Print the output for each row
    for row, formatted_string in formatted_rows.items():
        result = addItem(formatted_string, result)

    print(json.dumps(result))

if __name__ == "__main__":
    main()




import sys

keysDict = {
    "row1": {"q": 5, "w": 4, "e": 3, "r": 2, "t": 1, "y": 1, "u": 2, "i": 3, "o": 4, "p": 5, "[": 6, "]": 6},
    "row2": {"a": 4, "s": 3, "d": 2, "f": 1, "g": 1, "h": 2, "j": 3, "k": 4, "l": 5, ";": 6, "'": 6},
    "row3": {"z": 5, "x": 4, "c": 3, "v": 2, "b": 1, "n": 1, "m": 2, ",": 3, ".": 4, "/": 5},
    "row0": {"1": 5, "2": 4, "3": 3, "4": 2, "5": 1, "6": 1, "7": 2, "8": 3, "9": 4, "0": 5, "-": 6, "=": 6}
}

# Mapping numbers to corresponding keycap emojis
keycap_emoji = {
    1: "1️⃣", 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣", 6: "6️⃣"
}

def format_rows_with_emoji(keysDict, character=None):
    formatted_output = {}
    
    for row, key_values in keysDict.items():
        # Create the left and right hand portions
        left_hand = []
        right_hand = []
        
        for key, num in key_values.items():
            if character and key == character:  # Check if the key matches the user input
                formatted_key = f"{keycap_emoji[num]}{key}"  # Add emoji next to the character
            else:
                formatted_key = f"{key}"  # Just add the key normally
            
            # Separate keys into left and right hands
            if key in "qwertasdfgzxcvb12345":
                left_hand.append(formatted_key)
            else:
                right_hand.append(formatted_key)

        # Join hands with appropriate spacing
        formatted_output[row] = '  '.join(left_hand) + "        " + '  '.join(right_hand)  # Extra spaces between hands
    
    return formatted_output

# Main execution
if __name__ == "__main__":
    # Get the character from command line arguments
    user_character = sys.argv[1] if len(sys.argv) > 1 else None
    
    # Get the formatted rows with emoji for the specified character
    formatted_rows = format_rows_with_emoji(keysDict, user_character)
    
    # Print the output for each row
    for row, formatted_string in formatted_rows.items():
        print(f"{row}: {formatted_string}")
