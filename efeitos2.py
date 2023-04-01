#Python Typing Text Effect - www.101computing.net/python-typing-text-effect/
import time,os,sys

from time import sleep
import subprocess

string = "GROUNDFORCE" # Whatever string you want

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
    
typingPrint("GROUNDFORCE   \n")
time.sleep(1)
albert = 'GROUNDFORCE   '
albert.split('a')                 # splits on 'a'
['G', 'ROU', 'N', ' D', 'F','O ',' R', ' C' ,'E'] 
print(albert)
time.sleep(0.05)
os.system("cls")
albert.split('L')                 # splits on 'a'
['ROU', 'N', 'D ', ' F', 'O', 'R ', ' C', 'E ','G '] 
albert.split('B')  
print(albert)
time.sleep(0.75)
os.system("cls")             # splits on 'a'
albert = 'FORCE  GROUND'
albert.split('\n') 
time.sleep(2)
os.system("cls")
albert.split('L')                 # splits on 'a'
['ROUND', 'F', 'O ', ' R', 'C', 'E ', ' ', ' ','G'] 
albert.split('B')  
print(albert)
time.sleep(2)
os.system("cls")             # splits on 'a'
['R', 'C', 'E ', 'G', 'ROUN',' D',' F','O '] 
albert.split('A')  
albert = 'RCE   GROUNDFO'
albert.split('\n') 
print(albert)
time.sleep(2)
os.system("cls")
albert.split('L')                 # splits on 'a'
['G', 'ROUND', 'F ', ' O', 'R', 'C','E',' '] 
albert = 'G  ROUNDFORCE'
print(albert)
time.sleep(0.5)
os.system("cls")
albert.split('L')                 # splits on 'a'
['ROUND', 'F', 'O', ' R', 'C', 'E', 'G', ' ',' '] 
albert.split('B')  
print(albert)
time.sleep(2)
os.system("cls")             # splits on 'a'
['O','R', 'C', 'E', 'G', 'ROUN','D','F'] 
albert = 'GROUNDFO   RCE'
print(albert)
time.sleep(0.2)
os.system("cls")           # splits on 'a'
['F','O','R', 'C', 'E ', 'G', 'ROUND'] 
albert = '  GROUNDF ORCE'
print(albert)
time.sleep(2.75)
os.system("cls")
albert.split('E')                 # splits on 'a'
['RCE', 'G', 'R ', ' O', 'U','N','D','F','O'] 
albert = 'F ORCEGROUND   '
print(albert)
time.sleep(2.5)
albert.split('R')  
time.sleep(1)
os.system("cls")
albert.split('E')       # no parameter given: splits on whitespace
albert = 'RCE  GROUNDFO'
albert.split('\n') 
print(albert)
time.sleep(2.5)
albert.split('A')     
time.sleep(2)
albert.split('E') 
time.sleep(1)
os.system("cls")     # no parameter given: splits on whitespace
albert = 'GROUNDFO RCE'
albert.split('\n') 
print(albert)
albert.split()     
time.sleep(1 ) 

os.system("cls")     # no parameter given: splits on whitespace
albert = 'OUND   FORCEGR'
albert.split('\n') 
print(albert)
time.sleep(1)
os.system("cls")  
albert = 'ND FORCEGROU'
albert.split('\n') 
print(albert)
time.sleep(1)
os.system("cls")
albert.split()     
time.sleep(1) 

os.system("cls")      
albert = 'D   FORCEGROUN'
albert.split('\n') 
albert.split('E')               # splits on '\n' only
albert = 'RCE GROUND FO'
albert.split('\n') 
albert.split('a')                 # splits on 'a'
['G', 'ROUND', 'F ', 'O', 'R','C ',' E', ' '] 
albert.split()     
time.sleep(1)        # no parameter given: splits on whitespace
albert.split('\n')   
time.sleep(0.46)
['G', 'R', 'O ', 'UND', 'FO', 'RCE' ,'',' '] 
albert.split('A')  
albert = 'FORCE   GROUND'
albert.split('\n') 
print(albert)
time.sleep(0.5)
os.system("cls")
albert.split('G')                 # splits on 'a'
['G', 'ROUND', 'F ', ' O', 'RCE',' ',' ',' '] 
albert = ' FORCE GROUND'
albert.split('\n') 
print(albert)
time.sleep(4)
os.system("cls")
