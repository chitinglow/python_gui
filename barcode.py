from barcode import EAN13
from barcode.writer import ImageWriter

num_of_barcodes = int(input("How many barcode you need? "))
numbers = range(num_of_barcodes)

for i in numbers:
    id = input("Give 12-Digit number for your barcode")
    my_code = EAN13(id, writer=ImageWriter)
    my_code.save(name)