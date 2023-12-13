import re

text = "The quick brown fox is big fox and better fox"

pattren = r"fox"

search = re.search(pattren, text)

if search:
    print("Pattren found:" , search.group())
else:
    print("Pattren not found")


