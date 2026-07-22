"""
Day 1: Python 变量 / 数据类型 / f-string
任务：运行这个文件，补全下方的自测题代码
"""

# ============================================
# 自测题：输出测试报告
# ============================================

name = "李海申"
age = 22

# TODO: 补全 f-string，输出如下格式：
# ========== 测试报告 ==========
# 姓名：李海申 | 年龄：22
# Python成绩：95.5（优秀）
# 学过的语言：Java, Spring Boot, MyBatis
# =============================

score = 95.5
grade = "优秀" if score >= 90 else "良好"
languages = ["Java", "Spring Boot", "MyBatis"]

print("\n========== 测试报告 ==========")
# 👇 在这里补全你的代码
print(f"姓名:{name} | 年龄:{age}")
print(f"Python成绩:{score} ({grade})")
print(f"学过的语言:{', '.join(languages)}")
print("=============================")
