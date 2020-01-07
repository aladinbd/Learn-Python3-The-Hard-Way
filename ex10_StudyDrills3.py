backslash_cat = "I\'m \\ backslash"
single_cat = "I\'m \' single quote"
double_cat = "I'm \" double quotes"
ascii_bell = "I\'m \aASCII bell(BEL)"

ascii_backspace = """
I\'m \bASCII backspace (BS)
This is another\\ \bbackspace and this is the third\\ \bone 
"""
carriage_return = "I'm \rCarriage return" # /r carriage return will come the begening of whole string

horizontal_tab = """
Todays shopping list in horizontal tab:
\t1. Shirt
\t2. Pant
\t3. T-Shirt\rAnother
"""

vertical_tab = """
Todays shopping list in vertical tab tab:
\v1. Shirt
\v2. Pant
\v3. T-Shirt
"""
print(backslash_cat)
print(single_cat)
print(double_cat)
print(ascii_bell)
print(ascii_backspace)
print(carriage_return)
print(horizontal_tab)
print(vertical_tab)
