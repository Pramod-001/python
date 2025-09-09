data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(string):
    encString = ""
    shift = int(input("Enter the value of shift : "))
    sh %= len(data) #To keep the shift index in range
    for i in string :
        pos = data.index(i) + shift
        encString += data[pos]
    print(encString)
    
def decrypt(string):
    decString = ""
    shift = int(input("Enter shift number : "))
    sh %= len(data) 
    for i in string :
        pos = data.index(i) - shift
        encString += data[pos]
    print(encString)
cont = True
while cont :
    choice = int(input("Select 1 for Encryption or 2 for Decryption : "))
    if choice == 1:
        string = input("Enter String to encrypt : ")
        encrypt(string)
    else : 
        enstring = input("Enter Encrypted String to decrypt :")
        decrypt(enstring)
    restart = input("Do you want to continue (Yes or No) :").lower()
    
    if restart =="no" :
        cont = False
        print("Process Completed ")
    