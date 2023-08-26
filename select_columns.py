import argparse
import csv
import sys

def onepointone(source_file, target_file, cols):
    with open(target_file, 'w', newline='') as tgt:
        writer = csv.writer(tgt)

        with open(source_file, 'r') as src:
            reader = csv.reader(src)

            #find the indices of the columns to be selected
            header_row = next(reader)
            col_indices = [header_row.index(col) for col in cols]

            #write the selected columns as header
            selected_header = [header_row[i] for i in col_indices]
            writer.writerow(selected_header)

            #write rows with selected columns
            for row in reader:
                selected_row = [row[i] for i in col_indices]
                writer.writerow(selected_row)

def main():
    parser = argparse.ArgumentParser(description='Copy CSV data from source to target with specific columns.')
    parser.add_argument('source_file', help='path to the source CSV file')
    parser.add_argument('target_file', help='path to the target CSV file')
    parser.add_argument('columns', nargs='+', help='list of column names')
    args = parser.parse_args()

    source_file = args.source_file
    target_file = args.target_file
    columns = args.columns

    onepointone(source_file, target_file, columns)


main()
