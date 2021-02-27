import money


def send_money(add_money):
    print(f"存储前的saved_money：{money.saved_money}")
    print(f"存储前的saved_money ID:{id(money.saved_money)}")
    money.saved_money = money.saved_money + add_money
    print(f"存储后的saved_money：{money.saved_money}")
    print(f"存储后的saved_money ID:{id(money.saved_money)}")
    return money.saved_money
