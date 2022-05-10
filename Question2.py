num=int(input('enter the decimal number :'))
bin=[]
while num>=1:
    bin.append(num%2)
    num=num//2
bin.reverse()
for num in bin:
    print(num)
