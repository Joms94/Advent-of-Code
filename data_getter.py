import requests as rq
import datetime
from aoc_sesh import AOC_SESSION
import os


"""
Gets puzzle input from the "Advent of Code" site.
1. If no input file is present in current directory, scrape site and save contents to file.
2. Read contents of input file and store as string.
"""


class CalendarDataGetter(object):
    def __init__(self, advent_day: int) -> None:
        self.current_year = datetime.date.today().year
        self.advent_day = advent_day
        self.input_url = (
            f"https://adventofcode.com/{self.current_year}/day/{self.advent_day}/input"
        )
        self.saved_input_fname = (
            f"aoc_input_{self.current_year}_day_{self.advent_day}.txt"
        )

    def get_data(self) -> str:
        if not os.path.exists(self.saved_input_fname):
            self.input_data = rq.get(
                self.input_url, cookies={"session": AOC_SESSION}, headers={"user-agent": "github.com/Joms94/Advent-of-Code-2022/blob/main/data_getter.py by Joms94"
            ).text
            with open(self.saved_input_fname, "w") as data_to_write:
                data_to_write.write(self.input_data)

        with open(self.saved_input_fname, "r") as data_to_read:
            self.input_data = data_to_read.read()

        return self.input_data


def main(advent_day: int = 1):
    aoc_data_getter = CalendarDataGetter(advent_day=advent_day)
    aoc_data_getter.get_data()


if __name__ == "__main__":
    main(1)
