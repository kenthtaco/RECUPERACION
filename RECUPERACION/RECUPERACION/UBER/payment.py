import datetime

class Payment():
    id     = str
    valor  = float
    fecha  = datetime.datetime.now

    def __init__(self, id, valor, fecha):
        self.id    = id
        self.valor = valor
        self.fecha = fecha