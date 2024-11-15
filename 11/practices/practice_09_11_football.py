import csv


# def parse_next_line(cvs_file):
#     for line in csv.DictReader(cvs_file):
#         yield line

# def get_name_and_diff(team_stats):
#     diff = abs(int(team_stats["Goals For"]) - int(team_stats["Goals Against"]))
#     return team_stats["Team"], diff

def get_next_name_and_diff(cvs_file):
    for team_stats in csv.DictReader(cvs_file):
            diff = abs(int(team_stats["Goals For"]) - int(team_stats["Goals Against"]))
            yield team_stats["Team"], diff

def get_min_score_diff(filename):
    with open(path) as csv_file:
        return min(get_next_name_and_diff(csv_file), key=lambda x: x[1])

if __name__ == "__main__":
    path = "/home/vinotq/college/programming/python/11/practices/football.csv"
    print(*get_min_score_diff(path))
