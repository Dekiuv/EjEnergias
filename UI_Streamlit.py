import streamlit as st

# Título del formulario
st.title("Formulario de Registro")

# Campos del formulario
station = st.selectbox("Estación del año:", ["", "Invierno", "Verano"])
nºperson = st.number_input("Número de personas en la vivienda:", min_value=1, step=1)
energy_Type = st.selectbox("Tipo de energía:", ["", "Solar","Eólica","Hidroeléctrica","Nuclear","Carbón","Gas natural"])

# Botón para enviar los datos
if st.button("Enviar"):
    # Verificar si algún campo está vacío
    if station == "" or energy_Type == "":
        st.error("Todos los campos deben ser completados.")
    else:
            # Mostrar los resultados
            st.success("Formulario enviado exitosamente!")
            st.write("**Estación del año:**", station)
            st.write("**Número de personas en la vivienda:**", nºperson)
            st.write("**Tipo de energía:**", energy_Type)
 