import random

rps = ["Rock", "Paper", "Sissor"]
p1 = rps[random.randint(0,2)].lower()
p2 = input("Player please choose your gesture!\n").lower()
if p2 != "" and (p2 == "rock" or p2 == "paper" or p2 == "sissor"):
    print("Computer is "+p1)
    if (p1 == "rock" and p2 == "sissor") or (p1 == "paper" and p2 == "rock") or (p1 == "sissor" and p2 == "paper"):
        print("Computer wins!")
    elif (p1 == p2):
        print("Draw!")
    else:
        print("Player wins!")
else:
    print("Something wrong!")

# p1 = input("Player1 please choose your gesture!\n")
# if p1 != "" and (p1 == "Rock" or p1 == "Paper" or p1 == "Sissor"):
#     p2 = input("Player2 please choose your gesture!\n")
#     if p2 != "" and (p2 == "Rock" or p2 == "Paper" or p2 == "Sissor"):
#         if (p1 == "Rock" and p2 == "Sissor") or (p1 == "Paper" and p2 == "Rock") or (p1 == "Sissor" and p2 == "Paper"):
#             print("Player1 Wins!")
#         elif (p1 == p2):
#             print("Draw!")
#         else:
#             print("Player2 Wins!")
#     else:
#         p2 = input("Player2 please choose proper a gesture again!\n")
# else:
#     p1 = input("Player1 please choose a proper gesture! again!\n")