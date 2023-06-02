class Bank:
    def __init__(self,잔액,예금주,계좌번호):
        self.잔액=잔액
        self.예금주=예금주
        self.계좌번호=계좌번호
    def 입금(self,금액):
        self.잔액+=금액
        print(f"{self.예금주}님의 계좌에 {금액}원이 입금되어 현재 {self.잔액}원 입니다")
    def 출금(self,금액):
        self.잔액-=금액
        print(f"{self.예금주}님의 계좌에서 {금액}원이 출금되어 현재 {self.잔액}원 입니다")