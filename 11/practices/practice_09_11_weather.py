import csv

def get_day_and_avg_temp(cvs_file):
    for day_stats in csv.DictReader(cvs_file):
        day_number = int(day_stats["Day"])
        avg = (int(day_stats["MxT"]) + int(day_stats["MnT"])) / 2
        yield day_number, avg

def get_max_avg_temp(filename):
    with open(filename) as csv_file:
        return max(get_day_and_avg_temp(csv_file), key=lambda x: x[1])

if __name__ == "__main__":
    path = "/home/vinotq/college/programming/python/11/practices/weather.csv"
    print(*get_max_avg_temp(path))

