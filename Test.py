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

        Test_Div = NumbeRes1[i] / NumbeRes2[i]
        Divsion_Test.append(round(Test_Div,3))
        
        url_d = 'http://127.0.0.1:5000/div'
        Res4 = requests.get(url_d, params=parameters)
        Info4 = Res4.json()
        Divsion_Main.append(round(Info4,3))
        
         if Divsion_Main[i] == Divsion_Test[i]:
                print("division successfull:OK")
        else:
                print("division failed")
