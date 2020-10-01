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

    history.extend(hanoi(disk - 1, src, other, dst))  # Move next smallest disk to other pole
    history.append(HanoiMove(disk, src, dst))         # Move this disk to dst pole
    #print("Move disk {} from rod {} to rod {}".format(disk, src, dst))
    history.extend(hanoi(disk - 1, other, dst, src))  # Move the next smallest disk back on top of this disk (on dst)
    return history


for s in hanoi(4, 0, 1, 2):
    print(s)
