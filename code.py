import random
x = random.randint(0,101)

def intro():
    print("Welcome to he guessing game \n "
          "I have a Number between 0 to 100 in my mind \n"
          " Try guessing  it \n Good luck")

def achivement(flag):
    if flag<3:
        print("Woow!!! You are a fucking psychic")
    elif flag>3 and flag <8:
        print("Cool ,You got it in {} guesses".format(flag))
    elif flag >8 and flag<12:
        print("finally done ,in {} tries".format(flag))
    else :
        print("You want some more tries ,you Dumb tard ,you took {} tries".format(flag))

guess =[0]


def run():
    flag = 0
    a = int(input(" Guess the number  "))
    if a == x:
        print("yes Its {}".format(x))

    flag += 1
    while True:
        a = int(input(" wrong. go again  "))
        if a == x:
            print("yes Its {}".format(x))
            break
        elif a < 0 or a > 100:
            print("Out of Bound,Dude")

        guess.append(a)
        if guess[-2] and abs(guess[-1]-x)<10:
            if abs(x - a) < abs(x - guess[-2]):
                print("warmer")
            elif abs(a - x) > abs(x - guess[-2]):
                print("colder")
        else:
            if abs(a - x) <= 10:
                print('Garam ')
            else:
                print('Thanda')
        flag += 1
    return flag

intro()
achivement(run())
