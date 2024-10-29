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
        # Validar el patrón del DNI (8 dígitos y 1 letra)
        if len(dni) == 9 and dni[:8].isdigit() and dni[-1].isalpha():
            # Mostrar los resultados
            st.success("Formulario enviado exitosamente!")
            st.write("**DNI Cliente:**", dni)
            st.write("**Estación del año:**", estacion)
            st.write("**Número de personas en la vivienda:**", numero_personas)
            st.write("**Tipo de energía:**", tipo_energia)
        else:
            st.error("El DNI debe tener 8 dígitos seguidos de 1 carácter (ej. 12345678A).")
