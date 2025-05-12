def xor(a, b):
    # XOR operation between two binary strings
    result = []
    for i in range(1, len(b)):
        result.append('1' if a[i] != b[i] else '0')
    return ''.join(result)

def mod2_division(dividend, divisor):
    # Perform Modulo-2 Division
    pick = len(divisor)
    temp = dividend[:pick]
    
    while pick < len(dividend):
        if temp[0] == '1':
            temp = xor(divisor, temp) + dividend[pick]
        else:
            temp = xor('0' * pick, temp) + dividend[pick]
        pick += 1
    
    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0' * pick, temp)
    
    return temp

def encode_data(data, generator):
    # Append zeros to data
    data_with_zeros = data + '0' * (len(generator) - 1)
    remainder = mod2_division(data_with_zeros, generator)
    # Append remainder to original data
    codeword = data + remainder
    return codeword

# Example Usage
data = "1101011011"  # Input data in binary
generator = "10011"  # Generator polynomial in binary

print("Original Data: ", data)
print("Generator Polynomial: ", generator)

encoded_data = encode_data(data, generator)
print("Encoded Data (with CRC): ", encoded_data)
