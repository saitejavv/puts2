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

        Test_Mul = NumbeRes1[i] * NumbeRes2[i]
        Multiply_Test.append(round(Test_Mul,3)))
                
        url_m = 'http://127.0.0.1:5000/mul'
        Res3 = requests.get(url_m, params=parameters)
        Info3 = Res3.json()
        Multiply_Main.append(round(Info3,3))
        
        if Multiply_Main[i] == Multiply_Test[i]:
                print("multiplication successfull:OK")
        else:
                print("multiplication failed")
