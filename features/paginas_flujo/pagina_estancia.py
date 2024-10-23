from time import sleep
from selenium.webdriver.common.by import By
from features.flujos.flujo_reserva import LAYOUT_ESTANCIA
from features.paginas_flujo.pagina_base import Page

class EstanciaPage(Page):
    ID_ELEGIR_ESTAS_OPCIONES = (By.ID, LAYOUT_ESTANCIA["ID_ELEGIR_ESTAS_OPCIONES"])
    XPATH_SELECIONAR = (By.XPATH, LAYOUT_ESTANCIA["XPATH_SELECIONAR"])
    ID_BTN_SELECCIONAR = (By.ID, LAYOUT_ESTANCIA["ID_BTN_SELECCIONAR"])
    XPATH_RESERVAR_AHORA = (By.XPATH, LAYOUT_ESTANCIA["XPATH_RESERVAR_AHORA"])
    
    def eligiendo_opciones(self):
        self.click_on_element(self.XPATH_SELECIONAR)
        self.click_on_element(self.ID_BTN_SELECCIONAR)
        self.click_on_element(self.XPATH_RESERVAR_AHORA)
        # if self.find_element(self.ID_ELEGIR_ESTAS_OPCIONES):
        #     self.click_on_element(self.ID_ELEGIR_ESTAS_OPCIONES)
        # else:
        #     self.click_on_element(self.XPATH_SELECIONAR)
        sleep(2)
