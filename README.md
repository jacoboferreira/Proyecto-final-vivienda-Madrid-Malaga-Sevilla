
# **Situación actual de la vivienda en las ciudades de Madrid, Málaga y Sevilla.**
Situación actual de la vivienda en las ciudades Madrid, Málaga y Sevilla.

## **1. Resumen o descripción**
 Los datos han sido obtenidos de Idealista mediante tres formas diferentes.

Después de mudarme en febrero me dio que pensar después de observar la diferencia de precios en la vivienda. Donde queda la clase media y tener una buena vida a la que hace referencia siempre la clase política que nos gobierna. 

Por ello he realizado un análisis de rentabilidad a la hora de comprar y alquilar una casa, he realizado un análisis a la hora de comprar una vivienda, he realizado un análisis predictivo de la evolución del precio de la vivienda. 

Para observar de verdad si existe la clase media, como se ha visto afectada la evolución del precio de la vivienda y el de los salarios.

El proyecto consta de 3 bloques. He querido hacer un tipo de Análisis o uso de herramienta para cada bloque, expongo delante un resumen de los bloques:
•	Bloque 1:
	o	Herramienta: Excel.
	o	Ciudad: Málaga.
	o	Informe: Precios, Unidades, Rentabilidad.
	o	Obtención de datos: Aplicación Listly.io
•	Bloque 2:
	o	Herramienta: Power BI.
	o	Ciudad: Sevilla.
	o	Informe: Precios, Unidades.
	o	Obtención de datos: API idealista.
•	Bloque 3: 
	o	Herramienta: Python.
	o	Ciudad: Madrid.
	o	Informe: Machine learning, Predicción a future y rentabilidad.
	o	Obtención de datos: WEB Scraping idealista.
Mediante este proceso he querido desarrollar y experimentar mis conocimientos aprendidos con el programa de The Power MBA, Udemy y videos de YouTube. Para algunos de los procesos, me he apoyado de la herramienta Chat GPT.

## **2. Estructura del repositorio**
- 📂 **Bloque 1: ** Proyecto creado con Excel, datos de Málaga, obtenido los datos con IO.
	- 📂 **Alquiler: ** La carpeta contiene los archivos descargados en sucio de los precios de alquiler Benalmádena, Centro, Estepona, Fuengirola, Marbella y Torremolinos. Están en formato Excel, contienen de 30 a 5 anunció de pisos. Además, tiene un documento de Python que me ayudo a limpiar y ordenar los documentos.
	- 📂 **Compra: ** La carpeta contiene los archivos descargados en sucio de  los precios de compra Benalmádena, Centro, Estepona, Fuengirola, Marbella y Torremolinos. Están en formato Excel, contienen de 30 a 5 anunció de pisos. Además, tiene un documento de Python que me ayudo a limpiar y ordenar los documentos.
	- 📂 **Evolutivo 1: ** La carpeta contiene los archivos descargados en sucio del evolutivo del precio/ metro cuadrado de Málaga, Benalmádena, Centro, Estepona, Fuengirola, Marbella y Torremolinos. Están en formato Excel, Además, tiene un documento de Python que me ayudo a limpiar y ordenar los documentos. Dentro de la carpeta hay otra en la que se hacen la predicciones de LSTM y se guarda por distrito los datos con la predicción a 2036.
	- 📊 **Análisis Malaga:** Excel donde se realiza el proyecto.

- 📂 **Bloque 2: ** Proyecto creado con Power Bi, datos de Sevilla, obteniendo los datos con Python mediante la API de idealista.
	- 📂 **Alquiler: ** La carpeta contiene el archivo obtenido con los datos de alquiler de Sevilla, además del archivo donde se ejecuta el código de Python.
	- 📂 **Compra: ** La carpeta contiene el archivo obtenido con los datos de compra de Sevilla, además del archivo donde se ejecuta el código de Python.
	- 📂 **Fondos BI: ** Carpeta con los fondos disponibles para usar en Power BI.
	- 📄 **oauth2-documentation: ** Documento explicativo para conectarse a la API.
	- 📄 **property-search-api-v3_5: ** Documento con las especificaciones de los datos que se pueden descargar y los filtros a usar.
	- 📊 **power_bi_sevilla: ** Power Bi donde se realiza el proyecto.


- 📂 **Bloque 3: ** Proyecto creado con Python, datos de Madrid, obteniendo los datos con Python mediante la WEB scraping de idealista.
	- 📂 **Alquiler: ** Contiene los archivos obtenidos con los datos de alquiler de Madrid, además del archivo donde se ejecuta el código de Python.
	- 📂 **Compra: ** Contiene los archivos obtenidos con los datos de compra de Madrid, además del archivo donde se ejecuta el código de Python.
	- 📂 **Datos Extra: ** Contiene archivos con información extra para llevar acabo los análisis.
	- 📄 **ANALISIS_RENTABILIDAD: ** Archivo donde se lleva a cabo un análisis de rentabilidad de las viviendas de Madrid.
	- 📄 **CODIGO_PROYECTO_ALQUILER: ** Archivo donde se lleva a cabo la limpieza y preprocesado de datos de alquiler.
	- 📄 **CODIGO_PROYECTO_COMPRA_EDA: ** Archivo donde se lleva a cabo la limpieza, preprocesado de datos de alquiler. También se hace un modelo de Machine Learning.
	- 📄 **Datos_alquiler: ** Archivo con los datos definitivos de alquiler para utilizar en el análisis de rentabilidad.
	- 📄 **Datos_compra: ** Archivo con los datos definitivos de compra para utilizar en el análisis de rentabilidad.
	- 📄 **predicciones_hasta_2030: ** Archivo con los datos extraidos del análisis predictivo LSTM de los precios de medios del €/M2 hasta la fecha de 2030.
	- 📄 **predicciones_madrid: ** Archivo con los datos extraidos del análisis predictivo LSTM de los precios de medios del €/M2 hasta la fecha de 2024.
	- 📄 **PROYECTO_EVOLUTIVO-PRECIO: ** Archivo con el código para el análisis predictivo de LSTM del precio a futuro.


## **3. Instalaciones y requisitos**

Para ejecutar este proyecto, es necesario contar con las siguientes herramientas:

- Microsoft Excel
- Power Query
- Python
	- Padas: Manejo y análisis de datos en tablas.
	- Numpy: Cálculos numéricos y matrices.
	- request: Peticiones HTTP a páginas o APIs.
	- bs4: Extracción de datos de HTML/XML (web scraping).
	- time: Control del tiempo y pausas.
	- random: Generación de números aleatorios.
	- selenium: Automatización de navegadores web.
	- undetected_chromedriver: Selenium sin bloqueos anti-bot.
	- math: Funciones matemáticas.
	- os: Manejo de archivos y sistema operativo.
	- glob: Búsqueda de archivos por patrones.
	- lxml: Procesamiento rápido de HTML/XML.
	- matplotlib: Visualización de datos en gráficos.
	- sklearn - MinMaxScaler: Normaliza valores numéricos a un rango (ej. 0 a 1).
	- tensorflow - Sequential: Modelo secuencial de capas en red neuronal.
	- tensorflow - LSTM: Capa de memoria a largo plazo para series temporales.
	- tensorflow - Dense: Capa totalmente conectada en redes neuronales.
	- base64: Codificación y decodificación de datos en Base64.
	- json: Lectura y escritura de datos en formato JSON.
	- literal_eval: Evalúa cadenas como estructuras de datos seguras (listas, diccionarios, etc.).
	- seaborn: Visualización estadística con gráficos atractivos.
	- re: Expresiones regulares para búsqueda y manipulación de texto.
	- LabelEncoder: Convierte etiquetas categóricas a valores numéricos.
	- SimpleImputer: Rellena valores faltantes en los datos.
	- mean_squared_error: Métrica de error cuadrático medio en modelos.
	- r2_score: Métrica de precisión de modelos de regresión.
	- train_test_split: Divide datos en entrenamiento y prueba.
	- StandardScaler: Estandariza datos (media 0, varianza 1).
	- LinearRegression: Modelo de regresión lineal.
	- RandomForestRegressor: Modelo de regresión basado en bosques aleatorios.
	- GradientBoostingRegressor: Modelo de regresión basado en boosting de gradiente.
	- subprocess: Ejecuta comandos del sistema desde Python.
- Idealista
- Listly.io

## **4. Explicación de los datos**
Para comprender y llevar a cabo el análisis, es importante tener conocimiento del sector inmobiliario (*real estate*). 
Como he mencionado anteriormente el proyecto consta de 3 bloques. En su mayoría los datos son los mismos. Dentro de cada bloque del proyecto se dividen en otros tres apartados**compra, alquiler y evolutivo**. En el caso del ultimo también se han obtenido datos de páginas web oficiales del estado. 
Hay que tener claro que los datos cuando se usan en herramientas como Python, a la hora que va avanzando el proyecto se pueden ir cambiando el numero de columnas y el nombre. 
Por eso voy a exponer las principales columnas que tienen los archivos:
	- **Archivos de alquiler y compra:**
	- **Título:** Nombre del anuncio.
	- **Ciudad:** Ciudad en la que se encuentra la vivienda.
	- **Coste:** Precio en euros.
	- **Habitaciones:** Número de habitaciones.
	- **Metros cuadrados:** Superficie total del inmueble.
	- **Planta:** Altura en la que esta el piso
	- **Vivienda:** Tipo de inmueble (piso o casa).
	- **EXT – INT:** Si la vivienda da al exterior o interior.
	- **Área:** Área de la ciudad donde se encuentra el inmueble.
	- **Baños:** Numero de baños tiene el inmueble.
	- **Coste/Metro:** Precio del metro cuadrado.

Además, existen otras columnas como: **R-Coste, Ascensor, Garaje, columnas calculadas, negocio, ID del anuncio**.

- **Archivos evolutivos:**
	- **Fecha:** Fecha en meses a la que hace referencia.
	- **Coste:** Coste del metro cuadrado a la fecha.
	- **Área:** Área de la ciudad donde se encuentra el inmueble.
	- **Negocio:** Si valor pertenece a compra o alquiler.

En el caso del bloque 3 del proyecto se va a explicar también los datos:
	- **Fecha:** Fecha en años a la que hace referencia.
	- **Coste:** Coste del metro cuadrado a la fecha de la Comunidad de Madrid.
	- **SM Madrid**: Evolución del salario bruto.
	- **SB anual:** Salario bruto anual de España.
	- **Poblacion Madrid:** numero de residentes en la comunidad de Madrid.
	- **Nº DE LICENCIA CONSTRUCCION:** Numero de licencias concedidas en España.
	- **Nº DE EDIFICIOS:** Numero de edificios construidos en España.
	- **Nº DE VIVIENDAS:** Numero de viviendas construidas en España.

