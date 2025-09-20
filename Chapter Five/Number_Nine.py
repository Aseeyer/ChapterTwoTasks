# Defining the palindrome tester function
def is_palindrome(input_string):
    # Convert to lowercase and keep only alphanumeric characters
    normalized_string = ''.join(character.lower() for character in input_string if character.isalnum())

    # Use list as a stack
    character_stack = []
    for character in normalized_string:
        character_stack.append(character)

    # Build reversed string using the stack
    reversed_string = ''
    while character_stack:
        reversed_string += character_stack.pop()

    # Compare normalized string with reversed string
    return normalized_string == reversed_string


print(is_palindrome("radar"))
print(is_palindrome("tunde Ednut"))
print(is_palindrome("Hello"))
