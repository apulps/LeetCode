"""
There are n people that are split into some unknown number of groups.
Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in.
For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them.
It is guaranteed that there will be at least one valid solution for the given input.
"""


def group_the_people(group_sizes):
    groups = []
    
    for index, group_size in enumerate(group_sizes):
        if len(groups) == 0:
            groups.append([None] * group_size)
            groups[0].pop(0)
            groups[0].append(index)
        else:
            for index_2, group in enumerate(groups):
                if len(group) == group_size and None in group:
                    groups[index_2].pop(0)
                    groups[index_2].append(index)
                    break
                elif index_2 == len(groups) - 1:
                    groups.append([None] * group_size)
                    groups[index_2 + 1].pop(0)
                    groups[index_2 + 1].append(index)
                    break
        
    return groups
