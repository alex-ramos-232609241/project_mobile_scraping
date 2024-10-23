'''
    LA ESTRUCTURA DE DATOS DE FORMA MODULAR
    **Permitira crear flujos por layout, asi el analisis y 
    la identificacion de posibles fallas en el flujo, tendra 
    una mejor gestion.
'''
LAYOUT_BUSQUEDA = {
            "ID_BOTON_CONTINUE_BUSQUEDA": "com.alquiler:id/genius_onbaording_bottomsheet_cta",
            "ID_INPUT_BUSQUEDA_CIUDAD": "com.alquiler:id/facet_search_box_accommodation_destination",
            "ID_INPUT_CIUDAD":"com.alquiler:id/facet_with_bui_free_search_alquiler_header_toolbar_content",
            "XPATH_SELECCION_ITEM": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]",
            "XPATH_FECHA_IN": "//android.view.View[@content-desc='22 julio 2023']",
            "XPATH_FECHA_FIN": "//android.view.View[@content-desc='28 julio 2023']",
            "ID_BTN_CONFIRMACION": "com.alquiler:id/facet_date_picker_confirm",
            "ID_INPUT_HAB_ADUL_NI": "com.alquiler:id/facet_search_box_accommodation_occupancy",
            "XPATH_ADD_NINIO": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[3]/android.widget.LinearLayout/android.widget.Button[2]",
            "XPATH_CLICK_6_VECES":"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.NumberPicker/android.widget.Button[2]",
            
            "XPATH_NUMERO_HABITACIONES":"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.LinearLayout/android.widget.TextView",
            "XPATH_DIS_NUMHABITACIONES": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.LinearLayout/android.widget.Button[1]",
            "XPATH_ADD_NUMHABITACIONES": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.LinearLayout/android.widget.Button[2]",   
            "XPATH_NUMERO_ADULTOS": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.LinearLayout/android.widget.TextView",
            "XPATH_DIS_NUMADULTOS": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.LinearLayout/android.widget.Button[1]",
            "XPATH_ADD_NUMADULTOS": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.LinearLayout/android.widget.Button[2]",

            "ID_BTN_OK": "android:id/button1",
            "ID_BTN_APLICAR": "com.alquiler:id/group_config_apply_button",
            "ID_BTN_BUSCAR": "com.alquiler:id/facet_search_box_cta",
    }
LAYOUT_SELECCION = {
        "XPATH_SEGUNDO_ITEM": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]",
    }
LAYOUT_INFO_RESERVA_1 = {
        "ID_PRECIO_RESERVA": "com.alquiler:id/price_view_price",
        "ID_BTN_ELEGIR_HABITACION": "com.alquiler:id/select_room_cta",
    }
LAYOUT_ESTANCIA = {
        "ID_ELEGIR_ESTAS_OPCIONES": "com.alquiler:id/recommended_block_reserve_button",
        "XPATH_RESERVAR_AHORA" : "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout",
        "XPATH_SELECIONAR": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout",
        "ID_BTN_SELECCIONAR": "com.alquiler:id/room_select_button_layout_container",
    }
LAYOUT_DATOS_RESERVANTE = {
         "XPATH_INPUT_NOMBRE": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/javaClass[1]/android.widget.EditText",
         "XPATH_INPUT_APELLIDO": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/javaClass[2]/android.widget.EditText",
         "XPATH_INPUT_EMAIL": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/javaClass[3]/android.widget.EditText",
         "XPATH_INPUT_DIRECCION": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/javaClass[1]/android.widget.EditText",
         "XPATH_CODIGO_POSTAL": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/javaClass[2]/android.widget.EditText",
         "XPATH_INPUT_CIUDAD": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/javaClass[3]/android.widget.EditText",
         "XPATH_INPUT_PAIS": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/javaClass[1]/android.widget.EditText",
         "XPATH_INPUT_TELEFONO": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/javaClass[2]/android.widget.EditText",
         "ID_BTN_MOTIVO": "com.alquiler:id/business_purpose_leisure",
         "ID_BTN_PASO_SIGUIENTE": "com.alquiler:id/action_button"
    }
LAYOUT_INFO_RESERVA_2 = {
        "ID_PRECIO_COMPARAR": "com.alquiler:id/bp_price_summary_total_price_value",
        "XPATH_PRECIO_NAVBAR": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView",
        "ID_BTN_ULTIMO_PASO": "com.alquiler:id/action_button"
    }
LAYOUT_DATOS_BANCARIOS = {
         "ID_INPUT_NUMERO_TARJETA": "com.alquiler:id/new_credit_card_number_edit",
         "ID_NOMBRE_PROPIETARIO": "com.alquiler:id/new_credit_card_holder_edit",
         "ID_FECHA_CADUCIDAD": "com.alquiler:id/new_credit_card_expiry_date_edit",
    }
