import csv_reader
from numbers import Number

def get_name_and_diff(team_stats: dict) -> tuple:
    if "Team" not in team_stats or "Goals For" not in team_stats or "Goals Against" not in team_stats:
        raise KeyError(f"File missing columns!")

    if isinstance(team_stats["Team"], (str, Number)):
        raise TypeError(f"Team name must be a string!")


    diff = abs(int(team_stats["Goals For"]) - int(team_stats["Goals Against"]))
    return team_stats["Team"], diff

def get_min_score_diff(filename):
    with open(path) as csv_file:
        return min(csv_reader.get_next_result(csv_file, get_name_and_diff), key=lambda x: x[1])

if __name__ == "__main__":
    path = "/home/vinotq/college/programming/python/11/practices/football.csv"
    print(*get_min_score_diff(path))
