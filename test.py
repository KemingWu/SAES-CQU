from saes import SimplifiedAES
from double_saes import DoubleSimplifiedAES
from triple_saes import TripleSimplifiedAES_mode1, TripleSimplifiedAES_mode2
from utils import decimal_to_16bit_binary


def ascii_encrypt(plaintext_ascii, saes):
    plaintext_integers = [ord(char) for char in plaintext_ascii]
    encrypted_integers = [saes.encrypt(plaintext_int) for plaintext_int in plaintext_integers]
    binary_encrypted_integers = [decimal_to_16bit_binary(single_element) for single_element in encrypted_integers]
    return encrypted_integers, binary_encrypted_integers


def ascii_decrypt(encrypted_integers, saes):
    decrypted_integers = [saes.decrypt(encrypted_int) for encrypted_int in encrypted_integers]
    decrypted_ascii = "".join([chr(int_value) for int_value in decrypted_integers])
    return decrypted_ascii


# 3.3
# 创建SAES实例，使用16位密钥
key = 0b0100101011110101
saes = SimplifiedAES(key)

# 要加密的ASCII字符串，每个字符表示为一个16位整数
plaintext_ascii = "Hello SAES"
plaintext_integers = [ord(char) for char in plaintext_ascii]

# 加密
encrypted_integers, binary_encrypted_integers = ascii_encrypt(plaintext_ascii, saes)
# 输出加密后的整数
print("Encrypted Integers:", binary_encrypted_integers)

# 解密
decrypted_integers = [saes.decrypt(encrypted_int) for encrypted_int in encrypted_integers]

# 将解密后的整数转换回ASCII字符串
decrypted_ascii = ascii_decrypt(encrypted_integers, saes)

# 输出解密后的ASCII字符串
print("Decrypted ASCII:", decrypted_ascii)
