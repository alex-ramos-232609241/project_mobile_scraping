from behave import given, when, then


@given("Voy a realizar una nueva reserva")
def step_imp(context):
    context.app.paginaLanzamientoApp.continue_search()

@when("Llenando datos para busqueda")
def step_imp(context):
    context.app.paginaBusquedaPrincipal.click_input_busqueda()

@when("introduce ciudad de destino {ciudad} y seleccionar")
def step_imp(context, ciudad):
    context.app.paginaBusquedaPrincipal.add_data_in_frame(ciudad)

@when("Paso a elegir fechas de entrada y salida")
def step_imp(context):
    context.app.paginaBusquedaPrincipal.check_fechas()



@when("Voy a elegir el numero de habitaciones: {numHabitaciones} y numero adultos: {numAdultos}")
def step_imp(context, numHabitaciones, numAdultos):
    context.app.paginaBusquedaPrincipal.select_habitaciones_adultos(numHabitaciones, numAdultos)

@when("Eligo numero de niños: {numNinios} y declaro su edad: {edad}")
def step_imp(context, numNinios, edad):
    context.app.paginaBusquedaPrincipal.select_ninios_edad(numNinios, edad)

@then("selecciono y ejecuto buscar")
def step_imp(context):
    context.app.paginaBusquedaPrincipal.select_ejecutando_buscar()


@when("Voy a elegir el item numero 2")
def step_imp(context):
    context.app.paginaDeSeleccion.click_seleccion_busqueda()

@when("Capturo monto de reserva")
def step_imp(context):
    context.app.paginaInformacionReservaUno.get_price_reservation()

@then("Paso a elegir mi estancia")
def step_imp(context):
    context.app.paginaDeEstancia.eligiendo_opciones()    


@when("Voy a llenar la informacion de {nombre} {apellido} {correo}")
def step_imp(context, nombre, apellido, correo):
    context.app.paginaDatosCliente.add_data_reservante(nombre, apellido, correo)

@when('Completo la informacion de la ubicacion {direccion} {postal} {ciudad} {pais} {telefono}')
def step_imp(context, direccion, postal, ciudad, pais, telefono):
    context.app.paginaDatosCliente.add_data_reservante_ubicacion(direccion, postal, ciudad, pais, telefono)

@when("Capturando valor de precio para comparar")
def step_imp(context):
    context.app.paginaInformacionReservaDos.get_price_reservation_two()

@then("Comprobando conformidad de flujo")
def step_imp(context):
    context.app.paginaInformacionReservaDos.funcion_de_cierre()
