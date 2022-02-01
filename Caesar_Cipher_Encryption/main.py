alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def incode(plain_text, shift_amount):
    cipher = ""
    for letter in plain_text:
        # position give us corresponding position of the letter in the list
        # for example letter a = 0 d = 3
        position = alphabet.index(letter)
        # move the letter x shifted amount
        new_position = position + shift_amount
        # find the new letter in the new_position
        # alphabet[new_position"2"] = c
        new_letter = alphabet[new_position]

        cipher = cipher + new_letter
    print(cipher)


def decode(ciper_text, shift_amount):
    plain_text = ""
    for letter in ciper_text:
        position = alphabet.index(letter)

        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(plain_text)


should_continue = True

while should_continue:
    direction = input('write decode or incode:\n')

    text = input("enter a letter ").lower()
    shift = int(input('enter the amount shiftted \n'))
    #  حطينا الكود اللي فوق عشان مهما الشخص حط رقم كبير يصغره ويخليها 26 ضمن احروف الهجاء الموجوده فوق
    # if user put for example 100 as the shiftted amount we will divide it by 26 so that we don't get error
    shift = shift % 26
    if direction == "decode":
        decode(ciper_text=text, shift_amount=shift)
    else:
        incode(plain_text=text, shift_amount=shift)

    result = input("do you want to continue 'yes' or 'No': ").lower()

    if result == "no":
        should_continue = False
        print("Good bye")
