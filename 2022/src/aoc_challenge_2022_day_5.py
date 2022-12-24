from data_getter import CalendarChallenge


"""
After the rearrangement procedure completes, what crate ends up on top of each stack?
https://adventofcode.com/2022/day/5
"""


class Stackintosh(CalendarChallenge):
    def __init__(self, advent_day: int = 5) -> None:
        super().__init__(advent_day)
        self.all_inputs = self._get_data()
        self.stack_dict = dict()

    def _sift_for_type(self, strelement: str, desired_type: type):
        try:
            desired_type(strelement)
        except ValueError:
            strelement = None

        return strelement

    def _get_stacks(self):
        # Create list representing each row. Clear out parentheses and redundant spaces.
        row_config = [
            [box.replace("[", "").replace("]", "") for box in row][1::2][::2]
            for row in self.all_inputs.split("\n")[:8]
        ]

        # Create a dictionary where the keys are the column numbers and the values are lists of column elements.
        for column in range(0, len(row_config) + 1):
            column_items = []
            for row in row_config:
                column_items.append(row[column])
            self.stack_dict[column + 1] = [item for item in column_items if item != " "]

    def _get_crane_instructions(self):
        self.crane_instructions = [
            [
                int(word)
                for word in instructions.split(" ")
                if self._sift_for_type(word, int) != None
            ]
            for instructions in self.all_inputs.split("\n")[10:-1]
        ]

    def _follow_instructions(self, cratemover_9001_active: bool = False):
        for instruction in self.crane_instructions:
            qty_to_move = instruction[0]
            col_num_to_take_from = instruction[1]
            col_num_to_move_to = instruction[2]

            crates_to_move = self.stack_dict[col_num_to_take_from][:qty_to_move]

            print(
                f"Intending to move the following crates: {crates_to_move} from column {col_num_to_take_from} to {col_num_to_move_to}."
            )

            if cratemover_9001_active == False:
                for crate in crates_to_move:
                    self.stack_dict[col_num_to_move_to].insert(0, crate)
                    self.stack_dict[col_num_to_take_from].remove(crate)
            elif cratemover_9001_active == True:
                self.stack_dict[col_num_to_move_to] = (
                    crates_to_move + self.stack_dict[col_num_to_move_to]
                )
                for crate in crates_to_move:
                    self.stack_dict[col_num_to_take_from].remove(crate)

            print(
                f"Column {col_num_to_move_to} now contains: {self.stack_dict[col_num_to_move_to]}"
            )

        results = "".join([stack[0] for stack in self.stack_dict.values()])
        print(f"Top crate of each stack: {results}")

    def stack(self):
        self._get_stacks()
        self._get_crane_instructions()
        self._follow_instructions(cratemover_9001_active=True)


def main():
    craniac = Stackintosh()
    craniac.stack()


if __name__ == "__main__":
    main()
