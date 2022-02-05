from homework.homework06022022.el_auto.automobil import Automobil


class Electro(Automobil):
    def __init__(self, brand, model, year, odd, soh):
        self.soh = soh
        super().__init__(brand, model, year, odd)

    def electro_info(self):
        Automobil.auto_info(self)
        print(f"остаточная емкость батареи {self.soh} %")
