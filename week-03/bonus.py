import unittest

def bonus(year: int, target: bool) -> int:
    if year < 0:
        raise ValueError("year must be >= 0")
    elif 0 <= year < 1:
        return 5000000 if target else 0
    elif 1 <= year < 3:
        return 10000000 if target else 0
    return 15000000 if target else 0 

class bonus_test(unittest.TestCase):

    # Kiểm thử biên (kiểm thử trường hợp xấu nhất)
    def test_bonus_edge_0yr_miss(self):
        self.assertEqual(bonus(0, True), 5000000)
    def test_bonus_edge_0yr_hit(self):
        self.assertEqual(bonus(0, False), 0)
    def test_bonus_edge_1yr_hit(self):
        self.assertEqual(bonus(1, True), 10000000)
    def test_bonus_edge_1yr_miss(self):
        self.assertEqual(bonus(1, False), 0)
    def test_bonus_edge_2yr_hit(self):
        self.assertEqual(bonus(2, True), 10000000)
    def test_bonus_edge_2yr_miss(self):
        self.assertEqual(bonus(2, False), 0)
    def test_bonus_edge_3yr_hit(self):
        self.assertEqual(bonus(3, True), 15000000)
    def test_bonus_edge_3yr_miss(self):
        self.assertEqual(bonus(3, False), 0)
    def test_bonus_edge_4yr_hit(self):
        self.assertEqual(bonus(4, True), 15000000)
    def test_bonus_edge_4yr_miss(self):
        self.assertEqual(bonus(4, False), 0)
    
    
    # Kiểm thử cây quyết định
    def test_bonus_decisiontree_neg_yrs(self):
        with self.assertRaises(ValueError) as context:
            bonus(-1, True)
        self.assertEqual(str(context.exception), "year must be >= 0")
    def test_bonus_decisiontree_0yr_hit(self):
        self.assertEqual(bonus(0, True), 5000000)
    def test_bonus_decisiontree_0yr_miss(self):
        self.assertEqual(bonus(0, False), 0)
    def test_bonus_decisiontree_2yr_hit(self):
        self.assertEqual(bonus(2, True), 10000000)
    def test_bonus_decisiontree_2yr_miss(self):
        self.assertEqual(bonus(2, False), 0)
    def test_bonus_decisiontree_5yr_hit(self):
        self.assertEqual(bonus(5, True), 15000000)
    def test_bonus_decisiontree_5yr_miss(self):
        self.assertEqual(bonus(5, False), 0)
    
if __name__ == "__main__":
    unittest.main()