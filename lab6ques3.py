user_input = "Tom 25 Rahu22 2@$"

letters = list(map(lambda x: x.upper(), filter(lambda x: x.isalpha(), user_input)))
squared_digits = list(
    map(lambda x: int(x) ** 2, filter(lambda x: x.isdigit(), user_input))
)
alphanumeric = list(filter(lambda x: x.isalnum(), user_input.split()))

print(letters)
print(squared_digits)
print(alphanumeric)
