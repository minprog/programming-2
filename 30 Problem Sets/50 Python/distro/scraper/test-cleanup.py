#!/usr/bin/env python
'''
Test data clean-up Python exercise.
'''
import unittest
import csv

import cleanup


class CheckCSV(unittest.TestCase):
    def setUp(self):
        with open(cleanup.OUTPUT_CSV, 'rb') as f:
            self.rows = list(csv.DictReader(f))

    def test_population_column(self):
        # test that the Population column is clean
        for row in self.rows:
            self.assertNotIn(',', row['Population'])

    def test_for_MA(self):
        # test that the ', MA' is no longer present
        for row in self.rows:
            self.assertNotIn(', MA', row['City'])

    def test_n_columns(self):
        # test that each of the columns is present, and that
        # all rows are the same length
        n_columns = set()
        for row in self.rows:
            n_columns.add(len(row))

        self.assertEquals(len(n_columns), 1)
        self.assertEquals(n_columns.pop(), 21)


class CheckCrimeClenaup(unittest.TestCase):
    def setUp(self):
        with open(cleanup.CRIME_CSV, 'rb') as f:
            self.rows = list(csv.DictReader(f))

    def test_crime_cleanup(self):
        length_before = len(self.rows)
        ct = cleanup.clean_up_crime_table(self.rows)
        self.assertEquals(length_before, len(ct))


class CheckUnemploymentCleanup(unittest.TestCase):
    def setUp(self):
        with open(cleanup.UNEMPLOYMENT_CSV, 'rb') as f:
            self.rows = list(csv.DictReader(f))

    def test_unemployment_clenaup(self):
        length_before = len(self.rows)
        ct = cleanup.clean_up_unemployment_table(self.rows)
        self.assertEquals(length_before, len(ct))

if __name__ == '__main__':
    print 'Test the data clean-up using Python exercise.'
    print 'Note: this script checks only those things already mentioned in'
    print 'the exercise, there are more things you could do to clean up the'
    print 'the data.'

    # Check the main constraints mentioned in the exercise:
    suite1 = unittest.TestLoader().loadTestsFromTestCase(CheckCSV)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(CheckCrimeClenaup)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(CheckUnemploymentCleanup)
    alltests = unittest.TestSuite([suite1, suite2, suite3])
    unittest.TextTestRunner().run(alltests)

    # Put out some additional statistics (used in grading):
    with open(cleanup.OUTPUT_CSV, 'rb') as f:
        rows = list(csv.reader(f))
    print '\nNumber of rows in table: ', len(rows)
