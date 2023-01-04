# NBA_Statistics

El objetivo de los programas incluidos en este repositorio será crear un PDF en el que se exponga el análisis realizado sobre las principales medidas estadísticas y predicción de resultados futuros de un equipo concreto de la NBA a elección propia.

El equipo elegido ha sido el 'Boston Celtics', cuyo logo también incluimos para la posterior elaboración del pdf final.

El orden de ejecución será el siguiente:

- Antes de comenzar a ejecutar los programas , el usuario deberá encargarse de instalar las librerías especificadas en el requirements.txt para garantizar el buen funcionamiento del proyecto. Además, se deberá crear una cuenta propia en la API facilitada en el archivo API_final.py (https://v2.nba.api-sports.io). Una vez se haga se introducirá el ID propio de las credenciales en la linea de XXX... del archivo config.txt.

- En primer lugar se ejecutará el archivo scrap.py, el cual utilizará técnicas de webscrapping para analizar el contenido del html seleccionado (en este caso una web de predicciones sobre los resultados de los partidos de la NBA). El análisis consistirá en extraer de la página web los próximos encuentros entre equipos de la NBA y la predicción de sus resultados, guardando todo ello finalmente en un archivo .csv de nombre 'prediccion.csv'.

- Una vez se haya creado el archivo 'prediccion.csv', procederemos a ejecutar el último archivo, API_final.py, cuyo resultado final será el pdf del que hablábamos al principio, incluyendo tanto estadísticas generales del equipo durante la temporada 22-23 como los datos obtenidos mediante la elaboración del análisis de webscrapping. Para ejecutar este archivo incluiremos el id propio de cada usuario a la hora de acceder a la API.

Funcionamiento en profundidad:

 o scrap.py : Creado con la estructura de una ETL, este archivo cumple el objetivo de analizar una página web de predicciones relativas a los próximos partidos de la NBA. Para ello utilizaremos técnicas de webscrapping y librerías como beautifulsoup , analizando los datos necesarios y guardándolos en un DataFrame que posteriormente convertiremos en un archivo .csv
 
 o API_final.py : También con la estructura de una ETL, este archivo finalizará el trabajo extrayendo los datos necesarios sobre el equipo elegido de una API concreta. Una vez lo haga, se transformarán los datos de manera que sea más fácil trabajar con ellos. Por último, creará varias gráficas y tablas de importancia para el análisis de la posición global del equipo, fortalezas y puntos débiles. Además, incluirá la información extraida mediante scrap.py relativa al equipo seleccionado y elaborará un PDF completo incluyendo todos los datos previamente calculados y filtrados.
 
 
 Como extra incluimos la versión del archivo API_final.py en notebook de Jupyter, ya que se podría ejecutar el programa con ambos archivos.
