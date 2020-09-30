""" In class 200930 - Lucien Gaitskell """


class HanoiMove:
    def __init__(self, disk, src, dst):
        self.disk = disk
        self.src = src
        self.dst = dst
    def __repr__(self):
        return "Move ({}) rod {} -> {}".format(self.disk, self.src, self.dst)

    def __str__(self):
        return "Move disk {} from rod {} to rod {}".format(self.disk, self.src, self.dst)


def hanoi(disk, src, dst, other):
    history = []
    if disk == 1:
        #print("Move disk 1 from rod {} to rod {}".format(src, dst))
        return [HanoiMove(disk, src, dst)]

    history.extend(hanoi(disk - 1, src, other, dst))
    history.append(HanoiMove(disk, src, dst))
    #print("Move disk {} from rod {} to rod {}".format(disk, src, dst))
    history.extend(hanoi(disk - 1, other, dst, src))
    return history


for s in hanoi(4, 0, 1, 2):
    print(s)
