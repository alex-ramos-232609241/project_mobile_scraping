from selenium.webdriver.common.by import By
from features.paginas_flujo.reserva import Reserva
from features.flujos.flujo_reserva import LAYOUT_INFO_RESERVA_2
from features.paginas_flujo.pagina_base import Page

reserva = Reserva()

class InfoReservationPageTwo(Page):

    ID_PRECIO_COMPARAR = (By.ID, LAYOUT_INFO_RESERVA_2["ID_PRECIO_COMPARAR"])
    XPATH_PRECIO_NAVBAR = (By.XPATH, LAYOUT_INFO_RESERVA_2["XPATH_PRECIO_NAVBAR"])
    ID_BTN_ULTIMO_PASO = (By.ID, LAYOUT_INFO_RESERVA_2["ID_BTN_ULTIMO_PASO"])
    
    def get_price_reservation_two(self):

        pFinal = self.get_value_text(self.XPATH_PRECIO_NAVBAR)
        v_reserva = reserva.get_precio_reserva()
        print('------precios-----')
        print(pFinal)
        print(v_reserva)
        self.click_on_element(self.ID_BTN_ULTIMO_PASO)
        assert v_reserva == pFinal
        
        
        