# Printing a secret code between 2 friends
import random
import string

# Generate random 3-letter string
def random_chars():
# .join is used to combine a sequence of strings into one string, with a separator (here it’s either '' or ' ').
# String.ascii_letters -> It comes form the string module, It contains all alphabet letters form a to z both lower and uppercase.
    return ''.join(random.choices(string.ascii_letters, k=3))

# Function to encode a message
def encode(message):
    words = message.split()
    encoded_words = []

    for word in words:
        if len(word) >= 3:
            # Remove first letter and add it to the end
            modified_word = word[1:] + word[0]
            # Add 3 random characters at start and end
            secret_word = random_chars() + modified_word + random_chars()
        else:
            # Reverse the word for words with less than 3 characters
            secret_word = word[::-1]

        encoded_words.append(secret_word)

    return ' '.join(encoded_words)

# Function to decode a message
def decode(secret_message):
    words = secret_message.split()
    decoded_words = []

    for word in words:
        if len(word) <= 5:
            # Reverse the word if less than 3 characters
            decoded_word = word[::-1]
        else:
            # Remove 3 random characters from start and end
            modified_word = word[3:-3]
            # Move the last letter to the beginning
            decoded_word = modified_word[-1] + modified_word[:-1]

        decoded_words.append(decoded_word)

    return ' '.join(decoded_words)

# Input from the user
message = input("Enter your message: ")

# Encode the message
encoded_message = encode(message)
print(f"Encoded Message: {encoded_message}")

# Decode the message
decoded_message = decode(encoded_message)
print(f"Decoded Message: {decoded_message}")
