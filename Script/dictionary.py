#!/usr/bin/python3

from itertools import count
import random
from os import system
from typing import final

counts = 0;
finals = 0;
keyExpression = [];
numberList = [];
Expressions = {'acquaintance':'\"someone you have met, but do not know well\"','clique':'\"a small group of people who keep others from joining them\"','endure':'to experience and bear something difficult, painful, or unpleasant',
                'call the shots':  'to be a person who controls or organizes a situation','give someone/something an/the edge over':'to cause one to be in a favorable or superior position when compared to someone  or something else',
                'take something/someone at face value':'to accept or trust someone or something based only  on an initial or superficial presentation without taking further proof, verification or investigation into account',
                'create a (more) level playing field':'create more equitable conditions','offspring':'the young of an animal, or a person\'s children','seedling':'a very young plant that has grown  from a seed','sooner or later':'eventually, at some time in the future',
                'step by step':'gradully','now and then':'rarely','more or less':'approximately, almost','here and there':'in many different places','once and for all':'completely and finally'}

Vocabulary = {'selfless':'It is activity when you\'re thinking of other people before yourself','steering wheel':'A wheel that you turn to control the direction of a vehicle',
            'struggle':'to try very hard to do something difficult','lung':'The organs in the chest that you use to breathe', 'spread':'to affect or cause to affect more people, a large area, etc.',
            'squeeze':'to press something firmly','flooded':'covered with water','ever':'at any time','even':'emphasizes a surprising fact(hasta, incluso)',
            'laughing stock':'Someone or something that seems stupid or silly, especially by trying to be serious or important and not succeeding','misfit':'Someone who is not suited to a situation or who is not accepted by other people because their behavior is strange or unusual',
            'lie down':'to move from a sitting posisition to a horizaontal position'}

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
