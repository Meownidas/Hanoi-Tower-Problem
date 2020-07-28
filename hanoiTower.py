class Stack():

    def __init__(self):
        self._stack = []
        self._top = -1

    def __str__(self):
        return "".join("{}\n".format(x) for x in self._stack[::-1])

    def peek(self):
        if self.isEmpty():
            return
        return self._stack[self._top]

    def isEmpty(self):
        return self._top < 0

    def pop(self):
        if self.isEmpty():
            return
        self._top -= 1
        return self._stack.pop()

    def push(self, data):
        self._stack.append(data)
        self._top += 1


def moveTo(fromTower, toTower):
    toTower.push(fromTower.pop())


def moveToVia(fromTower, toTower, viaTower):
    moveTo(fromTower, viaTower)
    moveTo(viaTower, toTower)


def solve(numOfDisc, fromTower,  viaTower, toTower):
    if numOfDisc == 0:
        pass
    else:
        solve(numOfDisc-1, fromTower, toTower, viaTower)
        moveTo(fromTower, toTower)
        solve(numOfDisc-1, viaTower, fromTower, toTower)


def main():
    towerA = Stack()
    towerB = Stack()
    towerC = Stack()
    
    numOfDisc = 4
    for i in range(numOfDisc, 0, -1):
        towerA.push(i * 10)

    solve(numOfDisc, towerA, towerB, towerC)


if __name__ == "__main__":
    main()
