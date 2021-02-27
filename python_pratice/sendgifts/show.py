# from gift import have_gift
import gift


# 展示礼物
def show():
    have_gift = gift.have_gift
    print(f"show之前的 局部have_gift:{id(have_gift)}")
    print(f"show之前全局:{id(gift.have_gift)}")
    if have_gift == True:
        print("收到礼物啦，很开心~")
    else:
        print("没有礼物")

    print(f"show之后的 局部have_gift:{id(have_gift)}")
    print(f"show之后全局:{id(gift.have_gift)}")
