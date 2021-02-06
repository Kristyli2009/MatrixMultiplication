#!/usr/bin/env python3
import time
import math
from math import log2

M_times = 0
A_times = 0


def input_data():
    """ input data from the keyboard and into lists and then return them"""
    size = input("Please enter the size of the two matrices for multiplication: ")
    matrix_size = int(size)
    a = []
    print("Please enter numbers of the first " + size + "x" + size + " matrix:")
    for i in range(matrix_size):
        line = input()
        a.append(line.strip().split())

    b = []
    print("Please enter numbers of the second " + size + "x" + size + " matrix:")
    for i in range(matrix_size):
        line = input()
        b.append(line.strip().split())
    return matrix_size, a, b


def power_of_2(n):
    """ A function to check if the number is a power of 2, then return True or False"""
    if n == 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        else:
            n = n//2
    return True


def convert_str_to_int(a, b, matrix_a, matrix_b, matrix_size):
    """ A function to convert the data of string into the data of integer
    and store them in two lists and return the two list"""
    for i in range(matrix_size):
        for j in range(matrix_size):
            matrix_a[i][j] = int(a[i][j])
            matrix_b[i][j] = int(b[i][j])


def sub(matrix_a, matrix_b):
    """ A function to subtract two matrices"""
    global A_times
    matrix_size = len(matrix_a)
    matrix_c = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
    for i in range(matrix_size):
        for j in range(matrix_size):
            matrix_c[i][j] = matrix_a[i][j] - matrix_b[i][j]
            A_times += 1
    return matrix_c


def add(matrix_a, matrix_b):
    """ A function to add two matrices"""
    global A_times
    matrix_size = len(matrix_a)
    matrix_c = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
    for i in range(matrix_size):
        for j in range(matrix_size):
            matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j]
            A_times += 1
    return matrix_c


def split(matrix, sub_matrix, ik, jk):
    """ A function to split a matrix into 4 sub_matrices"""
    i2 = ik
    for i in range(len(sub_matrix)):
        j2 = jk
        for j in range(len(sub_matrix)):
            sub_matrix[i][j] = matrix[i2][j2]
            j2 += 1
        i2 += 1


def join(sub_matrix, matrix_c, ik, jk):
    """ A function to join 4 sub_matrices together into one matrix"""
    i2 = ik
    for i in range(len(sub_matrix)):
        j2 = jk
        for j in range(len(sub_matrix)):
            matrix_c[i2][j2] = sub_matrix[i][j]
            j2 += 1
        i2 += 1


def multiply(matrix_a, matrix_b):
    """ A recursive function to multiply two matrices"""
    matrix_size = len(matrix_a)
    half = int(matrix_size/2)
    matrix_c = [[0 for i in range(matrix_size)] for j in range(matrix_size)]

    global M_times
    # base case
    if matrix_size == 1:
        matrix_c[0][0] = matrix_a[0][0] * matrix_b[0][0]
        M_times += 1
    else:
        a = [[0 for i in range(half)] for j in range(half)]
        b = [[0 for i in range(half)] for j in range(half)]
        c = [[0 for i in range(half)] for j in range(half)]
        d = [[0 for i in range(half)] for j in range(half)]
        e = [[0 for i in range(half)] for j in range(half)]
        f = [[0 for i in range(half)] for j in range(half)]
        g = [[0 for i in range(half)] for j in range(half)]
        h = [[0 for i in range(half)] for j in range(half)]

        # split matrix_A into 4 sub_matrices
        split(matrix_a, a, 0, 0)
        split(matrix_a, b, 0, half)
        split(matrix_a, c, half, 0)
        split(matrix_a, d, half, half)

        # split matrix_B into 4 sub_matrices
        split(matrix_b, e, 0, 0)
        split(matrix_b, g, 0, half)
        split(matrix_b, f, half, 0)
        split(matrix_b, h, half, half)

        # compute p1, p2, p3, p4, p5, p6, p7
        p1 = multiply(a, sub(g, h))
        p2 = multiply(add(a, b), h)
        p3 = multiply(add(c, d), e)
        p4 = multiply(d, sub(f, e))
        p5 = multiply(add(a, d), add(e, h))
        p6 = multiply(sub(b, d), add(f, h))
        p7 = multiply(sub(a, c), add(e, g))

        # compute r, s, t, u
        r = add(sub(add(p5, p4), p2), p6)
        s = add(p1, p2)
        t = add(p3, p4)
        u = sub(sub(add(p5, p1), p3), p7)

        # join 4 sub_matrices into one matrix
        join(r, matrix_c, 0, 0)
        join(s, matrix_c, 0, half)
        join(t, matrix_c, half, 0)
        join(u, matrix_c, half, half)

    # return the result of the matrix
    return matrix_c


def output_data_on_screen(matrix_c, matrix_a, matrix_b, size, m_times, a_times, r_time):
    """ A function to output data of three matrices: matrix_c = matrix_a x matrix_b"""
    print("The size of matrices is: " + str(size))
    for i in range(size):
        print(str(matrix_c[i][0:size]) + "\t\t" + str(matrix_a[i][0:size]) + "\t\t" + str(matrix_b[i][0:size]))
    print("# multiplication operations: ", m_times)
    print("# addition operations: ", a_times)
    print("The running time: ", r_time)


if __name__ == '__main__':
    matrixSize, A, B = input_data()

    if power_of_2(matrixSize):
        matrix_A = [[0 for i in range(matrixSize)] for j in range(matrixSize)]
        matrix_B = [[0 for i in range(matrixSize)] for j in range(matrixSize)]
        convert_str_to_int(A, B, matrix_A, matrix_B, matrixSize)
    else:
        expo = math.ceil(log2(matrixSize))
        new_size = int(math.pow(2, expo))
        matrix_A = [[0 for i in range(new_size)] for j in range(new_size)]
        matrix_B = [[0 for i in range(new_size)] for j in range(new_size)]
        convert_str_to_int(A, B, matrix_A, matrix_B, matrixSize)

        for i in range(matrixSize, new_size):
            for j in range(matrixSize, new_size):
                matrix_A[i][j] = 0
                matrix_B[i][j] = 0

    start = time.time()
    matrix_C = multiply(matrix_A, matrix_B)
    end = time.time()
    running_time = end - start

    output_data_on_screen(matrix_C, matrix_A, matrix_B, matrixSize, M_times, A_times, running_time)
