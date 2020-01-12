import unittest
import json
import requests 
from fractions import Fraction 

NumbeRes1 = [4,120,15,48]
NumbeRes2 = [2,10,3,4]

Add_Main = []
Add_Test = []
Subtract_Main = []
Subtract_Test = []
Multiply_Main = []
Multiply_Test = []
Divsion_Main = []
Divsion_Test= []

for i in range(0,len(NumbeRes1)):
parameters={"A":Fraction(NumbeRes1[i]),"B":Fraction(NumbeRes2[i])}
        Test_SUB = NumbeRes1[i] - NumbeRes2[i]
        Subtract_Test.append(round(Test_SUB,3))
        
        url_b = 'http://127.0.0.1:5000/sub'
        Res2 = requests.get(url_b, params=parameters)
        Info2 = Res2.json()
        Subtract_Main.append(round(Info2,3))
        
        if Subtract_Main[i] == Subtract_Test[i]:
                print("subtraction successfull:OK")
        else:
                print("subtraction failed")
