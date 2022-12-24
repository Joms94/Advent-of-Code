from data_getter import CalendarChallenge


"""
What would your total score be if everything goes exactly according to your strategy guide?
https://adventofcode.com/2022/day/2
"""


class Strategiser(CalendarChallenge):
    def __init__(self, advent_day: int = 2) -> None:
        super().__init__(advent_day)

        # Listed: value this draws with, value this beats, value this loses to, and the score for selecting it.
        self.score_dict = {
            "X": ["A", "C", "B", 1], # Rock
            "Y": ["B", "A", "C", 2], # Paper
            "Z": ["C", "B", "A", 3] # Scissors
        }
        self.LOSE = 0
        self.DRAW = 3
        self.WIN = 6

    def _get_input_games(self):
        self.games = [game.replace(" ", "") for game in self._get_data().split("\n")]
        self.games.pop(-1)

    def _part_one_calculation(self):
        score = 0
        for game in self.games:
            opposing_choice = game[0]
            my_choice = game[1]
            score_dict_vals = self.score_dict[my_choice]
            draw_condition = score_dict_vals[0]
            win_condition = score_dict_vals[1]
            lose_condition = score_dict_vals[2]

            if lose_condition == opposing_choice:
                score += self.LOSE
            if draw_condition == opposing_choice:
                score += self.DRAW
            if win_condition == opposing_choice:
                score += self.WIN
            score += score_dict_vals[3] # Points earned purely from choice of hand gesture.

        print(f"Score for part one: {score}.")

    def _part_two_calculation(self):
        score = 0
        # Listed: value the key draws with, value it beats and value it loses to.
        opposition_map = {
            "A": ["A", "C", "B"], # Rock
            "B": ["B", "A", "C"], # Paper
            "C": ["C", "B", "A"] # Scissors
        }
        strategy_map = {
            "X": 1, # Lose
            "Y": 0, # Draw
            "Z": 2 # Win
        }
        shape_map = {
            "A": 1,
            "B": 2,
            "C": 3
        }
        for game in self.games:
            my_strategy = strategy_map[game[1]] # Int that gets passed into index of opposition_map
            opposing_choice = game[0]
            my_choice = opposition_map[opposing_choice][my_strategy]
            if my_strategy == 0:
                score += self.DRAW
            if my_strategy == 2:
                score += self.WIN
            if my_strategy == 1:
                score += self.LOSE

            score += shape_map[my_choice]

        print(f"Score for part two: {score}.")
            
    def score(self):
        self._get_input_games()
        self._part_one_calculation()
        self._part_two_calculation()


def main():
    strat_scorer = Strategiser()
    strat_scorer.score()


if __name__ == "__main__":
    main()
