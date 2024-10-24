#!/usr/bin/python3
"""
Log parsing
"""
import sys
import re
import signal


logs = {"file_size": 0}


def log_parse(stdin):
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
            if status_code in logs.keys():
                logs[status_code] += 1
            else:
                logs[status_code] = 1

            logs["file_size"] += int(parse_list[-1])

            if counter % 10 == 0:
                print(f'file size:{logs["file_size"]}')
                for key, value in sorted(logs.items()):
                    if key != "file_size" and isinstance(int(key), int):
                        print(f'{key}: {value}')
    except KeyboardInterrupt:
        print(f'file size:{logs["file_size"]}')
        for key, value in sorted(logs.items()):
            if key != "file_size":
                print(f'{key}: {value}')


if __name__ == "__main__":

    log_parse(sys.stdin)
