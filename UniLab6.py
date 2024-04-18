# -*- coding: cp1251 -*-
from itertools import count
from pprint import pprint

while True:
    
    checker = False
    primaryChoice = input("����� ������� ��� �������� : \n1)\n2)\n3)\n4) - �����\n����� : ")
    if [num for num in primaryChoice if num not in ".,/*-+1234567890"]: checker = True
    if checker == True:
        print("��� ������")
        break
    primaryChoice = int(primaryChoice)
    
    if primaryChoice == 1:
        countries = {'������':'������',  '��������':'�����', '������':'���'}
        x = len(countries)
        pprint(countries)
        print(countries['������'])
        countries = sorted(countries)
        pprint(countries)
    
    if primaryChoice == 2:
        superCounter = 0
        word = input("������� ����� ��� �������� : ")
        word = word.lower()
        if [letter for letter in word if letter in "���������"]: superCounter = superCounter + 1
        if [letter for letter in word if letter in "������"]: superCounter = superCounter + 2
        if [letter for letter in word if letter in "����"]: superCounter = superCounter + 3
        if [letter for letter in word if letter in "��"]: superCounter = superCounter + 4
        if [letter for letter in word if letter in "�����"]: superCounter = superCounter + 5
        if [letter for letter in word if letter in "���"]: superCounter = superCounter + 8
        if [letter for letter in word if letter in "���"]: superCounter = superCounter + 10
        print("����� ��������, ", superCounter)
     
    if primaryChoice == 3:
        studentLanguages = {
            '����': ['����������', '�����������', '��������'],
            '�����': ['����������', '���������'],
            '����': ['�����������', '���������'],
            '����': ['����������', '���������', '���������'],
            '�������': ['���������', '��������']}
        
        allLanguages = set()
        chineseKnowers = []
        
        for student, languages in studentLanguages.items():
            allLanguages.update(languages)
            if '���������' in languages:
                chineseKnowers.append(student)
                
        allLanguages = sorted(allLanguages)
        
        print("��� ����� ", allLanguages)
        print("�������� � ��������� ", chineseKnowers)        
        
    if primaryChoice == 4:
        break