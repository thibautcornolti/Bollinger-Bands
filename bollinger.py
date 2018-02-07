#! /usr/bin/env python3

from sys import argv

if len(argv) != 5:
    raise Exception("Invalid argument number")

try:
    index = int(argv[4])
    period = int(argv[1])
    sd_coefficient = float(argv[2])
except:
    raise Exception("Invalid argument value")
try:
    file_stream = open(argv[3], "r")
except:
    raise Exception("Invalid file")


def average(arr):
    return sum(arr) / len(arr) if (len(arr)) else 0


def deviation(arr, avg):
    return (1 / period * sum([(v - avg) ** 2 for v in arr])) ** (1 / 2)


def main():
    values = [
        float(line[:-1])
        for line in file_stream.readlines()
    ][index - period + 1: index + 1]
    avg = average(values)
    dev = deviation(values, avg)

    upper_band = avg + (dev * sd_coefficient)
    lower_band = avg - (dev * sd_coefficient)

    print("INPUT")
    print("Index:", index)
    print("Period:", period)
    print("SD_coef: %.2f" % sd_coefficient)
    print("\nOUTPUT")
    print("MA: %.2f" % avg)
    print("SD: %.2f" % deviation)
    print("B+: %.2f" % upper_band)
    print("B-: %.2f" % lower_band)


if __name__ == "__main__":
    main()
