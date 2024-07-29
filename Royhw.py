seen = set()
print("Please enter 7 numbers:")
for i in range(7):
    num = int(input())
    if num in seen:
        print('YES')
    else:
        print('NO')
        seen.add(num)
# for that code, you have to press enter for 7times to get Yes or No answer.


test_str = str(input())
count = 0
 
for i in test_str:
    if i == 'a':
        count = count + 1
print(count)

while True:
    A = input("enter a sentence: ") 
    if "a" in A:
        print(A.count('a'))
    else:
        print("no")    
    break

list1 = input()
list2 = input()
same_number = set(list1).intersection(list2)
if same_number:
    print("same number found:", ", ".join(same_number))
else:
    print("meh, there is no same numbers on those two lists.")






num1 = int(input("How many languages can you speak?: "))
lan1 = set()
for _ in range(num1):
    language = input("What languages can you speak in?: ").strip().lower()
    lan1.add(language)
num2 = int(input("How many languages can you speak?: "))
lan2 = set()
for _ in range(num2):
    language = input("What languages can you speak in?: ").strip().lower()
    lan2.add(language)
num3 = int(input("How many languages can you speak?: "))
lan3 = set()
for _ in range(num3):
    language = input("What languages can you speak in?: ").strip().lower()
    lan3.add(language)
common_languages = lan1 & lan2 & lan3
if common_languages:
    print("Common languages:", common_languages)
else:
    print("There are no languages that can be spoken by all people.")

