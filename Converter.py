def binary_to_decimal(binary):
    decimal=int(binary,2)
    return decimal

def octal_to_hexadecimal(octal):
    decimal=int(octal,8)
    hexadecimal=hex(decimal)
    return hexadecimal

binary_num=input("enter the binary value :")
decimal_num=binary_to_decimal(binary_num)

octal_num=input("enter the decimal value :")
hexadecimal_num=octal_to_hexadecimal(octal_num)

print("decimal equivalent of binary number is",decimal_num)
print("hexadecimal equivalent of octal number is",hexadecimal_num)