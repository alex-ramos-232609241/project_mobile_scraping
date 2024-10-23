from selenium.webdriver.common.by import By
from features.flujos.flujo_reserva import LAYOUT_SELECCION
from features.paginas_flujo.pagina_base import Page

class SelectionPage(Page):
    XPATH_SEGUNDO_ITEM = (By.XPATH, LAYOUT_SELECCION["XPATH_SEGUNDO_ITEM"])
    
    def click_seleccion_busqueda(self):
        self.click_on_element(self.XPATH_SEGUNDO_ITEM)
        