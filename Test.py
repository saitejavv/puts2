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

        Test_Add = NumbeRes1[i] + NumbeRes2[i]
        Add_Test.append(round(Test_Add,3))
        url_a = 'http://127.0.0.1:5000/add'
        Res1 = requests.get(url_a, params=parameters)
        Info1 = Res1.json()
        Add_Main.append(round(Info1,3))
        if Add_Main[i] == Add_Test[i]:
                print("addition successfull:OK")
        else:
                print("addition failed")
