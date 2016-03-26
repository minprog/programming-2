#!/usr/bin/env python
# Name:
# Student Number:
'''
Clean up and merge two CSV files.
'''
import csv

CRIME_CSV = 'massachusetts-crime.csv'
UNEMPLOYMENT_CSV = 'massachusetts-unemployment.csv'
OUTPUT_CSV = 'cleaned-merged.csv'


def load_table(csv_file_name):
    '''
    Load a CSV file, return a list of dictionaries (mapping columname to value)
    '''
    with open(csv_file_name, 'rb') as f:
        table = list(csv.DictReader(f))

    return table


def clean_up_crime_table(table):
    '''
    Clean massachusetts-crime.csv .

    inputs: <table> a list of dictionaries representing all cities in
            Massachussets for which crime statistics are available.
    '''
    clean = []  # Cleaned-up rows go into this list

    for row in table:
        # IMPLEMENT YOUR ROW CLEANING HERE:

        # 1) Remove the comma from the numbers in the Population column
        # 2) Remove the MA from the city names in the City column
        # 3) Look for other inconsistensies, fix them. Document your
        #    choices in cleanup_justifications.pdf.

        clean.append(row)

    return clean


def clean_up_unemployment_table(table):
    '''
    Clean massachusetts-unemployment.csv .

    inputs: <table> a list of dictionaries representing all cities in
            Massachussets for which unemployment statistics are available.
    '''
    clean = []  # Cleaned-up rows go into this list

    for i, row in enumerate(table):
        # IMPLEMENT YOUR ROW CLEANING HERE:

        # 1) Remove the MA from the city names in the City column
        # 2) Look for other inconsistensies, fix them. Document your
        #    choices in cleanup_justifications.pdf.

        clean.append(row)

    return clean


def merge_tables(table1, table2):
    '''
    Merge clean massachusetts-unemployment.csv and massachusetts-crime.csv .

    Note:
    - The tables are merged on the city names.
    - This function consumes table1 and table2!
    '''
    # YOU CAN SAFELY IGNORE THE DETAILS OF WHAT IS HAPPENING HERE:
    # (these are dictionary comprehensions, need at least Python 2.7)
    empty1 = {key: '' for key in table1[0].keys()}
    del empty1['City']
    empty2 = {key: '' for key in table2[0].keys()}
    del empty2['City']

    indexed1 = {row['City']: row for row in table1}
    indexed2 = {row['City']: row for row in table2}

    out = []

    # Merge the rows from the two tables (needs to deal with things that are
    # only in either table and those that are in both.
    for city, row in indexed1.iteritems():
        if city in indexed2:  # in both
            missing_columns = indexed2[city].copy()
            del missing_columns['City']
            del indexed2[city]
        else:  # only in table 1
            missing_columns = empty2

        new_row = row.copy()
        new_row.update(missing_columns)
        out.append(new_row)

    for city, row in indexed2.iteritems():  # only in table 2
        new_row = row.copy()
        new_row.update(missing_columns)
        out.append(new_row)

    # return both the merged tables and the full header
    return out, ['City'] + empty1.keys() + empty2.keys()

if __name__ == '__main__':
    # You don't have to change anything below.
    ct = clean_up_crime_table(load_table(CRIME_CSV))
    ut = clean_up_unemployment_table(load_table(UNEMPLOYMENT_CSV))
    all_rows, header = merge_tables(ct, ut)

    # Save the complete CSV file:
    with open(OUTPUT_CSV, 'wb') as f:
        writer = csv.DictWriter(f, header)
        # NO HEADER IS WRITTEN TO THE OUTPUT CSV FILE. LOOK UP THE
        # DOCUMENTATION TO THE csv MODULE IN THE PYTHON STANDARD
        # LIBRARY AND MAKE SURE THAT THE HEADER IS WRITTEN TO THE
        # OUTPUT.
        writer.writerows(all_rows)
