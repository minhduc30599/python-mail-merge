#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

new_names = []

with open('./Input/Names/invited_names.txt', 'r') as file:
    names = file.readlines()
    for name in names:
        new_names.append(name.replace('\n', ''))

with open('./Input/Letters/starting_letter.txt', 'r+') as file:
    letter = file.read()
    for name in new_names:
        new_letter = letter.replace('[name]', name)
        with open(f'./Output/ReadyToSend/letter_for_{name}', 'w') as f:
            f.write(new_letter)

