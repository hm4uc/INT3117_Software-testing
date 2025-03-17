import unittest
from bonus import bonus

# Kiểm thử với độ phủ all-uses
class TestBonus(unittest.TestCase):

    # TC 01
    def test_negative_year(self):
        with self.assertRaises(ValueError):
            bonus(-1, True)

    # TC 02
    def test_0_year_meet_target(self):
        self.assertEqual(bonus(0, True), 5000000)

    # TC 03
    def test_2_years_meet_target(self):
        self.assertEqual(bonus(2, True), 10000000)

    # TC 04
    def test_5_years_meet_target(self):
        self.assertEqual(bonus(5, True), 15000000)
    # TC 05
    def test_miss_target(self):
        self.assertEqual(bonus(1, False), 0)


if __name__ == "__main__":
    unittest.main()
