#!/usr/bin/env python3
import random


size = 10
with open("data10.txt", "w") as outfile:
    outfile.write(str(size) + "\n")
    for i in range(2*size):
        for j in range(int(size)):
            outfile.write(str(random.randint(0, 9)) + " ")
        outfile.write("\n")
