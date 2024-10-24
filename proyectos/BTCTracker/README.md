# 🪙 BTC Transactions Tracker

Este proyecto es una aplicación en Python diseñada para rastrear y analizar transacciones de Bitcoin (BTC) utilizando datos de una API JSON pública. Permite obtener información sobre las últimas transacciones, extraer detalles de las carteras involucradas y rastrear una dirección de Bitcoin específica. Además, el proyecto está preparado para ser dockerizado y ejecutado en un contenedor.

### 📋 Descripción del Proyecto

La aplicación descarga datos JSON desde una API para obtener información de las transacciones no confirmadas de Bitcoin y realiza las siguientes funciones:

1. **Importar datos de las últimas transacciones**: Obtiene detalles de las transacciones más recientes, incluyendo la información de las carteras involucradas.
2. **Extracción de información de carteras**: Para cada transacción, extrae datos como saldo, cantidad de transacciones, fecha y hora.
3. **Rastreo de direcciones de Bitcoin**: Permite buscar y obtener información de una dirección de Bitcoin específica.
4. **Almacenamiento y manipulación de datos**: Los datos obtenidos se almacenan en MongoDB 🟢, facilitando la consulta y manipulación.

### 🚀 Características

- **Descarga de Datos**: Obtiene datos JSON desde una API pública para las últimas transacciones de Bitcoin.
- **Procesamiento de Datos**: Los datos son procesados y almacenados en estructuras adecuadas.
- **Manipulación de Datos**: Permite buscar, filtrar y ordenar la información sobre las transacciones y las carteras.
- **Documentación Completa**: Incluye instrucciones sobre la instalación, configuración y uso de la aplicación.
- **Dockerización Opcional 🐳**: La aplicación está lista para ser ejecutada en un contenedor Docker para un despliegue fácil y rápido.

### 🛠 Instalación

1. Clona el repositorio:
   ```bash
### 🐳 Dockerización (Opcional)

### ✅ Requisitos del Proyecto

1. **Descarga de Datos**: La aplicación debe ser capaz de descargar datos JSON desde al menos una fuente en línea, como una API web o un archivo JSON remoto.

2. **Procesamiento de Datos**: Los datos JSON descargados deben ser procesados y almacenados en estructuras de datos adecuadas, como listas, diccionarios u objetos personalizados según la naturaleza de los datos.

3. **Manipulación de Datos**: Los usuarios deben poder realizar alguna forma de manipulación de datos, como búsqueda, filtrado, ordenamiento o cálculos sobre los datos descargados.

4. **Interfaz de Usuario (Opcional)**: Como apartado opcional, se propone crear una interfaz de usuario simple para interactuar con la aplicación. Esto podría ser una interfaz de línea de comandos o una GUI básica.

5. **Documentación**: Debéis proporcionar documentación clara y concisa que explique cómo funciona su aplicación, cómo se ejecuta y cómo se pueden utilizar sus características. Si la aplicación tiene dependencias para funcionar, debes explicar claramente cómo se instalan.

6. **Control de Versiones y entorno virtual**: Se debe utilizar un sistema de control de versiones, como Git, para realizar un seguimiento de las actualizaciones del código y colaborar en el desarrollo si se trabaja en grupo. Además, deberá estar ubicado en un entorno virtual.

7. **Entorno en container (Opcional)**: En este apartado opcional te propongo la creación de un contenedor con Docker en el que esté todo configurado y listo para funcionar.

8. **Presentación**: Al final del proyecto, el alumnado debe presentar su aplicación y su funcionamiento ante el grupo y el profesor, destacando las características implementadas y los problemas superados. Además, deberá crear un vídeo de menos de 2 minutos con los highlights de la app.

