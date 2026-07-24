# Python自动化测试学习知识库

> 每天结束自动追加，记录核心知识点。

---

## [2026-07-22] Day 1 - Python环境搭建、变量/数据类型/f-string

### 知识点1：Python变量（对比Java）
- **定义**：Python变量不需要声明类型，直接赋值即可。变量只是一个"标签"贴在值上，类型可以随时改变。
- **语法**：`name = "海申"`、`x = 10`（可比 Java 省略类型声明）
- **与Java对比**：Java 需要 `String name = "海申"; int x = 10;`，Python 无需类型声明，动态类型。
- **代码示例**：
  ```python
  name = "海申"       # 不需要 String name
  age = 22            # 不需要 int age
  score, grade = 95.5, "A"  # 一行声明多个
  x = 10              # x 是 int
  x = "hello"         # x 现在是 str，合法！
  ```
- **注意事项**：多变量赋值 `a, b = 1, 2` 本质是元组解包，左边变量数和右边值数要匹配。

### 知识点2：6大核心数据类型
- **类型表**：

| 类型 | Python | Java对应 | 注意 |
|------|--------|----------|------|
| 整数 | `int` | `int/long` | Python无限大，不会溢出 |
| 浮点 | `float` | `double` | 没有float/double之分 |
| 字符串 | `str` | `String` | 单引号双引号一样 |
| 布尔 | `bool` | `boolean` | 值是大写 `True`/`False` |
| 列表 | `list = [1,2,3]` | `List/ArrayList` | 动态扩容，任意类型 |
| 字典 | `dict = {"a":1}` | `Map/HashMap` | 和JSON天然互转 |

- **类型转换**：`int("42")`、`str(42)`、`float("3.14")`、`bool("")` → False（空字符串为假）
- **注意事项**：`type(x)` 返回类型对象，`type(x).__name__` 返回类型名字符串。

### 知识点3：f-string 格式化（7大维度）
- **定义**：Python 3.6+ 的字符串格式化，`{变量:格式说明符}` 结构，冒号左边是值，右边是格式。
- **语法结构**：`f"{变量:格式说明符}"`，冒号分隔变量和格式规则。
- **格式维度**：

| 维度 | 符号 | 示例 | 输出 |
|------|------|------|------|
| 左对齐 | `<` | `f"{'海申':<10}"` | `海申        ` |
| 右对齐 | `>` | `f"{'海申':>10}"` | `        海申` |
| 居中 | `^` | `f"{'海申':^10}"` | `    海申    ` |
| 符号左锁 | `=` | `f"{-3:=+5}"` | `-   3` (符号推最左) |
| 填充字符 | 任意 | `f"{42:0>5}"` | `00042` |
| 精度 | `.2f` | `f"{3.14:.2f}"` | `3.14` |
| 千分位 | `,` | `f"{123456:,}"` | `1,234,567` |
| 百分比 | `%` | `f"{0.875:.1%}"` | `87.5%` |
| 进制 | `b/o/x/X` | `f"{255:x}"` | `ff` |
| 正负号 | `+`/` ` | `f"{5:+}"` → `+5`; `f"{5: }"` → ` 5` | 正数前留空格 |
| 日期 | `%Y-%m-%d` | `f"{now:%Y-%m-%d}"` | `2026-07-22` |

- **核心三件套（日常够用）**：对齐（`<>^`）、精度（`.2f` `.1%`）、千分位（`,`）
- **注意事项**：`=` 对齐必须配合 `+` 或 ` ` 使用，只有数字类型有意义；`{变量: 填充 对齐 宽度 , .精度 类型}` 格式说明符顺序固定。

### 知识点4：字符串 join() 方法
- **定义**：用指定分隔符把列表元素拼接成一个字符串。
- **语法**：`"分隔符".join(列表)`
- **与Java对比**：Java 用 `String.join(", ", list)` 或 `StringUtils.join()`，Python 是分隔符直接调 join。
- **代码示例**：
  ```python
  ", ".join(["Java", "Spring", "MyBatis"])  # → "Java, Spring, MyBatis"
  "|".join(["a", "b"])                        # → "a|b"
  "".join(["a", "b", "c"])                    # → "abc"
  ```
- **注意事项**：join 要求列表元素都是字符串，有非字符串元素会报 TypeError。

### 知识点5：class 和 def 的区别
- **`class`**：定义类（容器/壳），类比 Java 的 `class`
- **`def`**：定义函数/方法（逻辑），类比 Java 的方法声明
- **`self`**：就是 Java 的 `this`，指向当前实例，Python 必须显式写在第一个参数
- **类型注解**：`def fn(x: int) -> int:` 中 `: int` 是参数类型提示，`-> int` 是返回值类型提示，不写也能跑，写了有 IDE 智能提示
- **注意事项**：LeetCode 的 `class Solution` 是固定模板，核心逻辑写在 `def` 的方法体里，return 返回结果。

### 知识点6：Python 缩进规则
- **核心原则**：Python 用缩进（4个空格）代替 `{}` 来划分代码块
- **对比Java**：
  ```python
  # Python
  if x > 0:
      print("正数")   # 缩进 = 属于 if 块
  print("结束")        # 不缩进 = 不属于 if
  ```
- **三个铁律**：①冒号下一行必须缩进 ②同一层级缩进量必须一致 ③VS Code 按 Tab 默认4空格
- **注意事项**：Tab 和空格不能混用，同一文件只能选一种。

### 知识点7：range() 和 len()
- **`len(list)`**：返回列表长度（元素个数），类比 Java 的 `list.size()`
- **`range(n)`**：生成 0 到 n-1 的整数序列，类比 Java 的 `for (int i = 0; i < n; i++)`
- **`range(start, stop)`**：从 start 到 stop-1
- **`for i in range(len(nums))`**：遍历列表的所有下标
- **注意事项**：`range(stop)` 不包括 stop；`range(len(list))` 等价于遍历 0 到 len-1。

### 知识点8：字典计数法（LC 1512 算法思维）
- **场景**：统计数组中相同元素能组成多少对
- **核心思路**：每遇到一个数字，查字典里它出现过几次 → 出现过 k 次就加 k 对 → 字典该数字次数+1
- **本质**：用字典的 O(1) 查找代替双重循环的 O(n²) 遍历
- **关键 API**：`dict.get(key, default)` 安全取值（键不存在返回默认值，不报错）
- **思维模型**：记事本（字典）随时记录"见过几次"，只用遍历一次数组
- **注意事项**：`count.get(num, 0)` 是高中频 API，比 `count[num]` 安全（不抛 KeyError）。

### 知识点9：GitHub SSH 推送配置
- **问题**：Windows 下 git HTTPS 推送可能遇到 Connection reset（防火墙/代理问题）
- **解决**：改用 SSH 协议
  1. `ssh-keygen -t ed25519 -C "邮箱"` 生成密钥
  2. 公钥（`~/.ssh/id_ed25519.pub`）添加到 GitHub Settings → SSH Keys
  3. `git remote set-url origin git@github.com:用户名/仓库.git` 切 SSH
- **日常推送**：`git add . && git commit -m "..." && git push`
- **注意事项**：HTTPS token 暴露后要立即删除；SSH 密钥要在每台新机器上重新配。

---

## [2026-07-23] Day 1 答疑补充 - list列表/f-string深化/原地排序/布尔值与dict安全取值

### 知识点1：list 列表核心操作与"可变引用"
- **定义**：list 是有序、可变的集合，方括号 `[]` 定义，一个列表可装不同类型的元素（Java 泛型 List 不行）。
- **常用操作**：`append(x)` 末尾追加、`insert(i,x)` 指定位置插、`remove(x)` 删首个匹配值、`pop()` 弹末尾并返回、`len(lst)` 长度、`x in lst` 是否存在、`count(x)` 计数、`sort()` 原地排序、`reverse()` 原地反转、`extend()` 合并、`clear()` 清空。
- **与Java对比**：`append`≈`add()`，`pop()`≈`remove(size-1)`，`sort()` 原地改（同 Java `Collections.sort`），`remove(x)`≈`remove(Object)`。
- **代码示例**：
  ```python
  lst = [3, 1, 2]
  lst.append(4)        # [3, 1, 2, 4]
  lst.insert(0, 9)     # [9, 3, 1, 2, 4]
  x = lst.pop()        # x=4, lst=[9,3,1,2]
  lst.sort()           # [1, 2, 3, 4, 9]
  ```
- **注意事项**：list 是可变引用类型，`b = a` 是共享同一对象（不是复制），改 b 会改 a；要真复制用 `a.copy()` 或 `a[:]`。

### 知识点2：list 索引与切片（左闭右开 + 负数倒序）
- **索引**：从 0 开始；支持负数从末尾数（`lst[-1]` 最后一个，`lst[-2]` 倒数第二），Java 没有负数索引。
- **切片 `[start:stop:step]`**：一次性取子列表，规则**左闭右开**；`[::2]` 隔一个取，`[::-1]` 反转列表。
- **索引 vs 切片**：`lst[2]` 返回**单个元素**；`lst[2:3]` 返回**列表**（哪怕只含一个元素）。
- **代码示例**：
  ```python
  lst = [0,1,2,3,4,5,6,7,8,9]
  lst[2]        # 2
  lst[-1]       # 9
  lst[2:5]      # [2,3,4]（不含5）
  lst[::2]      # [0,2,4,6,8]
  lst[::-1]     # [9,8,...,0] 反转
  ```
- **注意事项**：切片产生新列表（非原地），不改原列表；负数索引是 Python 特色，遍历倒数元素很方便。

### 知识点3：原地排序/反转 vs 非原地（最高频坑）
- **原地（in-place）**：`lst.sort()` / `lst.reverse()` 直接修改原列表，返回 `None`（不返回新列表）。
- **非原地**：`sorted(lst)` / `lst[::-1]` 不改原列表，返回新列表。
- **与Java对比**：Java `Collections.sort(list)` 也是原地、void，同 `lst.sort()`；但 Python 多 `sorted()` 返回新列表，更灵活。
- **代码示例**：
  ```python
  lst = [3, 1, 2]
  r = lst.sort()      # ❌ r 是 None！sort 没返回值
  print(lst)          # [1, 2, 3]  原列表被改

  new = sorted([3, 1, 2])  # ✅ new=[1,2,3]，原列表不变
  ```
- **注意事项**：想要新列表用 `sorted()` / `[::-1]`；想要改原列表用 `sort()` / `reverse()` 且**别接返回值**。初学者最高频 bug：`new_lst = lst.sort()` 拿到 `None`。

### 知识点4：f-string 深化（花括号写表达式 + 格式说明符）
- **定义**：`f"{值:格式}"`，冒号左边是变量/表达式，右边是格式说明符。
- **花括号里能写表达式**：`f"{x+5}"`、`f"{x>5}"`、`f"{'大' if x>5 else '小'}"`。
- **格式说明符维度**：

  | 维度 | 写法 | 示例→输出 |
  |------|------|----------|
  | 右对齐 | `:>宽` | `f"{'海申':>6}"`→`     海申` |
  | 左对齐 | `:<宽` | `f"{'海申':<6}"`→`海申     ` |
  | 居中 | `:^宽` | `f"{'海申':^6}"`→`  海申  ` |
  | 0填充 | `:0>宽` | `f"{3:0>3}"`→`003` |
  | 小数 | `:.2f` | `f"{3.14159:.2f}"`→`3.14` |
  | 千分位 | `:,` | `f"{1234567:,}"`→`1,234,567` |
  | 百分比 | `:.1%` | `f"{0.1234:.1%}"`→`12.3%` |
  | 进制 | `:x`/`:b` | `f"{255:x}"`→`ff` |

- **与Java对比**：比 Java `String.format("我是%s，今年%d岁", name, age)` 更直观，变量直接嵌入不用数占位符。
- **注意事项**：忘了 `f` 前缀会原样输出 `{name}`；引号嵌套冲突时外层双引号内层单引号；想输出字面 `{` 写 `{{`。

### 知识点5：True/False 写法 + dict.get 安全取值（Day1 易错点）
- **布尔值写法**：Python 是**首字母大写** `True` / `False`（其余小写），全小写 `true`/`false` 和全大写 `TRUE`/`FALSE` 都会报 `NameError`。Java 是 `true`/`false` 全小写，转换时最易写错。
- **dict.get(k, default) vs dict[k]**：`dict[k]` 键不存在直接抛 `KeyError` 程序崩；`dict.get(k, d)` 键不存在返回默认值 d，不报错。
- **代码示例**：
  ```python
  scores = {"语文": 90}
  scores["英语"]          # ❌ KeyError: '英语'
  scores.get("英语", 0)   # 0（安全兜底）
  # 计数场景必须用 get：
  counts = {}
  for num in [1, 2, 1, 1]:
      counts[num] = counts.get(num, 0) + 1   # {1:3, 2:1}
  ```
- **注意事项**：确定键存在用 `dict[k]`（不存在说明有 bug，让它早暴露）；不确定/计数/解析外部数据无脑用 `dict.get(k, 默认)`。

---

## [2026-07-23] Day 2 - 控制流(if/elif/else/for/while)+ 猜数字游戏

### 知识点1：if/elif/else 三分支判断
- **定义**：Python 用 `if/elif/else` 实现多分支判断，**elif 是 else if 的缩写**。
- **语法**：`if 条件1: ... elif 条件2: ... else: ...`
- **与Java对比**：

| 维度 | Python | Java |
|------|--------|------|
| 关键字 | `if / elif / else` | `if / else if / else` |
| 括号 | 条件不加 `()` | 条件必加 `()` |
| 代码块 | 缩进 4 空格 | `{ }` |
| 真值 | `if x:` 即可 | `if (x != 0)` 必写表达式 |
| 三元运算 | `a if cond else b` | `cond ? a : b` |

- **代码示例**：
  ```python
  score = 85
  if score >= 90:
      print("A")
  elif score >= 80:
      print("B")
  else:
      print("C")
  grade = "A" if score >= 90 else "B"   # Pythonic 三元
  ```
- **注意事项**：条件后必须有 `:` 冒号；`=` 赋值 / `==` 等于 不能混；Python 3.10+ 才有 match-case（基本不用）。

### 知识点2：Pythonic 真值表（重要！）
- **核心规则**：以下值全部为 `False`，其余全部为 `True`：
  - `False`、`0`、`0.0`、`""`（空串）、`[]`（空列表）、`{}`（空字典）、`None`
- **代码示例**：
  ```python
  if "":       # False
  if []:       # False
  if 0:        # False
  if -1:       # True（负数也是真！）
  if " ":      # True（空格不是空字符串）
  if [0]:      # True（列表非空，里面元素是 0 不影响）
  ```
- **注意事项**：这是 Python 特色，Java 思维转过来需要刻意练习；`None` 类似 Java 的 `null`。

### 知识点3：for 循环是遍历，不是计数
- **定义**：Python 的 `for` **遍历可迭代对象**，不是 Java 的 `for(int i=0;i<n;i++)` 计数循环。
- **语法形式**：
  ```python
  for x in list:           # 遍历元素（最常用）
  for i in range(n):       # 计数循环（range(0,n)）
  for i in range(1, 6):    # 1-5（前闭后开）
  for i, v in enumerate(list):  # 同时拿下标和值
  for k, v in dict.items():     # 遍历字典的 key-value
  for ch in "海申":         # 遍历字符串每个字符
  ```
- **与Java对比**：

| 需求 | Python | Java |
|------|--------|------|
| 遍历列表 | `for x in list:` | `for (X x : list)` |
| 遍历+下标 | `for i, x in enumerate(list):` | `for (int i=0; i<list.size(); i++)` |
| 循环 N 次 | `for i in range(N):` | `for (int i=0; i<N; i++)` |

- **注意事项**：`range(stop)` 不包含 stop，是**前闭后开**；`enumerate()` 是面试高频，会返回 `(下标, 值)` 元组。

### 知识点4：while 循环 + while...else 独家特色
- **while 经典形式**：
  ```python
  i = 0
  while i < 5:
      print(i)
      i += 1           # 必须有退出条件，否则死循环
  ```
- **while True + break 模式**（猜数字游戏典型写法）：
  ```python
  while True:
      cmd = input("> ")
      if cmd == "quit":
          break
  ```
- **独家特色：`while...else` / `for...else`**：
  - else 块在循环**正常结束**（没被 break 打断）时才执行
  - 被 break 跳出则 else 不执行
  ```python
  for i in range(5):
      if i == 3:
          break
  else:
      print("正常结束")   # 不会执行，因为被 break
  ```
- **注意事项**：`else` 关键字位置紧跟循环体，不是嵌套 if-else；这是 Python 独有，Java 没有，**面试高频**。

### 知识点5：三大控制语句
| 语句 | 作用 | Java 也有？ |
|------|------|----------|
| `break` | 跳出整个循环 | 有 |
| `continue` | 跳过本轮，进入下一轮 | 有 |
| `pass` | **啥也不干，占位用**（Python 独有） | 无 |

- **pass 场景**：
  ```python
  def todo_function():
      pass    # 还没想好怎么写，先放个空函数
  ```
- **注意事项**：不要在遍历 list 时增删元素（会跳过或报错），需要先 `list.copy()` 复制。

### 知识点6：input() 永远返回字符串
- **核心规则**：`input("提示语")` 永远返回 `str` 类型，**不管你输入什么**。
- **必须手动转类型**：
  ```python
  age = int(input("年龄："))    # 整数
  score = float(input("分数：")) # 浮点
  ```
- **异常处理（猜数字必备）**：
  ```python
  try:
      guess = int(input("输入数字："))
  except ValueError:
      print("输入有误")
      continue
  ```
- **Python vs Java 异常**：
  - Python：`try/except/finally`（不强制处理）
  - Java：`try/catch/finally`（checked 异常必须处理）
- **注意事项**：忘记 `int()` 转换是初学者最常见 bug；用户可能输错字母/空格，**猜数字一定要 try/except**。

### 知识点7：random 模块（猜数字游戏核心）
- **核心 API**：
  ```python
  import random
  random.randint(1, 100)    # 1-100 随机整数（包含两端）
  random.random()           # 0.0-1.0 浮点
  random.choice([1,2,3])    # 从列表随机选一个
  random.shuffle([1,2,3])   # 打乱列表（原地修改，无返回值）
  ```
- **与Java对比**：Java 用 `new Random().nextInt(100) + 1`，Python 直接 `random.randint(1, 100)` 更简洁。
- **注意事项**：`randint(a, b)` **两端都包含**（和 Java 的 `nextInt(100)` 不一样，Java 是 0-99）；`shuffle()` 是原地修改，**返回 None**，不能 `result = random.shuffle(list)`。

### 知识点8：完整猜数字游戏结构（Day 2 核心产出）
- **必须包含的 7 个要素**：
  1. `import random` 导入模块
  2. `random.randint(1, 100)` 生成答案
  3. `input()` + `int()` 接收用户输入
  4. `try/except ValueError` 处理输入异常
  5. `if/elif/else` 三分支判断大小
  6. `while` 循环 + 次数限制
  7. `while...else` 揭示答案（循环结束没猜中）
- **思维模型**：这是"循环 + 条件 + 异常处理"的综合训练，相当于 Java 的 Scanner + Random + if/else + 循环 + try/catch 五合一。
- **注意事项**：调试时可以把答案 print 出来，正式版删掉；用 `print(x, end=" ")` 不换行能改善体验。

---

## [2026-07-23] Day 2 答疑补充 - print控制/字符串比较/while边界坑

### 知识点1：print() 的 end 与 sep 参数（换行控制）
- **end**：控制结尾字符，默认 `"\n"`（换行）。`end=""` 不换行，`end=" "` 末尾加空格连着写。
- **sep**：多个参数之间的分隔符，默认空格。`print("a","b",sep="-")` → `a-b`。
- **代码示例**：
  ```python
  print("a", end=" ")   # 结尾空格不换行
  print("b")             # → a b
  print("a","b","c",sep="-")  # → a-b-c
  ```
- **注意事项**：默认就换行；想不换行必须显式写 `end=""`。

### 知识点2：input() 提示符 ≠ 对齐符号（易混）
- **核心**：`input("> ")` 里的 `"> "` 只是屏幕提示文字，引导用户输入，和格式/对齐毫无关系。
- **区分**：`f"{x:>10}"` 里的 `>` 才是右对齐（format spec）；**带冒号 `:` 在 f-string 里的 `>` 才是对齐**，input 引号里裸着的 `>` 只是提示符。
- **注意事项**：两个 `>` 长得一样但完全无关，别混。

### 知识点3：Python 字符串比较用 ==（Java 背景最高频坑）
- **Python**：`if pw == correct_pw:` 直接比**内容**，简单安全。
- **Java**：必须用 `pw.equals("x")`；用 `==` 比的是内存地址（对象引用），会判断错误。
- **代码示例**：
  ```python
  # Python（正确）
  if user_input == "admin123":
      print("登录成功")
  ```
- **注意事项**：从 Java 转 Python，字符串一律用 `==` 比内容，别带 Java 的 `.equals()` 思维。

### 知识点4：不要用 sum 作变量名（遮蔽内置函数）
- **原因**：`sum` 是 Python 内置函数（`sum([1,2,3])` → 6）。一旦写 `sum = 0` 赋值，就把内置函数覆盖了，后续想用真正的 `sum()` 会报错。
- **做法**：累加器改用 `total` / `result` / `acc`。
- **注意事项**：`list`/`dict`/`str`/`id`/`type`/`max`/`min` 等内置名都别用作变量名，这是老手常识。

### 知识点5：while 循环 <= vs < 的 off-by-one 边界坑
- **现象**：`while attempts <= max_attempts:`（如 max=3）会跑 **4 次**（attempts=0,1,2,3 都满足），导致"最多 3 次"变成 4 次。
- **正确**："最多 N 次"用 `while attempts < max_attempts:`（跑 0,1,2 三轮）。
- **口诀**：计数从 0 开始且要"最多 N 次" → 条件用 `< N`，不是 `<= N`。
- **调试技巧**：循环次数不对，先数条件边界（`<` 还是 `<=`），这是最高频的 off-by-one 错误。

### 知识点6：break vs continue 核心区别
- **break**：整个循环**立即终止**，跳出循环（走人）。
- **continue**：跳过**本轮**剩余代码，直接进入**下一轮**（这轮不算，继续干）。
- **大白话比喻**：break = 关掉电视不看了；continue = 跳过这集看下一集。
- **代码示例**：
  ```python
  for i in range(5):
      if i == 3: break
      print(i)    # 0 1 2（3,4 不跑）

  for i in range(5):
      if i == 3: continue
      print(i)    # 0 1 2 4（3 跳过，4 照常）
  ```

---

## [2026-07-24] Day 3 - 函数 def / *args / **kwargs / lambda / 重写 Java 工具方法

### 知识点1：函数 def 与四参数形式（顺序铁律）
- **定义**：`def` 定义函数，Python 用一个函数 + 四种参数形式吃下 Java 多个重载方法的活：**位置参数、默认参数、`*args`、`**kwargs`**。
- **顺序铁律（写错直接 SyntaxError）**：必选位置参数 → 默认参数 → `*args` → `**kwargs`，顺序不可乱。
- **与Java对比**：Java 靠方法重载 `overload` 实现多签名（如 `add(int)` / `add(int,int)`）；Python 一个 `def add(*args)` 全包。
- **代码示例**：
  ```python
  def f(a, b, c=10, *args, **kwargs):   # a,b 必选；c 默认；*args 多余位置；**kwargs 多余关键字
      return a, b, c, args, kwargs
  f(1, 2)                       # (1, 2, 10, (), {})
  f(1, 2, 3, 4, 5, x=9)         # (1, 2, 3, (4, 5), {'x': 9})
  # def f(**kwargs, a):         # ❌ SyntaxError：**kwargs 必须在最后
  ```
- **注意事项**：默认参数必须排在 `*args` 前面；`**kwargs` 永远最后一个；位置参数不能排在默认参数后面。

### 知识点2：*args / **kwargs 可变参数与解包
- **定义**：`*args` 把多余**位置参数**收集成元组；`**kwargs` 把多余**关键字参数**收集成字典。
- **调用端解包**：`func(*lst)` 把列表拆成位置参数；`func(**dict)` 把字典拆成关键字参数（测试里拼请求参数高频）。
- **与Java对比**：Java 用 `Object... args`（仅位置，无关键字版）；Python 的 `**kwargs` 灵活得多。
- **代码示例**：
  ```python
  def add(*args):
      return sum(args)                       # args 是元组 (1,2,3)
  add(1, 2, 3, 4)                            # 10

  def build_query(**kwargs):
      return "&".join(f"{k}={v}" for k, v in kwargs.items())
  build_query(name="海申", age=22)           # name=海申&age=22

  nums = [1, 2, 3]
  print(*nums)                               # 1 2 3（解包传参）
  ```
- **注意事项**：`args`/`kwargs` 只是约定名，前缀 `*`/`**` 才是关键；解包 `*` 还能合并列表 `[*a, *b]`。

### 知识点3：lambda 匿名函数 + sorted/map/filter
- **定义**：`lambda 参数: 表达式`，一行匿名函数，只能写一个表达式，**自动 return 表达式的值**，没有 `return` 关键字、不能写多行。
- **配合内置函数**：`sorted(iter, key=lambda)` 排序、`map(lambda, iter)` 映射、`filter(lambda, iter)` 过滤。
- **多条件排序**：`key=lambda x: (x["age"], -x["score"])` 按元组优先级排；`-` 实现降序。
- **与Java对比**：Java `list.stream().sorted(Comparator.comparing(User::getAge))`；Python `sorted(users, key=lambda u: u["age"])` 更短。
- **代码示例**：
  ```python
  users = [{"name":"b","age":20},{"name":"a","age":25},{"name":"c","age":20}]
  sorted(users, key=lambda u: u["age"])                 # 按 age 升序
  sorted(users, key=lambda u: (-u["age"], u["name"]))   # age 降序，name 升序

  list(map(lambda x: x*2, [1,2,3]))     # [2,4,6]
  list(filter(lambda x: x>1, [1,2,3]))  # [2,3]
  ```
- **注意事项**：lambda 只能一个表达式，复杂逻辑用 `def`；`map/filter` 返回迭代器，要看结果需 `list()` 包一层。

### 知识点4：默认参数陷阱（可变默认对象，面试高频）
- **现象**：默认参数只在**函数定义时**求值一次，如果默认值是可变对象（list/dict/set），多次调用会共享同一对象，累加污染。
- **代码示例（坑）**：
  ```python
  def add_item(item, lst=[]):
      lst.append(item)
      return lst
  add_item(1)    # [1]
  add_item(2)    # [1, 2]  ← 两次调用共享同一个 lst！
  ```
- **正确写法**：默认用 `None`，函数内再 new：
  ```python
  def add_item(item, lst=None):
      if lst is None:
          lst = []
      lst.append(item)
      return lst
  ```
- **注意事项**：默认参数**永远不要用可变对象**（list/dict/set），用 `None` + 函数内初始化替代。这是 Python 面试经典题，也是写 pytest fixture 时容易踩的坑。

### 知识点5：用 Python 重写 Java 工具方法（实战 - 测试常用）
- **场景**：把熟悉的 Java 工具（`StringUtils.isBlank`、`CollectionUtils`、`PageUtil`）用 Python 重写，是"开发转测试"的降维打击练习。
- **isBlank 重写（最实用，断言前置校验常用）**：
  ```python
  def is_blank(s: str) -> bool:
      """判断字符串是否为 None / 空串 / 全空白。测试里校验响应字段是否为空常用。"""
      return s is None or s.strip() == ""
  # is_blank(None) -> True; is_blank("") -> True; is_blank("  ") -> True; is_blank("a") -> False
  ```
- **与Java对比**：Java `org.apache.commons.lang3.StringUtils.isBlank(s)`；Python 几行搞定，用 `str.strip()` 替代 `trim()`。
- **注意事项**：重写时加**类型注解** + **docstring**（测试代码可读性要求高）；至少 3 个 case 验证边界（None / 空 / 空白 / 正常）。

---

## [2026-07-24] Day 3 任务推送摘要

- **阶段**：P1 Python基础
- **主题**：函数 def / *args / **kwargs / lambda / 重写 Java 工具方法
- **今日任务**：
  1. 函数 def 四参数形式与顺序铁律
  2. *args / **kwargs 可变参数与解包
  3. lambda + sorted/map/filter
  4. 用 Python 重写 Java 工具方法（is_blank）
- **产出文件**：
  - `python-auto-test-learning/day03/practice.py`（4个练习：add、build_query、sorted、is_blank）
  - `python-auto-test-learning/day03/is_blank.py`（重写版 + 至少4个断言验证）
- **小测验**：默认参数可变对象陷阱（`lst=[]` 共享问题，修复用 `lst=None`）
- **GitHub 提交**：`git add day03/ && git commit -m "Day 3: Python函数、*args/**kwargs、lambda、isBlank重写" && git push`
- **复习要点**：Day2 控制流（if/elif/else、for/while、while...else、break/continue、input转int、random）

---

## [2026-07-24] Day 2 易混点补充 - for...else / while...else 的 break 跳过语义（用户实测踩坑）

### 知识点1：for...else 里 break 会跳过 else（最高频误解）
- **误解**：用户以为 "else 和 for 同层级，break 不会跳过 else"，所以猜 `break` 后还会打印 `done`。❌ 完全相反。
- **真规则**：`for...else` / `while...else` 的 `else` 只在**循环完整跑完、一次 break 都没触发**时才执行；只要遇到 `break`，`else` 整块被跳过。
- **反例代码（实测输出只有 `end`）**：
  ```python
  for i in range(3):
      if i == 1:
          break
  else:
      print("done")     # ❌ 不执行，因为被 break 了
  print("end")           # end（唯一输出）
  ```
- **对照（无 break 才走 else）**：循环体加 `print(i)` 且不 break → 输出 `0 1 2 done end`。
- **记忆口诀**：else = "循环没被 break 打断才执行"。break 是 else 的死敌。
- **注意事项**：这是 Day 2 知识点4 的核心，面试高频；写"找到就返回、找不到就提示"类逻辑（如猜数字、查找元素）时，`else` 块放"未找到"提示。

---

## [2026-07-24] Day 3 易混点补充 - def 定义 vs 调用、形参 vs 实参（用户看 *args 示例卡住）

### 知识点1：定义函数 vs 调用函数，两个 () 含义完全不同
- **误解**：用户看到 `add(1, 2, 3, 4)` 里有数字，以为这是在"定义"函数，问"哪里有定义函数的代码"。
- **真规则**：`def add(*args):` 这一行**就是函数定义**（`add` 从此成为函数）；`add(1, 2, 3, 4)` 是**调用**（使用）已经定义好的函数，括号里的数字是实际传进去的**实参**。
- **两种 () 对照**：

  | 位置 | 代码 | () 里是什么 | 叫什么 |
  |------|------|------------|--------|
  | 定义时 | `def add(*args):` | `*args`（占位符，收集所有位置参数） | **形参 / 参数** |
  | 调用时 | `add(1, 2, 3, 4)` | `1, 2, 3, 4`（真实数据） | **实参 / 参数值** |

- **执行追踪（实测 args=(1,2,3,4) 返回 10）**：
  ```python
  def add(*args):          # 定义：args 是个"口袋"，啥都没装
      return sum(args)
  add(1, 2, 3, 4)          # 调用：1,2,3,4 被 *args 装进元组 (1,2,3,4)
  # 等价于 sum((1, 2, 3, 4)) -> 10
  ```
- **Java 对比**：`public int add(int... args) { return Arrays.stream(args).sum(); }` 是定义；`add(1,2,3,4)` 是调用。Java 的 `int... args` 就是 Python 的 `*args`（可变参数），结构一模一样。
- **注意事项**：不写 `*args` 而写 `def add(a, b, c, d):`，调用 `add(1,2,3,4)` 时 `a=1,b=2,c=3,d=4`（固定 4 个）；`*args` 的好处是能接**任意个数**参数，不用写死。

---

## [2026-07-24] Day 3 易混点补充 - *args/**kwargs 收集与解包方向相反 + lambda 自动 return/u 非固定

### 知识点1：同一个 `*`/`**`，在"定义侧"和"调用侧"方向相反（最易混）
- **核心区分**：`*`/`**` 出现在 **`def` 参数位置** = **收集（打包）**；出现在 **调用实参位置** = **解包（展开）**。方向完全相反！
- **收集（定义侧）**：`def f(*args)` 把调用时多传的位置参数打包成元组；`def f(**kwargs)` 把关键字参数打包成字典。
- **解包（调用侧）**：`f(*lst)` 把列表拆成多个位置参数传进去；`f(**dict)` 把字典拆成多个关键字参数传进去。
- **代码示例（实测）**：
  ```python
  def f(*args): print(args)          # 收集 → (1, 2, 3)
  f(1, 2, 3)

  def g(a, b, c): print(a, b, c)
  g(*[1, 2, 3])                       # 解包 → a=1,b=2,c=3（等价 g(1,2,3)）

  def h(**kwargs): print(kwargs)      # 收集 → {'name':'海申','age':22}
  h(name="海申", age=22)

  def k(name, age): print(name, age)
  k(**{"name":"海申","age":22})        # 解包 → name=海申,age=22
  ```
- **额外技巧**：`[*a, *b]` 合并列表、`{**a, **b}` 合并字典。
- **记忆口诀**：def 里 `*` = 收口袋；调用里 `*` = 拆包裹。同一符号，方向相反。

### 知识点2：lambda 自动 return + 参数名(如 u)不是固定的
- **自动 return**：`lambda 参数: 表达式` 是一个**一行匿名函数**，它**自动把"表达式的值"返回**，不需要写 `return` 关键字，也**不能写多行/多条语句**。
  ```python
  lambda x: x * 2
  # 完全等价于：
  def f(x):
      return x * 2
  ```
- **u 不是固定的**：`sorted(users, key=lambda u: u["age"])` 里的 `u` 只是**参数名（占位符）**，跟 `x`、`user`、`item` 没区别。它**不固定**——`sorted` 会**对每个元素各调用一次 lambda**，每次把当前元素绑给 `u`。
- **执行追踪（实测 u 依次取每个元素）**：
  ```python
  users = [{"name":"b","age":20},{"name":"a","age":25},{"name":"c","age":20}]
  sorted(users, key=lambda u: u["age"])
  # 第1次调用: u={"name":"b","age":20} → 返回 20
  # 第2次调用: u={"name":"a","age":25} → 返回 25
  # 第3次调用: u={"name":"c","age":20} → 返回 20
  # 按 [20,25,20] 排序 → [b(20), c(20), a(25)]
  ```
- **注意事项**：lambda 只能有一个表达式，复杂逻辑（if/循环/多步）必须用 `def`；参数名随便起，`u` 只是"user"的缩写约定，换成 `x` 结果一样。

---

## [2026-07-24] Day 3 易混点补充 - 元组 / lambda冒号前是参数(非函数名) / sorted+key 拆解

### 知识点1：元组 tuple —— 不可变的"冻结列表"
- **定义**：元组是有序、不可变的序列，用圆括号 `()` 或逗号定义：`t = (1, 2, 3)` 或 `t = 1, 2, 3`。
- **与 list 区别**：`list` 可改（append/赋值），`tuple` 创建后**不能改元素**（实测 `t[0]=99` 报 `'tuple' object does not support item assignment`）。
- **能用**：下标 `t[0]`、负数 `t[-1]`、遍历 `for x in t`（和 list 一样）。
- **为什么 `*args` 用元组**：收集来的参数不应被改动，元组天然"只读"更安全。
- **Java 对比**：Java 没原生元组，最接近 `List.of(1,2,3)`（不可变列表）或写个 record/class。
- **注意事项**：需要改内容用 `list`；只是打包传递用 `tuple`。`(1)` 不是元组（是 int），单元素元组要 `(1,)`。

### 知识点2：lambda 冒号前面是"参数"，不是函数名（关键纠正）
- **误解**：用户以为 `lambda x: x*2` 里 `x` 是"函数名"。❌ 错。lambda 是**匿名函数，根本没有名字**。
- **真结构**：
  ```
  lambda   参数1, 参数2, ...   :   表达式(自动返回)
    ↑            ↑                  ↑
  关键字       参数(占位符)       函数体/返回值
  ```
- **示例**：
  ```python
  lambda x: x * 2        # x 是参数；x*2 是表达式(自动返回)，x 不是函数名
  lambda x, y: x + y     # 多个参数用逗号
  f = lambda x: x * 2    # 只有assign给变量才"有名字"，但官方不推荐，直接用 def
  ```
- **注意事项**：lambda 前面永远是参数列表（可为空 `lambda: 42`）；想给函数起名用 `def`，不要用 `变量 = lambda`。

### 知识点3：sorted(users, key=lambda u: u["age"]) 逐段拆解
- **整体**：`sorted(可迭代, key=函数)` 返回**新的**排好序的列表（不改原列表，实测原 users 不变）。
- **`users`**：元素为字典的列表 `[{"name":"b","age":20}, ...]`。
- **`key=lambda u: u["age"]`**：`key=` 是 sorted 的关键字参数，传一个"取排序键"的函数；lambda 对每个元素调用一次，`u` 依次绑每个字典，`u["age"]` 取出年龄作排序依据。
- **拆解执行**：
  ```
  元素 {"name":"b","age":20} → key 20
  元素 {"name":"a","age":25} → key 25
  元素 {"name":"c","age":20} → key 20
  按 [20,25,20] 升序 → 元素顺序 [b(20), c(20), a(25)]
  ```
- **`u["age"]` 含义**：`u` 是字典，`["age"]` 取键 "age" 的值（即年龄数字）。
- **注意事项**：`sorted` 返回新列表，要保存结果得 `result = sorted(...)`；`key=` 只决定"按什么排"，不改动元素本身；降序加 `reverse=True`。

---

## [2026-07-24] Day 3 易混点补充 - sorted / map / filter 三大内置函数（含迭代器惰性陷阱）

### 知识点1：sorted —— 排序，返回新列表
- **签名**：`sorted(iterable, key=函数, reverse=False)`。返回**新的**排好序列表，**不改动原数据**（实测原 nums 不变）。
- **`key=`**：传一个"取排序键"的函数（常用 lambda）；`reverse=True` 降序。
- **与 list.sort() 区别**：`sorted()` 返回新列表不改原；`list.sort()` 原地改原列表、返回 None（Day2 已讲原地 vs 非原地）。
- **代码示例**：
  ```python
  nums = [3, 1, 2]
  sorted(nums)                 # [1, 2, 3]，nums 仍是 [3,1,2]
  sorted(nums, reverse=True)   # [3, 2, 1]
  sorted(users, key=lambda u: u["age"])   # 按 age 升序
  ```

### 知识点2：map —— 逐个映射，返回迭代器（惰性）
- **签名**：`map(func, iterable)`。对 iterable 每个元素调用 `func`，返回一个**迭代器**（不是列表！）。
- **惰性 + 一次性**：迭代器"用到才算"，且**只能消费一次**——第一次 `list(r)` 有值，第二次 `list(r)` 变空（实测）。
- **看结果必须 `list()` 包一层**：`list(map(lambda x: x*2, [1,2,3]))` → `[2,4,6]`。
- **Java 对比**：Java `list.stream().map(x -> x*2).collect(toList())`；Python `map` 对应 `.map()`，但 Python 要手动 `list()` 收尾。
- **代码示例**：
  ```python
  r = map(lambda x: x * 2, [1, 2, 3])
  list(r)            # [2, 4, 6]
  list(r)            # []  ← 第二次空了！迭代器已耗尽
  ```

### 知识点3：filter —— 按条件过滤，返回迭代器（惰性）
- **签名**：`filter(func, iterable)`。保留 `func` 返回"真值"的元素，返回**迭代器**。
- **真值规则**：沿用 Day2 真值表——空串/`0`/`None`/空列表等为假，其余为真。
- **看结果同样要 `list()`**：`list(filter(lambda x: x % 2 == 0, [1,2,3,4]))` → `[2, 4]`。
- **代码示例**：
  ```python
  list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))        # [2, 4]（只留偶数）
  list(filter(lambda s: not is_blank(s), ["a", "", "b"])) # 过滤掉空串
  ```
- **注意事项（map/filter 通用）**：返回的都是迭代器，①要看到内容用 `list()`；②只能遍历一次，重复使用要先 `list()` 存下来或重新 `map/filter`。

### 知识点4：三者对测试的价值
- `sorted`：断言前给期望/实际列表排序，避免因顺序不同误报失败；接口返回列表按字段排序校验。
- `map`：批量提取字段，如 `list(map(lambda u: u["id"], users))` 抽出所有 id。
- `filter`：从一堆数据筛出满足条件的，如筛出失败用例、非空字段。

## [2026-07-24] Day 3 易混点补充（续）：set 集合 + 验证方式

### 知识面：set 集合（无序、不重复）
- **定义**：用 `{}`（或 `set()`）创建，**元素唯一、无顺序、不能下标**。
  ```python
  s = {1, 2, 3}
  s.add(3)          # 已有, 无变化（实测仍 {1,2,3,4} 是又 add(4) 后）
  s.add(4)
  print(s)          # {1,2,3,4}  顺序不保证
  print(set([1, 1, 2, 2, 3]))   # {1,2,3}  ← 最常用: 去重
  ```
- **集合运算**（测试里做差异比对高频）：
  ```python
  a, b = {1, 2, 3}, {3, 4, 5}
  a & b     # 交集 {3}：两者都有
  a | b     # 并集 {1,2,3,4,5}：合并去重
  a - b     # 差集 {1,2}：a 有 b 没有
  ```
- **成员判断极快**：`2 in a` → `True`（O(1)，比 list 的 `in` 快得多，大数据量必用 set）。
- **坑**：`set` 不能下标 `s[0]`（实测 `'set' object is not subscriptable`）；空集合必须写 `set()`，不能写 `{}`（`{}` 是空字典）。
- **与 Java 对比**：Java `Set<Integer> s = new HashSet<>();`（同样无序去重）；Python `{}` 字面量更短。字符串用 `set("aab")` → `{'a','b'}`。

### 知识点：函数验证的三种方式（以 is_blank 为例）
- **背景**：Day3 任务4 要求给重写的 `is_blank` 写 ≥3 个 case 验证边界（None/空/空白/正常）。"验证"就是确认函数输出 == 你预期的输出。
- **方式1 直接打印（最糙，人工核对）**：
  ```python
  for c in [None, '', '  ', 'a']:
      print(repr(c), '->', is_blank(c))   # None->True  ''->True  '  '->True  'a'->False
  ```
  缺点：要人眼一个个看对不对，容易漏。
- **方式2 期望对照（推荐，一眼看出 OK/FAIL）**：
  ```python
  expected = {None: True, '': True, '  ': True, 'a': False}
  for c, exp in expected.items():
      got = is_blank(c)
      print(f"{'OK ' if got==exp else 'FAIL'} | 输入={c!r:6} 期望={exp} 实际={got}")
  # OK  | 输入=None   期望=True 实际=True  ...
  ```
  每个 case 自带"期望"，自动打 OK/FAIL，不用动脑核对。
- **方式3 assert（最专业，Day15 pytest 的底层）**：
  ```python
  assert is_blank(None) is True
  assert is_blank('') is True
  assert is_blank('  ') is True
  assert is_blank('a') is False
  # 全部通过才往下走; 任一不满足立刻抛 AssertionError 并标出哪行
  ```
  `assert 条件`：条件为真啥也不发生；为假直接报错中断——这正是 pytest 跑用例的核心机制（Day15 正式学）。
- **注意**：`is` 用于比 `True/False/None` 这种单例；比普通值用 `==`。验证时优先方式2（打印友好）或方式3（自动判错）。

### 知识点：迭代器 iterator 与惰性 laziness
- **迭代器是什么**：一种"一个一个往外吐元素"的对象，用 `iter(可迭代对象)` 造出来，用 `next()` 取下一个。列表/元组/字符串/set/dict 都是"可迭代的"（能被 for 遍历），但本身不是迭代器——`iter(列表)` 才得到迭代器。
  ```python
  it = iter([1, 2, 3])
  next(it)   # 1
  next(it)   # 2
  next(it)   # 3
  next(it)   # 抛 StopIteration（取完了）
  ```
- **一次性（最重要坑）**：迭代器**只能往前走、走完即废**。取尽后再 `next()` 抛 `StopIteration`；想要再遍历一遍，必须重新 `iter(原对象)` 造一个新迭代器（实测原列表 `lst` 还在，没被消耗）。这正是 `map`/`filter` 返回迭代器、第二次 `list()` 变空的原因。
- **惰性 laziness = 按需计算，不到用时不算**：
  - 列表推导 `[double(x) for x in data]` 是 **eager（急切）**——创建时立刻把所有元素算完（实测 double 立刻被调用 2 次）。
  - 生成器(`yield`)/`map`/`filter` 是 **lazy（惰性）**——`g = gen()` 或 `r = map(...)` 创建时**啥也不算**，只有 `next()` / `list()` 真正消费时才逐个计算（实测 `map` 创建后无任何打印，直到 `list(r)` 才逐个调 `double`）。
  - 好处：省内存（处理 1000 万条数据不必全加载进内存）、支持无限序列。
- **代码对比（实测）**：
  ```python
  def gen():
      print('  产出 1'); yield 1
      print('  产出 2'); yield 2
  g = gen()        # 此刻无打印（惰性）
  next(g)          # 才打印"产出 1"并返回 1
  ```
- **`for` 循环本质**：`for x in 列表` 内部就是先 `iter(列表)` 拿迭代器，再反复 `next()` 直到 `StopIteration`。所以"能被 for 遍历"的对象都叫可迭代对象。
- **Java 对比**：Java `Iterator<E>` 同样 `hasNext()`/`next()` 一次性遍历；Python 的 `yield` 生成器 ≈ Java `Stream`（惰性、链式）。
- **记忆口诀**：迭代器=一次性水龙头（拧完没水，要重开）；惰性=用到才拧，不预支。

### 知识面：list 是有序、可重复的
- **有序（order）**：list 严格保持**插入顺序**，每个元素有固定下标（0 起，`-1` 是最后一个），多次打印顺序不变（实测 `[1,2,2,3,1]` 顺序稳定）。
- **可重复（duplicate）**：同一个值可以出现多次（实测 `[1,2,2,3,1]` 长度 5，1 和 2 都重复）。
- **能改**：list 是可变的，可 `append`/`pop`/按下标改（对比 tuple 不可变、set 无序不重复）。
- **list vs set 对照**（实测）：
  | | 有序 | 可重复 | 能下标 | 能改 |
  |---|---|---|---|---|
  | `list []` | ✅ | ✅ | ✅ | ✅ |
  | `set {}` | ❌ | ❌ | ❌ | ✅(add) |
  | `tuple ()` | ✅ | ✅ | ✅ | ❌ |
- **Java 对比**：Java `List` 同样有序可重复；`Set` 才不重复（对应 Python set）。

### 知识点：`dict.items()` 是什么
- **`dict.items()`**：字典的方法，返回**键值对视图**（实测类型 `dict_items`），每个元素是 `(键, 值)` 元组：`list(d.items())` → `[('name','海申'), ('age',22)]`。
- **用途**：同时遍历键和值的最常用写法——
  ```python
  d = {'name': '海申', 'age': 22}
  for k, v in d.items():
      print(k, v)        # name 海申 / age 22
  ```
- **兄弟方法**：`d.keys()` 只取所有键；`d.values()` 只取所有值（实测 `keys()=['name','age']`、`values()=['海申',22]`）。
- **坑**：`items()` 返回的是"视图"不是列表（Python3），要当列表用必须 `list(d.items())`；遍历时改字典大小会报错，先转 `list()` 再改。
- **和 Day3/Day2 的关联**：`build_query(**kwargs)` 里 `kwargs.items()` 就是把 `**kwargs` 收来的字典拆成键值对拼 URL；Day2 `for i in range()` 是遍历数字，这里是遍历键值对。
- **Java 对比**：Java `map.entrySet()` 对应 `items()`；`map.keySet()` 对应 `keys()`；`map.values()` 对应 `values()`。

### 知识点：docstring 文档字符串
- **是什么**：写在 `def`/`class`/`模块` **第一行**、用**三引号 `'''` 或 `"""`** 包起来的字符串，专门给这个函数/类写"说明书"。
  ```python
  def is_blank(s):
      '''判断字符串是否为 None / 空串 / 全空白。
      参数:
          s (str|None): 待判断的字符串
      返回:
          bool: 为空返回 True, 否则 False
      '''
      return s is None or s.strip() == ''
  ```
- **怎么读出来**：存在 `函数名.__doc__` 属性里（实测 `is_blank.__doc__` 能打印出整段说明）；`help(函数名)` 也会读它显示帮助（实测 help 输出含 docstring）。
- **没写会怎样**：`函数.__doc__` 是 `None`（实测 `no_doc.__doc__ = None`），`help()` 只显示签名没有说明。
- **写法规范（测试代码可读性要求高，必写）**：
  - 单行：`'''一句话说明'''`
  - 多行：首行一句话概述，空一行写参数/返回值（Google 风格最常见）
  - 用 `:param s:` 或 `参数:` 标注入参类型与含义；`返回:` 标注返回类型
- **和注释 `#` 的区别**：`#` 是给读代码的人看的行内注释，不进属性；docstring 是对象的一部分，能被 `help()`/`__doc__`/IDE 提示/Sphinx 文档工具读取。
- **Day3 任务4 要求**：重写 `is_blank` 必须带 docstring（讲清"判断空/空白"的用途），这是测试代码规范的基本功。
- **Java 对比**：Java 用 Javadoc `/** ... */` + `@param`/`@return`，写在方法上方；Python docstring 写在方法体内第一行，作用相同（生成 API 文档）。
