import random


class Fifties:
    def start_game(self):
        dice = Dice()
        roll_again = True
        while dice.has_fives() and roll_again:
            dice.roll()
            print("\nYou rolled: ", dice.dies)
            print("Your score is: ", dice.score)
            roll_again = input("Roll again? [y/n] ") in ['y']


class Dice:
    def __init__(self):
        self.dies = [5]
        self.score = 0

    def roll(self):
        for i in range(5):
            die = random.randint(1, 6)
            self.dies.append(die)
        self.score += self.dies.count(5) * 50

    def has_fives(self):
        return self.dies.count(5) > 0


if __name__ == "__main__":
    fifties = Fifties()
    fifties.start_game()
