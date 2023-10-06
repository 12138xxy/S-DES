import random


class generation_key:
    def __init__(self, key_start):
        self.P_10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        self.P_8 = [6, 3, 7, 4, 8, 5, 10, 9]
        self.key_start = key_start
        self.key = self.P_10_Box()

    # 随机生成初始密钥
    # def random_int_list(self, start, end, len):
    #     random_list = []
    #     for i in range(len):
    #         random_list.append(random.randint(start, end))
    #
    #     return random_list

    def P_10_Box(self):
        key_P_10 = []
        for i in range(10):
            key_P_10.append(self.key_start[self.P_10[i] - 1])
        return key_P_10

    def P_8_Box(self):
        key_P_8 = []
        for i in range(8):
            key_P_8.append(self.key[self.P_8[i] - 1])
        return key_P_8

    def leftshift(self):
        a = self.key[0]
        b = self.key[5]
        for i in range(4):
            self.key[i] = self.key[i + 1]
        self.key[4] = a
        for i in range(5, 8):
            self.key[i] = self.key[i + 1]
        self.key[-1] = b

    def gen_key(self):
        self.leftshift()
        gen_key1 = self.P_8_Box()
        # print(self.key_start)
        # print(gen_key1)
        return gen_key1
