print("안녕하세요 희선 자판기입니다.\n")
money = int(input("돈을 넣어주세요.(단위는 빼고 숫자만 입력하세요.)"))

water = 300
coke = 500
sprite = 500
coffee = 700
juice = 800
milk = 1000

while (money >= water):
    drink = input("음료를 선택해 주세요.\n물: 300\n콜라: 500\n사이다: 500\n커피: 700\n오렌지주스: 800\n우유: 1000\n돈 반환은 '취소'를 입력하세요.")
    if drink == "취소":
        break
    elif drink == "물":
        if money < water:
            print("돈이 부족합니다. 다시 선택해주세요.\n")
            continue
        print("물 한 병 나왔습니다.\n")
        money -= water
        print("남은 돈은", money, "won 입니다.")
    elif drink == "콜라":
        if money < coke:
            print("돈이 부족합니다. 다시 선택해주세요.\n")
            continue
        print("콜라 한 병 나왔습니다.\n")
        money -= coke
        print("남은 돈은", money, "won 입니다.")
    elif drink == "사이다":
        if money < sprite:
            print("돈이 부족합니다. 다시 선택해주세요.\n")
            continue
        print("사이다 한 병 나왔습니다.\n")
        money -= sprite
        print("남은 돈은", money, "won 입니다.")
    elif drink == "커피":
        if money < coffee:
            print("돈이 부족합니다. 다시 선택해주세요.\n")
            continue
        print("커피 한 잔 나왔습니다.\n")
        money -= coffee
        print("남은 돈은", money, "won 입니다.")
    elif drink == "오렌지주스":
        if money < juice:
            print("돈이 부족합니다. 다시 선택해주세요.\n")
            continue
        print("오렌지주스 한 병 나왔습니다.\n")
        money -= juice
        print("남은 돈은", money, "won 입니다.")
    elif drink == "우유":
        if money < milk:
            print("돈이 부족합니다. 다시 선택해주세요.\n")
            continue
        print("우유 한 잔 나왔습니다.\n")
        money -= milk
        print("남은 돈은", money, "won 입니다.")
    else:
        print("잘못입력하셨습니다. 메뉴를 다시 선택해주세요!\n")
        continue
print("감사합니다! 잔돈:", money, "won 이 남았습니다. 안녕히가세요~")
