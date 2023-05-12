for i in range(11):
    fruits={"오렌지":30,"바나나":20,"사과":50}
    fruit=input("과일상점 임미당! 어떤 과일을 원하시나여?>v< : ")
    if fruit in fruits:
        print(f"{fruit}는 {fruits[fruit]}개 잇어영>v<")
    else:print(f"죄송하지만 저희 상점에는 {fruit}이 없어요 ㅠ.ㅠ")