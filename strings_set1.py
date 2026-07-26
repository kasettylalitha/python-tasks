# 1. Count Uppercase and Lowercase Letters Definition:
# Uppercase letters are A–Z and lowercase letters are a–z. 
# Task: Read a string and print the number of uppercase and lowercase letters.
# Example Input: PyTHon 
# Example Output: Uppercase = 3 Lowercase = 3
str=input("enter a  string")
uppercase=0
lowercase=0
for char in str:
    if char>='A'and char<='Z':
        uppercase+=1
    elif char>='a' and char <='z':
        lowercase+=1
print("Uppercase=",uppercase)
print("Lowercase=",lowercase)

# 2. Longest Word Length Definition: A word is a sequence of characters separated by spaces.
# Task: Read a sentence and print the length of the longest word.
# Example Input: Python is amazing
# Example Output: 7 
# 
words=input("enter a sentence:")
count=0
max_count=0
for ch in words:
    if ch !=' ':
        count+=1
    else:
         if count>max_count:
             max_count=count
         count=0   
if  count>max_count:
     max_count=count
print("max word=",max_count)

# 3.Count Vowels in Even Positions Definition: Vowels are a, e, i, o, u. 
# Task: Count vowels present at even index positions.
# Example Input: Education
# Example Output: 3

s=input("enter a word:")
count=0
for i in range(len(s)):
    if i%2 ==0:
        if s[i].lower() in "aeiou":
            count+=1
print("count",count)
    

# 4. Consecutive Duplicate Characters Definition:
# Consecutive duplicate characters appear one after another. 
# Task: Count consecutive duplicate character pairs. 
# Example Input: bookkeeper
# Example Output: 3

s=input("enter a string:")
count=0
for i in range (len(s)-1):
    if s[i]==s[i+1]:
        count+=1
print(" Consecutive Duplicate Characters=",count)

# 5. First Non-Repeating Character Definition:
# A non-repeating character appears exactly once. 
# Task: Print the first non-repeating character or Not Found.
# Example Input: swiss Example Output: w
s=input("enter a string")
found = False
for ch in s:
    count=0
    for c in s:
        if ch==c:
            count+=1
    if count==1:
        print(ch)
        found=True
        break
if found==False:
    print("not found")


# 6. Longest Consecutive Vowel Sequence Definition:
# A vowel sequence is consecutive vowels.
# Task: Find the longest consecutive vowel sequence.
# Example Input: beaautiful 
# Example Output: 3

s=input("enter a string:")
count=0
lon_count=0
for ch in (s):
    if ch.lower() in 'aeiou':
     count+=1
     if count>lon_count:
        lon_count=count
    else:
       count=0
print("longest count=",lon_count)

# 7. Character Frequency Definition: Frequency is the number of occurrences.
# Task: Read a string and a character. Count its occurrences. 
# Example Input: programming g.
# Example Output: 2

s=input("enter a string:")
ch = input("Enter a character: ")
count=0
for c in (s):
    if c == ch:
        count+=1
print("frequency=",count)

# 8. Mirror String Check Definition: A palindrome reads the same forwards and backwards.
# Task: Check whether the string is a palindrome. 
# Example Input: madam 
# Example Output: Palindrome

s=input("enter a string:")
reverse=""
for ch in s:
    reverse=ch+reverse
if s==reverse:
    print("palindrome")
else:
    print("not palindrome")

# 9. Largest Alphabet Definition: The largest alphabet has the highest alphabetical order.
# Task: Print the largest alphabet ignoring digits and symbols.
# Example Input: Pyth0n@Z 
# Example Output: Z 10. Compres
s = input()
largest = ''
for ch in s:
    if ch.isalpha():
        if largest == '' or ch.upper() > largest.upper():
            largest = ch
print(largest)

# 10. Compress Consecutive Characters Definition: 
# Replace repeated consecutive characters with character followed by count.
# Task: Compress the string.
# Example Input: aaabbccccd 
# Example Output: a3b2c4d1

s = input("Enter a string: ")
result = ""
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        result = result + s[i] + str(count)
        count = 1
result = result + s[-1] + str(count)
print(result)