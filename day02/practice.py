"""
Day 2 练习：控制流练习
自己动手写，不要看 guess_number.py 的答案
"""

# 练习1：用 for 循环打印 1-20 中所有的偶数
# 提示：if i % 2 == 0

for i in range(1,21):
    if i % 2 ==0:
        print(i)

# 第二种写法
for i in range(2,21,2):
    print(i)


# 练习2：用 while 循环计算 1+2+3+...+100 的和
# 提示：sum = 0, i = 1, while i <= 100

sum = 0
i = 1
while i <= 100:
    sum = sum + i
    i += 1
print(sum)

# 练习3：遍历列表，打印每个元素的下标和值
# 用 enumerate

fruits = ["苹果", "香蕉", "橘子", "西瓜"]
for i, v in enumerate(fruits,start=1):
    print(f"第{i}个:{v}")

# 练习4：写一个简易登录验证
# 用户输入密码，正确就打印"登录成功"，错误就继续输入，最多3次机会
# 正确密码：admin123

correct_pw = "admin123"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    pw = input("请输入正确密码：")
    if pw == correct_pw:
        print("密码正确！")
        break
    else:
        attempts += 1
        print(f"密码错误，还剩{max_attempts-attempts}次机会")
else:
    print("三次都错，账户锁定")

