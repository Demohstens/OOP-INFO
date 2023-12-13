class Gebäude:
    def __init__(self, typ, bewohner):
        self.typ = typ
        self.bewohner = bewohner
    def einziehen(self, person):
        self.bewohner = person
        