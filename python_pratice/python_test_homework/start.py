"""
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
"""

from select_money import select_money
from send_money import send_money

if __name__ == '__main__':
    save_money = 1000
    print(f"准备存储的金额：{save_money}")
    print(f"工资卡余额：{select_money()}")
    send_money(save_money)
    aa = select_money()
    print(f"查询出来的余额：{aa}")
    print(id(aa))
