import unittest
from array_problems.remove_duplicates import remove_duplicates, remove_duplicates_2

from easy_problems.two_sum import two_sum, two_sum_2
from easy_problems.reverse_integer import reverse_integer
from easy_problems.running_sum import running_sum, running_sum_2, running_sum_3
from easy_problems.kids_with_candies import kids_with_candies, kids_with_candies_2
from easy_problems.shuffle import shuffle
from easy_problems.num_identical_pairs import num_identical_pairs
from easy_problems.defang_IP_addr import defang_IP_addr
from easy_problems.num_jewels_in_stones import num_jewels_in_stones, num_jewels_in_stones_2
from easy_problems.number_of_steps import number_of_steps, number_of_steps_2
from easy_problems.shuffle_array import shuffle_array
from easy_problems.smaller_numbers_than_current import smaller_numbers_than_current
from easy_problems.subtract_product_and_sum import subtract_product_and_sum
from easy_problems.decompress_RLE_list import decompress_RLE_list
from easy_problems.max_depth import max_depth

from medium_problems.subrectangle_queries import SubrectangleQueries
from medium_problems.group_the_people import group_the_people
from medium_problems.max_increase_keeping_skyline import max_increase_keeping_skyline


class TestArrayProblems(unittest.TestCase):
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

        nums = []
        result = remove_duplicates(nums)
        self.assertEqual(result, 0)

    
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



class TestEasyProblems(unittest.TestCase):
    def test_two_sum(self):
        nums = [2,7,11,15]
        target = 9
        result = two_sum(nums, target)
        self.assertEqual(result, [0,1])

        nums = [3,2,4]
        target = 6
        result = two_sum(nums, target)
        self.assertEqual(result, [1,2])

        nums = [3,3]
        target = 6
        result = two_sum(nums, target)
        self.assertEqual(result, [0,1])

    def test_two_sum_2(self):
        nums = [2,7,11,15]
        target = 9
        result = two_sum_2(nums, target)
        self.assertEqual(result, [0,1])

        nums = [3,2,4]
        target = 6
        result = two_sum_2(nums, target)
        self.assertEqual(result, [1,2])

        nums = [3,3]
        target = 6
        result = two_sum_2(nums, target)
        self.assertEqual(result, [0,1])


    def test_reverse_integer(self):
        x = 123
        result = reverse_integer(x)
        self.assertEqual(result, 321)

        x = -123
        result = reverse_integer(x)
        self.assertEqual(result, -321)

        x = 120
        result = reverse_integer(x)
        self.assertEqual(result, 21)

        x = 0
        result = reverse_integer(x)
        self.assertEqual(result, 0)


    def test_running_sum(self):
        nums = [1,2,3,4]
        result = running_sum(nums)
        self.assertEqual(result, [1,3,6,10])

        nums = [1,1,1,1,1]
        result = running_sum(nums)
        self.assertEqual(result, [1,2,3,4,5])

        nums = [3,1,2,10,1]
        result = running_sum(nums)
        self.assertEqual(result, [3,4,6,16,17])

    def test_running_sum_2(self):
        nums = [1,2,3,4]
        result = running_sum_2(nums)
        self.assertEqual(result, [1,3,6,10])

        nums = [1,1,1,1,1]
        result = running_sum_2(nums)
        self.assertEqual(result, [1,2,3,4,5])

        nums = [3,1,2,10,1]
        result = running_sum_2(nums)
        self.assertEqual(result, [3,4,6,16,17])

    def test_running_sum_3(self):
        nums = [1,2,3,4]
        result = running_sum_3(nums)
        self.assertEqual(result, [1,3,6,10])

        nums = [1,1,1,1,1]
        result = running_sum_3(nums)
        self.assertEqual(result, [1,2,3,4,5])

        nums = [3,1,2,10,1]
        result = running_sum_3(nums)
        self.assertEqual(result, [3,4,6,16,17])


    def test_kids_with_candies(self):
        candies = [2,3,5,1,3]
        extra_candies = 3
        result = kids_with_candies(candies, extra_candies)
        self.assertEqual(result, [True,True,True,False,True])

        candies = [4,2,1,1,2]
        extra_candies = 1
        result = kids_with_candies(candies, extra_candies)
        self.assertEqual(result, [True,False,False,False,False])

        candies = [12,1,12]
        extra_candies = 10
        result = kids_with_candies(candies, extra_candies)
        self.assertEqual(result, [True,False,True])

    def test_kids_with_candies_2(self):
        candies = [2,3,5,1,3]
        extra_candies = 3
        result = kids_with_candies_2(candies, extra_candies)
        self.assertEqual(result, [True,True,True,False,True])

        candies = [4,2,1,1,2]
        extra_candies = 1
        result = kids_with_candies_2(candies, extra_candies)
        self.assertEqual(result, [True,False,False,False,False])

        candies = [12,1,12]
        extra_candies = 10
        result = kids_with_candies_2(candies, extra_candies)
        self.assertEqual(result, [True,False,True])


    def test_shuffle(self):
        nums = [2,5,1,3,4,7]
        n = 3
        result = shuffle(nums, n)
        self.assertEqual(result, [2,3,5,4,1,7])

        nums = [1,2,3,4,4,3,2,1]
        n = 4
        result = shuffle(nums, n)
        self.assertEqual(result, [1,4,2,3,3,2,4,1])

        nums = [1,1,2,2]
        n = 2
        result = shuffle(nums, n)
        self.assertEqual(result, [1,2,1,2])

    
    def test_num_identical_pairs(self):
        nums = [1,2,3,1,1,3]
        result = num_identical_pairs(nums)
        self.assertEqual(result, 4)

        nums = [1,1,1,1]
        result = num_identical_pairs(nums)
        self.assertEqual(result, 6)

        nums = [1,2,3]
        result = num_identical_pairs(nums)
        self.assertEqual(result, 0)

        nums = []
        result = num_identical_pairs(nums)
        self.assertEqual(result, 0)

    
    def test_defang_IP_addr(self):
        address = "1.1.1.1"
        result = defang_IP_addr(address)
        self.assertEqual(result, "1[.]1[.]1[.]1")

        address = "255.100.50.0"
        result = defang_IP_addr(address)
        self.assertEqual(result, "255[.]100[.]50[.]0")

    
    def test_num_jewels_in_stones(self):
        J = "aA"
        S = "aAAbbbb"
        result = num_jewels_in_stones(J, S)
        self.assertEqual(result, 3)

        J = "z"
        S = "ZZ"
        result = num_jewels_in_stones(J, S)
        self.assertEqual(result, 0)

    def test_num_jewels_in_stones_2(self):
        J = "aA"
        S = "aAAbbbb"
        result = num_jewels_in_stones_2(J, S)
        self.assertEqual(result, 3)

        J = "z"
        S = "ZZ"
        result = num_jewels_in_stones_2(J, S)
        self.assertEqual(result, 0)

    
    def test_number_of_steps(self):
        num = 14
        result = number_of_steps(num)
        self.assertEqual(result, 6)

        num = 8
        result = number_of_steps(num)
        self.assertEqual(result, 4)

        num = 123
        result = number_of_steps(num)
        self.assertEqual(result, 12)

    def test_number_of_steps_2(self):
        num = 14
        result = number_of_steps_2(num)
        self.assertEqual(result, 6)

        num = 8
        result = number_of_steps_2(num)
        self.assertEqual(result, 4)

        num = 123
        result = number_of_steps_2(num)
        self.assertEqual(result, 12)

    
    def test_shuffle_array(self):
        s = "aiohn"
        indices = [3,1,4,2,0]
        result = shuffle_array(s, indices)
        self.assertEqual(result, "nihao")

        s = "aaiougrt"
        indices = [4,0,2,6,7,3,1,5]
        result = shuffle_array(s, indices)
        self.assertEqual(result, "arigatou")

        s = "art"
        indices = [1,0,2]
        result = shuffle_array(s, indices)
        self.assertEqual(result, "rat")

        s = "abc"
        indices = [0,1,2]
        result = shuffle_array(s, indices)
        self.assertEqual(result, "abc")

    
    def test_smaller_numbers_than_current(self):
        nums = [8,1,2,2,3]
        result = smaller_numbers_than_current(nums)
        self.assertEqual(result, [4,0,1,1,3])

        nums = [6,5,4,8]
        result = smaller_numbers_than_current(nums)
        self.assertEqual(result, [2,1,0,3])

        nums = [7,7,7,7]
        result = smaller_numbers_than_current(nums)
        self.assertEqual(result, [0,0,0,0])
        

    def test_subtract_product_and_sum(self):
        n = 234
        result = subtract_product_and_sum(n)
        self.assertEqual(result, 15)

        n = 4421
        result = subtract_product_and_sum(n)
        self.assertEqual(result, 21)

        n = 450
        result = subtract_product_and_sum(n)
        self.assertEqual(result, -9)

    
    def test_decompress_RLE_list(self):
        nums = [1,2,3,4]
        result = decompress_RLE_list(nums)
        self.assertEqual(result, [2,4,4,4])

        nums = [1,1,2,3]
        result = decompress_RLE_list(nums)
        self.assertEqual(result, [1,3,3])


    def test_max_depth(self):
        s = "(1+(2*3)+((8)/4))+1"
        result = max_depth(s)
        self.assertEqual(result, 3)

        s = "(1)+((2))+(((3)))"
        result = max_depth(s)
        self.assertEqual(result, 3)

        s = "1+(2*3)/(2-1)"
        result = max_depth(s)
        self.assertEqual(result, 1)

        s = "1"
        result = max_depth(s)
        self.assertEqual(result, 0)



class TestMediumProblems(unittest.TestCase):
    def test_subrectangle_queries(self):
        subrectangle_queries = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
        result = subrectangle_queries.get_value(2,2)
        self.assertEqual(result, 1)

        result = subrectangle_queries.get_value(1,0)
        self.assertEqual(result, 4)

        result = subrectangle_queries.get_value(3,1)
        self.assertEqual(result, 1)

        subrectangle_queries.update_subrectangle(0,0,1,2,100)
        result = subrectangle_queries.get_value(0,1)
        self.assertEqual(result, 100)

        subrectangle_queries.update_subrectangle(2,0,2,2,90)
        result = subrectangle_queries.get_value(2,1)
        self.assertEqual(result, 90)

        subrectangle_queries.update_subrectangle(3,0,3,2,80)
        result = subrectangle_queries.get_value(3,1)
        self.assertEqual(result, 80)

        subrectangle_queries = SubrectangleQueries([[6,9,6,1,2],[8,8,6,5,9],[7,6,10,8,2],[7,7,4,9,1]])
        subrectangle_queries.update_subrectangle(1,4,2,4,5)
        result = subrectangle_queries.get_value(3,4)
        self.assertEqual(result, 1)

        subrectangle_queries.update_subrectangle(3,4,3,4,8)
        result = subrectangle_queries.get_value(2,0)
        self.assertEqual(result, 7)

    def test_subrectangle_queries_2(self):
        subrectangle_queries = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
        result = subrectangle_queries.get_value(2,2)
        self.assertEqual(result, 1)

        result = subrectangle_queries.get_value(1,0)
        self.assertEqual(result, 4)

        result = subrectangle_queries.get_value(3,1)
        self.assertEqual(result, 1)

        subrectangle_queries.update_subrectangle_2(0,0,1,2,100)
        result = subrectangle_queries.get_value(0,1)
        self.assertEqual(result, 100)

        subrectangle_queries.update_subrectangle_2(2,0,2,2,90)
        result = subrectangle_queries.get_value(2,1)
        self.assertEqual(result, 90)

        subrectangle_queries.update_subrectangle_2(3,0,3,2,80)
        result = subrectangle_queries.get_value(3,1)
        self.assertEqual(result, 80)

        subrectangle_queries = SubrectangleQueries([[6,9,6,1,2],[8,8,6,5,9],[7,6,10,8,2],[7,7,4,9,1]])
        subrectangle_queries.update_subrectangle_2(1,4,2,4,5)
        result = subrectangle_queries.get_value(3,4)
        self.assertEqual(result, 1)

        subrectangle_queries.update_subrectangle_2(3,4,3,4,8)
        result = subrectangle_queries.get_value(2,0)
        self.assertEqual(result, 7)


    
    def test_group_the_people(self):
        group_sizes = [3,3,3,3,3,1,3]
        result = group_the_people(group_sizes)
        self.assertEqual(result, [[0,1,2],[3,4,6],[5]])

        group_sizes = [2,1,3,3,3,2]
        result = group_the_people(group_sizes)
        self.assertEqual(result, [[0,5],[1],[2,3,4]])

    
    def test_max_increase_keeping_skyline(self):
        grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
        result = max_increase_keeping_skyline(grid)
        self.assertEqual(result, 35)

        grid = [[5,1,4],[0,2,3],[7,1,9]]
        result = max_increase_keeping_skyline(grid)
        self.assertEqual(result, 6)

        grid = [[1,4,2,7,9],[8,3,5,7,4],[5,9,2,3,2],[3,8,1,5,1],[6,9,2,9,0]]
        result = max_increase_keeping_skyline(grid)
        self.assertEqual(result, 79)



if __name__ == '__main__':
    unittest.main()