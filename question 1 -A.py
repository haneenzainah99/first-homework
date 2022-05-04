#question1 A
graduate=['haneen','ali','ward','leen','noor']
name=input('enter your name please ...')
for i in range(len(graduate)):
    if name in graduate:
        print(   '\U0001F60D   GRADUATED')
    else:
        print('   \U0001F642    FAILD')
