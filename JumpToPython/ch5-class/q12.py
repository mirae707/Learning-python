# time모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.
# 2018/04/03 17:20:32
import time
time.time()
time.localtime(time.time())
time.asctime(time.localtime(time.time()))
time.ctime()
print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time())))
