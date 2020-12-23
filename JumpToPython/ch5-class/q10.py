# os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자.
# C:\doit 디렉터리로 이동한다.
# dir 명령을 실행하고 그 결과를 변수에 담는다.
# dir 명령의 결과를 출력한다.
import os
print(os.getcwd())
os.chdir("/home/cocojun/Documents/project/test")
result = os.popen("ls")
print(result.read())
