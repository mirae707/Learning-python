# 다음과 같은 내용을 지닌 파일 test.txt가 있다.
# 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
# Life if too short
# you need java
f1 = open("test7.txt", 'w')
f1.write.replace("java", "python")
f1.close()

f2 = open("test7.txt", 'r')
print(f2.read())
f2.close()
