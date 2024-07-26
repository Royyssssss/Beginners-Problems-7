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
    if i == 'e':
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

