Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

import json
dict={}
while True:
    Q1=input('what is your name ?')
    Q2=input('How old are you ?')
    Q3=input('Where are you from  ?')
    Q4=input('Whats your family name  ?')
    Q5=input('Whats your address  ?')
    Q6=input('what is your phone number ?')
    Q7=input('When were you born  ?')
    Q8=input('Are you married  ?')
    Q9=input('what is your job  ?')
    Q10=input('Have you got a car  ?')
    dict[Q1]={'Name':Q1,'Age':Q2,'place':Q3,'family':Q4,'address':Q5,'phone':Q6,'born':Q7,'married?':Q8,'job':Q9,'car':Q10}
    con=input('continue ..?')
    if con.lower()=='y':
        continue
    else:
        break
s=json.dumps(dict)
with open('data.json','w') as f:
    f.write(s)