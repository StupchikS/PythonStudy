class Student:
    def __init__(self, name, name_machine, proc, ozu):
        self.name = name
        self.n_machine_ozu = self.Machine(name_machine, proc, ozu)

    def info(self):
        print(f"{self.name} => ", end="")
        self.Machine.info(self.n_machine_ozu)

    class Machine:
        def __init__(self, name_machine, proc, ozu):
            self.name_machine = name_machine
            self.proc = proc
            self.ozu = ozu

        def info(self):
            print(f"{self.name_machine}, {self.proc}, {self.ozu}")


p1 = Student("Roman", "HP", "i7", 16)
p2 = Student("Vladimir", "Acer", "i5", 8)
p3 = Student("Sergei", "Toshiba", "i7", 8)
p1.info()
p2.info()
p3.info()
