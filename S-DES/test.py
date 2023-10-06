import math
import numpy as np
import threading
from gen_key import generation_key as gk
from encrypt import encrypt as enc
import time


#  定义密钥
# k = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
#
#
# g_key = gk(k)
# # print(g_key.key_start)
# # print(g_key.key)
# key1 = g_key.gen_key()
# # print(g_key.key)
# key2 = g_key.gen_key()
# # print(key1)
# # print(g_key.key)
# # print(key2)
# input = [0,0,0,0,0,0,0,1]
# Enc = enc(key1, key2)
# cip = Enc.gen_cip(input)
# print(cip)
# a = [0,0,0,0,0,0,0,0]
# pla = Enc.sol_cip(a)
# print(pla)

def spl(input):
    transform = []
    for i in range(len(input)):
        transform.append(ord(input[i]))
    data = []
    for i in range(len(transform)):
        b = bin(transform[i]).replace('0b', '')
        b = b.zfill(8)
        for j in range(len(b)):
            data.append(int(b[j]))
    data1 = np.array(data)
    data1.resize((len(input), 8))
    print(data1)
    return data1


def sum_bin(input):
    sum_b = 0
    for i in range(len(input)):
        sum_b = sum_b + pow(2, len(input) - 1 - i) * input[i]
    return sum_b


# input = "abcd123"
# data = spl(input)
# cip = ""
# for i in range(data.shape[0]):
#     a = Enc.gen_cip(data[i, :])
#     cip = cip + chr(sum_bin(a))
#
# print(cip)
#
# data1 = spl(cip)
# pla = ""
# for i in range(data1.shape[0]):
#     b = Enc.sol_cip(data1[i, :])
#     pla = pla + chr(sum_bin(b))
# print(pla)


''' 此处为暴力破解
pla = [1, 1, 1, 1, 1, 1, 1, 1]
cip = [1, 1, 0, 0, 1, 1, 1, 0]


def violence_solve():
    for i in range(pow(2, 10)):

        bin_i = bin(i).replace('0b', '')
        str_i = bin_i.zfill(10)
        start_key = []
        for j in range(len(str_i)):
            start_key.append(int(str_i[j]))
        g_key = gk(start_key)
        key1 = g_key.gen_key()
        key2 = g_key.gen_key()
        Enc = enc(key1, key2)
        if Enc.gen_cip(pla) == cip:
            ans.append(start_key)
    return ans


ans = []
a = time.time()
ans = violence_solve()
b = time.time()
print("耗时为：", b - a)
for i in range(len(ans)):
    print("密钥为", ans[i])
'''

'''问题五第二部分
def violence_solve1(pla):
    for i in range(pow(2, 10)):
        bin_i = bin(i).replace('0b', '')
        str_i = bin_i.zfill(10)
        start_key = []
        for j in range(len(str_i)):
            start_key.append(int(str_i[j]))
        g_key = gk(start_key)
        key1 = g_key.gen_key()
        key2 = g_key.gen_key()
        Enc = enc(key1, key2)
        ans.append(Enc.gen_cip(pla))
    return ans


ans = []
for m in range(pow(2, 8)):
    bin_m = bin(m).replace('0b', '')
    str_m = bin_m.zfill(8)
    pla = []
    for j in range(len(str_m)):
        pla.append(int(str_m[j]))
    ans = violence_solve1(pla)

    cip = []
    key = []
    for i in range(len(ans)):
        for j in range(i + 1, len(ans)):
            if ans[i] == ans[j]:
                cip = ans[i]
                bin_i = bin(i).replace('0b', '')
                str_i = bin_i.zfill(10)
                key_i = []
                for k in range(len(str_i)):
                    key_i.append(int(str_i[k]))
                bin_j = bin(j).replace('0b', '')
                str_j = bin_j.zfill(10)
                key_j = []
                for k in range(len(str_j)):
                    key_j.append(int(str_j[k]))
                key.append(key_i)
                key.append(key_j)
                break
        if len(cip) != 0:
            break
    if len(key) != 0:
        print("对于明文:", pla)
        print("密钥1", key[0], "和", "密钥2", key[1], "都可以加密出密文:")
        print(cip)
    ans = []

'''
