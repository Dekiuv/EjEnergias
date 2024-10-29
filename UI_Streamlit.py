import streamlit as st

# Título del formulario
st.title("Formulario de Registro")

# Campos del formulario
dni = st.text_input("DNI Cliente:")
estacion = st.selectbox("Estación del año:", ["", "Invierno", "Verano"])
numero_personas = st.number_input("Número de personas en la vivienda:", min_value=1, step=1)
tipo_energia = st.selectbox("Tipo de energía:", ["", "Solar","Eólica","Hidroeléctrica","Nuclear","Carbón","Gas natural"])

# Botón para enviar los datos
if st.button("Enviar"):
    # Verificar si algún campo está vacío
    if not dni or estacion == "" or tipo_energia == "":
        st.error("Todos los campos deben ser completados.")
    else:
        # Mostrar los resultados
        st.success("Formulario enviado exitosamente!")
        st.write("**DNI Cliente:**", dni)
        st.write("**Estación del año:**", estacion)
        st.write("**Número de personas en la vivienda:**", numero_personas)
        st.write("**Tipo de energía:**", tipo_energia)
