import parent as p
class 우리은행(p.Bank):
    def __init__(self, 잔액, 예금주, 계좌번호):
        super().__init__(잔액, 예금주, 계좌번호)
        self.이자율 = 0.2
    def 입금(self,금액):
        self.잔액=self.잔액+금액*(1+self.이자율)
        print(f"{self.예금주}님의 계좌에 이자 {금액*self.이자율}원이 더해져 현재 {self.잔액}원 입니다")