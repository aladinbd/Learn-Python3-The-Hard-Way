from sys import argv

script, name = argv
user_input = '> '

print(f"Hi {name}, I want to ask few questions")
print(f"Where do you live {name}")
country = input(user_input)

print("What's your current city name?")
city = input(user_input)

print("Please let me know your ZIP code:")
zip = input(user_input)

print(f"""
So, you live in {country} and current city {city}
{zip} is your postal zip code.
Isn't it Mr {name}?
""")
