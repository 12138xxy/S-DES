import math

import numpy as np


class encrypt:
    def __init__(self, key1, key2):
        self.key1 = key1
        self.key2 = key2
        self.data = None
        self.IP = [2, 6, 3, 1, 4, 8, 5, 7]
        self.IP_1 = [4, 1, 3, 5, 7, 2, 8, 6]
        self.EPBox = [4, 1, 2, 3, 2, 3, 4, 1]
        self.SBox1 = np.array([[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 0, 2]])
        self.SBox2 = np.array([[0, 1, 2, 3], [2, 3, 1, 0], [3, 0, 1, 2], [2, 1, 0, 3]])
        self.SPBox = [2, 4, 3, 1]

    def P_Box(self):
        data = []
        for i in range(8):
            data.append(self.data[self.IP[i] - 1])
        self.data = data

    def F(self, R, key):
        a = []
        for i in range(8):
            a.append(R[self.EPBox[i] - 1])
        for i in range(8):
            if a[i] == key[i]:
                a[i] = 0
            else:
                a[i] = 1
        # print(key,a)
        x1 = 2 * a[0] + a[3]
        y1 = 2 * a[1] + a[2]
        x2 = 2 * a[4] + a[7]
        y2 = 2 * a[5] + a[6]
        left = [math.floor(self.SBox1[x1][y1] / 2), self.SBox1[x1][y1] % 2]
        right =[math.floor(self.SBox2[x2][y2] / 2), self.SBox2[x2][y2] % 2]
        left.extend(right)
        # print("left", left)
        b = []
        for i in range(4):
            b.append(left[self.SPBox[i] - 1])
        return b

    def swap(self):
        L = self.data[0:4]
        R = self.data[4:8]
        self.data = np.hstack([np.array(R), np.array(L)])

    def fk1(self):
        L = self.data[0:4]
        R = self.data[4:8]
        R1 = self.F(R, self.key1)
        for i in range(4):
            if L[i] == R1[i]:
                L[i] = 0
            else:
                L[i] = 1
        self.data = np.hstack([np.array(L), np.array(R)])

    def fk2(self):
        L = self.data[0:4]
        R = self.data[4:8]
        R1 = self.F(R, self.key2)
        # print(R1)
        for i in range(4):
            if L[i] == R1[i]:
                L[i] = 0
            else:
                L[i] = 1
        self.data = np.hstack([L, R])

    def P_Box_1(self):
        ciphertext = []
        for i in range(8):
            ciphertext.append(self.data[self.IP_1[i] - 1])
        return ciphertext

    def gen_cip(self, input):
        self.data = input
        self.P_Box()
        # print(self.data)
        self.fk1()
        self.swap()
        self.fk2()
        cip = self.P_Box_1()
        return cip

    def sol_cip(self, input):
        self.data = input
        self.P_Box()
        self.fk2()
        self.swap()
        self.fk1()
        pla = self.P_Box_1()
        return pla

