#! /usr/bin/env python3

from sys import argv

if len(argv) != 5:
    raise Exception('Invalid argument number')

index = int(argv[4])
period = int(argv[1])
sd_coefficient = float(argv[2])
file_stream = open(argv[3], "r")


def average(arr):
    return sum(arr) / len(arr)


def deviation(arr, avg):
    dev = [
        (v - avg) ** 2 for v in arr
    ]
    return (1 / period * sum(dev)) ** (1 / 2)


values = [
    float(line[:-1])
    for line in file_stream.readlines()
]
values = values[index - period + 1: index + 1]
deviation = deviation(values, average(values))

upper_band = average(values) + (deviation * sd_coefficient)
lower_band = average(values) - (deviation * sd_coefficient)

print("MA: %.2f" % average(values))
print("SD: %.2f" % deviation)
print("B+: %.2f" % upper_band)
print("B-: %.2f" % lower_band)
