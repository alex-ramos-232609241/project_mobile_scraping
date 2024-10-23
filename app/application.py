from features.paginas_flujo.pagina_launch import LaunchPage
from features.paginas_flujo.pagina_busqueda import SearchMainPage
from features.paginas_flujo.pagina_seleccion import SelectionPage
from features.paginas_flujo.pagina_info_reserva_1 import InfoReservationPage
from features.paginas_flujo.pagina_estancia import EstanciaPage
from features.paginas_flujo.pagina_datos_reservante import DatosClientePage
from features.paginas_flujo.pagina_info_reserva_2 import InfoReservationPageTwo

class Application:
    def __init__(self, driver):
        self.paginaLanzamientoApp = LaunchPage(driver)
        self.paginaBusquedaPrincipal = SearchMainPage(driver)
        self.paginaDeSeleccion = SelectionPage(driver)
        self.paginaInformacionReservaUno = InfoReservationPage(driver)
        self.paginaDeEstancia = EstanciaPage(driver)
        self.paginaDatosCliente = DatosClientePage(driver)
        self.paginaInformacionReservaDos = InfoReservationPageTwo(driver)
