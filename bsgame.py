import math
import random

print("Hey there, Think of any number in your mind and I will try to guess the number in the least number of questions from you.")
print("You only have you give me a range of number, no restrictions on the range.")
print("Are you ready?")
resp = input('Enter "y" for "Yes, "n" for "No":')
if resp == "y":
    ran = input("Now, think of any number and give me its range as <first number, last number>(both inclusive):").split(",")
    l  = list(range(int(ran[0]), int(ran[1])))
    ans_steps = math.log(len(l), 2)
    print("I will tell the number you thought in maximum of", int(ans_steps//1)+1,"questions of Yes/No type.")
    print("Now I will ask you some questions, based on that I will tell what number you thought.")
    while len(l)!=1:
        mid = len(l)//2
        gos = random.randint(0,1)
        if gos == 0:
            option_g = input("Is the number greater than or equal to {} ? (y/n):".format(l[mid])).lower().strip()=="y"
            if option_g:
                l=l[mid:]
            else:
                l=l[:mid]
        if gos == 1:
            option_s = input("Is the number smaller than {} ? (y/n):".format(l[mid])).lower().strip()=="y"
            if option_s:
                l=l[:mid] 
            else:
                l=l[mid:]         
    print("The number you have thought is",l[0])
    print("Thank you for playing the game from my creators side: Vaibhavi Tiwari & Pratham Bhalla")
if resp == "n":
    print("Thank you for trying me. Have a nice day!")
