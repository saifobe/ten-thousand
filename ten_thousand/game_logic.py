import random
from collections import Counter

class GameLogic():
    def __init__(self):
        pass

    @staticmethod
    def validate_keepers(roll, keepers):
        """
        A function for determining if the dice a user wants to keep is valid.
        validate_keepers(roll, keepers): Returns a boolean

        """
        roll_counter = Counter(roll)
        keepers_counter = Counter(keepers)
        for i in keepers_counter:
            if keepers_counter[i] > roll_counter[i]:
                return False
        return True
    
    @staticmethod
    
    def get_scorers(input):
        """
        A function for determining the dice that are scoring.
        get_scorers(input): Returns a tuple

        """
        
        input_counter = Counter(input)
        scoring_dice = []
        if input_counter[1] >= 1 and input_counter[1] < 3:
            scoring_dice.append(1)
        if input_counter[5] >= 1 and input_counter[5] < 3:
            scoring_dice.append(5)
        if input_counter[1] == 3:
            scoring_dice.append(1)
        for i in range(2, 7):
            if input_counter[i] == 3:
                scoring_dice.append(i)
        if len(input_counter) == 3 and all(value == 2 for value in input_counter.values()):
            return input
        return tuple(scoring_dice)
    

        
    @classmethod
    def calculate_score(cls,tupleroll):
        """
        A class for calculating the score of a given roll in a dice game.
        calculate_score(cls, tupleroll): Calculates the score of a given roll and returns it as an integer

        """
        unbanked_points = 0
        new_counter = Counter(tupleroll)

        if new_counter[1] >= 1 and new_counter[1] < 3:
            unbanked_points += 100 * new_counter[1]

        if new_counter[5] >= 1 and new_counter[5] < 3:
            unbanked_points += 50 * new_counter[5]

        if new_counter[1] == 1 and new_counter[2] == 1 and new_counter[3] == 1 and new_counter[4] == 1 and new_counter[5] == 1 and new_counter[6] == 1:
            return 2000
        
        

        if new_counter[1] == 3:
            unbanked_points += 1000
        for i in range(2, 7):
            if new_counter[i] == 3:
                unbanked_points += i * 100
        

        if new_counter[1] == 4:
            unbanked_points += 2000
        # if new_counter[2] == 4:
        #     unbanked_points += 400
        # if new_counter[3] == 4:
        #     unbanked_points += 600
        # if new_counter[4] == 4:
        #     unbanked_points += 800
        # if new_counter[5] == 4:
        #     unbanked_points += 1000
        # if new_counter[6] == 4:
        #     unbanked_points += 1200
        for i in range(2, 7):
            if new_counter[i] == 4:
                unbanked_points += i * 200

        if new_counter[1] == 5:
            unbanked_points += 4000
        for i in range(2, 7):
            if new_counter[i] == 5:
                unbanked_points += i * 400

        if new_counter[1] == 6:
            unbanked_points += 8000
        for i in range(2, 7):
            if new_counter[i] == 6:
                unbanked_points += i * 800

        
        if len(new_counter) == 3 and all(value == 2 for value in new_counter.values()):
            unbanked_points = 1500

        if len(new_counter) == 2 and len(set(new_counter.values())) == 1 and list(set(new_counter.values()))[0] == 3:
            unbanked_points = unbanked_points*2
           
        
        
        return unbanked_points
    
    @staticmethod
    def roll_dice(num_dice):
        """
        A static method for rolling a given number of dice.
        roll_dice(num_dice): Rolls a given number of dice and returns the result as a tuple of integers

        """
        return tuple(random.randint(1, 6) for _ in range(num_dice))
    
    


if __name__ == "__main__":
    
    game = GameLogic()
    print(game.roll_dice(6))
    print(game.calculate_score((5,)))  # 50



