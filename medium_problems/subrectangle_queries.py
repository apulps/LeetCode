"""
Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods:


1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)

Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).


2. getValue(int row, int col)

Returns the current value of the coordinate (row,col) from the rectangle.
"""


class SubrectangleQueries:
    def __init__(self, rectangle):
        self.columns = len(rectangle[0])
        self.rectangle = rectangle

    def update_subrectangle(self, row1, col1, row2, col2, new_value):
        """
        Faster update
        """
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = new_value

    def update_subrectangle_2(self, row1, col1, row2, col2, new_value):
        initial = col1
        while row1 <= row2 and col1 <= col2:
            self.rectangle[row1][col1] = new_value
            col1 += 1

            if not col1 < self.columns or not col1 <= col2:
                col1 = initial
                row1 += 1
            
    def get_value(self, row, col):
        return self.rectangle[row][col]
