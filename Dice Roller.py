#SOUVIK DEY
import random
def roll_dice(num_dice):
    """Return a list of integers with length `num_dice`.

    Each integer in the returned list is a random number between
    1 and 6, inclusive.
    """
    roll_results = []
    for i in range(num_dice):
        r = random.randint(1, 6)
        roll_results.append(r)
    return roll_results
ans=True
while(ans):
    num_dice= int(input("How many dice do you want to roll? [1-6] "))
                
    # 2. Roll the dice
    roll_results = roll_dice(num_dice)
    print("Result of the roll ")
    print(roll_results)
    ans=input("Do you want to play again?(Y/N): ")
    if(ans=="Y"):
        ans=True
    else:
        ans=False
