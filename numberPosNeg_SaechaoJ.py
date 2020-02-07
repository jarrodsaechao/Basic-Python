#numberPosNeg_SaechaoJ.py
#How many positive and negative numbers
#Jarrod Saechao
#11/19/17
#Python 3.6.2






def main():

    
    pos = 0
    neg = 0
    ans = "n"

    
    while True:
        
        if float(input("Give me a number: ")) < 0:
            neg += 1
        else:
            pos += 1
            
        ans = input("Continue? y/n ")
        if ans == "y":
            print("Positive:", pos, "Negative:", neg)
            break
        
            
main()






main()
    
