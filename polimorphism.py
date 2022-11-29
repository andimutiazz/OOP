class Division1():

    def __init__(self, wfo, wfh):
        self.work_from_office = wfo
        self.work_from_home = wfh

    def total_workers_present(self):
        return self.work_from_office + self.work_from_home

class Division2():
    def __init__(self, rw, h):
        self.remaining_worker = rw
        self.holiday = h

    def total_workers_present(self):
        return self.remaining_worker - self.holiday


d1 = Division1(223, 70)
d2 = Division2(765, 87)

print(d1.total_workers_present())
print(d2.total_workers_present())

