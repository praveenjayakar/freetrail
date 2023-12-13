import re

text = "The quick brown fox"

pattren = r"brown"

search = re.search(pattren, text)
if search:
    print("Pattren found : " , search.group())
else:
    print("pattren not found")

