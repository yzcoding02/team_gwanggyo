class 도형넓이:
    def __init__(self,반지름,밑변,높이):
        self.원주율=3.141592
        self.반지름=반지름
        self.밑변=밑변
        self.높이=높이
    def 원(self):
        결과=self.원주율*self.반지름*self.반지름
        return 결과
    def 삼각형(self):
        결과=self.밑변*self.높이/2
        return 결과
    def 평행사변형(self):
        결과=self.밑변*self.높이
        return 결과
    def 원기둥겉넓이(self):
        결과=2*self.원주율*self.반지름*self.높이+2*self.원주율*self.반지름*self.반지름
        return 결과
중등도형넓이=도형넓이(2,3,4)
print(중등도형넓이.원())
print(중등도형넓이.삼각형())
print(중등도형넓이.평행사변형())
print(중등도형넓이.원기둥겉넓이())