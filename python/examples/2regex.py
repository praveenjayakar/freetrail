#!/bin/python3


import re

text = "The quick brown fox is fox"

pattren = r"fox"

match = re.match(pattren , text)

if match:
    print("Match found :" , match.group())
else:
        print("No match found")

