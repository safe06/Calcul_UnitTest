class Calcul:
    def additionner(self, a, b):
        return a + b

    def soustraire(self, a, b):
        return a - b

    def multiplier(self, a, b):
        return a * b

    def diviser(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Division par zéro impossible"

    # # version 2 de division par 0    
    # def diviser(self, a, b):
    #     if b == 0:
    #         raise ZeroDivisionError("Division par zéro impossible")
    #     return a / b