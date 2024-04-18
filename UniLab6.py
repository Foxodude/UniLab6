# -*- coding: cp1251 -*-
from itertools import count
from pprint import pprint

while True:
    
    checker = False
    primaryChoice = input("Выбор задания для проверки : \n1)\n2)\n3)\n4) - Выход\nВыбор : ")
    if [num for num in primaryChoice if num not in ".,/*-+1234567890"]: checker = True
    if checker == True:
        print("Так нельзя")
        break
    primaryChoice = int(primaryChoice)
    
    if primaryChoice == 1:
        countries = {'Россия':'Москва',  'Беларусь':'Минск', 'Италия':'Рим'}
        x = len(countries)
        pprint(countries)
        print(countries['Россия'])
        countries = sorted(countries)
        pprint(countries)
    
    if primaryChoice == 2:
        superCounter = 0
        word = input("Введите слово для проверки : ")
        word = word.lower()
        if [letter for letter in word if letter in "авеинорст"]: superCounter = superCounter + 1
        if [letter for letter in word if letter in "дклмпу"]: superCounter = superCounter + 2
        if [letter for letter in word if letter in "бгёья"]: superCounter = superCounter + 3
        if [letter for letter in word if letter in "йы"]: superCounter = superCounter + 4
        if [letter for letter in word if letter in "жзхцч"]: superCounter = superCounter + 5
        if [letter for letter in word if letter in "шэю"]: superCounter = superCounter + 8
        if [letter for letter in word if letter in "фщъ"]: superCounter = superCounter + 10
        print("Слово набирает, ", superCounter)
     
    if primaryChoice == 3:
        studentLanguages = {
            'Иван': ['английский', 'французский', 'немецкий'],
            'Мария': ['английский', 'китайский'],
            'Петр': ['французский', 'испанский'],
            'Анна': ['английский', 'китайский', 'испанский'],
            'Алексей': ['китайский', 'немецкий']}
        
        allLanguages = set()
        chineseKnowers = []
        
        for student, languages in studentLanguages.items():
            allLanguages.update(languages)
            if 'китайский' in languages:
                chineseKnowers.append(student)
                
        allLanguages = sorted(allLanguages)
        
        print("Все языки ", allLanguages)
        print("Студенты с Китайским ", chineseKnowers)        
        
    if primaryChoice == 4:
        break
