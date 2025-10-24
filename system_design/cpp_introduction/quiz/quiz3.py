import numpy as np


class Matrix:
    # Rotates the matrix by 90 degrees clockwise in-place
    def rotate(self, matrix):
        # Your code for the rotate function starts here
        matrix[:] = np.rot90(matrix, 3)

    # Your code for the rotate function ends here


if __name__ == "__main__":
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m = Matrix()
    m.rotate(matrix)
    # Output the rotated matrix
    print(matrix)
