# def say_hi():
#     return "yoooooooooo"
# def aaa(a, b, yoo):
#     print (f"{yoo()} {a} {b}")

# aaa(5,6, say_hi)

# Define speak below:
# howls = dict(pig="oink", duck="quack", cat="meow", dog="woof")
# def speak(animal="dog"):
#     return howls.get(animal, '?')

# print(speak("naa"))
# print(speak("dog"))
# def single_letter_count(s="", l=""):
#     if s and l:
#         return s.count(l)
#     else:
#         return 0
# print (single_letter_count("srgerge", "e"))

# def list_manipulation(l=[], c="", p="", v=None):
#     if l and c and p and (not v):
#         if c.lower() == "remove" and (p.lower() == "end" or p.lower() == "beginning"):
#             if p.lower() == "end":
#                 return l.pop(-1)
#             else:
#                 return l.pop(0)
#         else:
#             return "Please check the arguments ya pass are correct!"
#     else:
#         if c.lower() == "add" and (p.lower() == "end" or p.lower() == "beginning"):
#             if p.lower() == "end":
#                 l.append(v)
#                 return l
#             else:
#                 l[0:0]=[v]
#                 return l
#         else:
#             return "Please check the arguments ya pass are correct!"

# print (list_manipulation([1,2,3], "remove", "end"))
# print (list_manipulation([1,2,3], "add", "end", 10))


# s = "Hello world! kferkgep  rkgoreg "
# c = s.count(" ")
# # .pop(indexofspace[i]) for i in range(len(indexofspace))
# lss = list(s)
# print(lss)
# for i in range(c):
#     lss.remove(" ")

# def is_palindrome(s=""):
#     if s:
#         lss = list(s.lower())
#         temp = lss.count(" ")
#         for i in range(temp):
#             lss.remove(" ")
#         if len(lss)%2 == 0:
#             for i in range(int(len(lss)/2)):
#                 if lss[i] != lss[len(lss)-i-1]:
#                     return False
#             return True
#         else:
#             i = 0
#             while i != (len(lss)-i-1):
#                 if lss[i] != lss[len(lss)-i-1]:
#                     return False
#                 i += 1
#             return True
#     else:
#         print("Please check the argument(s) you passed")
#         return None

# print(is_palindrome("tacocat"))


# def frequency(l=[], v=None):
#     if l and (v or v==0):
#         return l.count(v)
#     else:
#         print("Cheeeeck the arguments you passed")
#         return None

# print(frequency([1,2,2,2,3,3], 2))

'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''
# def isEven(n):
#     return n%2 == 0

# def partition(l=[], fn=isEven):
#     if l and fn:
#         return [[b for b in l if fn(b)], [a for a in l if not fn(a)]]
#     else:
#         return None

# def test_func(b= 0,*args, a = 0, **kwargs):
#     print (a)
#     print (b)
#     print (kwargs)
#     print (args)
# test_func(1,2,3,4,"c",c="fdg", d="ge",a= 20, e="fbf")

# def (s="", **kwa):
#     if s:
#         if kwa:
#             if "prefix" in kwa and "suffix" not in kwa:
#                 return kwa.get("prefix")+s
#             elif "prefix" not in kwa and "suffix":
#                 return kwa.get("suffix")+s
#         else:
#             return s
#     else:
#         return None
# calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
# calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
# def calculate(**trytry):
#     if trytry.get("make_float"): 
#         return trytry.get("message","The result is")+" "+str(float(operate(trytry.get("first"), trytry.get("second"), trytry.get("operation"))))
#     else:
#         return trytry.get("message","The result is")+" "+str(int(operate(trytry.get("first"), trytry.get("second"), trytry.get("operation"))))

# def operate(f,s,o):
#     if o == "add": return f+s
#     elif o == "subtract": return f-s
#     elif o == "multiply": return f*s
#     elif o == "divide": return f/s
#     else: return None
# print (calculate(make_float=False, operation='add', message='You just added', first=2, second=4))

# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     a ={}
#     tn = tuple(nums)
#     for i in range(len(tn)):
#         if target-tn[i] in a:
#             return [a[target-tn[i]], i]
#         else:
#             a[tn[i]] = i

# print(twoSum([3,2,4], 7))


# def remove_negatives(l) : return list(filter(lambda x:x >= 0, l))
# l = [1,2,3,4,5]
# a = map(lambda x : x, l)
# print (type(filter(lambda x : x, l)))


def interleave(s1, s2):
    s = ""
    for ss in zip(*[s1, s2]):
        s = s + ss[0] + ss[1] 
    return s

print(interleave("hi", "ha"))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print (dict(zip(*names)))