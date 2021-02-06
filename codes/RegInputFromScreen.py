#!/usr/bin/env python3
import time


def input_data():
    """ input data from the keyboard and into lists and then return them"""
    size = input("Please enter the size of the two matrices for multiplication: ")
    n_size = int(size)

    a = []
    print("Please enter numbers of the first " + str(n_size) + "x" + str(n_size) + " matrix:")
    for i in range(n_size):
        line = input()
        a.append(line.strip().split())

    b = []
    print("Please enter numbers of the second " + str(n_size) + "x" + str(n_size) + " matrix:")
    for i in range(n_size):
        line = input()
        b.append(line.strip().split())
    return n_size, a, b


def convert_str_to_int(a, b, size):
    """ A function to convert the data of string into the data of integer
    and store them in two lists and return the two list"""
    for i in range(size):
        for j in range(size):
            a[i][j] = int(a[i][j])
            b[i][j] = int(b[i][j])
    return a, b


def multiply_two_matrices(matrix_a, matrix_b, size, m_times, a_times):
    """multiply two matrices and store the result into another list,
    and calculate the number of multiplication operation and addition operation"""
    matrix_c = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            total = matrix_a[i][0] * matrix_b[0][j]
            m_times = m_times + 1
            for k in range(1, size):
                total = total + matrix_a[i][k] * matrix_b[k][j]
                m_times = m_times + 1
                a_times = a_times + 1
            matrix_c[i][j] = total
    return matrix_c, m_times, a_times


def output_data_on_screen(matrix_c, matrix_a, matrix_b, m_times, a_times, r_time):
    """ A function to output data of three matrices: matrix_c = matrix_a x matrix_b"""
    print("The size of matrices is: " + str(len(matrix_c)))
    for i in range(len(matrix_c)):
        print(str(matrix_c[i]) + "\t\t" + str(matrix_a[i]) + "\t\t" + str(matrix_b[i]))
    print("# multiplication operations: ", m_times)
    print("# addition operations: ", a_times)
    print("The running time: ", r_time)


if __name__ == '__main__':
    matrix_size, A, B = input_data()
    matrix_A, matrix_B = convert_str_to_int(A, B, matrix_size)

    M_times = 0
    A_times = 0
    start = time.time()
    matrix_C, M_times, A_times = multiply_two_matrices(matrix_A, matrix_B, matrix_size, M_times, A_times)
    end = time.time()
    running_time = end - start

    output_data_on_screen(matrix_C, matrix_A, matrix_B, M_times, A_times, running_time)
