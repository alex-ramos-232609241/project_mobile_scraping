class SinglentonReserva(type):

    _instancias = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            instance = super().__call__(*args, **kwargs)
            cls._instancias[cls] = instance
        return cls._instancias[cls]     

class Reserva(metaclass=SinglentonReserva):
    
    costoReserva = ''
    comprobandoFlujo = False

    def set_precio_reserva(self, value):
        self.costoReserva = value

    def get_precio_reserva(self):
        return self.costoReserva

    def set_comprobando_flujo(self, value):
        self.comprobandoFlujo = value

    def get_comprobando_flujo(self):
        return self.comprobandoFlujo    