for i in range(11):
    fruits={"오랜지":30,"바나나":20,"사과":50}
    fruit=input("과일 상점 입니당. 어떤 과일을 드릴까여??@^@:")
    if fruit in fruits:
        print(f"{fruit}는 {fruits[fruit]}개 있습니당!!")
else:
    print(f"죄송하지만 저희 상점에는 {fruit}이 없어용ㅠ")