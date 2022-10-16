from resource import *

alphabet = alphabet.split(' ')
morse_code = morse_code.split(' / ')
run = True
while run:
    print(ascii_art)
    output = ""
    option = input("Convert text to morse or back! What do you want to translate? Enter 'T' for text to morse or "
                   "'M' for morse to text!\n").lower()
    if option == 'end':
        run = False
        pass
    else:
        user_input = input('What prompt to translate:\n').lower()

        if option == 't':
            for bit in user_input:
                if bit == ' ':
                    output += ' / '
                else:
                    al_index = alphabet.index(bit)
                    output += f"{morse_code[al_index]} "
            print(output)

        elif option == 'm':
            refined = user_input.split(' ')
            for bit in refined:
                if bit == '/':
                    output += ' '
                elif bit == '':
                    pass
                else:
                    ml_index = morse_code.index(bit)
                    output += f"{alphabet[ml_index]}"
            print(output)
        else:
            print("Invalid option. Please try again.")
