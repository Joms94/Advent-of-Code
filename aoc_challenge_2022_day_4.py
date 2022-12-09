from data_getter import CalendarChallenge


class CleanupCrew(CalendarChallenge):
    def __init__(self, advent_day: int=4) -> None:
        super().__init__(advent_day)
        self.elf_pairs = self._get_data().splitlines()
        self.elf_ranges = []
        self.subset_existence = []

    def _convert_pairs_to_nums(self):
        for pair_ind, elf_pair in enumerate(self.elf_pairs):
            self.elf_ranges.append([list(range(*[int(bound) for bound in elf.split("-")])) for elf in elf_pair.split(",")])
            for idx, elf in enumerate(elf_pair.split(",")):
                if int(elf.split("-")[0]) == int(elf.split("-")[1]):
                    self.elf_ranges[pair_ind][idx] = [str(elf.split("-")[0])]

    def _add_extra_range_index(self):
        for range_pair in self.elf_ranges:
            for ind in range(0, 2):
                try:
                    range_pair[ind].append(range_pair[ind][-1]+1)
                except IndexError:
                    pass
                except TypeError:
                    # Single-number ranges have been made strings so as to trip this error and not append anything.
                    range_pair[ind] = [int(range_pair[ind][0])]

    def _check_for_containment(self, fully_engulfed: bool = True):
        for idx, range_pair in enumerate(self.elf_ranges):
            elf_1 = set(range_pair[0])
            elf_2 = set(range_pair[1])
            if not elf_1 or not elf_2:
                print(idx, elf_1, elf_2)
                continue
            elif fully_engulfed:
                if elf_1.issubset(elf_2) or elf_2.issubset(elf_1):
                    self.subset_existence.append("True")
            else:
                if elf_1.intersection(elf_2):
                    self.subset_existence.append("True")

        print(len(self.subset_existence))

    def reorganise_cleanup_crews(self, fully_engulfed: bool):
        self._convert_pairs_to_nums()
        self._add_extra_range_index()
        self._check_for_containment(fully_engulfed=fully_engulfed)


def main():
    crew = CleanupCrew()
    crew.reorganise_cleanup_crews(False)


if __name__ == "__main__":
    main()
