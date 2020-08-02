import random

class DiceDecorator():
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)

    def setGame(self):
        game = self
        return game

    def criticalRoll(self):
        print("NATURAL 20")

    def roll(self,game):
        rollCount = ((self.split("d")[0]))
        diceType = ((self.split("d")[1]))
        rolls = int(rollCount)

        # Check the split values are correct
        # print(rollCount)
        # print(diceType)

        values = []
        while int(rolls) > 0:
            toss = random.randint(1,int(diceType))
            if game.lower() == "monopoly":
                # print(toss)
                values.append(toss)
            elif game.lower == "dnd":
                if toss == 20 and int(diceType) == 20:
                    DiceDecorator.criticalRoll(self)
                else:
                    print(toss)
            else:
                print(toss)
            rolls -= 1
        return values

@DiceDecorator
def function(game, dice):
    print("{}, {}".format(DiceDecorator.setGame(game), dice))
    if game.lower() == "monopoly":
        values = DiceDecorator.roll(dice,game)
        if values[0] == values[1]:
            print('DOUBLES: ' + str(tuple(values)))
            print("Roll Again!\n")
            function(game,dice)
        else:
            print(tuple(values))
    else:
        DiceDecorator.roll(dice,game)

input_game = input("What Game are you playing?\n")
if input_game.lower() == "monopoly":
    function(input_game,"2d6")
    while True:
        user_input = input("Roll Again? (Yes or No)\n")
        if user_input.lower() == "no":
            break
        function(input_game, "2d6")
elif input_game.lower() == "dnd":
    input_dice_roll = input("What type of dice are you rolling?\n"+"(d4,d6,d8,d10,d12,d20)\n")
    input_how_many_dice = input("How many of the type of dice are you rolling?\n")
    function(input_game, str(input_how_many_dice+input_dice_roll))
else:
    raise("Unknown Game")


