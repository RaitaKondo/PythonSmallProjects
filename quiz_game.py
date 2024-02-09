print("hello world")

playing = input("Do you wanna play? ")

if playing.lower() != "yes":
    quit()

score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect..")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect..")

answer = input("What does RAM stands for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect..")

answer = input("What does PSU stands for? ").lower()
if answer == "power supply":
    print("Correct!")
    score+=1
else:
    print("Incorrect..")

print("Your score is " + str(score) + "!")
print("You've got " + str(score / 4 * 100) + "%.")
