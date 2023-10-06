import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np
from gen_key import generation_key as gk
from encrypt import encrypt as enc
from PIL import Image, ImageTk
def choose():
    def change1():
        root0.destroy()
        one()
    def change2():
        root0.destroy()
        two()

    # 创建主窗口
    root0 = tk.Tk()
    root0.title('加解密系统')

    # 获取屏幕宽度和高度
    screen_width = root0.winfo_screenwidth()
    screen_height = root0.winfo_screenheight()

    # 计算窗口左上角坐标使其居中
    x = (screen_width - 400) // 2
    y = (screen_height - 600) // 2

    # 设置窗口大小和位置
    root0.geometry('400x600+{}+{}'.format(x, y))

    # 设置主窗口背景颜色
    root0.configure(bg='blue')

    # 创建一个Frame来容纳按钮，并使其在窗口中垂直居中
    frame = tk.Frame(root0)
    frame.pack(expand=True, fill=tk.BOTH)
    # 添加背景图片
    background_image = Image.open("background.jpg")  # 替换成你的背景图片文件路径
    background_image = background_image.resize((400, 600), Image.ANTIALIAS)  # 调整大小
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(frame, image=background_photo)
    background_label.place(relwidth=1, relheight=1)
    # 创建并设置标签的外观
    label = tk.Label(frame, text='请选择你要加密的文本格式', bg='lightblue', font=('宋体', 14))
    label.pack(fill=tk.X, pady=10)

    # 创建并设置按钮的外观
    btn01 = tk.Button(frame, text="二进制文本", command=change1, font=('宋体', 12), width=15, height=2)
    btn01.pack(pady=100, padx=5, anchor='center')

    btn02 = tk.Button(frame, text="字符文本", command=change2, font=('宋体', 12), width=15, height=2)
    btn02.pack(pady=10, padx=5, anchor='center')

    root0.mainloop()

def one():
    def spl_bin(input):
        cip = []
        for i in range (len(input)):
            cip.append(int(input[i]))
        return cip
    
    def encrypt():
        k = spl_bin(str(entry.get()))
        g_key = gk(k)
        key1 = g_key.gen_key()
        key2 = g_key.gen_key()
        Enc = enc(key1, key2)
        input = spl_bin(str(en1.get()))
        Enc = enc(key1, key2)
        cip = Enc.gen_cip(input)
        print(cip)
        messagebox.showinfo("密文",cip)
    
    def solve():
        k = spl_bin(str(entry.get()))
        input1 = spl_bin(str(en2.get()))
        g_key = gk(k)
        key1 = g_key.gen_key()
        key2 = g_key.gen_key()
        Enc = enc(key1, key2)
        pla = Enc.sol_cip(input1)
        print(pla)
        messagebox.showinfo("明文",pla)

    def back():
        root1.destroy()
        choose()

    # 创建主窗口
    root1 = tk.Tk()
    root1.title('二进制编码')

    # 获取屏幕宽度和高度
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()

    # 计算窗口左上角坐标使其居中
    x = (screen_width - 400) // 2
    y = (screen_height - 600) // 2

    # 设置窗口大小和位置
    root1.geometry('400x600+{}+{}'.format(x, y))

    # 添加背景图片
    background_image = Image.open("background.jpg")  # 替换成你的背景图片文件路径
    background_image = background_image.resize((400, 600), Image.ANTIALIAS)  # 调整大小
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root1, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    # 创建文本变量
    v1 = tk.StringVar()

    # 创建输入框
    # 创建文本变量
    v1 = tk.StringVar()
    lab00 = tk.Label(root1, text='密钥', bg='lightblue', font=('宋体', 12))
    lab00.pack(pady=20)
    # 创建输入框并设置字体和大小
    entry = tk.Entry(root1, textvariable=v1, font=('宋体', 12), width=40)
    v1.set("1, 0, 1, 0, 0, 0, 0, 0, 1, 0")
    entry.pack(pady=10)

    # 创建标签并设置字体、大小和背景颜色
    lab01 = tk.Label(root1, text='请输入明文', bg='lightblue', font=('宋体', 12))
    lab01.pack(pady=30)

    # 创建明文输入框并设置字体和大小
    en1 = tk.Entry(root1, font=('宋体', 12), width=40)
    en1.pack(pady=5)

    # 创建加密按钮，设置字体、大小和背景颜色
    button1 = tk.Button(root1, text="加密", command=encrypt, font=('宋体', 12), width=15, height=2)
    button1.pack(pady=10)

    # 创建标签并设置字体、大小和背景颜色
    lab02 = tk.Label(root1, text='请输入密文', bg='lightblue', font=('宋体', 12))
    lab02.pack(pady=30)

    # 创建密文输入框并设置字体和大小
    en2 = tk.Entry(root1, font=('宋体', 12), width=40)
    en2.pack(pady=5)

    # 创建解密按钮，设置字体、大小和背景颜色
    button2 = tk.Button(root1, text="解密", command=solve, font=('宋体', 12), width=15, height=2)
    button2.pack(pady=10)

    # 创建返回按钮，设置字体、大小和背景颜色
    button3 = tk.Button(root1, text="返回", command=back, font=('宋体', 12), width=15, height=2)
    button3.pack(pady=10)


    root1.mainloop()

def two():
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
    
    def spl_bin(input):
        cip = []
        for i in range (len(input)):
            cip.append(int(input[i]))
        return cip
    
    def encrypt():
        print("明文: " + en3.get())
        k = spl_bin(str(entry1.get()))
        g_key = gk(k)
        key1 = g_key.gen_key()
        key2 = g_key.gen_key()
        Enc = enc(key1, key2)
        data = spl(str(en3.get()))
        cip = ""
        for i in range(data.shape[0]):
            a = Enc.gen_cip(data[i, :])
            cip = cip + chr(sum_bin(a))
        print(cip)
        messagebox.showinfo("密文", cip)

    def solve():
        print("明文: " + en3.get())
        k = spl_bin(str(entry1.get()))
        g_key = gk(k)
        key1 = g_key.gen_key()
        key2 = g_key.gen_key()
        Enc = enc(key1, key2)
        print("密文：" + en4.get())
        data1 = spl(str(en4.get()))
        pla = ""
        for i in range(data1.shape[0]):
            b = Enc.sol_cip(data1[i, :])
            pla = pla + chr(sum_bin(b))
        
        print(pla)
        messagebox.showinfo("明文", pla)
    
    def back():
        root2.destroy()
        choose()

        # 创建主窗口

    root2 = tk.Tk()
    root2.title('二进制编码')

    # 获取屏幕宽度和高度
    screen_width = root2.winfo_screenwidth()
    screen_height = root2.winfo_screenheight()

    # 计算窗口左上角坐标使其居中
    x = (screen_width - 400) // 2
    y = (screen_height - 600) // 2

    # 设置窗口大小和位置
    root2.geometry('400x600+{}+{}'.format(x, y))

    # 添加背景图片
    background_image = Image.open("background.jpg")  # 替换成你的背景图片文件路径
    background_image = background_image.resize((400, 600), Image.ANTIALIAS)  # 调整大小
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root2, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    # 创建文本变量
    v1 = tk.StringVar()

    # 创建输入框
    # 创建文本变量
    v1 = tk.StringVar()
    lab00 = tk.Label(root2, text='密钥', bg='lightblue', font=('宋体', 12))
    lab00.pack(pady=20)
    # 创建输入框并设置字体和大小
    entry1 = tk.Entry(root2, textvariable=v1, font=('宋体', 12), width=40)
    v1.set("1010000010")
    entry1.pack(pady=10)

    # 创建标签并设置字体、大小和背景颜色
    lab01 = tk.Label(root2, text='请输入明文', bg='lightblue', font=('宋体', 12))
    lab01.pack(pady=30)

    # 创建明文输入框并设置字体和大小
    en3 = tk.Entry(root2, font=('宋体', 12), width=40)
    en3.pack(pady=5)

    # 创建加密按钮，设置字体、大小和背景颜色
    button1 = tk.Button(root2, text="加密", command=encrypt, font=('宋体', 12), width=15, height=2)
    button1.pack(pady=10)

    # 创建标签并设置字体、大小和背景颜色
    lab02 = tk.Label(root2, text='请输入密文', bg='lightblue', font=('宋体', 12))
    lab02.pack(pady=30)

    # 创建密文输入框并设置字体和大小
    en4 = tk.Entry(root2, font=('宋体', 12), width=40)
    en4.pack(pady=5)

    # 创建解密按钮，设置字体、大小和背景颜色
    button2 = tk.Button(root2, text="解密", command=solve, font=('宋体', 12), width=15, height=2)
    button2.pack(pady=10)

    # 创建返回按钮，设置字体、大小和背景颜色
    button3 = tk.Button(root2, text="返回", command=back, font=('宋体', 12), width=15, height=2)
    button3.pack(pady=10)

    root2.mainloop()


#  定义密钥
"""
k = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
k = [1 ,1, 1, 1, 1, 0, 0, 0, 0, 0]

g_key = gk(k)
key1 = g_key.gen_key()
key2 = g_key.gen_key()
Enc = enc(key1, key2)
# cip = Enc.gen_cip(input)
# print(cip)
# a = [1, 1, 0, 0, 1, 1, 1, 0]
# print(pla)  ù@3ª÷
"""

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

if __name__ == '__main__':
    choose()
