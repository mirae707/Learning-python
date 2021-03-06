<<<<<<< HEAD
=======
"""
A 씨는 게시판 프로그램을 작성하고 있다.
그런데 게시물의 총 건수와 한 페이지에 보여 줄 게시물 수를 입력으로 주었을 때 총 페이지 수를 출력하는 프로그램이 필요하다고 한다.

    ※ 이렇게 게시판의 페이지 수를 보여 주는 것을 "페이징"한다고 부른다.

    함수 이름은? getTotalPage
    입력 받는 값은? 게시물의 총 건수(m), 한 페이지에 보여줄 게시물 수(n)
    출력하는 값은? 총 페이지수

A씨가 필요한 프로그램을 만들기 위해 입력값과 결괏값이 어떻게 나와야 하는지 먼저 살펴보자.
게시물의 총 건수가 5이고 한 페이지에서 보여 줄 게시물 수가 10이면 총 페이지 수는 당연히 1이 된다.
만약 게시물의 총 건수가 15이고 한 페이지에서 보여 줄 게시물 수가 10이라면 총 페이지 수는 2가 될 것이다.
"""

>>>>>>> b593de3cf6a09f330d1740b60d8567e3f1e2822f
def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))
