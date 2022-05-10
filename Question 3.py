import json
question={}
score=0
numofques=1
student={'The number of bones in the human body is 206':'T',
'5 * 5 equals 16':'F','The largest country in the world is Russia':'T'
,'Geology is the science of the layers of the earth':'T',
'The most powerful type of stone is diamond':'T',
'The unit of measurement for sound intensity is the volt':'F','2 * 2 equals 4':'T','10 * 10 equals 11':'F',
'3*3=9':'T','8*8=16':'F','1*1=2':'F','The root of 4 is 2 ':'T','5**2=25':'T','6*6=36':'T','9*4=7':'F',
'Damascus, the capital of Syria':'T','The capital of Lebanon is Beirut':'T','1+4=5':'T','8+9=10':'F','3+3=6':'T'}
with open('student.json','w') as f:
    json.dump(student,f)
with open('student.json') as v:
    question=json.load(v)

name=input('please enter your name:')
print('welcom',name,'good luck in the test')

for q in question.keys():
    print('Question-',numofques,q)
    res=input('the answer is')
    if res.upper()==question[q].upper():
        score=score+1
        print('well done')
        numofques=numofques+1
    else:
        print('wrong answer')
        numofques=numofques+1
    result={name:score}
    with open('score.json','a')as v:
        result=json.dump(result,v)
