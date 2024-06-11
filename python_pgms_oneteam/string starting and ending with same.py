#strings from the list having length more than 2 and startin and ending with same alphabet
n = int(input("Enter the number of names: "))
l = []
for i in range(n):
    item = input("Enter a name: ")
    l.append(item)
count = 0
for item in l:
    if len(item) >= 2:
        if item[0] == item[-1]:
            count += 1
print("Number of strings with length 2 or more and same first and last character:", count)
