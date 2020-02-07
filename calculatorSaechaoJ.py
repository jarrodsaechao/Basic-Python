#Calulator_pwiese.Saechao
#Jarrod Saechao
#Nov 7 2017
#This program is a calculator
#Python 3.6.2

def main():
    ops = operation()
    num_1 = get_num()
    num_2 = get_num() 

    if ops == '+':
        answer = addition(num_1, num_2)

    elif ops == '*':
        answer = multiplication(num_1, num_2)

    elif ops == '-':
        answer = subtraction(num_1, num_2)

    elif ops == '/':
        answer = division(num_1, num_2)
        
    else:
        print("invalid operator")
        return
    show_answer(answer)

def operation():
    op = input('Pick an operation ')
    return op

def get_num():
    banana = int(input("Gimme a number "))
    return banana


def addition(king, queen):
    answer = king + queen
    return answer


def multiplication(apple,banana):
    answer = apple * banana
    return answer

def subtraction(num1,num2):
    potato = num1 + num2
    return potato

def division(jes,pyt):
    if pyt == 0:
        print('You can not do that')
        return 0
    money = jes / pyt
    return money

def show_answer(answer):
    print(answer,'is the answer')
main()

    

        

        
        

    
