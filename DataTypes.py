#Create two boolean variables, is_sunny and is_weekend, and assign them values. Print both variables
is_sunny=False
is_weekend=True
print("is_sunny:"+str(is_sunny))
print("is_weekend:"+str(is_weekend))
#create an integer variable num and assign it a value. Calculate the remainder when num is divided by 3 and print the result   
num=34
result=num%3
print( "the remainder when "+str(num) +" is divided by 3 =" +str(result))

#Create an integer variable base and exponent. Calculate the result of raising base to the power of exponent and print the result.
base=4
exponent=5
result=base**exponent
print(result)
# here the base is 4 and exponent is 5 and finally the base to the power of exponent is 1024 
print(" here the base is "+str(base)+" and exponent is "+ str(exponent)+" and finally the base to the power of exponent is " +str(result))
# Create two integer variables dividend and divisor. Perform integer division and print the result.
dividend=10
divisor=3
result=dividend//divisor
print(result)
#here the dividend is 10 and divisor is 3 and finally when dividend divided by divisor is 3
print(" the dividend is "+str(dividend)+" and divisor is "+str(divisor )+" and finally when dividend divided by divisor is "+str(result))
print(f"#here the dividend is {str(dividend)}and divisor is {str(divisor)} and finally when dividend divided by divisor is {str(result)}")

#Create an integer variable count with an initial value of 10. Increment the value of count by 1 in three different ways and print the result each time.
count=10
result=count+1



#Create two float variables, float1 and float2, and assign them values. Perform addition, subtraction, multiplication, and division, then print the results.
float1=4.3
float2=10.1
print(float1+float2)
print(float1-float2)
print(float1*float2)
print(float1/float2)


#Create a float variable number and assign it a value with many decimal places. Round this number to two decimal places and print the result.

float=4.344567
result=round(float,2)
print(result)



#Create two float variables numerator and denominator. Perform division and print the result.

numerator=40.3
denominator=10.1
result=numerator/denominator
print(result)


#Create an integer variable int_num and a float variable float_num. Add them together and print the result.

int_num=10
float_num=4.3
result=int_num+float_num
print(result)

#Create two float variables part and whole. Calculate the percentage of part relative to whole and print the result.

discounted=5389
original=5649
result=(discounted/original)*100
print(int(result))

#WORKING WITH STRINGS 
num="25"
num2="34"
result=num+num2
result2=int(num)+int(num2)
print(result2)

madhav="sahithi"
name=madhav

age=22
beautiful=True

study="btech"
#hi this is sahithi iam 22 years old and if you say iam beautiful girl its true and iam studing btech 
print("hi this is " +madhav+" iam "+str(age)+" years old and if you say iam beautiful girl its "+str(beautiful)+" iam studing "+study )

print("i love you madhav"*10000000)
