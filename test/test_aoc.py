import os
os.chdir('../')

import aoc_7

class Test_AdventOfCode():

    def test_day7a(self):
        testlist = [['bright white', 'shiny gold'],
                    ['muted yellow', 'shiny gold'],
                    ['light red', 'bright white'],
                    ['dark orange', 'bright white'],
                    ['light red', 'muted yellow'],
                    ['dark orange', 'muted yellow']]

        assert aoc_7.day7a(testlist, 'shiny gold') == 4

    def test_day7b(self):
        testlist = [['shiny gold white', 'dark red', 2],
                    ['dark red', 'dark orange', 2],
                    ['dark orange', 'dark yellow', 2],
                    ['dark yellow', 'dark green', 2],
                    ['dark green', 'dark blue', 2],
                    ['dark blue', 'dark violet', 2],
                    ['dark violet', 'no other', 0]]

        assert aoc_7.day7b() == 4