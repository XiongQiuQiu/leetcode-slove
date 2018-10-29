# -*- encoding=utf-8 -*-
# total = int(input("请输入利润总额："))
# total = 200000
# money_ranges = [100000, 100000, 200000, 200000, 400000, 1000000000]
# rates = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
# ans = 0
# for money,rate in zip(money_ranges,rates):
#     if total>money:
#         ans += money * rate
#         total -= money
#     else:
#         ans += total*rate
#         break
#
# for i in range(len(money_ranges)):
#     money = money_ranges[i]
#     rate = rates[i]
def reward_count(total):
    '''
    题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型
    :param total:
    :return: ans:
    '''
    money_ranges, rates = [100000, 100000, 200000, 200000, 400000, 1000000000], [0.1, 0.075,
                                                                                                                0.05, 0.03,
                                                                                                                0.015, 0.01]
    ans = reduce(lambda a, b: a + b, (
    pack[0] * pack[1] if total - sum(money_ranges[0:i + 1]) > 0 else max((total - sum(money_ranges[0:i])) * pack[1], 0) for
    i, pack in enumerate(zip(money_ranges, rates))))
    return ans
