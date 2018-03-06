#! /usr/bin/env python3

import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("period", help="number of indexes for the moving average", type=int)
    parser.add_argument("standard_dev", help="standard deviation coefficient to apply", type=float)
    parser.add_argument("indexes_file", help="file containing daily indexes")
    parser.add_argument("index_number", help="index number to compute moving average and Bollinger bands", type=int)
    return parser.parse_args()


def error_handling(args, file_stream):
    if args.period > args.index_number:
        print("Period can't be lower than index", file=sys.stderr)
        exit(84)
    elif len(file_stream.readlines()) < args.period:
        print("Period can't be lower than the number of value")
        exit(84)
    elif args.period <= 0:
        print("Period must be higher than 0")
        exit(84)
    file_stream.seek(0)


def open_file(filename):
    try:
        return open(filename, "r")
    except Exception as e:
        print(e, file=sys.stderr)
        exit(84)


def average(arr):
    return sum(arr) / len(arr) if (len(arr)) else 0


def deviation(period, arr, avg):
    return (1 / period * sum([(v - avg) ** 2 for v in arr])) ** (1 / 2)


def main():
    args = parse_args()
    file_stream = open_file(args.indexes_file)
    error_handling(args, file_stream)
    values = [
        float(line[:-1])
        for line in file_stream.readlines()
    ][args.index_number - args.period + 1: args.index_number + 1]
    avg = average(values)
    dev = deviation(args.period, values, avg)

    upper_band = avg + (dev * args.standard_dev)
    lower_band = avg - (dev * args.standard_dev)

    print("INPUT")
    print("Index:", args.index_number)
    print("Period:", args.period)
    print("SD_coef: %.2f" % args.standard_dev)
    print("\nOUTPUT")
    print("MA: %.2f" % avg)
    print("SD: %.2f" % dev)
    print("B+: %.2f" % upper_band)
    print("B-: %.2f" % lower_band)


if __name__ == "__main__":
    main()
