from selenium.webdriver.common.by import By
from features.flujos.flujo_reserva import LAYOUT_DATOS_RESERVANTE
from features.paginas_flujo.pagina_base import Page

class DatosClientePage(Page):
    XPATH_INPUT_NOMBRE = (By.XPATH, LAYOUT_DATOS_RESERVANTE["XPATH_INPUT_NOMBRE"])
    XPATH_INPUT_APELLIDO = (By.XPATH, LAYOUT_DATOS_RESERVANTE["XPATH_INPUT_APELLIDO"])
    XPATH_INPUT_EMAIL = (By.XPATH, LAYOUT_DATOS_RESERVANTE["XPATH_INPUT_EMAIL"])
    XPATH_INPUT_DIRECCION = (By.XPATH, LAYOUT_DATOS_RESERVANTE["XPATH_INPUT_DIRECCION"])
    XPATH_CODIGO_POSTAL = (By.XPATH, LAYOUT_DATOS_RESERVANTE["XPATH_CODIGO_POSTAL"])
    XPATH_INPUT_CIUDAD = (By.XPATH, LAYOUT_DATOS_RESERVANTE["XPATH_INPUT_CIUDAD"])
    XPATH_INPUT_PAIS = (By.XPATH, LAYOUT_DATOS_RESERVANTE["XPATH_INPUT_PAIS"])
    XPATH_INPUT_TELEFONO = (By.XPATH, LAYOUT_DATOS_RESERVANTE["XPATH_INPUT_TELEFONO"])
    ID_BTN_MOTIVO = (By.ID, LAYOUT_DATOS_RESERVANTE["ID_BTN_MOTIVO"])
    ID_BTN_PASO_SIGUIENTE = (By.ID, LAYOUT_DATOS_RESERVANTE["ID_BTN_PASO_SIGUIENTE"])
    
        
    def add_data_reservante(self, nombre, apellido, email ):
        self.hide_keyboard()
        self.find_element(self.XPATH_INPUT_NOMBRE).clear()
        self.input(nombre, self.XPATH_INPUT_NOMBRE)
        self.find_element(self.XPATH_INPUT_APELLIDO).clear()
        self.input(apellido, self.XPATH_INPUT_APELLIDO)
        self.find_element(self.XPATH_INPUT_EMAIL).clear()
        self.input(email, self.XPATH_INPUT_EMAIL)

    def add_data_reservante_ubicacion(self, direccion, postal , ciudad, pais, telefono): 
        self.find_element(self.XPATH_INPUT_DIRECCION).clear()
        self.input(direccion, self.XPATH_INPUT_DIRECCION)
        self.find_element(self.XPATH_CODIGO_POSTAL).clear()
        self.input(postal, self.XPATH_CODIGO_POSTAL)
        self.find_element(self.XPATH_INPUT_CIUDAD).clear()
        self.input(ciudad, self.XPATH_INPUT_CIUDAD)
        self.find_element(self.XPATH_INPUT_PAIS).clear()
        self.input(pais, self.XPATH_INPUT_PAIS)
        self.find_element(self.XPATH_INPUT_TELEFONO).clear()
        self.input(telefono, self.XPATH_INPUT_TELEFONO)
        self.click_on_element(self.ID_BTN_MOTIVO)
        self.click_on_element(self.ID_BTN_PASO_SIGUIENTE)
