#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("\\Users\\pramo\\OneDrive\\Desktop\\python\\mailMerge\\Mail Merge Project Start\\Input\Names\\invited_names.txt") as names :
    namelist = names.read()
    print(namelist)
