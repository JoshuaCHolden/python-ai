import tempfile
from pandas import read_csv
import csv


class Utils:

    @staticmethod
    # convert a csv filepath to a panda read_csv dataset object, takes a csv with headers
    def get_dataset_from_csv(csv_):
        with open(csv_, newline='') as f:
            original_file = csv.reader(f)
            names = next(original_file)
            with tempfile.NamedTemporaryFile(mode='w') as temp_csv:
                wr = csv.writer(temp_csv, dialect='excel')
                for row in original_file:
                    wr.writerow(row)
                temp_csv.flush()
                return read_csv(temp_csv.name, names=names)
