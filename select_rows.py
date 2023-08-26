import argparse
import csv
import sys

def onepointtwo(source_file, target_file, col, val):
    with open(source_file, 'r') as src, open(target_file, 'w', newline='') as tgt:
        reader = csv.DictReader(src)
        writer = csv.DictWriter(tgt, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            if row.get(col) == val:
                writer.writerow(row)

def main():
    parser = argparse.ArgumentParser(description='Filter rows in a CSV file based on a specific column value.')
    parser.add_argument('source_file', help='path to the source CSV file')
    parser.add_argument('target_file', help='path to the target CSV file')
    parser.add_argument('column_name', help='name of the column to filter')
    parser.add_argument('field_value', help='value to filter on')
    args = parser.parse_args()

    source_file = args.source_file
    target_file = args.target_file
    column_name = args.column_name
    field_value = args.field_value

    onepointtwo(source_file, target_file, column_name, field_value)

if __name__ == "__main__":
    main()
