import re

text = "apple,banana,cat,dog"

pattren = r","

search = re.split(pattren, text)

print(search)


