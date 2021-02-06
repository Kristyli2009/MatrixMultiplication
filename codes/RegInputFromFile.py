#!/usr/bin/env python3
import time
import csv


def input_data():
    """ A function to read data from a file and store them in a list and return it"""
    numbers = []
    data_file = input("Please enter the file name with extension: ")
    with open(data_file) as file:
        for line in file:
            numbers.append(line.strip().split())
    return numbers


def convert_str_to_int(numbers, matrix_a, matrix_b, size):
    """A function to convert the data of string into the data of integer, then split into two matrices"""
    for i in range(size):
        for j in range(size):
            matrix_a[i][j] = int(numbers[i + 1][j])
            matrix_b[i][j] = int(numbers[size + i + 1][j])


def multiply_two_matrices(matrix_a, matrix_b, size, m_times, a_times):
    """A function to multiply two matrices and store the result into another list,
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


def output_data_into_file(matrix_c, m_times, a_times, r_time):
    """ A function to output the data into a file"""
    with open("RegularOutput.txt", "a") as outfile:
        outfile.write("The size of matrix is " + str(matrix_size) + ".\n\n")
        for i in matrix_c:
            for j in i:
                outfile.write(str(j) + " ")
            outfile.write("\n")
        outfile.write("The number of multiplication operation is " + str(m_times) + ".\n")
        outfile.write("The number of addition operations is " + str(a_times) + ".\n")
        outfile.write("The total number of operations is " + str(m_times + a_times) + ".\n\n")
        outfile.write("The running time is " + str(r_time) + ".\n\n")
        outfile.write("*" * 200 + "\n\n")


def out_data_to_csv_file(size, m_times, a_times, r_time):
    """ A function to output the data about the number of multiplication operations and addition operations
    and running time"""
    with open('RegularOutput.csv', 'a') as file:
        the_writer = csv.writer(file)
        the_writer.writerow([size, m_times, a_times, m_times + a_times, r_time])


if __name__ == '__main__':
    data = input_data()
    matrix_size = int(data[0][0])
    matrix_A = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
    matrix_B = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
    convert_str_to_int(data, matrix_A, matrix_B, matrix_size)

    M_times = 0
    A_times = 0
    start = time.time()
    matrix_C, M_times, A_times = multiply_two_matrices(matrix_A, matrix_B, matrix_size, M_times, A_times)
    end = time.time()
    running_time = end - start

    output_data_into_file(matrix_C, M_times, A_times, running_time)
    out_data_to_csv_file(matrix_size, M_times, A_times, running_time)
    print("Please check the output file: RegularOutput.txt or RegularOutput.csv for the result!")
