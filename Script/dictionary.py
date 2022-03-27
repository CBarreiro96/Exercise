#!/usr/bin/python3

from itertools import count
import random
from os import system
from typing import final

counts = 0;
finals = 0;
keyExpression = [];
numberList = [];
phrasalVerb = [];
Expressions = {'acquaintance':'\"someone you have met, but do not know well\"','clique':'\"a small group of people who keep others from joining them\"','endure':'to experience and bear something difficult, painful, or unpleasant',
                'call the shots':  'to be a person who controls or organizes a situation','give someone/something an/the edge over':'to cause one to be in a favorable or superior position when compared to someone  or something else',
                'take something/someone at face value':'to accept or trust someone or something based only  on an initial or superficial presentation without taking further proof, verification or investigation into account',
                'create a (more) level playing field':'create more equitable conditions','offspring':'the young of an animal, or a person\'s children','seedling':'a very young plant that has grown  from a seed','sooner or later':'eventually, at some time in the future',
                'step by step':'gradully','now and then':'rarely','more or less':'approximately, almost','here and there':'in many different places','once and for all':'completely and finally'}

Vocabulary = {'selfless':'\"It is activity when you\'re thinking of other people before yourself\"','steering wheel':'\"A wheel that you turn to control the direction of a vehicle\"',
            'struggle':'\"to try very hard to do something difficult\"','lung':'\"The organs in the chest that you use to breathe\"', 'spread':'\"to affect or cause to affect more people, a large area, etc.\"',
            'squeeze':'\"to press something firmly especially from all sides in order to change its shape, reduce its size, or remove liquid from it\"','flooded':'covered with water','ever':'at any time','even':'emphasizes a surprising fact(hasta, incluso)',
            'laughing stock':'Someone or something that seems stupid or silly, especially by trying to be serious or important and not succeeding','misfit':'Someone who is not suited to a situation or who is not accepted by other people because their behavior is strange or unusual',
            'lie down':'a short rest, usually in or on a bed','rather':'in preference to, or as a preference','whether':'(used to refer to one or more possibilities or to express uncertainty) if'}

VocabularyBook = { 'beat':'\"to defeat or do better than\"','bend':'\"to (cause to) curve\"','bleed':'\"to lose blood\"','bite':'\"to use your teeth to cut into something or someone\"',
                    'blow':'\"to move and make currents of air, or to be moved or make something move on a current of air\"','breed':'\"to keep animals for the purpose of producing young animals in a controlled way\"',
                    'bring':'\"to take or carry someone or something to a place or a person, or in the direction of the person speaking\"','burn':'\"to be hurt, damaged, or destroyed by fire or extreme heat, or to cause this to happen\"',
                    'catch':'\"to stop and hold a moving object or person, especially in your hands\"','come':'\"to arrive somewhere\"','creep':'\"to move with your body close to the ground; to move slowly on your hands and knees\"',
                    'deal':'\"an agreement or an arrangement, especially in business\"','dig':'\"to make a hole in the ground by moving some of the ground or soil away\"','fall':'\"to suddenly go down onto the ground or towards the ground without intending to or by accident\"',
                    'fit':'\"to be suitable for something\"','feed':'\"to give food to a person, group, or animal\"','forbid':'\"to tell someone that they must not do something\"','forgive':'\"to decide not to be angry with someone, or not to punish them for something bad they have done\"',
                    'punish':'\"to cause someone who has done something wrong or committed a crime to suffer, by hurting them, forcing them to pay money, sending them to prison, etc.\"','blame':'\"to say or think that someone or something did something wrong or is responsible for something bad happening\"',
                    'hang':'\"to fasten something so that the top part is fixed but the lower part is free to move, or to be held in this way\"','hold':'\"to take and keep something in your hand or arms\"','lay':'\"to put something down somewhere\"',
                    'lead':'\"to control a group of people, a country, or a situation\"','afford':'\"to have/not have enough money to buy something or enough time to do something\"','law':'\"An official rule in a country\"','fasten':'\"to attach two parts of sth to close it\"',
                    'refuse':'\"to say that you will not do or accept something\"'}

phrasalVerb = {'fed up':'\"bored, annoyed, or disappointed, especially by something that you have experienced for too long\"','seek out':'\"to look for someone or something, especially for a long time until you find him, her, or it\"'}
Lists = [Expressions,Vocabulary, VocabularyBook,phrasalVerb]

print('What word\'s list do you like to study?')
print('0. Expressions\n1. Vocabulary\n2. VocabularyBook\n')
List_Number=int(input("Select an option: "))
system("clear")

for i in Lists[List_Number].keys():
    keyExpression.append(i)


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
