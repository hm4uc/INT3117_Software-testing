import unittest
from bonus import bonus

# Kiểm thử với độ phủ C2
class TestBonus(unittest.TestCase):

    # Path 1
    def test_negative_year(self):
        with self.assertRaises(ValueError):
            bonus(-1, True)

    # Path 2
    def test_miss_target(self):
        self.assertEqual(bonus(1, False), 0)

    # Path 3
    def test_0_year_meet_target(self):
        self.assertEqual(bonus(0, True), 5000000)

    # Path 4
    def test_2_years_meet_target(self):
        self.assertEqual(bonus(2, True), 10000000)

    # Path 5
    def test_5_years_meet_target(self):
        self.assertEqual(bonus(5, True), 15000000)

if __name__ == "__main__":
    unittest.main()
