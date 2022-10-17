favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Looping Through a Dictionary's Keys in a Particular Order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping Through All Values in a Dictionary
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
