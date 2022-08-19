import random
# Snake Water Gun or Rock Paper Scissors
def gameWin(comp,player):
    if comp == player:
        return None
    elif comp == 's':
        if player == 'w':
            return False
        elif player =='g':
                return True
    elif comp == 'w':
        if player == 'g':
            return False
        elif player =='s':
                return True

    elif comp == 'g':
        if player == 's':
            return False
        elif player =='w':
                return True


# pass: it means the function is empty


print("Comp's Turn: Snake(s) Water(w) Gun(g)?")
randNo = random.randint(1,3)

if randNo==1:
    comp = 's'
elif randNo==2:
    comp = 'w'
elif randNo==3:
    comp = 'g'

player = input("Player's Turn: Snake(s) Water(w) Gun(g)?")
c = gameWin(comp,player)

print(f"Computer choose {comp}")
print(f"Player choose {player}")

if  c == None:
    print("The game is tied")
elif c:
    print("You Win!")
else:
    print("You Lose!")
