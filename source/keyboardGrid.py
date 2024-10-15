#!/usr/bin/env python3
import json

result = {"items": []}

for i in range(1, 42):
    result["items"].append({
            "title": '' , 
            'subtitle': "",
            'valid': True,
            'uid': "myUID",
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
                    },
            },
            "icon": {
                "path": 'Picture1.png'
            },
            'arg': "resultString"
                }) 

result["items"].append({
        "title": '' , 
        'subtitle': "",
        'valid': True,
        'uid': "myUID",
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
                },
        },
        "icon": {
            "path": 'Picture2.png'
        },
        'arg': "resultString"
            }) 

print(json.dumps(result))