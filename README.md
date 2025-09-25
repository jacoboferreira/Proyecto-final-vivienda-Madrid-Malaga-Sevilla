
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
- 📂 **Bloque 1:** Proyecto creado con Excel, datos de Málaga, obtenido los datos con IO.
	- 📂 **Alquiler:** La carpeta contiene los archivos descargados en sucio de los precios de alquiler Benalmádena, Centro, Estepona, Fuengirola, Marbella y Torremolinos. Están en formato Excel, contienen de 30 a 5 anunció de pisos. Además, tiene un documento de Python que me ayudo a limpiar y ordenar los documentos.
   
	- 📂 **Compra:** La carpeta contiene los archivos descargados en sucio de  los precios de compra Benalmádena, Centro, Estepona, Fuengirola, Marbella y Torremolinos. Están en formato Excel, contienen de 30 a 5 anunció de pisos. Además, tiene un documento de Python que me ayudo a limpiar y ordenar los documentos.
   
	- 📂 **Evolutivo 1:** La carpeta contiene los archivos descargados en sucio del evolutivo del precio/ metro cuadrado de Málaga, Benalmádena, Centro, Estepona, Fuengirola, Marbella y Torremolinos. Están en formato Excel, Además, tiene un documento de Python que me ayudo a limpiar y ordenar los documentos. Dentro de la carpeta hay otra en la que se hacen la predicciones de LSTM y se guarda por distrito los datos con la predicción a 2036.
   
	- 📊 **Análisis Malaga:** Excel donde se realiza el proyecto.

- 📂 **Bloque 2:** Proyecto creado con Power Bi, datos de Sevilla, obteniendo los datos con Python mediante la API de idealista.
	- 📂 **Alquiler:** La carpeta contiene el archivo obtenido con los datos de alquiler de Sevilla, además del archivo donde se ejecuta el código de Python.
	- 📂 **Compra:** La carpeta contiene el archivo obtenido con los datos de compra de Sevilla, además del archivo donde se ejecuta el código de Python.
	- 📂 **Fondos BI:** Carpeta con los fondos disponibles para usar en Power BI.
	- 📄 **oauth2-documentation:** Documento explicativo para conectarse a la API.
	- 📄 **property-search-api-v3_5:** Documento con las especificaciones de los datos que se pueden descargar y los filtros a usar.
	- 📊 **power_bi_sevilla:** Power Bi donde se realiza el proyecto.


- 📂 **Bloque 3:** Proyecto creado con Python, datos de Madrid, obteniendo los datos con Python mediante la WEB scraping de idealista.
	- 📂 **Alquiler:** Contiene los archivos obtenidos con los datos de alquiler de Madrid, además del archivo donde se ejecuta el código de Python.
	- 📂 **Compra:** Contiene los archivos obtenidos con los datos de compra de Madrid, además del archivo donde se ejecuta el código de Python.
	- 📂 **Datos Extra:** Contiene archivos con información extra para llevar acabo los análisis.
	- 📄 **ANALISIS_RENTABILIDAD:** Archivo donde se lleva a cabo un análisis de rentabilidad de las viviendas de Madrid.
	- 📄 **CODIGO_PROYECTO_ALQUILER:** Archivo donde se lleva a cabo la limpieza y preprocesado de datos de alquiler.
	- 📄 **CODIGO_PROYECTO_COMPRA_EDA:** Archivo donde se lleva a cabo la limpieza, preprocesado de datos de alquiler. También se hace un modelo de Machine Learning.
	- 📄 **Datos_alquiler:** Archivo con los datos definitivos de alquiler para utilizar en el análisis de rentabilidad.
	- 📄 **Datos_compra:** Archivo con los datos definitivos de compra para utilizar en el análisis de rentabilidad.
	- 📄 **predicciones_hasta_2030:** Archivo con los datos extraidos del análisis predictivo LSTM de los precios de medios del €/M2 hasta la fecha de 2030.
	- 📄 **predicciones_madrid:** Archivo con los datos extraidos del análisis predictivo LSTM de los precios de medios del €/M2 hasta la fecha de 2024.
	- 📄 **PROYECTO_EVOLUTIVO-PRECIO:** Archivo con el código para el análisis predictivo de LSTM del precio a futuro.


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

	- Archivos de alquiler y compra.
	
	- Título: Nombre del anuncio.
	
	- Ciudad: Ciudad en la que se encuentra la vivienda.
	
	- Coste: Precio en euros.
	
	- Habitaciones: Número de habitaciones.

	- Metros cuadrados: Superficie total del inmueble.
	
	- Planta: Altura en la que esta el piso.
	
	- Vivienda: Tipo de inmueble (piso o casa).
	
	- EXT – INT: Si la vivienda da al exterior o interior.
	
	- Área: Área de la ciudad donde se encuentra el inmueble.
	
	- Baños: Numero de baños tiene el inmueble.
	
	- Coste/Metro: Precio del metro cuadrado.

Además, existen otras columnas como: **R-Coste, Ascensor, Garaje, columnas calculadas, negocio, ID del anuncio**.

- Archivos evolutivos:
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

## **5. Proceso llevado a cabo**
Voy a explicar el proceso por partes, ya que a cada parte lo he querido crear con la intención de aprender, usar diferentes herramientas y metodología de obtener los datos.
- ### **5.1. Bloque 1**
Este primer bloque es una continuación y mejora del primer proyecto de análisis compra y alquiler. He mejorado el numero de viviendas, la obtención de información nueva como la ciudad y área, baños, etc. Expongo a continuación el proceso llevado.

**5.1.1 Descarga de datos**
Se utilizo la aplicación utilizada anteriormente pero con una suscripción mejor, la cual me permitía descargar de forma ilimitada la información. Seguía tenia las limitaciones de solo poder obtener la información de las portadas de los anuncios de idealista, a esto se le suma que en cada pagina solo tiene un máximo de 30 anuncios.
El problema que tiene esta metodología es que tienes que repetir mucho el proceso y la información no se descarga ordenadamente. Cuando abres el archivo podías encontrar diferentes ordenes. Además, para poder obtener los baños antes de descargar la información tenia que filtrar en idealista. Cuando tenía descargada la información de un área, seleccionaba todos los documentos y con el comando de f2 le daba el nombre que quería y se ponían en todos con la diferencia de un numero entre paréntesis a si luego podía utilizarlo luego para poner el nombre del área en la columna.
En el bloque puedes encontrar las 3 carpetas de alquiler, compra y evolutivo. De alquiler tengo 111 Excel con información. De compra 426 y de evolutivo 17.

**5.1.2 Limpieza de los datos**
Primero, se analizó qué datos se descargaban, su formato y su relevancia. Luego, se estructuraron y dividieron para el análisis.

Inicialmente, la información no seguía un patrón uniforme, por lo que se tuvo que ordenar manualmente eliminando, añadiendo o cambiando el orden de las columnas.

Una vez organizado, los datos se procesaron con Power Query en Excel para realizar la limpieza: 
- Extracción de información según delimitadores.
- División de columnas.
- Inserción de nuevas columnas.
- Reemplazo de valores.

Para los documentos de compras, se utilizó un código en Python para estructurar la información en columnas, quedando con la misma estructura que los documentos de alquiler.

**5.1.3 Unión de la información**
Los datos obtenidos estaban divididos por ciudades y en cada documento había 32 filas. Mediante código de Python su puedo automatizar el proceso de unión, cogiendo todos lo documentos de la carpeta y uniéndolos, además como he mencionado antes añadió una columna con el nombre del archivo a cada fila. Este proceso se hizo con las tres partes. 
El último documento creado para este análisis fue el **"Análisis Malaga"**, consta de 11 hojas:

1. **Tabla de alquiler: ** Información consolidada de los pisos en alquiler. Tiene 3034 filas y 18 columnas.
2. **Tabla de compra: ** Información consolidada de los pisos en venta. Tiene 12498 filas y 18 columnas.
3. **Gráficos:** Hoja donde creo los tablas dinámicas, gráficos y segmentadores para el Dashboard-€.
4. **Dashboard-€:** Visualización de las características de los pisos más rentables para compra y alquiler, así como la evolución y % de cambio de los precios.
5. **Dashboard-UN:** Visualización de la cantidad de unidades disponibles.
6. **Dashboard-HIPO:** Hoja en la que te permite calcular dos casos de hipoteca y rentabilidad.
7. **Hipoteca_1:** hojas donde se hacen los cálculos para la presentación en el dashboard-hipo.
8. **Hipoteca_1:** hojas donde se hacen los cálculos para la presentación en el dashboard-hipo.
9. **ITP:** hojas donde crean listas con los datos de ITP de las CCAA y una estimación del alquiler que se va a tener, para utilizar en la dashboard-hipo.
6. **Alquiler_provincia:** Tabla con los precios medios por metro cuadrado según fechas. También puedes encontrar las tablas dinámicas, gráficos y sementadores para utilizar en el Dashboard-€.
7. **Venta_provincia:** Tabla con los precios medios por metro cuadrado según fechas. También puedes encontrar las tablas dinámicas, gráficos y sementadores para utilizar en el Dashboard-€.

**5.1.4 Explicación de los dashboard y uso**
-	**Dashboard-€:** 
Se compone de 4 partes. Está orientado para ver la diferencia económica entre las diferentes características de vivienda. 
La de arriba, contiene el titulo y tres cajas. La llamada ‘Análisis compra y alquiler’, aparece la información económica y unidades de las viviendas en compra. La siguiente caja, análisis alquiler’ es igual a la anterior pero de las viviendas de alquiler. Por ultimo de este apartado, ‘rec compra-alquiler’ donde se puede ver los meses y años que se tardaría en recuperar la inversión. 
Hay que mencionar que las cifras que aparecen son dinámicas y se cambian con los filtros del lateral derecho. Paso a explicarlo
El apartado de los filtros está dividido en dos, alquile y compra. En ello puedes segmentar la información de las cajas y los gráficos a explicar a continuación. Se puede segmentar por área, vivienda, ascensor, garaje, habitaciones, baños, exterior-interior y rango de coste.
Los gráficos centrales, es donde se observa la información principal del dashboard. Como los apartados anteriores se divide en dos. Alquiler y compra, en estos se puede observar los siguientes gráficos, el primero precio medio, en el segundo el precio medio en las plantas que se encuentran las viviendas y por ultimo las el coste medio por habitaciones que tiene la vivienda.
Por último, explicar de este dashboard, la zona de los gráficos de líneas de alquiler y compra. En ellos se puede ver cómo ha evolucionado el coste medio de compra y alquiler de las áreas de Málaga. En el centro, separando los gráficos hay segmentadores para poder filtrar por área y dos tipos de fechas. Estos dos últimos segmentadores solo afectan a las cajas que tienen a la derecha donde se puede hacer una comparación de precio de una fecha a otra. 
Mencionar que hay segmentadores que afectan a todas las cajas y gráficos, pero hay otras que no. Principalmente se hizo eso para los gráficos del centro y que no se viese afectado el grafico de habitaciones y no filtrase por su propio segmentador.

-	**Dashboard-UN:**
Esta pantalla es similar a la anterior, su intención es que se pueda visualizar el numero de unidades que hay por las diferentes viviendas. En este caso se puede observar 3 partes diferenciadas. 
Como en el dashboard anterior, en la parte superior podemos encontrar, la caja con el título: ‘Análisis compra y alquiler’. En las siguientes cajas la información que aparece son las unidades de viviendas en venta y alquiler. 
En el apartado de la derecha están los filtros, los mismos y estructurados iguales. Se ven afectados los filtros de una página a otra.
En esta pantalla la parte principal lo tiene los gráficos dedicados a visualizar las unidades de las características de los pisos. Me ha parecido interesante dejar el grafico del precio medio de la página anterior, pudiendo ver así el precio de los filtros. Los siguientes graficos están centrados en ver la cantidad de unidades y porcentaje del tipo de viviendas que hay. El siguiente se puede ver si las viviendas se publicitan con garaje, sin garaje o de pago. El ultimo grafico de la derecha nos da el porcentaje y unidades de que las viviendas tengan ascensor. 

-	**Dashboard-HIPO:**
Esta es la ultimo dashboard de esta parte del proyecto. Te permite comprar dos casos de rentabilidad a la hora de comprar y alquilar una vivienda. Esta pantalla tiene 4 apartados. Antes de empezar la explicación de los 4 apartados mencionar dos cosas importantes, la primer es que solo se tiene que rellenar las celdas que están en azul. Las celdas que están en blanco se rellenan solas con los datos aportados a las azules. Lo siguiente a tener en cuenta son las celdas de color verde, son listas despegables que automáticamente hacen que afecte a la rentabilidad.

Lo primero que voy a explicar, son las dos cajas que están arriba de Caso-1 y Caso-2. En las celdas de color verde podemos elegir la categoría de alquiler que consideremos. Esta elección influye en el porcentaje de tiempo alquilado que vamos a tener la vivienda. Pasando de un fijo de un 100% a un pesimista del 50%.

Los dos siguientes apartados son similares a los ya explicados en los Dashboard anteriores. En ellos podemos encontrar las cajas con los precios y unidades de las categorías seleccionadas en los segmentadores. Además, las dos ultimas cajas de la derecha donde aparece el titulo de ‘Total a Pagar’ de cada caso. En el se puede visualizar el total a pagar de la vivienda, con los gastos de la vivienda, incremento por la hipoteca y gastos previos antes de alquilar la vivienda.
No me voy a extender en el apartado de los filtros ya que son los mismos que en las pantallas anteriores.

Si me voy a centrar en la parte central. Aquí puedes encontrar los casos para analizar la rentabilidad de dos viviendas. Tiene 4 columnas,

- Primera: Asociado a la compra.
o	ITP CCAA: Elegir la comunidad autónoma para ver que % de ITP te corresponde.
o	Precio vivienda: Precio por el que consideras comprar la vivienda.
o	Cantidad a hipotecar: Cantidad de dinero que vas a solicitar al banco.
o	% Hipoteca: automáticamente te aparece. Porcentaje de la cantidad total de la vivienda.
o	Gastos previos: Cantidad de dinero que consideras que te vas a gastar asociados en la compra de la vivienda o inmueble y en reformarlo. 

-	Segunda: Asociado al alquiler.
o	Alquiler: tendrás que rellenar por la cantidad que consideres el alquiler al mes. El del año se rellenara solo.
o	Costes: Aquí se tendrá que poner los costes que consideras tendrá la vivienda durante un año. Comunidad, IBI, Seguro y más cosas decidas ponerle. En los costes del mes te aparecerán automáticamente.
o	Facturación: Hay que poner por la cantidad que estimas alquilar la vivienda al mes, se pone automáticamente al año.

- Tercera: asociado a la hipoteca y rentabilidad.
o	Hipoteca en años: años a los que vas a pedir la hipoteca.
o	Tipo de interés: El interés por que te concederán la hipoteca.
o	Cuotas: automáticamente se calcula la cantidad a pagar al mes y al año.
o	Cash Flow: la cantidad económica que te queda al mes y año, después de pagar los gastos mensuales y la cuota.
o	Rentabilidad: La rentabilidad que tienes de la vivienda solo contando compra y alquiler.
o	ROE: Rentabilidad de la vivienda contando los gastos totales.

-	Cuarta: 
o	Mes: Fecha a la que quieres visualizar el estado del negocio.
o	Total Ingresado: la cantidad a la económica que se ha facturado hasta la fecha. 
o	Total Beneficio: la parte de lo ingresado menos los gastos a la fecha.
o	Total amortizado: cantidad económica y porcentual de la hipoteca a la fecha.


- ### **5.2. Bloque 2**

Este bloque del proyecto está centrado en otra metodología de obtención de datos, a traves de API's, asi como el uso de otra herramienta de visualización de datos, Power BI.

**5.2.1 Descarga de datos**

En este bloque hay dos apartados de información. La primera es la de información de los pisos. Descargada mediante API's de Idealista y la segunda cree un documento con información asociada a las viviedas para poder hacer un modelo de estralla. Permitiendo así que la información se puedise represantar mejor. Ahora expongo como lo realice:

Gracias a los estudios del modulo y de videos que vi repetidas veces entendí que eran las API's y que tenia que hacer para el proceso. Por lo que me puse en contacto con idealista para que me permitiesen utilizar sus API's para realizar el proyecto. Me lo dieron mi Apikey y mi Secret, para poder conectarme. 

El codigo utilizado lo consegui desarrollar leyendo y estudiando los pasos que me habia indicado idealista en un documento que me envio, ademas, utilice unos videos que encontre en youtube donde explicaba paso a pasos. El codigo que muestro en el proyecto es uno ya validado y puesto en claro, despues de hacer varios intento erroneos.

En el codigo puedes encontrar en la primera parte las librerias que se necesitan, despue la funición para utilizar Apikey y el secret. Despues crear el mensaje que se tiene que enviar a idealista para que te permita el acceso y el porceso de uso de un token.

La siguente parte es indicarle cuales son las caracteristicas de la información quieres acceder para descargar. Permitiendo así crear una lista con las pagianas que se han accedido y convirtiendolo posteriormente despues a dataframe.

Para terminar se guarda la información en un csv. Esto dara paso a los siguientes pasos. Este proceso de obtención mediante API's se hizo tanto para alquiler como para compra. 

El limite de desgarga que podia hacer al mes erá de 3000. Antes de empezar la descarga ya habia estudiado la cantiad de pisos de sevilla y habia unas 2000 viviendas de compra y otras 1000 de alquiler. Por lo que al ponerle un limite de distancia de un radio me iba a dejar una pocas viviendas fuera, teniendo que la información que mas me interesba estaba en el centro de la ciudad

**5.2.2 Limpieza de los datos**

La limpieza de los datos la realice con Power Queri. En ella realice los siguentes pasos:
- Cambiar el nombre de las columnas.
- Remplazar valores.
- Eliminar columnas.
- Crear columnas calculadas.
- Separar información de columnas para crear nuevas.

Este proceso lo hice para el archivo de alquiler como de compra.

**5.2.3 Unión de la información**

Tras haber hecho el proceso de transformación de los datos ya tenerlos disponibles en la vista de informes de Power BI, me di cuenta que la información no se me representaba bien. Por lo que cree otro documento en el cuales tuviese otras tablas que me permitiesen crear un modelo de estrella y usarlas para representar mejor la información.

**5.2.4 Explicación de los dashboard y uso**

El proyecto de Power BI consta de 5 pantalla.

-	 **Principal:**

En esta pantalla tienes 3 areas que ver. El apartado de arriba donde tienes un filtros basicos. En la parte central encuentras dos columnas, columnas y alquiler. En ellas puedes ver un recuento de las unidades y el precio de medio de la viviendas.
Si presionas control y click encima de cualquiera de las cajas te llevara al dashboard en cuestion.

- **Precio-compra y alquiler:**

Voy a explicar que graficos y como se puede utilizar las pantallas de precio ya que son similares en su estructura pero no en el contenido que aparece.

En el apartado de arriba hay una represantación mas amplia de filtros: tipo de casa, habitaciones, baños, garaje, tipo de vivienda. Ademas, de un boton para borrar todos los filtros y un navegador de página para volver a la principal.

En el apartado de los graficos, empiezo por la izquierda un grafico de barras horizonales para representar el precio promedio por las plantas del edificio.  En la parte inferior podemos un grafico de tarta donde se representa el porcentaje de viviendas con garaje.

En el centro de la pantalla hay tres graficos de barras verticales, en el que se puede ver asimple vista la diferencia de precios entre las casas y los pisos. Los graficos tiene en el eje X: habitaciones, esterior interior y parking.

A la derecha de la pantalla se pueden ver diferentes tipos de cajas, arriba hay dos que muestrar el precio promedio de aluiler y compra. Debajo de estas 2, hay un grafico de mapa donde se utilizo como referencia el codigo postal. A la derecha de este un grafico de medidor en el que secalcula el % de rentabilidad. Se le indico un marcador de destino de un 6%. Abajo podemos encontrar dos tablas una para ver el ID y precio de ese inmueble. Por ultimo la tabla que esta a la derecha de esta se puede ver por municipio y distrito el tiempo de recuperación en años y % de recuperación.

- **Unidades-alquiler y compra**:

Los filtros de la parte superior son iguales a las pantallas anteriores. En cambio las cajas de este dashboard son algunos diferentes. En el lado de la izquierda se puede encontra un grafico de barras horizontales de donde se puede ver un recuento de pisos por planta.
En el centro hay dos graficos de tarta donde se representa un recuento de las vivienda que dan al interior o exterior. y un recuento casas con los diferentes tipos de garajes.

En el lateral derecho hay un grafico de barras para hacer un recuento unidades por habitaciones. También puedes ver un grafico de mapa y de treemap. Por ultimo, abajo de estos dos graficos hay una tabla donde se puede el recuento de unidades por municipio, distrito y tipo de viviendas.

- ### **5.3. Bloque 3**

**5.3.1 Descarga de datos**

**5.3.2 Limpieza de los datos**

**5.3.3 Unión de la información**

**5.3.4 Explicación de los dashboard y uso**
-	**Dashboard-€:**

