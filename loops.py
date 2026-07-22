# 1. Count Passing Students Task: Read marks of N students. 
# Count how many scored 35 or more.
# Example Input: 5 45 20 67 35 18 Example Output: 3


n= int(input("enter the number :"))
count = 0
for i in range (n):
    marks=int(input("enter marks :"))
    if marks>=35:
        count+=1
print(count)

# 2.Shop Profit Days Task: Read profit for N days.
# Count days with profit greater than Rs.1000.
# Example Input: 5 800 1200 1500 950 2000 Example Output: 3
n= int(input("enter number of days:"))
countdays=0
for i in range(n):
    profit=int(input("enter the profit:"))
    if profit>1000:
        countdays+=1
print(countdays)

# 3.Largest Multiple of 5 Task: Read N numbers. 
# Print the largest divisible by 5, else 'No Multiple of 5'. 
# Example Input: 5 12 25 18 40 7 Example Output: 40
# 
n = int(input("Enter the number of elements: "))
largest = 0
found = False
for i in range(n):
    num = int(input("Enter a number: "))
    if num % 5 == 0:
        if found == False or num > largest:
            largest = num
            found = True
if found:
    print(largest)
else:
    print("No Multiple of 5")

# 4.Average of Even Numbers Task: Read N numbers.
# Print average of even numbers, else 'No Even Numbers'.
# Example Input: 5 2 5 8 7 10 Example Output: Average = 6.67

n=int(input("enter the numbers:"))
sum=0
count=0
for i in range (n):
    num=int(input("enter a numbers:"))
    if num % 2==0:
        sum=sum+num
        count=count+1
if count>1:            
    ave=sum/count
    print(ave)
else:
    print("no even numbers")



# 5.Student Improvement Task: Read marks in N tests.
#  Count how many times marks increased.
#  Example Input: 5 50 55 52 60 70 Example Output: 3
n = int(input("Enter the number of tests: "))
count = 0
prev = int(input("Enter marks: "))
for i in range(1, n):
    marks = int(input("Enter marks: "))
    if marks > prev:
        count = count + 1
    prev = marks
print(count)

# 6.Divisors Count Task: Read a number and count its divisors.
# Example Input: 12 Example Output: 6
n=int(input("enter anumber:"))
count=0
for i in range(1,n+1):
    if n % i==0:
        count+=1
print(count)

# 7.Smallest Odd Number Task: Read N numbers. 
# Print smallest odd number or 'No Odd Number'. 
# Example Input: 5 8 13 6 5 10 Example Output: 5

n=int(input("enter a number"))
smallest=0
found=False
for i in range (n):
    num=int(input("enter a number:"))
    if num % 2!=0:
        if found==False or num<smallest:
         smallest=num
         found=True
if found:
   print("smallest odd number",smallest)
else:
   print("no odd number")


# 8.Count Numbers Ending with 7 
# Task: Read N numbers.Count numbers ending with digit 7. 
# Example Input: 5 27 15 97 120 47 Example Output: 3
n=int(input("enter a number"))
count=0
for i in range (n):
    num=int(input("enter a number:"))
    if num % 10==7:
       count+=1
print(count)

# 9.Multiplication Table Task: Read a number and print table from 1 to 15.
# Example Input: 7Example Output: 7 x 1 = 7 ... 7 x 15 = 105
for i in range (1,11):
    print ("table of",i)
    for j in range(1,11):
        print( i, "x" , j ,"=" ,i * j)

# 10. Sum Until Negative Number Task: Read numbers until a negative number is entered.
# Print sum of positive numbers.
# Example Input: 5 10 8 2-1 Example Output: 25
sum=0
while True:
    num=int(input("enter a number:"))
    if num <0:
        break
    elif num >0:
        sum=sum+num
print(sum)