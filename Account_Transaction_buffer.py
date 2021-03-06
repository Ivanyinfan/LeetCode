class F:
    def __init__(self, lines) -> None:
        for i in range(len(lines)):
            if len(lines[i])>0 and lines[i][-1]!='\n':
                lines[i] += '\n'
        self.lines = lines
        self.index = -1

    def readline(self):
        self.index += 1
        return self.lines[self.index]

from collections import deque
class Bank:
    def __init__(self,transfer_limit, window_size) -> None:
        self.transfer_limit = transfer_limit
        self.window_size = window_size
        self.account_fre = dict()
        self.account_blance = dict()
        self.recent_transactions = deque()
        self.recent_accounts = set()
        self.recent_flagged = list()

    def addAccount(self, account):
        if account not in self.account_blance:
            self.account_blance[account] = 0
            self.account_fre[account] = 0
        self.recent_accounts.add(account)

    def checkFrequency(self, trans_acc:list[int]):
        if len(self.recent_transactions)>=self.window_size:
            trans = self.recent_transactions.popleft()
            for account in trans:
                if account in self.account_fre:
                    self.account_fre[account] -= 1
        for account in trans_acc:
            if account in self.account_fre:
                self.account_fre[account] += 1
                if self.account_fre[account]>=self.transfer_limit:
                    self.recent_flagged.append(account)
                    self.account_fre.pop(account)
        self.recent_transactions.append(trans_acc)

    def amountChange(self, account, amount):
        self.addAccount(account)
        self.account_blance[account] += amount

    def deposit(self, account, amount:int):
        self.amountChange(account, amount)
        self.checkFrequency([account])

    def withdraw(self, account, amount:int):
        self.amountChange(account, -amount)
        self.checkFrequency([account])

    def transfer(self, sender, recipient, amount):
        self.amountChange(sender, -amount)
        self.amountChange(recipient, amount)
        self.checkFrequency([sender, recipient])

    def getBalance(self, account):
        return self.account_blance[account]

    def getBatchResult(self):
        accounts, flagged = self.recent_accounts, self.recent_flagged
        accounts = list(accounts)
        accounts.sort()
        flagged.sort()
        self.recent_accounts = set()
        self.recent_flagged = list()
        return accounts, flagged

def Solution(f:F):
    batch_size = int(f.readline())
    transfer_limit = int(f.readline())
    window_size = int(f.readline())
    bank = Bank(transfer_limit, window_size)
    output = list()
    while True:
        last = False
        for _ in range(batch_size):
            line:str = f.readline()
            if not line:
                last = True
                break
            line = line.split(',')
            char = line[0][0]
            if char == 'd':
                account = int(line[1])
                bank.deposit(account, int(line[2]))
            
            elif char == 'w':
                account = int(line[1])
                bank.withdraw(account, int(line[2]))
            else:
                sender = int(line[1])
                recipient = int(line[2])
                bank.transfer(sender, recipient, int(line[3]))
                
        accounts, flagged = bank.getBatchResult()
        for account in accounts:
            output.append(f'{account},{bank.getBalance(account)}\n')
        if len(flagged)==0:
            output.append("EMPTY\n")
        else:
            for account in flagged:
                output.append(f'{account}\n')
        if last == True:
            break
    return output

from utils import test
if __name__ == "__main__":
    f = F(["3\n",\
            "4\n",\
            "5\n",\
            "deposit,1,100",\
            "withdraw,2,100",\
            "transfer,1,2,100",\
            "transfer,1,3,100",\
            "deposit,2,100",\
            ""])
    test(Solution(f),["1,0\n",\
                        "2,0\n",\
                        "EMPTY\n",\
                        "1,-100\n",\
                        "2,100\n",\
                        "3,100\n",
                        "EMPTY\n"])
    f = F(["5",\
            "3",\
            "5",\
            "deposit,1,200",\
            "transfer,1,2,200",\
            "deposit,2,200",\
            "transfer,2,1,200",\
            "transfer,1,3,100",\
            "transfer,1,2,100",\
            "transfer,3,2,100",\
            ""])
    test(Solution(f),["1,100\n",\
                        "2,200\n",\
                        "3,100\n",\
                        "1\n",\
                        "2\n",\
                        "1,0\n",\
                        "2,400\n",\
                        "3,0\n",
                        "EMPTY\n"])
