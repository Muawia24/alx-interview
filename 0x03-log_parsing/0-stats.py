#!/usr/bin/python3
"""
Log parsing
"""
import sys
import re
import signal


def log_parse(stdin: str, logs: dict) -> None:
    """
    Function that reads stdin line by line and computes
    metrics
    """
    pattern = (
            r'^(?:\d{1,3}\.){3}\d{1,3} - '
            r'\[(.*?)\] '
            r'"GET /projects/260 HTTP/1.1" '
            r'(\d{3}) '
            r'(\d+)$'
            )
    try:
        counter = 0
        for line in stdin:
            match = re.match(pattern, line)
            if not match:
                continue

            counter += 1

            parse_list = line.split(' ')
            status_code = parse_list[-2]

            if status_code in logs:
                logs[status_code] += 1

            logs['file_size'] += int(parse_list[-1])

            if counter % 10 == 0:
                print_stat(logs)

        print_stat(logs)

    except KeyboardInterrupt:
        print_stat(logs)
        raise


def print_stat(logs: dict, ) -> None:
    """
    logs the statistics
    """
    print(f'File size: {logs["file_size"]}')
    for key, value in sorted(logs.items()):
        if key != "file_size" and value:
            print(f'{key}: {value}')


if __name__ == "__main__":
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    logs = {code: 0 for code in codes}
    logs['file_size'] = 0

    log_parse(sys.stdin, logs)
