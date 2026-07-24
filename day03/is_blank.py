# 练习4：用 Python 重写一个 Java 工具方法
# 选 StringUtils.isBlank 或 你熟悉的 Java 工具方法
# 要求：函数 + 默认参数 + docstring + 至少 3 个 case 验证
def is_blank(s, trim=True):
    '''判断字符串是否为空或全空白。
    规则：null、空串、首尾全身空白字符，都是为"空”

    参数：
        s(str|None):待判断的字符串，允许传None
        trim(bool):True(默认)时把首尾空白也判空；
                    False时仅 null/空串判为空，含非空白字符即非空

    返回：
        bool：为空返回True，否则返回 False
    '''
    # 你的代码：判断字符串为 None / "" / 全空白 都算 blank
    if s is None:
        return True
    if trim:
        s=s.strip()
    return s  == ""

# === 验证：用“期望对照法”，自带预期值，自动打OK/FAIL ===
if __name__ == "__main__":
    excepted = {
        None:True,      # null → 空
        "":True,        # 空串 → 空
        "   ":True,     # 全空白 → 空
        "a":False,      # 有字符 → 非空
        " hi ":False,   # 含非空白 → 非空
    }
    for case, exp in excepted.items():
        got = is_blank(case)
        status = "OK" if got == exp else "FAIL"
        print(f"{status} | 输入={case!r:6} 期望={exp} 实际={got}")


# print(is_blank(None), is_blank(""), is_blank("  "), is_blank("a"))