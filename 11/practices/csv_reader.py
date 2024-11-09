import csv

def get_next_result(cvs_file, func):
    for stats in csv.DictReader(cvs_file):
        yield func(stats)
