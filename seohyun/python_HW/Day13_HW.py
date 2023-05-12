fruits={"오렌지":30, "바나나":20, "사과":50}
for i in range(10):
    fruit=input("과일 상점 입니다. 어떤 과일을 원하시나요?:")
    if fruit in fruits:
        print(f"{fruit}는 {fruits[fruit]}개 있어요")
    else:
        print(f"저희 상점에는 {fruit}가 없습니다.")