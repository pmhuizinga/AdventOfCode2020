import os
os.chdir('../')

import aoc_7


class Test_AdventOfCode():


    def test_day7a(self):

        assert aoc_7.day7a(aoc_7.prep_data(r'test/aoc7a_test.txt'), 'shiny gold') == 4


    def test_day7b(self):

        assert aoc_7.day7b(aoc_7.prep_data(r'test/aoc7b_test.txt'), 'shiny gold') == 126