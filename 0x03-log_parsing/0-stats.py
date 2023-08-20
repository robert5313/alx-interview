<<<<<<< HEAD

=======
#!/usr/bin/python3
'''Module 0 Tasks log parsing.
'''

import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for i, line in enumerate(sys.stdin, start=1):
        try:
            ip, _, _, _, status_code, file_size = line.split()
            status_code = int(status_code)
            file_size = int(file_size)
            total_size += file_size
            status_codes[status_code] += 1
        except ValueError:
            continue

        if i % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_codes):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    print(f"\nTotal file size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
>>>>>>> eb3a41d595a1ed241ac05433741daf21f2ac2106
