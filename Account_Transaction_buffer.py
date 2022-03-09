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

from collections import defaultdict, deque
class Bank:
    def __init__(self,transfer_limit, window_size) -> None:
        self.transfer_limit = transfer_limit
        self.window_size = window_size
        self.account_fre = dict()
        self.account_blance = dict()
        self.recent_transactions = deque()

    def addAccount(self, account):
        if account not in self.account_blance:
            self.account_blance[account] = 0
            self.account_fre[account] = 0

    def checkFrequency(self, trans_acc:list[int]):
        if len(self.rerecent_transactions)>=self.window_size:
            trans = self.recent_transactions.popleft()
            for account in trans:
                if account in self.account_fre:
                    self.account_fre[account] -= 1
        r = list()
        for account in trans_acc:
            if account in self.account_fre:
                self.account_fre[account] += 1
                if self.account_fre[account]>=self.transfer_limit:
                    r.append(account)
        self.recent_transactions.append(trans_acc)
        return r

    def amountChange(self, account, amount):
        self.addAccount(account)
        self.account_blance[account] += amount

    def deposit(self, account, amount:int):
        self.amountChange(account, amount)
        return self.checkFrequency([account])

    def withdraw(self, account, amount:int):
        self.amountChange(account, -amount)
        return self.checkFrequency([account])

    def transfer(self, sender, recipient, amount):
        self.amountChange(sender, -amount)
        self.amountChange(recipient, amount)
        return self.checkFrequency([sender, recipient])

    def getBalance(self, account):
        return self.account_blance[account]

def Solution(f:F):
    batch_size = int(f.readline())
    transfer_limit = int(f.readline())
    window_size = int(f.readline())
    bank = Bank(transfer_limit, window_size)
    output = list()
    while True:
        accounts = set()
        flagged = list()
        last = False
        for i in range(batch_size):
            line:str = f.readline()
            if not line:
                last = True
                break
            line = line.split(',')
            char = line[0][0]
            if char == 'd':
                account = int(line[1])
                flag = bank.deposit(account, int(line[2]))
                accounts.add(account)
            elif char == 'w':
                account = int(line[1])
                flag = bank.withdraw(account, int(line[2]))
                accounts.add(account)
            else:
                sender = int(line[1])
                recipient = int(line[2])
                flag = bank.transfer(sender, recipient, int(line[3]))
                accounts.add(sender)
                accounts.add(recipient)
            flagged.extend(flag)
        accounts = list(accounts)
        accounts.sort()
        flagged.sort()
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

