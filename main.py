from saes import SimplifiedAES
from double_saes import DoubleSimplifiedAES
from triple_saes import TripleSimplifiedAES_mode1, TripleSimplifiedAES_mode2
from utils import decimal_to_16bit_binary, ascii_encrypt, ascii_decrypt

# 3.1 &  3.2
plaintext = 0b0000111100001111
key = 0b0010110101010101
ciphertext = SimplifiedAES(key).encrypt(plaintext) # 0b0010010011101100
# print(decimal_to_16bit_binary(ciphertext))
print(decimal_to_16bit_binary(ciphertext))

ciphertext = 0b0010010011101100
key = 0b0010110101010101
plaintext = SimplifiedAES(key).decrypt(ciphertext) # 0b1101011100101000
print(bin(plaintext))



# 3.3
# 创建SAES实例，使用16位密钥
# key = 0b0100101011110101
# saes = SimplifiedAES(key)
#
# # 要加密的ASCII字符串，每个字符表示为一个16位整数
# plaintext_ascii = "Hello SAES"
# plaintext_integers = [ord(char) for char in plaintext_ascii]
#
# # 加密
# encrypted_integers, binary_encrypted_integers = ascii_encrypt(plaintext_ascii, saes)
# # 输出加密后的整数
# print("Encrypted Integers:", binary_encrypted_integers)
#
# # 解密
# decrypted_integers = [saes.decrypt(encrypted_int) for encrypted_int in encrypted_integers]
# # 将解密后的整数转换回ASCII字符串
# decrypted_ascii = ascii_decrypt(encrypted_integers, saes)
#
# # 输出解密后的ASCII字符串
# print("Decrypted ASCII:", decrypted_ascii)



# 3.4.1
plaintext = 0b0000111100001111
key = 0b00101101010101010010110101010101

# 创建DoubleSimplifiedAES实例
double_aes = DoubleSimplifiedAES(key)

# 加密
ciphertext = double_aes.encrypt(plaintext)
print("加密后的密文:", decimal_to_16bit_binary(ciphertext))

# 解密
decrypted_plaintext = double_aes.decrypt(ciphertext)
print("解密后的明文:", decimal_to_16bit_binary(decrypted_plaintext))


# 3.4.3

# mode 1
# 使用32位密钥进行三重加密
# key1 = 0b0100101011110101
# key2 = 0b1101011100101000
# triple_aes = TripleSimplifiedAES_mode1(key1, key2)
#
# plaintext = 0b0000111100001111
# ciphertext = triple_aes.encrypt(plaintext)
# print("加密后的密文:", decimal_to_16bit_binary(ciphertext))
#
# decrypted = triple_aes.decrypt(ciphertext)
# print("解密后的明文:", decimal_to_16bit_binary(decrypted))
#
# # mode 2
# # 使用48位密钥进行三重加密
# key1 = 0b0100101011110101
# key2 = 0b1101011100101000
# key3 = 0b1111000011110000
# triple_aes = TripleSimplifiedAES_mode2(key1, key2, key3)
#
# plaintext = 0b0000111100001111
# ciphertext = triple_aes.encrypt(plaintext)
# print("加密后的密文:", decimal_to_16bit_binary(ciphertext))
#
# decrypted = triple_aes.decrypt(ciphertext)
# print("解密后的明文:", decimal_to_16bit_binary(decrypted))