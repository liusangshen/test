import time, datetime


def get_week_day(date):
    week_day_dict = {
        0: '周一',
        1: '周二',
        2: '周三',
        3: '周四',
        4: '周五',
        5: '周六',
        6: '周日',
    }
    # 获取date对应的时间选项
    day = date.weekday()
    # 返回date匹配到的周X
    return week_day_dict[day]


# 获取今日的日期
now = datetime.datetime.now()
# 获取30天后的日期
later = now + datetime.timedelta(days=30)

#
n = get_week_day(now)
l = get_week_day(later)

print("今天是:", n)
print("30天后是:", l)


# 打印99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{0}*{1}={2} ".format(i, j, i * j), end="")
    print("")

# 打印直角三角形
for i in range(1, 5):
    for j in range(1, i + 1):
        print("*", end="")
    print("")

# 打印等腰三角形
for i in range(1, 6):
    for k in range(6 - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print("* ", end="")
    print("")
