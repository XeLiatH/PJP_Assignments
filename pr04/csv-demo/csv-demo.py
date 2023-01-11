"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above,
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
"""
import csv
import pprint
import re

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

TMASK = re.compile('(\d{4})-\d{2}-\d{2}T.+')


def check_year(year):
    """
    check if year is betwwen 1886 and 2014
    """
    if 1886 <= year <= 2014:
        return True
    return False


def process_file(input_file):
    """
    parse and split the input file
    """
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        good_data = []
        bad_data = []
        for row in reader:
            if row['URI'].startswith("http://dbpedia.org/"):
                try:
                    try:
                        year = int(TMASK.findall(row["productionStartYear"])[0])
                    except IndexError:
                        raise ValueError("bad year")
                    else:
                        if check_year(year):
                            row["productionStartYear"] = year
                            good_data.append(row)
                        else:
                            raise ValueError("bad year")
                except ValueError:
                    bad_data.append(row)

        return good_data, bad_data, header                

  
def write_result(filename, data, header):
    """
    write result to file
    """
    with open(filename, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames=header)
        writer.writeheader()
        for row in data:
            writer.writerow(row)



def test():

    good, bad, header = process_file(INPUT_FILE)
    write_result(OUTPUT_GOOD, good, header)
    write_result(OUTPUT_BAD, bad, header)


if __name__ == "__main__":
    test()