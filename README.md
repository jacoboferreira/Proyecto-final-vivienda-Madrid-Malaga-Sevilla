# **Situación actual de la vivienda en las ciudades de Madrid, Málaga y Sevilla.**
Rentabilidad y posibilidades de compra en España a 2025.

## **1. Resumen o descripción**
 Los datos han sido obtenidos de Idealista mediante tres formas diferentes.

Después de mudarme en febrero me dio que pensar después de observar la diferencia de precios en la vivienda. ¿Dónde queda la clase media? ¿tener una vivienda? a la que hace referencia siempre la clase política. La intención de este proyecto es observar de verdad si existe la clase media, ¿cómo se ha visto afectada la evolución del precio de la vivienda y el de los salarios?.

Por ello he realizado un análisis de rentabilidad a la hora de comprar y alquilar una casa, he realizado un análisis a la hora de comprar una vivienda, he realizado un análisis predictivo de la evolución del precio de la vivienda. 

El proyecto consta de 3 bloques. He realizado una metodología de obtención de datos y uso de herramienta para cada bloque, expongo delante un resumen de los bloques:

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
	o	Informe: Correlación, machine learning, predicción a future y rentabilidad.
	o	Obtención de datos: WEB Scraping idealista.
	
Mediante este proceso he querido desarrollar y explorar más mis conocimientos aprendidos con el programa de The Power MBA, Udemy y videos de YouTube. Para algunos de los procesos, me he apoyado en la herramienta Chat GPT.


## **2. Estructura del repositorio**
- 📂 **Bloque 1:** Proyecto creado con Excel, datos de Málaga, obtenido los datos con IO.
	- 📂 **Alquiler:** La carpeta contiene los archivos descargados en sucio de los precios de alquiler Benalmádena, Centro, Estepona, Fuengirola, Marbella y Torremolinos. Están en formato Excel, contienen de 30 a 5 anunció de pisos. Además, tiene un documento de Python que me ayudo a limpiar y ordenar los documentos.
	- 📂 **Compra:** La carpeta contiene los archivos descargados en sucio de los precios de compra Benalmádena, Centro, Estepona, Fuengirola, Marbella y Torremolinos. Están en formato Excel, contienen de 30 a 5 anunció de pisos. Además, tiene un documento de Python que me ayudo a limpiar y ordenar los documentos.
	- 📂 **Evolutivo 1:** La carpeta contiene los archivos descargados en sucio del evolutivo del precio/ metro cuadrado de Málaga, Benalmádena, Centro, Estepona, Fuengirola, Marbella y Torremolinos. Están en formato Excel, Además, tiene un documento de Python que me ayudo a limpiar y ordenar los documentos. Dentro de la carpeta hay otra en la que se hacen la predicciones de LSTM y se guarda por distrito los datos con la predicción a 2036.
   	- 📊 **Análisis Málaga:** Excel donde se realiza el proyecto.

- 📂 **Bloque 2:** Proyecto creado con Power Bi, datos de Sevilla, obtenido los datos con Python mediante la API de idealista.
	- 📂 **Alquiler:** La carpeta contiene el archivo con los datos de alquiler de Sevilla, además del archivo donde se ejecuta el código de Python.
	- 📂 **Compra:** La carpeta contiene el archivo con los datos de compra de Sevilla, además del archivo donde se ejecuta el código de Python.
	- 📂 **Fondos BI:** Carpeta con los fondos disponibles para usar en Power BI.
	- 📄 **oauth2-documentation:** Documento explicativo para conectarse a la API.
	- 📄 **property-search-api-v3_5:** Documento con las especificaciones de los datos que se pueden descargar y los filtros a usar.
	- 📊 **power_bi_sevilla:** Power Bi donde se realiza el proyecto.


- 📂 **Bloque 3:** Proyecto creado con Python, datos de Madrid, obteniendo los datos con Python mediante la WEB scraping de idealista.
	- 📂 **Alquiler:** Contiene los archivos obtenidos con los datos de alquiler de Madrid, además del archivo donde se ejecuta el código de Python.
	- 📂 **Compra:** Contiene los archivos obtenidos con los datos de compra de Madrid, además del archivo donde se ejecuta el código de Python.
	- 📂 **Datos Extra:** Contiene archivos con información extra para llevar acabo los análisis.
- 📂 **Evolutivo precio:** Contiene archivos para el análisis evolutivo.
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
Como he mencionado anteriormente el proyecto consta de 3 bloques. En su mayoría los datos son los mismos. Dentro de cada bloque del proyecto se dividen en otros tres apartados**compra, alquiler y evolutivo**. En el caso del último también se han obtenido datos de páginas web oficiales del estado. 
Hay que tener claro, que los datos cuando se usan en herramientas como Python, a la hora que va avanzando el proyecto se pueden ir cambiando el número de columnas y el nombre. 
Por eso voy a exponer las principales columnas que tienen los archivos:

	- Archivos de alquiler y compra.
	
	- Título: Nombre del anuncio.
	
	- Ciudad: Ciudad en la que se encuentra la vivienda.
	
	- Coste: Precio en euros.
	
	- Habitaciones: Número de habitaciones.

	- Metros cuadrados: Superficie total del inmueble.
	
	- Planta: Altura en la que está el piso.
	
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
- **Población Madrid:** numero de residentes en la comunidad de Madrid.
- **Nº DE LICENCIA CONSTRUCCION:** Número de licencias concedidas en España.
- **Nº DE EDIFICIOS:** Numero de edificios construidos en España.
- **Nº DE VIVIENDAS:** Número de viviendas construidas en España.


## **5. Proceso llevado a cabo**

Voy a explicar el proceso por partes, ya que a cada parte lo he querido crear con la intención de aprender, usar diferentes herramientas y metodología de obtener los datos.

- ### **5.1. Bloque 1**

Este primer bloque es una continuación y mejora del primer proyecto de análisis compra y alquiler. He mejorado el número de viviendas, la obtención de información nueva como la ciudad y área, baños, etc. Expongo a continuación el proceso llevado.

**5.1.1 Descarga de datos**

Se utilizo la aplicación utilizada anteriormente, pero con una suscripción mejor, la cual me permitía descargar de forma ilimitada la información. Seguía teniendo limitaciones de solo poder obtener la información de las portadas de los anuncios de idealista, a esto se le suma que en cada página solo tiene un máximo de 30 anuncios y no podía pasar de la página 60.
El problema que tiene esta metodología es que tienes que repetir mucho el proceso y la información no se descarga ordenadamente. Cuando abres el archivo podías encontrar diferentes órdenes. Además, para poder obtener los baños antes de descargar la información tenía que filtrar en idealista. Cuando tenía descargada la información de un área, seleccionaba todos los documentos y con el comando de f2 le daba el nombre que quería y se ponían en todos con la diferencia de un numero entre paréntesis a si luego podía utilizarlo luego para poner el nombre del área en la columna.
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
El último documento creado para este análisis fue el **"Análisis Málaga"**, consta de 11 hojas:

1. **Tabla de alquiler: ** Información consolidada de los pisos en alquiler. Tiene 3034 filas y 18 columnas.
2. **Tabla de compra: ** Información consolidada de los pisos en venta. Tiene 12498 filas y 18 columnas.
3. **Gráficos:** Hoja donde creo las tablas dinámicas, gráficos y segmentadores para el Dashboard-€.
4. **Dashboard-€:** Visualización de las características de los pisos más rentables para compra y alquiler, así como la evolución y % de cambio de los precios.
5. **Dashboard-UN:** Visualización de la cantidad de unidades disponibles.
6. **Dashboard-HIPO:** Hoja en la que te permite calcular dos casos de hipoteca y rentabilidad.
7. **Hipoteca_1:** hojas donde se hacen los cálculos para la presentación en el dashboard-hipo.
8. **Hipoteca_2:** hojas donde se hacen los cálculos para la presentación en el dashboard-hipo.
9. **ITP:** hojas donde crean listas con los datos de ITP de las CCAA y una estimación del alquiler que se va a tener, para utilizar en la dashboard-hipo.
6. **Alquiler_provincia:** Tabla con los precios medios por metro cuadrado según fechas. También puedes encontrar las tablas dinámicas, gráficos y segmentadores para utilizar en el Dashboard-€.
7. **Venta_provincia:** Tabla con los precios medios por metro cuadrado según fechas. También puedes encontrar las tablas dinámicas, gráficos y segmentadores para utilizar en el Dashboard-€.

**5.1.4 Explicación de los dashboard y uso**
-	**Dashboard-€:** 
Se compone de 4 partes. Está orientado para ver la diferencia económica entre las diferentes características de vivienda. 
La de arriba, contiene el titulo y tres cajas. La llamada ‘Análisis compra y alquiler’, aparece la información económica y unidades de las viviendas en compra. La siguiente caja, análisis alquiler’ es igual a la anterior, pero de las viviendas de alquiler. Por último de este apartado, ‘rec compra-alquiler’ donde se puede ver los meses y años que se tardaría en recuperar la inversión. 
Hay que mencionar que las cifras que aparecen son dinámicas y se cambian con los filtros del lateral derecho. Paso a explicarlo
El apartado de los filtros está dividido en dos, alquile y compra. En ello puedes segmentar la información de las cajas y los gráficos a explicar a continuación. Se puede segmentar por área, vivienda, ascensor, garaje, habitaciones, baños, exterior-interior y rango de coste.
Los gráficos centrales, es donde se observa la información principal del dashboard. Como los apartados anteriores se divide en dos. Alquiler y compra, en estos se puede observar los siguientes gráficos, el primero precio medio, en el segundo el precio medio en las plantas que se encuentran las viviendas y por último el coste medio por habitaciones que tiene la vivienda.
En la parte inferior del dashboard, tiene dos gráficos de líneas de alquiler y compra. En ellos se puede ver cómo ha evolucionado el coste del metro cuadrado medio de compra y alquiler de las áreas de Málaga. En el centro, separando los gráficos hay segmentadores para poder filtrar por área y dos tipos de fechas. Estos dos últimos segmentadores solo afectan a las cajas que tienen a la derecha, donde se puede hacer una comparación de precio de una fecha a otra. 
Mencionar que hay segmentadores que afectan a todas las cajas y gráficos, pero hay otras que no. Principalmente se hizo eso para los gráficos del centro y que no se viese afectado el grafico de habitaciones y no filtrase por su propio segmentador.

-	**Dashboard-UN:**
Esta pantalla es similar a la anterior, su intención es que se pueda visualizar el número de unidades que hay en las diferentes características de viviendas. En este caso se puede observar 3 partes diferenciadas. 
Como en el dashboard anterior, en la parte superior podemos encontrar, la caja con el título: ‘Análisis compra y alquiler’. En las siguientes cajas la información que aparece son las unidades de viviendas en venta y alquiler. 
En el apartado de la derecha están los filtros, los mismos y estructurados iguales. Se ven afectados los filtros de una página a otra.
En esta pantalla la parte principal lo tiene los gráficos dedicados a visualizar las unidades de las características de los pisos. Me ha parecido interesante dejar el grafico del precio medio de la página anterior, pudiendo ver así el precio de los filtros. Los siguientes gráficos están centrados en ver la cantidad de unidades y porcentaje del tipo de viviendas que hay. El siguiente se puede ver si las viviendas se publicitan con garaje, sin garaje o de pago. El ultimo grafico de la derecha nos da el porcentaje y unidades que las viviendas tengan ascensor. 

-	**Dashboard-HIPO:**
Este es el último dashboard de esta parte del proyecto. Te permite comprar dos casos de rentabilidad a la hora de comprar y alquilar una vivienda y ver la cantidad de tu salario iría a pagar la hipoteca. Esta pantalla tiene 4 apartados. Antes de empezar la explicación de los 4 apartados mencionar dos cosas importantes, la primera, es que solo se tiene que rellenar las celdas que están en azul. Las celdas que están en blanco se rellenan solas con los datos aportados a las azules. Lo siguiente a tener en cuenta son las celdas de color verde, son listas despegables que automáticamente hacen que afecte a la rentabilidad.

Lo primero que voy a explicar, son las dos cajas que están arriba de Caso-1 y Caso-2. En las celdas de color verde podemos elegir la categoría de alquiler que consideremos. Esta elección influye en el porcentaje de tiempo alquilado que vamos a tener la vivienda. Pasando de un fijo de un 100% a un pesimista del 50%.

Los dos siguientes apartados son similares a los ya explicados en los Dashboard anteriores. En ellos podemos encontrar las cajas con los precios y unidades de las categorías seleccionadas en los segmentadores. Además, las dos últimas cajas de la derecha donde aparece el título de ‘Total a Pagar’ de cada caso. En él se puede visualizar el total a pagar de la vivienda, con los gastos de la vivienda, incremento por la hipoteca y gastos previos antes de alquilar la vivienda.
No me voy a extender en el apartado de los filtros ya que son los mismos que en las pantallas anteriores.

Si me voy a centrar en la parte central. Aquí puedes encontrar los casos para analizar de dos viviendas. Tiene 5 columnas,

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
-	Quinta: 
o	Ingresos brutos: Cantidad de ingresos brutos anuales, tuyo o en pareja.
o	% del bruto: Porcentaje de la cantidad puesta antes tendrías que destinar a la hipoteca.

- ### **5.2. Bloque 2**

Este bloque del proyecto está centrado en otra metodología de obtención de datos, a traves de API's, así como el uso de otra herramienta de visualización de datos, Power BI.

**5.2.1 Descarga de datos**

En este bloque hay dos apartados de información. La primera es la de información de los pisos. Descargada mediante API's de Idealista y la segunda cree un documento con información asociada a las viviendas, para poder hacer un modelo de estrella. Permitiendo así que la información se pudiese representar mejor. Ahora expongo como lo realice:

Gracias a los estudios del módulo y de videos que vi repetidas veces entendí que eran las API's y que tenía que hacer para el proceso. Por lo que me puse en contacto con idealista para que me permitiesen utilizar sus API's para realizar el proyecto. Me lo dieron mi Apikey y mi Secret, para poder conectarme. 

El código utilizado lo conseguí desarrollar leyendo y estudiando los pasos que me había indicado idealista en un documento que me envió, además, utilice unos videos que encontré en YouTube donde explicaba paso a pasos. El código que muestro en el proyecto es uno ya validado y puesto en claro, después de hacer varios intento erróneos.

En el código puedes encontrar en la primera parte las librerías que se necesitan, después la función para utilizar Apikey y el secret. Después crear el mensaje que se tiene que enviar a idealista para que te permita el acceso y el proceso de uso de un token.
La siguiente parte es indicarle cuales son las características de la información quieres acceder para descargar. Permitiendo así crear una lista con las páginas que se han accedido y convirtiéndolo posteriormente a dataframe.
Para terminar, se guarda la información en un csv. Esto dará paso a los siguientes pasos. Este proceso de obtención mediante API's se hizo tanto para alquiler como para compra. 

El límite de descarga que podía hacer al mes era de 3000 viviendas. Antes de empezar la descarga ya había estudiado la cantidad de pisos de Sevilla y había unas 2000 viviendas de compra y otras 1000 de alquiler. Por lo que al ponerle un límite de distancia de un radio me iba a dejar una pocas viviendas fuera, teniendo que la información que más me interesaba estaba en el centro de la ciudad

**5.2.2 Limpieza de los datos**

La limpieza de los datos la realice con Power Query. En ella realice los siguientes pasos:
- Cambiar el nombre de las columnas.
- Remplazar valores.
- Eliminar columnas.
- Crear columnas calculadas.
- Separar información de columnas para crear nuevas.

Este proceso lo hice para el archivo de alquiler como de compra.

**5.2.3 Unión de la información**

Tras haber hecho el proceso de transformación de los datos y tenerlos disponibles en la vista de informes de Power BI, me di cuenta que la información no se me representaba bien. Por lo que cree otro documento en el cuales tuviese otras tablas que me permitiesen crear un modelo de estrella y usarlas para representar mejor la información.

**5.2.4 Explicación de los dashboard y uso**

El proyecto de Power BI consta de 5 pantalla.

-	 **Principal:**

En esta pantalla tienes 3 áreas que ver. El apartado de arriba donde tienes un filtro básico. En la parte central encuentras dos columnas, columnas y alquiler. En ellas puedes ver un recuento de las unidades y el precio de medio de las viviendas.
Si presionas control y click encima de cualquiera de las cajas te llevara al dashboard en cuestion.

- **Precio-compra y alquiler:**

Voy a explicar que gráficos y como se puede utilizar las pantallas de precio, ya que son similares en su estructura pero no en el contenido que aparece.

En el apartado de arriba, hay una representación más amplia de filtros: tipo de casa, habitaciones, baños, garaje, tipo de vivienda. Además, de un botón para borrar todos los filtros y un navegador de página para volver a la principal.

En el apartado de los gráficos, empiezo por la izquierda. Un gráfico de barras horizontales para representar el precio promedio por las plantas del edificio.  En la parte inferior, hay una tabla en la que se puede ver el tiempo de recuperación en años y el % de retorno. En el caso del precio-alquiler podemos ver un gráfico de tarta donde se representa el porcentaje de viviendas con garaje.

En el centro de la pantalla hay tres gráficos de barras verticales, en el que se puede ver a simple vista la diferencia de precios entre los diferentes tipo de viviendas. Los gráficos tiene en el eje X: habitaciones, exterior-interior y parking.

A la derecha de la pantalla, se pueden ver diferentes tipos de cajas, arriba hay dos que muestran el precio promedio de alquiler y compra. Debajo de estas 2, hay un gráfico de mapa donde se utilizó como referencia el código postal. A la derecha de este un gráfico de medidor en el que se calcula el % de rentabilidad. Se le indico un marcador de destino de un 6%. Abajo podemos encontrar una tabla en la que te permite cuanto te costaría pagar la hipoteca para una vivienda con diferentes habitaciones y municipio. Además, el porcentaje del salario bruto medio de Andalucía. En la pestaña de alquiler, es diferente hay dos tablas una para ver el ID y precio de ese inmueble y la otra tabla se puede ver por municipio y distrito el tiempo de recuperación en años y % de recuperación.

- **Unidades-alquiler y compra**:

Los filtros de la parte superior son iguales a las pantallas anteriores. En cambio, las cajas de este dashboard son algunos diferentes. En el lado de la izquierda, se puede encontrar un gráfico de barras horizontales de donde se puede ver los porcentajes que hay de tipo de viviendas municipios. El de su derecha es igual, pero para ver si la clasificación que tienen de parking. 
En el centro hay un grafico de barras horizontales para ver las unidades de viviendas que hay por planta, ya que en su mayoría son pisos.
En el lateral derecho hay un gráfico de barras para hacer un recuento unidades por habitaciones. También puedes ver un gráfico de mapa y de treemap. Por último, abajo de estos dos gráficos hay una tabla donde se puede el recuento de unidades por municipio, distrito y tipo de viviendas.

Una de las características de Power BI, es la capacidad de poner información en la herramienta, así puedes visualizar más información como precio promedio, la mediana de precios, etc. En los gráficos de los dashboard se han utilizado ya que aporta más información. 
Es importante entender cómo funcionan las metodologías de filtro en Power BI. 

- ### **5.3. Bloque 3**

El bloque 3, es el último y más complejo. Es al que más tiempo le he dedicado y profundidad en cuanto a desarrollo. En el utilizo la metodología de Web Scraping para descargar la información y todo el proyecto se hace con Python. En el realizo un modelo de Maching Learning, un modelo de predicción a futuro de precios y un análisis de rentabilidad. En este caso he elegido la ciudad de Madrid.

**5.3.1 Descarga de datos**
Como he mencionado arriba el método utilizado en este caso para descargar la información, ha sido Web Scraping. Para ello tuve que leer información y consultar videos en los que explicaban como se tenía que hacer. La información descargada son 3, viviendas en venta, en alquiler y la evolución diferentes datos relacionados con la vivienda en españa.
Para explicar el proceso de descarga me voy a centrar en código de alquiler. Antes de empezar explicar características de Idealista. Limita el acceso si superar un Nº de anuncios y si superas más de 60 páginas. Esto limito la descarga de información en un solo día. También el bloqueador de captcha, al cual tenía que estar atento porque si no me bloqueaba la descarga. Además, cuando incluso los distritos tenían más de 1200 inmuebles, tuve que poner un limitador. Durante el código le he incluido “print” para ir viendo lo que está procesando.
La información se sacaba de idealista, primero me tenía que meter desde un navegador a ver el distrito que me quería descargar y coger la URL. Reduciendo así en número de viviendas y teniendo que replicar por cada distrito o municipio.
El proceso se dividide en 3 partes, la primera obtener los id de los anuncios, posterior el proceso para parsear y lo último es guardar el archivo en un csv.
Ahora voy a explicar más en detalle el código, es el siguiente, primero hay que pedirle a Python que abra una pantalla de Google Chrome, crear el valor de X, crear una lista para que posteriormente se vaya rellenando y el limitador. 
Todo el proceso de obtener los ID en un bucle while true, para que pase por todas las páginas cogiendo los ID, hasta llegar al limitador o final de los anuncios.
La siguiente parte del código se centra en parsear, esto es ir entrando en cada anuncio y seleccionar la información que se le ha indicado que busque en el código de la página Web. Se crea el código en una función para que se repita por cada anuncio. Se crea la variable que luego se ha va a pedir que te retorne y así se va ir creando cada fila. Los apartados seleccionados del código de idealista fueron los siguientes: id, titulo, localización, precio, características básicas, características extra, ubicación y edificio. Estos datos posteriormente tendrán que ser procesado y limpiados. 
La siguiente parte del código lo que hace es crear un DataFrame donde se acumule la información de todos los anuncios y guardarlo en un csv. 

Al timar el proceso de Scraping de alquiler y compra y empezar a limpiar los datos, me di cuenta que no había obtenido la información del edificio, lo que hace referencia a la planta, si es exterior o interior y si tiene ascensor. Aspectos importantes que influyen el precio y por lo tanto en el análisis. Por lo que tuve que repetir el proceso, pero solo para ese apartado. Cuando esto lo hice, pasaron ya unas semanas y descubrir que muchos de los anuncios ya no existían, por lo que pude comprobar la alta demanda y rotación que hay en Madrid.

La descarga de la información del evolutivo tuve que hacerla de diferentes formas ya que se me bloqueo el Scraping y no tuve forma de solucionarlo. Seleccione las mismas áreas de Madrid que en el bloque anterior y además me descargue información de salarios relacionados con la edad, sexo, año, comunidad autónoma y el evolutivo por comunidad autónoma. Estos datos fueron obtenidos de páginas oficiales del gobierno.

**5.3.2 Preparación de los datos**
5.3.2.1 Alquiler y compra
Cuando ya había terminado la descarga, me di cuenta como mencioné de la falta de información del edificio. Repite el proceso entero. Posteriormente tenía que unificar la información en uno solo archivo. Por lo que primero tenía que unir los archivos de todas las áreas a uno solo y luego conectar mediante merge la información extra. Este proceso lo hice para los datos de alquiler y compra por separado, ya que la primera parte del análisis es un modelo de regresión (Machine Learning) de los pisos de compra, en otro documento realice una unión de los pisos de compra como de alquiler, para poder realizar un análisis de rentabilidad. 
Ahora pasaré a explicar el proceso de tratamiento de los datos para poder llegar los análisis. 
Lo primero que hice fue comprobar cómo podía dividir las columnas para extraer la información de forma correcta. En tres columnas tenía mucha información separada por una coma, pero no podía hacer una separación simple ya que no sería eficaz. Se podía detectar unos patrones de texto que servían para poder separar en diferentes columnas. Pasando de las columnas características básicas a (superficie_m2, superficie_utiles_m2, habitaciones, baños, terraza, estado, armarios_empotrados, orientación, año_construccion y calefacción), la columna de características_extra se dividio en: aire_acondicionado, certificado_cosumo, cert_emisiones. La columna de ubicación la dividí en calle, barrio, distrito y ciudad. El siguiente paso que realice fue eliminar las columnas que ya no me interesaban (superficie_util_m2, cert_consumo, cert_emisiones, características_basicas, caracterisiticas_extra y ubicación). Trate también las columnas de orientación, para quedarme con solo la información que estaba delante de la coma. Posteriormente la borraría. 
Ahora es cuando uniría la información que me descargue por segunda vez. Añadiendo, Planta, Ascensor y EXT-INT. Este DataFrame lo guarde como “datos_analizar_compras” (“datos_unificados_alquiler”).


5.3.2.2 Evolutivo
En cuanto a la información del evolutivo solo tuve que añadir con merge los documentos de las diferentes áreas. Posteriormente cuando fui analizar la información decidí solo coger la información de Madrid ciudad a nivel global, sin diferenciar por distrito. También para poder hacer mas enriquecido el análisis le añadí:
- SM Madrid: Evolución del salario bruto.	
- SB anual: Salario bruto anual de España.
- Población Madrid: Número de residentes en la comunidad de Madrid.
- Nº DE LICENCIA CONSTRUCCION: Número de licencias concedidas en España.
- Nº DE EDIFICIOS: Numero de edificios construidos en España.
- Nº DE VIVIENDAS: Número de viviendas construidas en España.
Estos datos que acabo de mencionar están descritos por año por lo que tuve que reducir la información que tenia del documento de evolutivo de meses a años para que pudiese coincidir, para hacer el análisis. 

**5.3.3 Explicación del código**
El proyecto lo realizo en un nuevo documento. Al que había estado antes trabajando. Tengo un total de 4 archivos. El primero que voy a desarrollar es de machine learning.
-	**Codigo_proyecto_compra:**

En este apartado voy a explicar el proceso y código que he utilizado para el proyecto de machine learning. Para conseguirlo, continue procesando la información y realizando otros análisis antes. El procesado mencionado anteriormente, fue el básico que hice para luego empezar a trabajar. 
Importante mencionar, que como la base de datos era muy amplia, se decidió filtrar la información por pisos y de la ciudad de Madrid Descartando todas la viviendas de las afueras y tipo de vivienda casa, chalet, finca, etc.
Para poder continuar con los análisis había que seguir tratando los datos. Antes de seguir explicándolo, mencionar que modifique las set_option para poder ver todas la columnas y texto de las celdas. 
Siguientes pasos que realicé, crear una columna de vivienda, del título pude sacar de la primera palabra que tipo de vivienda era. Creando así una nueva columna. También pase las columnas habitaciones, baños, superficies_m2 y años de construcción a Inte64. El siguiente paso fue crear una columna del precio por metro cuadrado. Elimine las columnas de localización y calle. Cambie el texto de la columna superficie_m2 por m2.
Ante de realizar el modelo predictivo del precio de las viviendas tengo que hacer más limpieza de los datos y análisis. Lo primero que hice fue ver, el número y porcentaje de nulos que tenía en las columnas. Después cree una columna nueva, categorizando las viviendas en dos tipos: piso y casa. 
Elimine más columnas debido al número de nulos y creencia de poco valor predictivo de las columnas, terraza, orientación, año_construccion, calefacción. 
También tuve que categorizar las plantas, para que todas tuviesen un valor numérico. Eliminando así esta columna, para quedarme con la nueva. También elimine la columna titulo y id.
Posteriormente dividí las columnas en numéricas y categóricas. Esto me permitió hacer un bucle for para representar en un gráfico de barras las columnas.
Las columnas, estado, ascensor, EXT-INT, tipo de vivienda, armarios_empotrados, aire_acondicionado, los codifique.
Realice dos correlación, una con pisos en Madrid y la segunda con todas las variables para comprobar que columnas tenían más peso en el precio. Después, realice la primera regresión, con precio como variable predictora. El tamaño de X train es del 80% y de X_test es de 20%. En el primer caso utilice una regresión lineal. Pero posteriormente quise comprobar entre diferentes modelos cual era el mejor para predecir el valor del precio, eligiendo también los modelos Random Forest y Gradient Boosting.

 -	**ANALISIS_RENTABILIDAD:**
 
En esta parte del proyecto, quise analizar la rentabilidad de la compra y alquiler de viviendas mediante Pyhton. 
Lo primero que hice fue abrir los dos archivos de alquiler y compra que tenia de Madrid. Para que el proceso fuese más limpio y eficaz me centre en las viviendas de tipo piso. El siguiente paso fue normalizar los nombres de las columnas para más tarde conectarlas. 
También cree una nueva columna en la que categorice las viviendas por cada 20 metros cuadrados. Intentando así poder utilizar los metros cuadrados dentro del análisis. 
Cree una variable tanto para alquiler como para compra, en la que agrupe el valor de precio por barrio, distrito, habitaciones, baños y rango m2. Pudiendo así utilizar la fórmula de rentabilidad entres cada una de esas categorizaciones. Ya teniendo esto, solo queda representar los datos. La primera vez hago una representación de los 20 casos que mejor rentabilidad tienen y un gráfico del distrito centro. 
En el siguiente bloque de código creo un bucle ‘for’ en el que un gráfico y represente los 10 mejores casos por cada distrito.

-	**PROYECTO_EVOLUTIVO_PRECIO:**

Este es el último archivo del proyecto, en el he querido hacer un análisis de series temporales en el que predijese el precio de la vivienda teniendo en cuenta una serie de valores.
El código de este proyecto, ya lo había trabajado y pulido en otro documento en el que había estado probando antes. La única diferencia es que como ya mencioné antes los datos que utilice en este archivo no estaban en meses sino en años. Tuve que utilizar una fórmula para interpolar los datos a meses, ya que así se pueden analizar mejor. La predicción la realice 2 veces. La primera hasta la fecha de 06/2024 y la segunda hasta 2030.
Voy a pasar a explicar el bloque del codigo. Lo primero es abrir el archivo donde están los datos, se llama “Datos Evolutivos”, está en formato CSV. Lo siguiente es normalizar los nombres de las columnas, pasar a valor fecha la columna “Fecha”. Como he mencionado antes interpolar los datos a mes. Después de esto, ya se puede pasar a normalizar los datos para un mejor análisis. Ahora, toca la parte del código enfocado al modelo LSTM y su entrenamiento, indicando en el primer caso de unos 24 meses y hasta 2030. Ya lo que queda es representar en un gráfico y una tabla los datos que arroja el modelo.

## **6. Resultados y conclusiones**
Los resultados responden a la pregunta de si la clase media ha desaparecido o no de España, centrándonos en las ciudades de Madrid, Málaga y Sevilla. Teniendo como uno de los pilares del proyecto la compra de la vivienda, como uno de los aspectos fundamentales de la vida adulta, capacidad de independencia, seguridad y estabilidad en el desarrollo de una vida a futuro. ¿Esto se debe a un cambio generacional en el consumo y capacidad de consumo? ¿La vivienda ha pasado a un segundo plano? ¿Se debe a un encarecimiento? O ¿a un cambio de estilo de una vida a futuro?
Por ello investigue la rentabilidad de comprar una casa y alquilarla. Además de cuanto supone en salario de una pareja el comprar una vivienda. Este análisis es una aproximación, en el que he trabajado durante mucho tiempo. No afirmo, ni puedo decir que los datos son 100% exactos, pero si una aproximación a tres grandes ciudades de España.

Ahora pasare a exponer los datos generales del proyecto y posteriormente entrare en detalle a exponerlos. Se ha obtenido una muestra de 23.545 viviendas en venta y 12.359 viviendas en alquiler. De esas corresponde a las siguientes ciudades:
- Málaga: Venta 40245 (12497 (31%)) / Alquiler 9497 (3027 (32%))
- Sevilla: Venta 10533 (2147 (20%)) / Alquiler 2141 (1162 (54%))
- Madrid: Venta 25821 (8901 (34%)) / Alquiler 11788 (7442 (63%))

Para entrar en más detalle de las viviendas descargadas, te recomiendo ver el Excel “Anexo”, pestaña “Unidades_viviendas”.  Mencionar que en Excel este apartado, se pueden encontrar % superiores a 100, esto es debido, a que en el momento de la descarga se podían encontrar más anuncios de los que hay en el momento. En el documento de Anexo recojo en su mayoría los datos que voy a exponer en las conclusiones.

Las cifras mostradas fuera de los paréntesis son el número de viviendas publicitadas en Idealista a fecha de 02/10/2025. Los datos de dentro de los paréntesis, son los obtenidos durante el tiempo que he trabajado en este bloque. Voy a explicar mi conclusión acerca de las metodologías de obtención de datos:
Listly.io: es la más simple de usar, no hace falta tener conocimientos específicos. Tiene 6 inconvenientes, si quieres obtener mucha información tienes que pagar una subscripción, el proceso lo tienes que repetir muchas veces, ya que solo puedes obtener 30 anuncios por descarga, solo puedes obtener la información del título del anuncio, la información no se descarga con una estructura fija y la cantidad de páginas para descargar de una categoría o filtros es de 60, unas 1800 viviendas.
API’s: La descarga de la información se hace muy rápidamente y bien estructurada. Limitaciones, Idealista solo te permite obtener unas 3000 viviendas al mes, la obtención de la información se hace marcando un perímetro y no por municipios. Si quieres un número más grande de viviendas tienes que pagar. Tienes que tener un conocimiento avanzado de Python.
Web Scraping: Puedes obtener toda la información que quieras, es la que más información de cada vivienda te permite descargar y te permite obtener la información por municipios y filtros. Las limitaciones son, Tienes que tener un conocimiento avanzado de Python tanto para descargar como para limpiar los datos, la cantidad de páginas para descargar de una categoría o filtros es de 60, unas 1800 viviendas, el tiempo de ejecución es prolongado, se podría reducir en el codigo. También el tener que estar atento para que no se te bloque con un Snapchat.

Antes de entrar en detalla de cada bloque, mencionar que el estudio de los porcentajes del coste en salario de la compra de viviendas, se ha hecho de pisos, de 1, 2 y 3 habitaciones. Pidiendo una hipoteca del 90% y entregando una entrada del 10%. Para tomar el precio de las viviendas, se ha tomado el precio medio por cada municipio de los datos obtenidos de Idealista. En cuanto a los salarios los he obtenido del INEM y tenido que aplicar el aumento de los últimos dos años para poder tener la referencia a el año 2025. Están marcados en color rojo.

- ### **6.1. Bloque 1 - Málaga**

En cuanto a los datos descargados el porcentaje del tipo de viviendas descargada se encuentra en un 30% pisos - 70% casas. Con un porcentaje más similar en Marbella. En cuanto al número de viviendas que se publicitan con Parking incluido, mencionar que en el centro tienen un porcentaje menor. En el caso de pisos el número de anuncios con ascensores son similares. 
En el Análisis de Rentabilidad a la hora de recuperar el dinero invertido se ha podido ver que las viviendas de 1 habitación con uno o dos baños, con las viviendas con 2 habitaciones y 1 baño, son las que tiene tiempos de retornos más cortos. Por lo tanto, un ROE mayor. En el caso de Málaga en el anexo se puede diferenciar por los pisos por municipio que tienen ascensor o no.
Ahora voy a exponer el caso de que una pareja quisiese comprarse una vivienda. En la pestaña orientada a estos datos el tipo de vivienda representada son pisos de 1, 2 y 3 habitaciones. El salario que se utiliza para hacer el cálculo es salario medio de Andalucía. Con el planteamiento expuesto anteriormente, las personas tendrían que destinar más del 20% de su salario bruto en pareja los dos trabajando para un piso de una habitación y más del 30% para un piso de dos habitaciones.  En el caso de 3 habitaciones llegaría a ser más del 45% de sus salarios brutos.
El aumento del salario medio en Andalucía ha sido desde 2015 de un 23% o desde 2008 de un 31%. En comparación con el valor del metro cuadrado que ha subido un 128% desde el 2015. 

- ### **6.2. Bloque 2 - Sevilla **

En el caso de Sevilla es importante mencionas el % de viviendas descargadas, el 74% son viviendas del municipio de Sevilla y la relación con los datos generales de idealistas las viviendas del municipio son el 47%. Cuando nos fijamos en el alquiler, de los datos descargados es el 90%, del general un 72%. Siendo importante para entender mejor ahora los datos de pisos y viviendas, ya que la mayoría de las viviendas están en el municipio de Sevilla y el 86% en compra son pisos y el 99% en alquiler. Esto se repercute también en el muero de garajes incluidos en la compra o alquiler. 

Cuando hice el análisis de rentabilidad no excluye el tipo de vivienda casa, ya que me limitaba el poder estudiar los municipios fuera de Sevilla y el numero de casos por su limitada cantidad de viviendas y habitaciones. Las características son similares que, en Málaga, a diferencia del municipio de Sevilla donde sí que las viviendas con 2, 3, 4 e incluso las de 5 con un solo baño tienen una rentabilidad mejor. En comparación con las mismas habitaciones, pero con 2 baños, la rentabilidad de divide a la mitad.

Se puede observar que las viviendas de fuera de sevilla tienen un coste menor, en comparación a Málaga.  Si que las viviendas del municipio de Sevilla hay que llegar  destinar un porcentaje del 22% para las viviendas de 1 habitación y más del 23% para las de 2 habitaciones y hasta un 30.6% del salario bruto a las de 3 habitaciones.
El aumento del salario medio en Andalucía ha sido desde 2015 de un 23% o desde 2008 de un 31%. En comparación con la subida del precio de la vivienda en la provincia de Sevilla que ha subido un 40%. 

- ### **6.3. Bloque 3 - Madrid**

Los inmuebles que he descargado con web scraping en Madrid, siguen el mismo patrón que Sevilla, el porcentaje más alto se encuentra en la ciudad, pero en este caso, sí que hay un amplio número de viviendas fuera de las ciudades en ciertos municipios que permite su análisis en profundidad.

En Madrid como en Sevilla, también se puede observar un tiempo de retorno más bajo en los municipios externos. Esto se debe también a menor precio. En cuanto a los pisos de Madrid ciudad, los tiempos de retorno no bajan de los 20 años. Observando también los precios de las viviendas se puede prever que el comprar una vivienda ahora con una hipoteca y querer alquilarla puede llevarte a tener un ROE negativo. Siendo el momento en el que estamos a ser un mal momento para invertir. Se puede observar en idealista que los precios por metro cuadrado en los dos últimos meses han bajado, pudiendo ser el comienzo de una tendencia a la baja.

A diferencia con los bloques anteriores, este lo he realizado con Python.
Lo que me ha permitido realizar una serie de análisis, que con las otras herramientas no las había hecho. He realizado 2 correlaciones y 3 tipos de modelos predictivos, voy a exponer ahora:
- Correlación 1: filtre las viviendas por pisos y que se encontrasen dentro de Madrid municipio. Puse el precio como variable predictora y los resultados más importantes fueron los siguientes:
	- Metro cuadrado con un 0.85.
	- Habitaciones con 0.53.
	- Baños con un 0.72.
	- Planta con un 0.27.- 
	
- Correlación 2: no filtre la información, quise ver cómo se afectaba las viviendas casa al análisis. Puse el precio como variable predictora y los resultados más importantes fueron los siguientes:
	- Metro cuadrado con un 0.44.
	- Habitaciones con 0.45.
	- Baños con un 0.62.
	
Posterior a las correlaciones realice un bucle for gráficos seaborn, en el que diferencie el tipo de vivienda con hue = tipo de vivienda, en el que la variable predictora era el precio y analizar con el resto de columnas numéricas. En el primer grafico se representaba el precio y metros cuadrados, en los pisos se puede ver como el precio asciende cuantos más metros tiene la casa. En el caso de las casas se puede ver como los marcadores están orientados a la derecha y abajo-medio, indicando que los metros cuadrados no son tan influyentes en el precio. Lo mismo paso con las habitaciones y los baños de las casas no son variables tan influyentes como en los casos de los pisos. Los pisos con ascensor tienden a un mayor precio y que las casa casi ninguna o ninguna tiene ascensor.

En el siguiente bloque de código hago un bucle for para analizar las columnas categóricas con precio. Además, le añadí unas líneas de código para que me printease la mediana de las variables de cada columna. Como se podía reflejar he mencionado en el párrafo anterior, en este caso podemos ver que la mediana de los precios con ascensor es 80.000 más alto. Lo mismo sucede con las viviendas que dan al exterior e interior, y con las viviendas con un buen estado o buen estado/ reformar.
Los precios de los dúplex y áticos son similares, siendo el precio de los pisos 300.000 € más baratos. 

El último análisis que hice fue la regresión, hice primero un primer modelo de regresión lineal, paso a paso. Posteriormente realice tres modelos diferentes. Regresión lineal, random forest y Gradient Boosting. En el código puse una línea de subplot para que se representasen los tres gráficos uno al lado del otro.
Permitiéndome así compararlos mejor. Paso a exponer y explicar los resultados:
- Regresión Lineal: R2 = 0.685 | RMSE = 804,299
- Random Forest: R2 = 0.983 | RMSE = 187,898
- Gradient Boosting: R2 = 0.993 | RMSE = 118,272

Como se puede observar la regresión lineal es el modelo más simple y el que tiene un error cuadrático medio. Random forest predice un 98,3 del precio y tiene un RMSE de 187,898. Por último, esta Gradient Boosting, viendo su grafica y resultado comprendemos que el mejor, pero se debería comprobar si no está habiendo overfiting.

Mis conclusiones finales en cuanto a este proyecto son, que la metodología para obtener la información es web scraping, aunque tiene limitaciones y es más lenta que por API, pero la cantidad de información que te ofrece es mayor y te permite obtener mejores análisis. En cuanto las herramientas utilizarían las 3 en conjuntos. En cuanto a la rentabilidad de las viviendas se puede observar que las casas de municipios pequeños y con una y dos habitaciones son mas rentables en cuanto a tiempo de recuperación
Mi conclusión para la compra de una vivienda en pareja en España, que estamos en el peor momento de la historia de España, las personas no tienen capacidad ahorro y encima los precios de los alquileres y compras no han evolucionado al ritmo del salario. Provocando una disminución de la posibilidad ahorrar para comprar. El precio también se ha visto incrementado por la alta demanda, cada vez hay mas residentes y la construcción de viviendas no está aumentando a la par. Además, que cada vez hay más impuestos y se sube el sueldo pero no se suben las tablas de IRPF. Siendo este el mayor problema y no tanto que las personas no quieran ahorra. Se da en las ciudades pequeñas es más fácil obtener una vivienda y céntrica, pero si a haber una menor capacidad de desarrollo profesional debido a la falta de empresas. 

## **7. Proximos pasos**
Mis próximos pasos serían:
- Mejorar fallos cometidos en la obtención, limpieza y uso del código.
- Replicar el estudio en más profundidad por ciudad usando web scraping y usando la misma información en las tres herramientas.
- Replicarlos a más ciudades.
- Obtener información de diferentes plataformas para comparar precios y duplicar datos.
- Realizar el estudio, pero con alquileres espontáneos y comparar rentabilidad.
- Mejorar el análisis de LSTM. 

## **8. Contribuciones**
Si deseas contribuir a este proyecto, puedes enviar sugerencias a través de:
- **LinkedIn:** [www.linkedin.com/in/jacobo-pérez-ferreira-0937905b](www.linkedin.com/in/jacobo-pérez-ferreira-0937905b)
- **Email:** jacoboferreira91@gmail.com
