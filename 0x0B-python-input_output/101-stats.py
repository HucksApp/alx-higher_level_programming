#!/usr/bin/python3
"""Reads from standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""
from sys import stdin, exit


def stats_metrics():
    """Reads from standard input, computes metrics
        and print metrics
    """

    total_size = 0
    stats = {'200': 0, '301': 0, '400': 0, '401': 0,
             '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        line_no = 1
        for line in stdin:
            total_size += parse_metrics(line, stats)
            if line_no == 10:
                line_no = 0
                print_stats(total_size, stats)
            line_no += 1
        print_stats(total_size, stats)

    except KeyboardInterrupt:
        print_stats(total_size, stats)
        raise


def print_stats(total_size, stats):
    """Print accumulated metrics.
    Args:
        total_size: The accumulated read file size.
        stats: The accumulated count of status codes.
    """

    print(f"File size: {total_size}")
    for key in sorted(stats):
        if stats[key]:
            print(f"{key}: {stats[key]}")


def parse_metrics(line, stats):
    """parse the current line
    Args:
        str: current stdin line
        stats: The accumulated count of status codes.
    """

    try:
        values = (line.strip().split(" "))[-2:]
        if values[0] in [*stats]:
            stats[values[0]] += 1
        return int(values[1]) if values[1] else 0
    except (IndexError, ValueError):
        return 0


if __name__ == "__main__":
    stats_metrics()
