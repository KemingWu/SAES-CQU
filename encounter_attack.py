


from double_saes import DoubleSimplifiedAES

def find_key_from_intermediates(plaintexts, ciphertexts):
    ciphertexts = [int(binary_str, 2) for binary_str in ciphertexts]
    key_candidates = []

    for i in range(len(plaintexts)):
        for j in range(len(plaintexts)):
            if i != j:
                plaintext1 = plaintexts[i]
                ciphertext1 = ciphertexts[i]
                plaintext2 = plaintexts[j]
                ciphertext2 = ciphertexts[j]

                double_aes = DoubleSimplifiedAES(0)  # 初始化一个双AES实例

                key1 = double_aes.aes1.find_key(int(plaintext1, 2), ciphertext1)
                key2 = double_aes.aes2.find_key(int(plaintext2, 2), ciphertext2)

                full_key = (key1 << 16) | key2
                key_candidates.append(full_key)
    if key_candidates:

        key_candidates = [format(item, '032b') for item in key_candidates]
        return key_candidates
    else:
        return "未找到中间相遇。"


plaintexts=['1010001110110000', '0000011010101011']
bin_ciphertexts=['1001100101100101', '1100011110100100']

# 示例用法
print(
    find_key_from_intermediates(plaintexts, bin_ciphertexts)
)


# import random
#
# def generate_random_plaintext():
#     return format(random.randint(0, 0xFFFF), '016b')  # 生成16位的二进制明文

# # 示例用法
# plaintexts = [generate_random_plaintext() for _ in range(2)]  # 4个16位明文
# # ciphertexts = [DoubleSimplifiedAES(0x12345678).encrypt(int(plaintext, 2)) for plaintext in plaintexts]
# #
# # print("明文")
# # print(plaintexts)
# # print("密文")
# # bin_ciphertexts = [decimal_to_16bit_binary(single_element) for single_element in ciphertexts]
# # print(bin_ciphertexts)