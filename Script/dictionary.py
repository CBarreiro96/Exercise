#!/usr/bin/python3

import random
from os import system

keyExpression = [];
numberList = [];
Expressions = {'acquaintance':'\"Someone you have met, but do not know well\"','clique':'\"A small group of people who keep others from joining them\"','3':'3-','4':'4-'}
Vocabulary = {'hola2':'hola2-','22':'22-','33':'33-','44':'44-'}
Lists = [Expressions,Vocabulary]

print('What word\'s list do you like to study?')
print('1) Expressions\n2) Vocabulary\n')
List_Number=int(input("Select an option: "))

for i in Expressions.keys():
    keyExpression.append(i)

print(Expressions.get(keyExpression[2]))

while (len(numberList) < len(keyExpression)):
    numero = random.randint(0, len(keyExpression)-1)
    if numero not in numberList:
        numberList.append(numero)

def PrintOut():
    print("press enter to continue")
    input()

print(numberList)
for i in numberList:
    print(f'What is {Expressions.get(keyExpression[i])}?')
    answer = input()
    if answer == keyExpression[i]:
        print('It is correct')
        PrintOut()
    else:
        print('Do you like to know the answer?(Y/N)')
        answer = input()
        if answer == 'Y':
            print(keyExpression[i])
            PrintOut()
    system("clear")
