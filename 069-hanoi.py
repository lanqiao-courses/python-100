class Hanoi(object):

    def move_disks(self, num_disks, src, dest, buff):
        if src is None or dest is None or buff is None:
            raise TypeError('Cannot have a None input')
        self._move_disks(num_disks, src, dest, buff)

    def _move_disks(self, num_disks, src, dest, buff):
        if num_disks == 0:
            return
        self.move_disks(num_disks - 1, src, buff, dest)
        dest.push(src.pop())
        self.move_disks(num_disks - 1, buff, dest, src)