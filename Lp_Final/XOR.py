def and_xor_string(input_string):
    result_and = ""
    result_xor = ""
    for char in input_string:
        char_ascii = ord(char)
        result_and += chr(char_ascii & 127)
        result_xor += chr(char_ascii ^ 127)
    return result_and, result_xor

input_string = "\\Hello World"
result_and, result_xor = and_xor_string(input_string)
print("Original string:", input_string)
print("After AND operation with 127:", result_and)
print("After XOR operation with 127:", result_xor)
