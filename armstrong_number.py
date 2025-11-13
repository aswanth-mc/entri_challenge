
# check whether a given number is an Armstrong number or not

n =(input('enter a number : '))

a=len(n)
num=int(n)
temp=num
sum=0

while num !=0:
    digit=num%10
    sum+=(digit **a)
    num=num//10

if sum == temp:
    print(temp,"is a armstrong number")
else:
    print(temp, "is not a armstrong number")


#Write a program that prints all Armstrong numbers in a given range.

lower=int(input("enter the lowest limit : "))
upper=int(input("enter the upper limit"))

for i in range(lower,upper+1):
    l=len(str(i))
    sum=0
    temp=i

    while temp >0:
        digit=temp%10
        sum+=(digit **l)
        temp=temp//10

    if i==sum:
        print(i)

    