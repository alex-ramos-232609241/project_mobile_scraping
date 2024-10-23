# Feature: Realizar Reserva y Comprobar precios de reserva 

# Scenario: Validar flujo de reserva y precios
#     Given Abro la app y me posiciono en pagina busqueda
#     When Llenando datos para busqueda
#     When introduce destino Cusco y seleccionar
#     When elegir fechas check_in y check_out
#     When seleccionando adultos, niños
#     When seleccionando Habitacion
#     When Capturando monto de reserva
#     When Eligiendo opciones de reserva
#     When Llenando informacion del cliente Jose Hurtado josehurtado@gmail.com
#     When Llenando informacion de datos ubicacion "los jazmines bogota" 1151 bogota colombia 512457856
#     When Capturando valor de precio para comparar
#     Then La prueba de su flujo fue un exito

Feature: Realizar Reserva y Comprobar precios de reserva 

Scenario Outline: Validar flujo de reserva y precios
    Given Voy a realizar una nueva reserva
        """
        Una vez ya logeado me posiciono en la pantalla
        de bienvenido, desde ahi se iniciara el flujo.
        """
    When Llenando datos para busqueda
    When introduce ciudad de destino <ciudad> y seleccionar
    When Paso a elegir fechas de entrada y salida

    When Voy a elegir el numero de habitaciones: <numHabitaciones> y numero adultos: <numAdultos>
    When Eligo numero de niños: <numNinios> y declaro su edad: <edad>
    Then selecciono y ejecuto buscar

    When Voy a elegir el item numero 2
    When Capturo monto de reserva
    Then Paso a elegir mi estancia

    When Voy a llenar la informacion de <nombre> <apellido> <correo>
    When Completo la informacion de la ubicacion <direccion> <postal> <ciudad> <pais> <telefono>
    When Capturando valor de precio para comparar 
    Then Comprobando conformidad de flujo
    Examples:
        | ciudad   |nombre|apellido|correo               |direccion     |postal  |ciudad    |pais           |telefono       |numHabitaciones|numAdultos|numNinios|edad|
        | Tumbes   |Jose  |hurtado |josehurtado@gmail.com|alizos        | 760011 |Cali      | Colombia      |+57 960991395|        1      |     2    |    1    | 5  |
        | Cajamarca|Steve |jobs    |stevejobs@gmail.com  |geranios25    | 05124  | Lima     | Peru          |+51 948752645|        2      |     6    |    2    | 6  |
        
