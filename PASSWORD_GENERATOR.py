import random
import string

length = int(input("Enter the legth of the password -: "))


char = list(string.ascii_letters)
num = [1,2,3,4,5,6,7,8,9,0]
special_char = list(string.punctuation)


password = ""

for i in range(0, length):

    char_selection = random.randrange(1, 3)

    if (char_selection == 1):
        password = password + random.choice(char)

    elif (char_selection == 2):
        password = password + str(random.choice(num))

    else:
        password = password + random.choice(special_char)

print(password)