from data_getter import CalendarChallenge


"""
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
https://adventofcode.com/2022/day/1
"""


class CalorieCounter(CalendarChallenge):
    def __init__(self, advent_day: int = 1) -> None:
        super().__init__(advent_day)

    def _convert_numstr(self, numstr: str):
        try:
            num = int(numstr)
        except ValueError:
            num = 0

        return num

    def _split_data(self) -> None:
        self.elf_list = []
        calorie_list = [elf.split("\n") for elf in self._get_data().split("\n\n")]
        for calories_carried in calorie_list:
            self.elf_list.append([self._convert_numstr(food_item) for food_item in calories_carried])

    def _sum_calories(self) -> None:
        self.elf_list = [sum(food_items) for food_items in self.elf_list]

    def _get_most_calorific_elf(self) -> None:
        max_cals = max(self.elf_list)

        print(f"Elf {self.elf_list.index(max_cals)} is a hungry lad carrying {max_cals} calories.")

    def _get_top_three(self) -> None:
        top_three_elves = sum(sorted(self.elf_list, reverse=True)[0:3])

        print(f"The top three elves are carrying {top_three_elves} calories total.")

    def count_cals(self) -> None:
        self._split_data()
        self._sum_calories()
        self._get_most_calorific_elf()
        self._get_top_three()
        

def main():
    cntr = CalorieCounter(advent_day=1)
    cntr.count_cals()
    

if __name__ == '__main__':
    main()
