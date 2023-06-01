import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print("倒计时:", seconds, "秒")
        time.sleep(1)
        seconds -= 1
    print("时间到！专注结束。")

# 设置专注时长为25分钟
focus_timer(25)
