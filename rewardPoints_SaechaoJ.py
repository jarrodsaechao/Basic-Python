#rewardPoints
#show reward points for each membership
#Jarrod Saechao
#11/29/17
#Python3.6.2


def main():
    membership = input("please select a membership type, standard, plus or premium").lower()
    purchase = float(input("Cost of purchase "))

    if membership == "premium":
        reward = premium(purchase)
        
    elif membership == "plus":
        reward = plus(purchase)
        
    elif membership == "standard":
        reward = standard(purchase)

    print("Your reward points are", reward)

def premium(money):
    if money < 200:
        return 0.04*money
    return 0.15*money

def plus(money):
    if money < 150:
        return 0.06*money
    return 0.13*money

def standard(money):
    if money < 75:
        return 0.05*money
    elif money < 150:
        return 0.075*money
    return 0.1*money


main()
