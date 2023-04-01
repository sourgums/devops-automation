#Python Typing Text Effect - www.101computing.net/python-typing-text-effect/
import time,os,sys

from time import sleep
import subprocess

string = "ALBERTO" # Whatever string you want

for letter in string:
  sleep(0.01) # In seconds
  sys.stdout.write(letter)
  sys.stdout.flush()

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value  
  
def clearScreen():
  os.system("cls")
    
typingPrint("ALBERTO   \n")
time.sleep(1)
albert = 'ALBERTO   '
albert.split('a')                 # splits on 'a'
['A', 'LBE', 'R ', ' T', 'O',' ',' ', ' '] 
print(albert)
time.sleep(0.05)
os.system("cls")
albert.split('L')                 # splits on 'a'
['LBE', 'R', 'T ', ' O', 'A', ' ', ' ', ' ',' '] 
albert.split('B')  
print(albert)
time.sleep(0.75)
os.system("cls")             # splits on 'a'
albert = 'RTO  ALBE'
albert.split('\n') 
time.sleep(2)
os.system("cls")
albert.split('L')                 # splits on 'a'
['LBE', 'R', 'T ', ' O', 'A', ' ', ' ', ' ',' '] 
albert.split('B')  
print(albert)
time.sleep(2)
os.system("cls")             # splits on 'a'
['R', 'T', 'O ', 'A', 'LBE',' ',' ',' '] 
albert.split('A')  
albert = 'TO   ALBER'
albert.split('\n') 
print(albert)
time.sleep(2)
os.system("cls")
albert.split('L')                 # splits on 'a'
['A', 'LBE', 'R ', ' T', 'O', ' ',' ',' '] 
albert = 'O  ALBERT'
print(albert)
time.sleep(0.5)
os.system("cls")
albert.split('L')                 # splits on 'a'
['LBE', 'R', 'T ', ' O', 'A', ' ', ' ', ' ',' '] 
albert.split('B')  
print(albert)
time.sleep(2)
os.system("cls")             # splits on 'a'
['R', 'T', 'O ', 'A', 'LBE'] 
albert = 'RTOAL   BE'
print(albert)
time.sleep(0.2)
os.system("cls")           # splits on 'a'
['R', 'T', 'O ', 'A', 'LBE'] 
albert = '  EBLA ORT'
print(albert)
time.sleep(2.75)
os.system("cls")
albert.split('E')                 # splits on 'a'
['LBE', 'R', 'T ', ' O', 'A'] 
albert = 'AOLBERT   '
print(albert)
time.sleep(2.5)
albert.split('R')  
time.sleep(1)
os.system("cls")
albert.split('E')       # no parameter given: splits on whitespace
albert = 'LA   BERTO'
albert.split('\n') 
print(albert)
time.sleep(2.5)
albert.split('A')     
time.sleep(2)
albert.split('E') 
time.sleep(1)
os.system("cls")     # no parameter given: splits on whitespace
albert = ' ORTBER AL'
albert.split('\n') 
print(albert)
albert.split()     
time.sleep(1 ) 

os.system("cls")     # no parameter given: splits on whitespace
albert = 'BLA   ORTE'
albert.split('\n') 
print(albert)
time.sleep(1)
os.system("cls")  
albert = 'TRO ALBE'
albert.split('\n') 
print(albert)
time.sleep(1)
os.system("cls")
albert.split()     
time.sleep(1) 

os.system("cls")      
albert = 'A   ORTBEL '
albert.split('\n') 
albert.split('E')               # splits on '\n' only
albert = 'O BERT AL'
albert.split('\n') 
albert.split('a')                 # splits on 'a'
['A', 'LBE', 'R ', ' T', 'O',' ',' ', ' '] 
albert.split()     
time.sleep(1)        # no parameter given: splits on whitespace
albert.split('\n')   
time.sleep(0.46)
['R', 'T', 'O ', 'A', 'LBE',' ',' ',' '] 
albert.split('A')  
albert = 'ERTO   ALB'
albert.split('\n') 
print(albert)
time.sleep(0.5)
os.system("cls")
albert.split('A')                 # splits on 'a'
['A', 'LBE', 'R ', ' T', 'O',' ',' ',' '] 
albert = ' BERTO  AL'
albert.split('\n') 
print(albert)
time.sleep(4)
os.system("cls")
