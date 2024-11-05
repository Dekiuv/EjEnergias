import streamlit as st
from modelo_consumo import predecir_consumo
from modelo_tipo import clasificar_energia
from modelo_npersonas import calcular_personas

# Título del formulario
st.title("Formulario de Registro")

# Inicializar session_state para rastrear qué formulario mostrar
if "show_form" not in st.session_state:
    st.session_state.show_form = None

# CSS para fijar el ancho de cada botón
st.markdown("""
    <style>
    .button-container {
        display: flex;
        justify-content: space-around;
    }
    .stButton button {
        width: 200px; /* Ajusta el tamaño según tus necesidades */
        padding: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Crear los botones dentro de un contenedor para aplicar el CSS
st.markdown('<div class="button-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Predecir Consumo"):
        st.session_state.show_form = "form_1"
with col2:
    if st.button("Calcular nºpersonas del habitage"):
        st.session_state.show_form = "form_2"
with col3:
    if st.button("Clasificar por tipo"):
        st.session_state.show_form = "form_3"
st.markdown('</div>', unsafe_allow_html=True)

# Mostrar el formulario según el botón seleccionado y almacenado en session_state
if st.session_state.show_form == "form_1":
    st.header("Predecir Consumo")
    nºperson = st.number_input("Número de personas en la vivienda:", min_value=1, step=1, key="nºperson_Form1")
    energy_price = st.number_input("Precio de la energía:", min_value=0.0, step=0.1, key="energy_price_Form1")
    energy_type = st.selectbox("Tipo de energía:", ["", "Solar", "Eólica", "Hidroeléctrica", "Nuclear", "Carbón", "Gas natural"],key="energy_type_Form1")
    renovable = st.selectbox("Energia renovable:", ["", "Sí", "No"],key="renovable_Form1")
    station = st.selectbox("Estación del año:", ["", "Invierno", "Verano"],key="station_Form1")

    # Botón para enviar los datos
    if st.button("Enviar Formulario Predecir Consumo"):
        if  energy_price <= 0 or energy_type =="" or station == "" or renovable == "":
            st.error("Todos los campos deben ser completados.")
        else:
            renovable = 1 if renovable == "Sí" else 0
            # Aquí puedes añadir el método para procesar los datos ingresados
            consume = predecir_consumo(n_personas=nºperson,precio_energia=energy_price,renovable=renovable,estacion=station,tipo_energia=energy_type)
            st.metric(label="Consumo estimado", value=f"{consume} kWh")


elif st.session_state.show_form == "form_2":
    st.header("Calcular nºpersonas del habitage")
    energy_consume = st.number_input("Consumo de la energía:", min_value=0.0, step=0.1,key="energy_consume_Form2")
    energy_price = st.number_input("Precio de la energía:", min_value=0.0, step=0.1,key="energy_price_Form2")
    energy_type = st.selectbox("Tipo de energía:", ["", "Solar", "Eólica", "Hidroeléctrica", "Nuclear", "Carbón", "Gas natural"],key="energy_type_Form2")
    renovable = st.selectbox("Energia renovable:", ["", "Sí", "No"],key="renovable_Form2")
    station = st.selectbox("Estación del año:", ["", "Invierno", "Verano"],key="station_Form2")

    # Botón para enviar los datos
    if st.button("Enviar Formulario Calcular NºPersonas del Habitage"):
        if energy_consume <= 0 or energy_price <= 0 or  renovable == "" or station == "":
            st.error("Todos los campos deben ser completados.")
        else:
            renovable = 1 if renovable == "Sí" else 0
            nºpersonas = calcular_personas(energy_consume,energy_price,energy_type,renovable,station)
            st.metric(label="Personas estimadas", value=f"{nºpersonas}")
            
            # Aquí puedes añadir el método para procesar los datos ingresados

elif st.session_state.show_form == "form_3":
    st.header("Clasificar por tipo")
    energy_consume = st.number_input("Consumo de la energía:", min_value=0.0, step=0.1,key="energy_consume_Form3")
    energy_price = st.number_input("Precio de la energía:", min_value=0.0, step=0.1,key="energy_price_Form2")
    nºperson = st.number_input("Número de personas en la vivienda:", min_value=1, step=1,key="nºperson_Form3")
    renovable = st.selectbox("Energia renovable:", ["", "Sí", "No"],key="renovable_Form3")
    station = st.selectbox("Estación del año:", ["", "Invierno", "Verano"],key="station_Form2")

    # Botón para enviar los datos
    if st.button("Enviar Formulario Clasificar Por Tipo de Energía"):
        if energy_consume <= 0 or renovable == "":
            st.error("Todos los campos deben ser completados correctamente.")
        else:
            renovable = 1 if renovable == "Sí" else 0
            tipo_clasificacion = clasificar_energia(energy_consume, renovable,nºperson,energy_price,station)
            st.write(f"Tipo de energía clasificada: {tipo_clasificacion}")
