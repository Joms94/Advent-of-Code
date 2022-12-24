from data_getter import CalendarChallenge
import sys


class PacketInterpreter(CalendarChallenge):
    def __init__(self, advent_day: int = 6) -> None:
        super().__init__(advent_day)
        self.packets = self._get_data()
        self.unique_occurrence_positions = list()

    def _packet_clause(self, ind: int, upper_bound: int):
        if len(set(self.packets[ind : ind + upper_bound])) != upper_bound:
            pass
        else:
            print(self.packets[ind : ind + upper_bound])
            print(ind + upper_bound)
            sys.exit()

    def get_markers(self, find_message: bool = False):
        for ind, letter in enumerate(self.packets):
            if not find_message:
                self._packet_clause(ind=ind, upper_bound=4)
            else:
                self._packet_clause(ind=ind, upper_bound=14)


def main():
    radio = PacketInterpreter()
    radio.get_markers(find_message=True)


if __name__ == "__main__":
    main()
