from car import Car

class UberXL(Car):
    asientos  =  int

    def __init__(self, placa, modelo, color, año, driver, asientos):
        super().__init__(placa, modelo, color, año, driver)
        self.asientos = asientos