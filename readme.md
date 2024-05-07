## python script to generate swiss payment reference (The ISO Creditor Reference ISO-11649)

### csv example
```csv
invoice_number;name
123;John
```

### Usage
```console
$ python3 main.py file.csv
```

### output file 

```csv
invoice_number,name,invoice_reference
123,John,RF78000000000000000000123
```