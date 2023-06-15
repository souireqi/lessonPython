from random import *
user = input("choose item: ")
list = ["R","P","S"]
AA = choice(list)
print(AA)
if AA == "R" and user == "R":
    print("draw")
if AA == "P" and user == "S":
    print("you win")
if AA == "S" and user == "P":
    print("you lose")
if AA == "S" and user == "S":
    print("draw")
if AA == "P" and user == "P":
    print("draw")
if AA == "S" and user == "R":
    print("you win")
if AA == "R" and user == "P":
    print("you win")
if AA == "P" and user == "R":
    print("you lose")
if AA == "R" and user == "S":
    print("you lose")