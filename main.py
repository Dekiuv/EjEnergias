import PySimpleGUI as sg

# Diseño de la ventana
Usuario = [
    [sg.Text("Introduzca su DNI")],
    [sg.InputText(key='DNI')],
    [sg.Text("Especifique la estación del año que quiera consultar")],
    [sg.Radio('Verano', "RADIO1", key="Verano")],
    [sg.Radio('Invierno', "RADIO1", key="Invierno")],
    [sg.Text("Seleccione cuantas personas viven en la vivienda:")],
    [sg.Slider(range=(0, 10), orientation='h', size=(20, 15), key='Slider1')],
    [sg.Text("Quieres que sea energia renovable?")],
    [sg.Radio('Si', "RADIO1", key="Renovable")],
    [sg.Radio('No', "RADIO1", key="Norenovable")],
    [sg.Text("Selecciona el tipo de energia")],
    [sg.OptionMenu(['Eolica','Solar'],s=(15,2))],
    [sg.Button('Siguiente'), sg.Button('Cancelar')]
]
# Create the Window
window = sg.Window('Ejercicio energias', Usuario)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    else:
        print('Hello', values[0], '!')

window.close()