# pipeline-project

Pipeline es un programa escrito en Python donde el usuario puede consultar información de los vuelos de su próximo viaje.
Para recibir esta información simplemente necesita introducir la ciudad de origen y la ciudad de destino, de esta forma
obtendrá los próximos vuelos más baratos. Además, tiene la opción de recibir información de los mejores hoteles en su país de destino.

La aplicación consulta la api de Amedeus para obtener datos sobre los vuelos.
Por otro lado, para conseguir datos de los hoteles se consulta un DataSet obtenido de Kaggle.

# Información para ejecutar el proyecto
Para ejecutar el código es necesario instalar Amadeus desde la consola: pip install amadeus
También necesitarás obtener las api keys. En los enlaces que dejo más abajo, encontrás una url que te llevará a la guía
para desarrolladores de Amadeus, ahí están todos los pasos a seguir.

# Enlaces
Api:
    https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335
    https://amadeus4dev.github.io/amadeus-python/index.html
DataSet:
    https://www.kaggle.com/harmanpreet93/hotelreviews
