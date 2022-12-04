from data_getter import CalendarChallenge
import string


"""
Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
https://adventofcode.com/2022/day/3
"""


class RucksackManager(CalendarChallenge):
    def __init__(self, advent_day: int = 3) -> None:
        super().__init__(advent_day)
        self.compartmentalised_rucksacks = []
        self.score = 0
        self.score_dict = dict()
        for ind, letter in enumerate(string.ascii_letters):
            self.score_dict[letter] = ind + 1

    def _get_sack_contents(self):
        self.rucksacks = self._get_data().split("\n")[:-1]

        # Checking for any odd-length rucksacks that might trip me up.
        for ind, rucksack in enumerate(self.rucksacks):
            if (len(rucksack) % 2) != 0:
                print(f"Warning! Rucksack {ind} has an odd number of elements.")

    def _get_rucksack_compartments(self):
        for rucksack in self.rucksacks:
            compartment_capacity = int(len(rucksack) / 2)
            compartment_1 = set(rucksack[:compartment_capacity])
            compartment_2 = set(rucksack[compartment_capacity:])

            self.compartmentalised_rucksacks.append([compartment_1, compartment_2])

    def _find_commonality(self):
        self.common_contents = []
        for compartments in self.compartmentalised_rucksacks:
            self.common_contents.append(
                list(compartments[0].intersection(compartments[1]))
            )

    def _score_sacks_by_compartment(self):
        for common_content in self.common_contents:
            for content in common_content:
                self.score += self.score_dict[content]

        print(f"Sum of priority scores for every compartment: {self.score}")

    def _get_three_sack_groups(self):
        self.grouped_sacks = []
        for ind, rucksack in enumerate(self.rucksacks):
            if (ind % 3) == 0:
                self.grouped_sacks.append(self.rucksacks[ind - 3 : ind])
        sackcount = len(self.rucksacks)
        self.grouped_sacks.append(self.rucksacks[sackcount - 3 : sackcount])
        self.grouped_sacks = self.grouped_sacks[1:]

        # Have I goofed up the grouping?
        for ind, group in enumerate(self.grouped_sacks):
            if len(group) != 3:
                print(f"Warning! Rucksack {ind} does not contain three sacks.")

    def _score_sacks_by_group(self):
        sack_group_content = []
        grouped_score = 0
        for group in self.grouped_sacks:
            sack_group_content.append(
                set(group[0]).intersection(set(group[1]), set(group[2]))
            )

        for commonality in sack_group_content:
            for item in commonality:
                grouped_score += self.score_dict[item]

        print(f"Sum of priority scores for grouped compartments: {grouped_score}")

    def organise_rucksacks(self):
        self._get_sack_contents()
        self._get_rucksack_compartments()
        self._find_commonality()
        self._score_sacks_by_compartment()
        self._get_three_sack_groups()
        self._score_sacks_by_group()


def main():
    caravan = RucksackManager()
    caravan.organise_rucksacks()


if __name__ == "__main__":
    main()
