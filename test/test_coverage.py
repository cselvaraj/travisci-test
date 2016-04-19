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
