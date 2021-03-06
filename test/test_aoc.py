import os
os.chdir('../')

import aoc_7
import aoc_8
import aoc_9
import aoc_10

class Test_AdventOfCode():


    def test_day7a(self):

        assert aoc_7.day7a(aoc_7.prep_data(r'test/aoc7a_test.txt'), 'shiny gold') == 4


    def test_day7b(self):

        assert aoc_7.day7b(aoc_7.prep_data(r'test/aoc7b_test.txt'), 'shiny gold') == 126


    def test_day8a(self):

        assert aoc_8.day8a(aoc_8.prep_data(r'test/aoc8.txt')) == 5


    def test_day8b(self):

        assert aoc_8.day8b(aoc_8.prep_data(r'test/aoc8.txt')) == 8


    def test_day9a(self):

        assert aoc_9.day9a(aoc_9.prep_data(r'test/aoc9.txt'), preamble=5) == 127


    def test_day9b(self):

        assert aoc_9.day9b(aoc_9.prep_data(r'test/aoc9.txt'), preamble=5) == 62


    def test_day10a(self):

        assert aoc_10.day10a(aoc_10.prep_data(r'test/aoc10.txt')) == 220

    def test_day10b(self):

        assert aoc_10.day10b(aoc_10.prep_data(r'test/aoc10.txt')) == 8