# Sistema de Expertos en Energías
## Descripción

Este proyecto es un **Sistema de Expertos en Energías** diseñado para ayudar a los usuarios a obtener información sobre el consumo energético en función de varios factores. A través de una interfaz amigable, los usuarios pueden buscar datos relacionados con el consumo de energía, y el sistema proporciona recomendaciones basadas en la estación del año.

### Características

- **Interfaz Gráfica**: Utiliza **PySimpleGUI** para crear una experiencia de usuario intuitiva.
- **Carga de Datos desde CSV**: Lee datos de un archivo CSV que contiene información sobre el consumo de energía.
- **Búsqueda por ID**: Permite a los usuarios buscar información específica ingresando un ID.
- **Cálculo de Consumo Ajustado**: Si la estación es "invierno", el sistema ajusta el consumo multiplicándolo por 0.7.
- **Visualización de Resultados**: Muestra información detallada sobre el consumo, la ciudad, el tipo de energía, y más.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación utilizado para desarrollar el sistema.
- **PySimpleGUI**: Biblioteca para crear interfaces gráficas de usuario.
- **CSV**: Formato de archivo para almacenar datos sobre el consumo energético.

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/Dekiuv/EjEnergias
   cd sistema_experto
