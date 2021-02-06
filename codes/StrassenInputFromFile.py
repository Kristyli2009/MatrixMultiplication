#!/usr/bin/env python3
import time
import csv
import math
from math import log2


M_times = 0
A_times = 0


def input_data():
    """read data from a file and store them in a list and return it"""
    numbers = []
    data_file = input("Please enter the file name with extension: ")
    with open(data_file) as file:
        for line in file:
            numbers.append(line.strip().split())
    return numbers


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


def convert_str_to_int(numbers, matrix_a, matrix_b, size):
    """convert the data of string into the data of integer, then split into two matrices"""
    for i in range(size):
        for j in range(size):
            matrix_a[i][j] = int(numbers[i + 1][j])
            matrix_b[i][j] = int(numbers[size + i + 1][j])


def sub(matrix_a, matrix_b):
    """ A function to subtract two matrices"""
    global A_times
    size = len(matrix_a)
    matrix_c = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            matrix_c[i][j] = matrix_a[i][j] - matrix_b[i][j]
            A_times += 1
    return matrix_c


def add(matrix_a, matrix_b):
    """ A function to add two matrices"""
    global A_times
    size = len(matrix_a)
    matrix_c = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
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
    size = len(matrix_a)
    half = int(size/2)
    matrix_c = [[0 for i in range(size)] for j in range(size)]

    global M_times
    # base case
    if size == 1:
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


def output_data_into_file(size, matrix_c, m_times, a_times, r_time):
    """ A function to output the data into a file"""
    with open("StrassenOutput.txt", "a") as outfile:
        outfile.write("The size of matrix is " + str(size) + ".\n\n")
        for i in range(size):
            for j in range(size):
                outfile.write(str(matrix_c[i][j]) + " ")
            outfile.write("\n")
        outfile.write("The number of multiplication operation is " + str(m_times) + ".\n")
        outfile.write("The number of addition operations is " + str(a_times) + ".\n")
        outfile.write("The total number of operations is " + str(m_times + a_times) + ".\n\n")
        outfile.write("The running time is " + str(r_time) + ".\n\n")
        outfile.write("*" * 200 + "\n\n")


def out_data_to_csv_file(size, m_times, a_times, r_time):
    with open('StrassenOutput.csv', 'a') as file:
        the_writer = csv.writer(file)
        the_writer.writerow([size, m_times, a_times, m_times + a_times, r_time])


if __name__ == '__main__':
    data = input_data()
    matrix_size = int(data[0][0])
    if power_of_2(matrix_size):
        matrix_A = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
        matrix_B = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
        convert_str_to_int(data, matrix_A, matrix_B, matrix_size)
    else:
        expo = math.ceil(log2(matrix_size))
        new_size = int(math.pow(2, expo))
        matrix_A = [[0 for i in range(new_size)] for j in range(new_size)]
        matrix_B = [[0 for i in range(new_size)] for j in range(new_size)]
        convert_str_to_int(data, matrix_A, matrix_B, matrix_size)
        for i in range(matrix_size, new_size):
            for j in range(matrix_size, new_size):
                matrix_A[i][j] = 0
                matrix_B[i][j] = 0

    start = time.time()
    matrix_C = multiply(matrix_A, matrix_B)
    end = time.time()
    running_time = end - start

    output_data_into_file(matrix_size, matrix_C, M_times, A_times, running_time)
    out_data_to_csv_file(matrix_size, M_times, A_times, running_time)
    print("Please check the output file: StrassenOutput.txt or StrassenOutput.csv for the result!")

