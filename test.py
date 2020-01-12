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

        Test_SUB = NumbeRes1[i] - NumbeRes2[i]
        Subtract_Test.append(round(Test_SUB,3))

        Test_Mul = NumbeRes1[i] * NumbeRes2[i]
        Multiply_Test.append(round(Test_Mul,3))

        Test_Div = NumbeRes1[i] / NumbeRes2[i]
        Divsion_Test.append(round(Test_Div,3))

        url_a = 'http://127.0.0.1:5000/add'
        Res1 = requests.get(url_a, params=parameters)
        Info1 = Res1.json()
        Add_Main.append(round(Info1,3))

        url_b = 'http://127.0.0.1:5000/sub'
        Res2 = requests.get(url_b, params=parameters)
        Info2 = Res2.json()
        Subtract_Main.append(round(Info2,3))

        url_m = 'http://127.0.0.1:5000/mul'
        Res3 = requests.get(url_m, params=parameters)
        Info3 = Res3.json()
        Multiply_Main.append(round(Info3,3))

        url_d = 'http://127.0.0.1:5000/div'
        Res4 = requests.get(url_d, params=parameters)
        Info4 = Res4.json()
        Divsion_Main.append(round(Info4,3))

        if Add_Main[i] == Add_Test[i]:
                print("addition successfull:OK")
        else:
                print("addition failed")
        
        if Subtract_Main[i] == Subtract_Test[i]:
                print("subtraction successfull:OK")
        else:
                print("subtraction failed")

        if Multiply_Main[i] == Multiply_Test[i]:
                print("multiplication successfull:OK")
        else:
                print("multiplication failed")

        if Divsion_Main[i] == Divsion_Test[i]:
                print("division successfull:OK")
        else:
                print("division failed")
