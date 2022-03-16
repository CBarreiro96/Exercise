#!/usr/bin/python3

from itertools import count
import random
from os import system
from typing import final

counts = 0;
finals = 0;
keyExpression = [];
numberList = [];
Expressions = {'acquaintance':'\"Someone you have met, but do not know well\"','clique':'\"A small group of people who keep others from joining them\"','3':'3-','4':'4-'}
Vocabulary = {'selfless':'It is activity when you\'re thinking of other people before yourself','steering wheel':'A wheel that you turn to control the direction of a vehicle',
            'struggle':'to try very hard to do something difficult','lung':'The organs in the chest that you use to breathe', 'spread':'to affect or cause to affect more people, a large area, etc.',
            'squeeze':'to press something firmly','flooded':'covered with water','ever':'at any time','even':'emphasizes a surprising fact(hasta, incluso)',
            'laughing stock':'Someone or something that seems stupid or silly, especially by trying to be serious or important and not succeeding','misfit':'Someone who is not suited to a situation or who is not accepted by other people because their behavior is strange or unusual'}

Lists = [Expressions,Vocabulary]

print('What word\'s list do you like to study?')
print('0) Expressions\n1) Vocabulary\n')
List_Number=int(input("Select an option: "))
system("clear")

for i in Lists[List_Number].keys():
    keyExpression.append(i)

print(Lists[List_Number].get(keyExpression[2]))

while (len(numberList) < len(keyExpression)):
    numero = random.randint(0, len(keyExpression)-1)
    if numero not in numberList:
        numberList.append(numero)

def PrintOut():
    if finals == 1:
        print("press enter to exit")
    else:
        print("press enter to continue")
    input()

print(numberList)
for i in numberList:
    print(f'What is {Lists[List_Number].get(keyExpression[i])}?')
    answer = input()
    if answer == keyExpression[i]:
        print('It is correct')
        counts = counts + 1
        PrintOut()
    else:
        print('Do you like to know the answer?(Y/N)')
        answer = input()
        if answer == 'Y':
            print(keyExpression[i])
            PrintOut()
    system("clear")

calification = counts*5/len(keyExpression)
finals=1;
print(f'\nYour calification is: {calification}\n')
PrintOut()
system("clear")
