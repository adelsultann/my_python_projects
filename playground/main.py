alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(alphabet[1])
words = input("write a words: ")

shiffted = int(input("enter a number"))
word = ""
for letter in words:

    position = alphabet.index(letter)
    print(position)
    new_position = shiffted + position
    new_letter = alphabet[new_position]
    word += new_letter
    print(word)




