from letters_to_mic import MORSE_CODE_DICT


def encrypt(message):
    cipher = ""
    for letter in message:
        # if letter not space meanst it's only on words no space between them
        if letter != " ":
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            # + " " to add space between
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            # so if there is space we will add space in the cipher variable
            cipher += " "
    return cipher


def decrypt(message):
    # extra space added at the end to access the
    # last morse code
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        # بيستمر في اللوب الين يكون الرمز كامل مثلا كذا --. ثلاث رموز بعدها بيكون فيه سبيس وبينتقل ل الشرط الثاني
        if letter != ' ':

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter


        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:

                # adding space to separate words
                decipher += ' '

            else:

                # accessing the keys using their values (reverse of encryption)
                # how to access the value of dic from its key
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                              .values()).index(citext)]

                # رجعناها فاضيه في نهايه اللوب
                # after this code citext is empty
                citext = ''

    return decipher


# Hard-coded driver function to run the program
def main():
    should_continue = True
    while should_continue:
        direction = input('write decode or incode: \n').lower()
        if direction == "decode":
            message = input("enter a letter: ").upper()
            result = encrypt(message)
            print(result)
        else:
            message = input("enter a letter: ")
            result = decrypt(message)
            print(result)

        keep_playing = input("do you want to continue 'yes' or 'no' ").lower()

        if keep_playing == "no":
            should_continue = False
            print("Good bye")


main()
