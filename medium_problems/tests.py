import unittest
from subrectangle_queries import SubrectangleQueries
from group_the_people import group_the_people


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

    
    def test_group_the_people(self):
        group_sizes = [3,3,3,3,3,1,3]
        result = group_the_people(group_sizes)
        self.assertEqual(result, [[0,1,2],[3,4,6],[5]])

        group_sizes = [2,1,3,3,3,2]
        result = group_the_people(group_sizes)
        self.assertEqual(result, [[0,5],[1],[2,3,4]])


if __name__ == '__main__':
    unittest.main()