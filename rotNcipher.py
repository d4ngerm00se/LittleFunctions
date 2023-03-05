import string
lowercase = string.ascii_letters
uppercase = string.ascii_uppercase

def rot13(message, rot):
    new_message = []
    for x in message:
        if x in uppercase:
            index = (uppercase.find(x) + rot) % 26
            new_message.append(uppercase[index])
        elif x in lowercase:
            index = (lowercase.find(x) + rot) % 26
            new_message.append(lowercase[index])
        else:
            new_message.append(x)
    stringymessage = ''.join(new_message)
    return stringymessage

message = input("Please enter the message you wish to be encrypted:")
rotation = int(input("Please state the rotation you wish to implement:"))

print(rot13(message, rotation))