from selenium.webdriver.common.by import By
from features.paginas_flujo.reserva import Reserva
from features.flujos.flujo_reserva import LAYOUT_INFO_RESERVA_1
from features.paginas_flujo.pagina_base import Page

reserva = Reserva()

class InfoReservationPage(Page):
    ID_PRECIO_RESERVA = (By.ID, LAYOUT_INFO_RESERVA_1["ID_PRECIO_RESERVA"])
    ID_BTN_ELEGIR_HABITACION = (By.ID, LAYOUT_INFO_RESERVA_1["ID_BTN_ELEGIR_HABITACION"])
    
    
    def get_price_reservation(self):
        valor_precio_reserva = self.find_element(self.ID_PRECIO_RESERVA).text
        reserva.set_precio_reserva(valor_precio_reserva)
        self.click_on_element(self.ID_BTN_ELEGIR_HABITACION)
        
        