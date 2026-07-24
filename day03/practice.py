# Day 3 练习 - 函数 def / *args / **kwargs / lambda
# 要求：独立完成下面 4 个练习，每个写 2-3 行 test case 打印验证后再 commit
# 提示：运行 python day03/practice.py 看输出

# 练习1：用 *args 实现任意个数数字相加
# 例如 add(1, 2) -> 3, add(1, 2, 3, 4) -> 10, add() -> 0
def add(*args):
    # 你的代码（args 是元组，用 sum 或循环累加）
    return sum(args)

# 练习2：用 **kwargs 把参数拼成 URL query string
# 例如 build_query(name="海申", age=22) -> "name=海申&age=22"
# 加分：用 urllib.parse.urlencode 做 URL 编码
def build_query(**kwargs):
    # 你的代码
    return "&".join(f"{k}={v}" for k, v in kwargs.items())

# 练习3：用 lambda + sorted 给字典列表按指定 key 排序
# 要求：按 age 升序，再按 name 降序各来一次
users = [{"name": "b", "age": 20}, {"name": "a", "age": 25}, {"name": "c", "age": 20}]
# 你的代码（key=lambda u: ...）
# print(sorted(users,key=lambda u : u["age"]))
# print(sorted(users,key=lambda u: u["name"],reverse=True))




# ===== 测试验证（写完上面函数后取消注释运行）=====
print(add(1, 2, 3, 4))
print(build_query(name="海申", age=22))
print(sorted(users,key=lambda u : u["age"]))
print(sorted(users,key=lambda u: u["name"],reverse=True))

