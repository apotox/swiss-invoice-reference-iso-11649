# Author: Safi
# Usage: python main.py <csv_file_path>
# Example: python main.py test.csv

def generate_invoice_reference(invoice_number):
    MODULO_97 = 97
    CHARCODE_A = 65
    CHARCODE_A_MULTIPLIER = 100
    CHARCODE_A_OFFSET = 55
    CHARCODE_0_MULTIPLIER = 10
    CHARCODE_0_OFFSET = 48
    value = invoice_number + 'RF00'
    length = len(value)
    buffer = 0
    # ISO-11649
    for i in range(length):
        char_code = ord(value[i])
        if char_code >= CHARCODE_A:
            multiplier = CHARCODE_A_MULTIPLIER
            offset = CHARCODE_A_OFFSET
        else:
            multiplier = CHARCODE_0_MULTIPLIER
            offset = CHARCODE_0_OFFSET

        buffer *= multiplier
        buffer -= offset
        buffer += char_code
        buffer %= MODULO_97

    check_code = 98 - buffer

    return 'RF' + ('0' if check_code < 10 else '') + str(check_code) + '0' * (21 - len(invoice_number)) + invoice_number

def process_csv_file(file_path):
    import csv
    import os

    if not os.path.exists(file_path):
        print("File not found")
        return

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file,delimiter=';')
        rows = list(reader)

    print(f"Processing {len(rows)} rows")

    for row in rows:
        invoice_number = row.get('invoice_number')
        if invoice_number:
            row['invoice_reference'] = generate_invoice_reference(invoice_number)

    new_file_path = file_path.replace('.csv', '_new.csv')
    with open(new_file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames + ['invoice_reference'])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please provide csv file path")
    else:
        process_csv_file(sys.argv[1])