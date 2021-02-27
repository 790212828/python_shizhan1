from gift import have_gift
import gift


# 发礼物方法
def send():
    print("发礼物拉")
    # global  have_gift
    # have_gift=True
    print(f"send之前：{id(have_gift)}")
    gift.have_gift = True
    print(f"send后:{id(gift.have_gift)}")
