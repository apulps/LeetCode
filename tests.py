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
from easy_problems.create_target_array import create_target_array, create_target_array_2
from easy_problems.xor_operation import xor_operation
from easy_problems.parking_system import ParkingSystem
from easy_problems.reverse_string import reverse_string, reverse_string_2
from easy_problems.depth_of_binary_tree import depth_of_binary_tree
from easy_problems.single_number import single_number, single_number_2 ,single_number_3, single_number_4
from easy_problems.delete_node_linked_list import delete_node_linked_list

from medium_problems.subrectangle_queries import SubrectangleQueries
from medium_problems.group_the_people import group_the_people
from medium_problems.max_increase_keeping_skyline import max_increase_keeping_skyline
from medium_problems.get_target_copy import get_target_copy
from medium_problems.deepest_leaves_sum import deepest_leaves_sum

from assets.problems_data_structures import TreeNode, LinkedList


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

    
    def test_create_target_array(self):
        nums = [0,1,2,3,4]
        index = [0,1,2,2,1]
        result = create_target_array(nums, index)
        self.assertEqual(result, [0,4,1,3,2])

        nums = [1,2,3,4,0]
        index = [0,1,2,3,0]
        result = create_target_array(nums, index)
        self.assertEqual(result, [0,1,2,3,4])

        nums = [1]
        index = [0]
        result = create_target_array(nums, index)
        self.assertEqual(result, [1])
    
    def test_create_target_array_2(self):
        nums = [0,1,2,3,4]
        index = [0,1,2,2,1]
        result = create_target_array_2(nums, index)
        self.assertEqual(result, [0,4,1,3,2])

        nums = [1,2,3,4,0]
        index = [0,1,2,3,0]
        result = create_target_array_2(nums, index)
        self.assertEqual(result, [0,1,2,3,4])

        nums = [1]
        index = [0]
        result = create_target_array_2(nums, index)
        self.assertEqual(result, [1])


    def test_xor_operation(self):
        n = 5
        start = 0
        result = xor_operation(n, start)
        self.assertEqual(result, 8)

        n = 4
        start = 3
        result = xor_operation(n, start)
        self.assertEqual(result, 8)

        n = 1
        start = 7
        result = xor_operation(n, start)
        self.assertEqual(result, 7)

        n = 10
        start = 5
        result = xor_operation(n, start)
        self.assertEqual(result, 2)

    
    def test_parking_system(self):
        parking_system = ParkingSystem(1, 1, 0)
        self.assertTrue(parking_system.add_car(1))
        self.assertTrue(parking_system.add_car(2))
        self.assertFalse(parking_system.add_car(3))
        self.assertFalse(parking_system.add_car(1))

        parking_system = ParkingSystem(0, 0, 1)
        self.assertTrue(parking_system.add_car(3))

        self.assertRaises(ValueError, parking_system.add_car, 4)

    
    def test_reverse_string(self):
        s = ['h','e','l','l','o']
        reverse_string(s)
        self.assertEqual(s, ['o','l','l','e','h'])

        s = ['a','b','c','d','e']
        reverse_string(s)
        self.assertEqual(s, ['e','d','c','b','a'])

    def test_reverse_string_2(self):
        s = ['h','e','l','l','o']
        reverse_string_2(s)
        self.assertEqual(s, ['o','l','l','e','h'])

        s = ['a','b','c','d','e']
        reverse_string_2(s)
        self.assertEqual(s, ['e','d','c','b','a'])

    
    def test_depth_of_binary_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        result = depth_of_binary_tree(root)
        self.assertEqual(result, 3)

        root = TreeNode(8)
        root.left = TreeNode(6)
        root.right = TreeNode(10)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(15)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(7)
        root.left.right.left = TreeNode(4)
        root.left.right.right = TreeNode(21)
        result = depth_of_binary_tree(root)
        self.assertEqual(result, 4)

    
    def test_single_number(self):
        nums = [2,2,1]
        result = single_number(nums)
        self.assertEqual(result, 1)
        
        nums = [4,1,2,1,2]
        result = single_number(nums)
        self.assertEqual(result, 4)

        nums = [1]
        result = single_number(nums)
        self.assertEqual(result, 1)

    def test_single_number_2(self):
        nums = [2,2,1]
        result = single_number_2(nums)
        self.assertEqual(result, 1)
        
        nums = [4,1,2,1,2]
        result = single_number_2(nums)
        self.assertEqual(result, 4)

        nums = [1]
        result = single_number_2(nums)
        self.assertEqual(result, 1)

    def test_single_number_3(self):
        nums = [2,2,1]
        result = single_number_3(nums)
        self.assertEqual(result, 1)
        
        nums = [4,1,2,1,2]
        result = single_number_3(nums)
        self.assertEqual(result, 4)

        nums = [1]
        result = single_number_3(nums)
        self.assertEqual(result, 1)

    def test_single_number_4(self):
        nums = [2,2,1]
        result = single_number_4(nums)
        self.assertEqual(result, 1)
        
        nums = [4,1,2,1,2]
        result = single_number_4(nums)
        self.assertEqual(result, 4)

        nums = [1]
        result = single_number_4(nums)
        self.assertEqual(result, 1)
    

    def test_delete_node_linked_list(self):
        head = LinkedList(4)
        head.next = LinkedList(5)
        head.next.next = LinkedList(1)
        head.next.next.next = LinkedList(9)
        delete_node_linked_list(head) # remove 4
        self.assertEqual(head.val, 5)
        self.assertEqual(head.next.val, 1)
        self.assertEqual(head.next.next.val, 9)
        self.assertEqual(head.next.next.next, None)

        head = LinkedList(4)
        head.next = LinkedList(5)
        head.next.next = LinkedList(1)
        head.next.next.next = LinkedList(9)
        delete_node_linked_list(head.next) # remove 5
        self.assertEqual(head.val, 4)
        self.assertEqual(head.next.val, 1)
        self.assertEqual(head.next.next.val, 9)
        self.assertEqual(head.next.next.next, None)

        head = LinkedList(4)
        head.next = LinkedList(5)
        head.next.next = LinkedList(1)
        head.next.next.next = LinkedList(9)
        delete_node_linked_list(head.next.next) # remove 1
        self.assertEqual(head.val, 4)
        self.assertEqual(head.next.val, 5)
        self.assertEqual(head.next.next.val, 9)
        self.assertEqual(head.next.next.next, None)



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


    def test_get_target_copy(self):
        tree = TreeNode(7)
        tree.right = TreeNode(3)
        tree.left = TreeNode(4)
        tree.right.right = TreeNode(19)
        tree.right.left = TreeNode(6)
        cloned = tree
        target = TreeNode(3)
        result = get_target_copy(tree, cloned, target)
        assert result is cloned.right

        tree = TreeNode(7)
        cloned = tree
        target = TreeNode(7)
        result = get_target_copy(tree, cloned, target)
        assert result is cloned

        tree = TreeNode(8)
        tree.right = TreeNode(6)
        tree.right.right = TreeNode(5)
        tree.right.right.right = TreeNode(4)
        tree.right.right.right.right = TreeNode(3)
        tree.right.right.right.right.right = TreeNode(2)
        tree.right.right.right.right.right.right = TreeNode(1)
        cloned = tree
        target = TreeNode(4)
        result = get_target_copy(tree, cloned, target)
        assert result is cloned.right.right.right

        tree = TreeNode(1)
        tree.right = TreeNode(3)
        tree.left = TreeNode(2)
        tree.right.right = TreeNode(7)
        tree.right.left = TreeNode(6)
        tree.left.right = TreeNode(5)
        tree.left.left = TreeNode(4)
        tree.left.left.right = TreeNode(9)
        tree.left.left.left = TreeNode(8)
        tree.left.right.left = TreeNode(10)
        cloned = tree
        target = TreeNode(5)
        result = get_target_copy(tree, cloned, target)
        assert result is cloned.left.right

        tree = TreeNode(1)
        tree.left = TreeNode(2)
        tree.left.left = TreeNode(3)
        cloned = tree
        target = TreeNode(2)
        result = get_target_copy(tree, cloned, target)
        assert result is cloned.left
    

    def test_deepest_leaves_sum(self):
        tree = TreeNode(1)
        tree.right = TreeNode(3)
        tree.left = TreeNode(2)
        tree.right.right = TreeNode(6)
        tree.left.right = TreeNode(5)
        tree.left.left = TreeNode(4)
        tree.left.left.left = TreeNode(7)
        tree.right.right.right = TreeNode(8)
        result = deepest_leaves_sum(tree)
        self.assertEqual(result, 15)

        tree = TreeNode(1)
        tree.right = TreeNode(3)
        tree.left = TreeNode(2)
        tree.right.right = TreeNode(6)
        tree.left.right = TreeNode(5)
        tree.left.left = TreeNode(4)
        result = deepest_leaves_sum(tree)
        self.assertEqual(result, 15)

        tree = TreeNode(3)
        tree.right = TreeNode(5)
        tree.left = TreeNode(2)
        tree.right.right = TreeNode(8)
        tree.left.left = TreeNode(1)
        result = deepest_leaves_sum(tree)
        self.assertEqual(result, 9)

        tree = None
        result = deepest_leaves_sum(tree)
        self.assertEqual(result, 0)



if __name__ == '__main__':
    unittest.main()