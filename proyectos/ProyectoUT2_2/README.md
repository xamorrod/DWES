## 🪙 BTC Transactions Tracker

Este proyecto es una aplicación en Python diseñada para rastrear y analizar transacciones de Bitcoin (BTC) utilizando datos de una API JSON pública. Permite obtener información sobre las últimas transacciones, extraer detalles de las carteras involucradas y rastrear una dirección de Bitcoin específica. Además, el proyecto está preparado para ser dockerizado y ejecutado en un contenedor.

# 📋 Descripción del Proyecto

La aplicación descarga datos JSON desde una API para obtener información de las transacciones no confirmadas de Bitcoin y realiza las siguientes funciones:

1. **Importar datos de las últimas transacciones**: Obtiene detalles de las transacciones más recientes, incluyendo la información de las carteras involucradas.
2. **Extracción de información de carteras**: Para cada transacción, extrae datos como saldo, cantidad de transacciones, fecha y hora.
3. **Rastreo de direcciones de Bitcoin**: Permite buscar y obtener información de una dirección de Bitcoin específica.
4. **Almacenamiento y manipulación de datos**: Los datos obtenidos se almacenan en MongoDB 🟢, facilitando la consulta y manipulación.

# 🚀 Características

- **Descarga de Datos**: Obtiene datos JSON desde una API pública para las últimas transacciones de Bitcoin.
- **Procesamiento de Datos**: Los datos son procesados y almacenados en estructuras adecuadas.
- **Manipulación de Datos**: Permite buscar, filtrar y ordenar la información sobre las transacciones y las carteras.
- **Documentación Completa**: Incluye instrucciones sobre la instalación, configuración y uso de la aplicación.
- **Dockerización Opcional 🐳**: La aplicación está lista para ser ejecutada en un contenedor Docker para un despliegue fácil y rápido.

# 🛠 Instalación

1. Clona el repositorio:
   ```bash
# 🐳 Dockerización (Opcional)

# ✅ Requisitos del Proyecto


# Este proyecto cumple con los siguientes requisitos:

1. Descarga de Datos: Obtiene datos de una API en línea.
2. Procesamiento de Datos: Los datos son almacenados y manipulados adecuadamente.
3. Manipulación de Datos: Se pueden realizar búsquedas y consultas sobre los datos.
4. Documentación: Incluye este archivo README.md detallado.
5. Control de Versiones: El proyecto utiliza Git para el control de versiones.
6. Entorno Virtual: Se recomienda usar un entorno virtual para gestionar las dependencias.
7. Opcional: Dockerización 🐳: El proyecto incluye la opción de ser ejecutado en Docker.

