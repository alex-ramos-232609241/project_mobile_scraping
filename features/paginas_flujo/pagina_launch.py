from selenium.webdriver.common.by import By
from features.flujos.flujo_reserva import LAYOUT_BUSQUEDA
from features.paginas_flujo.pagina_base import Page


class LaunchPage(Page):
    BUTTON_CONTINUE_SEARCH = (By.ID, LAYOUT_BUSQUEDA["ID_BOTON_CONTINUE_BUSQUEDA"])

    def continue_search(self):
        self.click_on_element(self.BUTTON_CONTINUE_SEARCH)
