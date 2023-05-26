class 수학:
    def 삼각형넓이(self,가로,세로):
        넓이=가로*세로/2
        return 넓이
구냥=수학()

for i in range(5):
    rnsid=input("밑변의 길이를 입력하시오:")
    rnsids=input("높이의 길이를 입력하시오:")
    print(f"밑변이 {rnsid}이고 높이가{rnsids}일때 삼각형의 넓이는{구냥.삼각형넓이(int(rnsid), int(rnsids))}")