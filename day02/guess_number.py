"""
Day 2: 猜数字小游戏
知识点：if/elif/else + for/while + input() + random
"""

import random

 # 生成1-100的随机数
answer = random.randint(1,100)
print("=====猜数字游戏=====")
print("我心里想了一个 1-100 的数字，你来猜！")

attempts = 0 
max_attempts = 7

while attempts < max_attempts:
    # input() 返回字符串，要转成 int
    guess = int(input(f"\n第{attempts + 1}/{max_attempts}次猜，输入数字："))
    attempts += 1

    if guess > answer:
        print("大了，往小了猜")
    elif guess < answer:
        print("小了，往大了猜")
    else:
        print(f"恭喜！！第{attempts}次猜对了")
        break
else:
    # while...else：循环正常结束（没被 break）才执行
    print(f"游戏结束，正确答案是{answer}")
print("="*20)