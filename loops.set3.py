# 1. Consecutive Pass Count Definition: 
# A consecutive pass means students pass one after another without any failure in between. 
# Task: Read marks of N students and 
# find the longest consecutive sequence of students scoring 35 or more. 
# Example Input: 8 40 55 20 36 70 90 15 45
# Example Output: Longest Consecutive Passes =3
n=int(input("enter a num"))
count=0
longest=0
for i in range(n):
    marks=int(input())
    if marks>=35:
        count+=1
        if count>longest:
          longest=count
    else:
      count=0
print("longest consecutive passes",longest)

# 2.Largest Prime Entered Definition: A prime number has exactly two positive divisors. 
# Task: Read N numbers and print the largest prime.
# Example Input: 6 12 17 21 29 18 7 
# Example Output: Largest Prime = 29
n=int(input("enter no.of elements:"))
largest=0
for i in range(n):
    num=int(input("enter numbers"))
    if n>0:
        prime=True
        for j in range(2,num):
            num%j==0
            prime=False
            break
        if num>largest:
            largest=num
if num==0:
    print("number not found")
else:
    print("largset prime =",largest)

#3.Sum of Even Digits Definition: Even digits are 0,2,4,6,8.4827316
# Task: Read a number and print the sum of even digits. 
# Example Input: 4827316 Example Output: 20

num=int(input("enter a number:"))
sum=0
while num>0:
    digit=num % 10
    if digit %2==0:
      sum=sum+digit
    num=num//10
print("sum of digits",sum)

# 4.Factory Quality Check Definition: Quality below 50 is defective. 
# Task: Read N scores and print defective and good counts. 
# Example Input: 6 45 60 72 38 80 49 
# Example Output: Defective = 3 Good = 3
n= int(input("enter a num:"))
defcount=0
gudcount=0
for i in range (n):
    num=int(input("enter a number:"))
    if num < 50:
        defcount+=1
    else:
        gudcount+=1
print("defctive",defcount)
print("good",gudcount)

# 5.Maximum Sales Increase Definition: Increase is today's sales minus yesterday's.
# Task: Find the maximum increase between consecutive days.
# Example Input: 5 100 130 110 180 200
# Example Output: Maximum Increase = 70

n=int(input("enter a number:"))
sales=[]
for i in range(n):
 sales.append(int(input("enter a number:")))
max_increase = sales[1]-sales[0]
for i in range(1,n):
   increase=sales[i]-sales[i-1]
   if increase>max_increase:
      max_increase=increase
print("max_increase",max_increase)

# 6. Number with Most Digits Definition: Digit count is the number of digits.
# Task: Print the number with the most digits.
#  Example Input: 5 23 9876 105 123456 89 
#  Example Output: 123456
n = int(input("Enter number of values: "))
max_digits = 0
result = 0
for i in range(n):
    num = int(input("Enter a number: "))
    temp = abs(num)
    count = 0
    if temp == 0:
        count = 1
    else:
        while temp > 0:
            count += 1
            temp //= 10
    if count > max_digits:
        max_digits = count
        result = num
print("Number with most digits =", result)


# 7. Count Numbers Divisible by Both 4 and 6 Definition: Such numbers are divisible by 12.
# Task: Count such numbers. 
# Example Input: 6 12 24 18 36 40 48
# Example Output: 4
n=int(input("enter a num:"))
count=0
for i in range(n):
    num=int(input())
    if num % 4==0 and num%6==0:
        count+=1
print("count",count)

# 8.Longest Odd Streak Definition: An odd streak is consecutive odd numbers.
# Task: Find the longest odd streak. 
# Example Input: 8 3 5 8 7 9 11 4 13
# Example Output: 3
n=int(input("enter a num:"))
count=0
longest=0
for i in range(n):
  num=int(input())
  if num % 2 !=0:
        count+=1
        if count>longest:
         longest=count
  else:
     count=0
print("longest",longest)

# 9.Smallest Digit Sum Definition: Digit sum is the sum of a number's digits. 
# Task: Print the number with the smallest digit sum.
#  Example Input: 4 123 81 44 70 
#  Example Output: 70
n=int(input())
result=0
smallest_sum=99999

for i in range(n):
  num=int(input())
  temp=num
  sum=0

  while temp>0:
   digit=num%10
   sum=sum+digit
   temp=temp//10

   if sum<smallest_sum:
      smallest_sum=sum
      result=num
print("smallest_sum",result)
 
# 10. Running Balance Definition: Running balance updates after each transaction. 
# Task: Print balance after each transaction and final balance.
# Example Input: 1000 4 500-200 300-100
# Example Output: Balance=1500 Balance=1300 Balance=1600 Balance=1500 Final Balance=1500

balance = int(input("Enter initial balance: "))
n = int(input("Enter number of transactions: "))
for i in range(n):
    transaction = int(input("Enter transaction: "))
    balance = balance + transaction
    print("Balance =", balance)
print("Final Balance =", balance)