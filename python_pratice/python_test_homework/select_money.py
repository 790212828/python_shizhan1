import money


def select_money():
    print(f"select出来的saved_money ID：{id(money.saved_money)}")
    # print(f"查询出来余额：{money.saved_money}")
    return money.saved_money
