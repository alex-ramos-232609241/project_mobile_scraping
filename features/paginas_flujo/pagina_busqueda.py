from msilib.schema import Error
from selenium.webdriver.common.by import By
from features.flujos.flujo_reserva import LAYOUT_BUSQUEDA
from features.paginas_flujo.pagina_base import Page

class SearchMainPage(Page):
    
    ID_INPUT_BUSQUEDA_CIUDAD = (By.ID, LAYOUT_BUSQUEDA["ID_INPUT_BUSQUEDA_CIUDAD"])
    ID_INPUT_CIUDAD = (By.ID, LAYOUT_BUSQUEDA["ID_INPUT_CIUDAD"])
    XPATH_SELECCION_ITEM = (By.XPATH, LAYOUT_BUSQUEDA["XPATH_SELECCION_ITEM"])
    XPATH_FECHA_IN = (By.XPATH, LAYOUT_BUSQUEDA["XPATH_FECHA_IN"])
    XPATH_FECHA_FIN = (By.XPATH, LAYOUT_BUSQUEDA["XPATH_FECHA_FIN"])
    ID_BTN_CONFIRMACION = (By.ID, LAYOUT_BUSQUEDA["ID_BTN_CONFIRMACION"])
    ID_INPUT_HAB_ADUL_NI = (By.ID, LAYOUT_BUSQUEDA["ID_INPUT_HAB_ADUL_NI"])
    XPATH_ADD_NINIO = (By.XPATH, LAYOUT_BUSQUEDA["XPATH_ADD_NINIO"])
    XPATH_CLICK_6_VECES = (By.XPATH, LAYOUT_BUSQUEDA["XPATH_CLICK_6_VECES"])
 
    XPATH_NUMERO_HABITACIONES = (By.XPATH, LAYOUT_BUSQUEDA["XPATH_NUMERO_HABITACIONES"])
    XPATH_DIS_NUMHABITACIONES = (By.XPATH, LAYOUT_BUSQUEDA["XPATH_DIS_NUMHABITACIONES"])
    XPATH_ADD_NUMHABITACIONES = (By.XPATH, LAYOUT_BUSQUEDA["XPATH_ADD_NUMHABITACIONES"])
    XPATH_NUMERO_ADULTOS = (By.XPATH, LAYOUT_BUSQUEDA["XPATH_NUMERO_ADULTOS"])
    XPATH_DIS_NUMADULTOS = (By.XPATH, LAYOUT_BUSQUEDA["XPATH_DIS_NUMADULTOS"])
    XPATH_ADD_NUMADULTOS = (By.XPATH, LAYOUT_BUSQUEDA["XPATH_ADD_NUMADULTOS"])
    
    ID_BTN_OK = (By.ID, LAYOUT_BUSQUEDA["ID_BTN_OK"])
    ID_BTN_APLICAR = (By.ID, LAYOUT_BUSQUEDA["ID_BTN_APLICAR"])
    ID_BTN_BUSCAR = (By.ID, LAYOUT_BUSQUEDA["ID_BTN_BUSCAR"])
    
    def click_input_busqueda(self):
        self.click_on_element(self.ID_INPUT_BUSQUEDA_CIUDAD)
        
    def add_data_in_frame(self, value):
        self.hide_keyboard()
        self.input(value, self.ID_INPUT_CIUDAD)
        self.click_on_element(self.XPATH_SELECCION_ITEM)
        

    def check_fechas(self):
        self.click_on_element(self.XPATH_FECHA_IN)    
        self.click_on_element(self.XPATH_FECHA_FIN)    
        self.click_on_element(self.ID_BTN_CONFIRMACION) 

    def select_habitaciones_adultos(self, nHabitaciones, nAdultos):
        self.click_on_element(self.ID_INPUT_HAB_ADUL_NI)
        #restamos en numero de habitaciones pedidas menos la que ha existe 
        #guardado asi sabremos el numero de click a dar
        habDentrodelText = int(self.find_element(self.XPATH_NUMERO_HABITACIONES).text)
        dif_habitaciones = int(nHabitaciones) - habDentrodelText
        
        for i in range(abs(dif_habitaciones)):
            if dif_habitaciones < 0:
                self.click_on_element(self.XPATH_DIS_NUMHABITACIONES)
            elif dif_habitaciones > 0:
                self.click_on_element(self.XPATH_ADD_NUMHABITACIONES)
            else:
                pass
            i = i + 1

        adultosDentrodelText = int(self.find_element(self.XPATH_NUMERO_ADULTOS).text)
        dif_adultos = int(nAdultos) - adultosDentrodelText
        for j in range(abs(dif_adultos)):
            if dif_adultos < 0:
                self.click_on_element(self.XPATH_DIS_NUMADULTOS)
            elif dif_adultos > 0:
                self.click_on_element(self.XPATH_ADD_NUMADULTOS)
            else:
                pass     
            j = j + 1

           

    def select_ninios_edad(self, nNinios, edad):
            # pongo a cero el input text de ninios
            val_edad = int(edad) + 1 #la edad de los niños comienza menos de 1 año
            for i in range(int(nNinios)):
                self.click_on_element(self.XPATH_ADD_NINIO)
                for j in range(val_edad):
                    self.click_on_element(self.XPATH_CLICK_6_VECES)
                    j = j + 1
                i = i + 1 
                self.click_on_element(self.ID_BTN_OK)     
            self.click_on_element(self.ID_BTN_APLICAR)

    def select_ejecutando_buscar(self):            
        self.click_on_element(self.ID_BTN_BUSCAR)
        