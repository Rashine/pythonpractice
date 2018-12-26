# task = ["Install Python3", "Learn python", "Take a break"]
# print(type(task.clear()))

# number = [1,2,3,4,5]
# number[0:0] = ["aaa","bbb","ccc"]
# print(number)
# print (len(number))

# number2 = [1,2,3,4,5]
# number2.extend(["aaa","bbb","ccc"])
# print(number2)
# print (len(number2))

# num = [1,2,3,4,5]
# print ([x*20 for x in num])

abbb = ["a" if x%2==0 else "b" if x%3==0 else "c" for x in range(1, 7)]
print (abbb)

print([[n for n in range(1,4)] for b in range(1,4)])