def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}")

print("Way: 1")
greet_user("alauddin")

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

print("Way: 2")
describe_pet("hamster", "harry")
describe_pet("dog", "willie")

print("Way: 3")
describe_pet(animal_type = "cat", pet_name = "ronny")

print("Way: 4")
describe_pet("cat", "rony")

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    return full_name.title()

print("Way: 5")
musician = get_formatted_name("john", "lee", "hooker")
print(musician)

def breakfast_menu(vagitable_name, price_of_vagitable):
    print(f"I have completed my breakfast with {vagitable_name.title()}")
    print(f"I bought {vagitable_name.title()} for {price_of_vagitable}")


breakfast_menu("carrot", 5)
