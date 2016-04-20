'''
Created on Apr 19, 2016

@author: SELVARAJC
'''

from traviscitest import operations


class TestCoverage:

    def test_coverage(self):

        actual = operations.plus(1, 2)
        expected = 3

        assert expected == actual

    def test_completecoverage(self):

        actual = operations.minus(3, 2)
        expected = 1

        assert expected == actual

    def test_divide(self):

        actual = operations.divide(6, 2)
        expected = 3

        assert expected == actual
