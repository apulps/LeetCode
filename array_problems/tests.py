import unittest
from remove_duplicates import remove_duplicates, remove_duplicates_2


class TestEasyProblems(unittest.TestCase):
    def test_remove_duplicates(self):
        nums = [1,1,2]
        result = remove_duplicates(nums)
        self.assertEqual(result, 2)
        self.assertEqual(nums, [1,2])

        nums = [0,0,1,1,1,2,2,3,3,4]
        result = remove_duplicates(nums)
        self.assertEqual(result, 5)
        self.assertEqual(nums, [0,1,2,3,4])

        nums = [1,1]
        result = remove_duplicates(nums)
        self.assertEqual(result, 1)
        self.assertEqual(nums, [1])
    
    def test_remove_duplicates_2(self):
        nums = [1,1,2]
        result = remove_duplicates_2(nums)
        self.assertEqual(result, 2)
        self.assertEqual(nums, [1,2])

        nums = [0,0,1,1,1,2,2,3,3,4]
        result = remove_duplicates_2(nums)
        self.assertEqual(result, 5)
        self.assertEqual(nums, [0,1,2,3,4])

        nums = [1,1]
        result = remove_duplicates_2(nums)
        self.assertEqual(result, 1)
        self.assertEqual(nums, [1])



if __name__ == '__main__':
    unittest.main()