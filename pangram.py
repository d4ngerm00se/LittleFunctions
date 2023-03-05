
alphabet = "abcdefghijklmnopqrstuvwxyz"

def is_pangram(s):
    for x in alphabet:
        if x not in s.lower():
            return False
    return True

message = input("Please enter a phrase you wish to check for pangramage: ")

print(is_pangram(message))
