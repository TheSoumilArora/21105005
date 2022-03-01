def list_of_letters(string):
    list_out = []
    for i in string:
        list_out.append(i)
    return list_out

def check_meaning(word):
    import enchant
    


while True:                                                                                             #Loop to make sure only one word is entered by the shopkeeper
    word_george = input("Enter word uttered by George: ").lower().split()
    if len(word_george) == 1:
        word_george = word_george[0]
        break
    else:
        print("Only one word is to be entered\nPlease try again!")

while True:                                                                                             #Loop to make sure only one word is entered by the shopkeeper
    word_barbie = input("Enter word made by Barbie: ").lower().split()
    if len(word_barbie) == 1:
        word_barbie = word_barbie[0]
        break
    else:
        print("Only one word is to be entered\nPlease try again!")

letters_in_word_george = list_of_letters(word_george)
letters_in_word_barbie = list_of_letters(word_barbie)

while True:                                                                                             #Loop to ask the shopkeeper if he wants to consider same number of letters or not
    same_letters = input("Do you want to consider same no. of letters?\n")
    if same_letters in ("N","n","No","NO","no"):
        same_letters = False
        break
    elif same_letters in ("YES","Yes","Y","y","yes"):
        same_letters = True
        break
    else:
        print("Please enter 'Yes' or 'No'")

if same_letters:
    if sorted(letters_in_word_barbie) == sorted(letters_in_word_george):
        word_created = True
    else:
        word_created = False
else:
    if set(letters_in_word_barbie) == set(letters_in_word_george):
        word_created = True
    else:
        word_created = False

if word_created:
    print("Barbie has made a word!")
    while True:
        meaning_check = input("Do you want to check whether it is meaningful or not?")
        if meaning_check in ("N","n","No","NO","no"):
            meaning_check = False
            break
        elif meaning_check in ("YES","Yes","Y","y","yes"):
            meaning_check = True
            break
        else:
            print("Please enter 'Yes' or 'No'")
else:
    print("Barbie isn't able to create a word.\nTheir friendship is fake.")