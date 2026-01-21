Alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def en_decrypt (text , Key, decrypt):
    text_lower = text.lower()
    myArray = list(text_lower)
    answer = ""
    i = 0
    
    for x in myArray:
        i = 0
        for y in Alpabet: 
            if x == y: 
                if decrypt == True:
                    answer += str(Alpabet[i - Key])
                else:
                    if i + Key > 25:
                        temp  = (i + Key) - 26 
                    else:
                        temp = i + Key
                    answer += str(Alpabet[temp] )
                
            i += 1
    return answer

while(True):
    
    print("input message:")
    message = input()
    print("input key:")
    nummer  = input()
    print("1 for encrypt 2 for decrypt:")
    temp = input()
   
    if temp == "2" or temp == "1":
        
        if temp == "2":
            dec = True

        elif temp == "1":
            dec = False
        print(en_decrypt(message , int(nummer), dec))
    else:
        print("invalid entry")
    exit()


    


