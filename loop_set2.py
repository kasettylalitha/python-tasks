# 1. Highest Profit Month Definition: Find the maximum value and its position while reading inputs. 
# Task: A shop owner records the profit for N months. 
# Print the highest profit and its month number. Example Input: 5 12000 15000 9800 17500 16000
# Example Output: Highest Profit = 17500 Month = 4
n=int(input("enter a months:"))
month=1
highest=int(input("enter profit :"))
for i in range(2,n+1):
   profit=int(input("enter a profit:"))
   if profit > highest:
      highest=profit
      month=i
print(highest)
print(month)

#2. Perfect Square Counter Definition: A perfect square is the square of an integer.
# Task: Read N numbers and count how many are perfect squares.
# Example Input: 5 16 20 25 18 49 Example Output: 3
n=int(input("enter the numbers:"))
count=0
for i in range (n):
    num=int(input("enter the  num:"))
    root=int(num**0.5)
    if root*root==num:
        count+=1
print("perfect square = ",count)

# 3.Sum of Multiples of 7 Definition: Multiples of 7 are numbers divisible by 7.
# Task: Read A and B. Sum all multiples of 7 between them. 
# Example Input: 10 35 Example Output: 84

firstnum=int(input("enter an 1num :"))
secondnum=int(input("enter a 2num :"))
sum=0
for i in range(firstnum,secondnum+1):
    if i%7==0:
        sum=sum+i
print(sum)


# 4. Longest Positive Streak Definition: A streak is consecutive values satisfying a condition. 
# Task: Read N numbers and find the longest positive streak. 
# Example Input: 8 5 7-2 4 9 10 12-5 Example Output: 4
n=int(input("enter a number:"))
count=0
max=0
for i in range(n):
    num=int(input("enter a number:"))
    if num>0:
        count+=1
        if count>max:
            max=count
    else:
        count=0
print(max)

# 5. Count Numbers with Exactly Three Divisors Definition: 
# Some numbers have exactly three positive divisors.
# Task: Read N numbers and count them. 
# Example Input: 5 4 9 8 16 25 Example Output: 3

n=int(input("enter a num:"))
count = 0
for i in range(n):
    num = int(input())
    divisors = 0
    for j in range(1, num + 1):
        if num % j == 0:
            divisors += 1
    if divisors == 3:
        count += 1
print(count)

# 6.Largest Difference Definition: Difference is the gap between two values.
# Task: Find the largest difference between consecutive inputs.
# Example Input: 5 10 25 18 40 32 Example Output: 22
n = int(input())
previous = int(input())
max = 0
for i in range(2, n + 1):
    current = int(input())
    difference = abs(current - previous)
    if difference > max:
        max = difference
    previous = current
print(max)

# 7.Salary Bonus Definition: Employees below a threshold qualify.
# Task: Count salaries below Rs.30000. 
# Example Input: 5 25000 40000 18000 32000 29000 Example Output: 3

n = int(input("Enter number of employees: "))
count = 0
for i in range(n):
    salary =int(input("Enter salary: "))
    if salary < 30000:
        count += 1
print("Count =", count)

# 8.Largest Digit Sum Definition: Digit sum is the sum of all digits.
# Task: Print the number having the largest digit sum. 
# Example Input: 4 123 98 555 71 Example Output: 555


n = int(input("Enter number of values: "))
max_sum = 0
result = 0
for i in range(n):
    num = int(input("Enter number: "))
    temp = num
    digit_sum = 0
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp //= 10
    if digit_sum > max_sum:
        max_sum = digit_sum
        result = num
print(result)

# 9.Average Until Zero Definition: Average equals total divided by count.
# Task: Read numbers until 0 and print the average. 
# Example Input: 8 12 20 0 Example Output: 13.33

sum=0
count=0
while True:
    num=int(input("enter a number:"))
    if num==0:
        break
    sum+=num
    count+=1
ave=sum/count
print(ave)

# 10. Count Numbers Greater Than Average Definition:
# Compare values with the calculated average.
# Task: Read N numbers, compute average, then count numbers above it. 
# Example Input: 5 10 20 30 40 50 Example Output: 2
n=int(input("enter anumber:"))
sum=0
for i in range (n):
    num=int(input())
    sum=sum+num
ave=sum/n
count=0
if num>ave:
    count+=1
print(count)