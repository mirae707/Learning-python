drink = {"물": 300, "우유": 1000, "커피":700, "콜라": 500}
money = int(input("돈을 넣어주세요: "))
while money >= 300:
    choice = input('음료를 선택하세요\n물: 300\n우유: 1000\n커피:700\n콜라: 500\n환불: 취소\n')
    if choice == "취소":
        break
    for beverage, price in drink.items():
        if beverage == choice:
            money -= price
            if money < 0:
               print("\n잔액이 부족합니다. 다시 선택해주세요.\n")
               money += price
               continue
            print("\n\t***", beverage, " 나왔습니다. ***\n")
    print("남은돈은", money, "입니다.\n")
print("\n----- 잔돈", money, "원 입니다. 안녕히가세요~ -----\n")
