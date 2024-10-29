import streamlit as st

# Título del formulario
st.title("Formulario de Registro")

col1, col2, col3 = st.columns(3)

with col1:
    show_form_1 = st.button("Predecir Consumo")
with col2:
    show_form_2 = st.button("Calcular nºpersonas del habitage")
with col3:
    show_form_3 = st.button("Clasificar por tipo")
    
if show_form_1:
    st.header("Predecir Consumo")
    nºperson = st.number_input("Número de personas en la vivienda:", min_value=1, step=1)
    energy_price = st.number_input("Precio de la energía:", min_value=0.0, step=0.1) 
    renovable = st.selectbox("Energia renovable:", ["", "Sí", "No"])
    station = st.selectbox("Estación del año:", ["", "Invierno", "Verano"])
    
    # Botón para enviar los datos
    if st.button("Enviar Formulario 1"):
        if not nºperson or not energy_price or station == "" or renovable == "":
            st.error("Todos los campos deben ser completados.")
        else:
            st.success("Formulario 1 enviado exitosamente!")

elif show_form_2:
    st.header("Calcular nºpersonas del habitage")
    energy_consume = st.number_input("Consumo de la energía:", min_value=0.0, step=0.1) 
    energy_price = st.number_input("Precio de la energía:", min_value=0.0, step=0.1) 
    energy_type = st.selectbox("Tipo de energía:", ["", "Solar","Eólica","Hidroeléctrica","Nuclear","Carbón","Gas natural"])
    renovable = st.selectbox("Energia renovable:", ["", "Sí", "No"])
    station = st.selectbox("Estación del año:", ["", "Invierno", "Verano"])
    # Botón para enviar los datos
    if st.button("Enviar Formulario 2"):
        if not energy_consume or pais == "":
            st.error("Todos los campos deben ser completados.")
        else:
            st.success("Formulario 2 enviado exitosamente!")
            st.write("**Nombre Completo:**", nombre)
            st.write("**Edad:**", edad)
            st.write("**País de residencia:**", pais)

elif show_form_3:
    st.header("Formulario 3")
    producto = st.text_input("Producto:")
    cantidad = st.number_input("Cantidad:", min_value=1, step=1)
    precio = st.number_input("Precio por unidad:", min_value=0.0, step=0.01)
    
    # Botón para enviar los datos
    if st.button("Enviar Formulario 3"):
        if not producto or precio <= 0:
            st.error("Todos los campos deben ser completados correctamente.")
        else:
            st.success("Formulario 3 enviado exitosamente!")
            st.write("**Producto:**", producto)
            st.write("**Cantidad:**", cantidad)
            st.write("**Precio por unidad:**", precio)
            st.write("**Total:**", cantidad * precio)


# # Campos del formulario
# station = st.selectbox("Estación del año:", ["", "Invierno", "Verano"])
# nºperson = st.number_input("Número de personas en la vivienda:", min_value=1, step=1)
# energy_Type = st.selectbox("Tipo de energía:", ["", "Solar","Eólica","Hidroeléctrica","Nuclear","Carbón","Gas natural"])

# # Botón para enviar los datos
# if st.button("Enviar"):
#     # Verificar si algún campo está vacío
#     if station == "" or energy_Type == "":
#         st.error("Todos los campos deben ser completados.")
#     else:
#             # Mostrar los resultados
#             st.success("Formulario enviado exitosamente!")
#             st.write("**Estación del año:**", station)
#             st.write("**Número de personas en la vivienda:**", nºperson)
#             st.write("**Tipo de energía:**", energy_Type)
 