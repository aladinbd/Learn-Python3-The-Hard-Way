from sys import argv

script, profession = argv
prompt = '> '

print(f"So you're a {profession}")
print("Are you ready to ask to you few questions?")
ready = input(prompt)

print("What's your favourite programming language?")
language = input(prompt)

print("What's your second favourite language?")
others_language = input(prompt)

print(f"Do you know about recent trends of {language}?")
trends = input(prompt)

print(f"""
So, you're a {profession} and you love {language} so much
Recently {language} has been more popular than {others_language}
""")
