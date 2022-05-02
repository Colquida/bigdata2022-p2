# bigdata2022-p2

![image](https://user-images.githubusercontent.com/83324055/166158021-9218aea0-d009-4e72-bcbd-dcee883cc655.png)

Segundo examen parcial de Big Data - Universidad Sergio Arboleda.

Fecha: 1 de Mayo de 2022
Autores: Rubén Alexis Núñez Montaña, Jonathan Alexander Torres Benítez

Para este examen se requiere el scraping diario de dos portales web de noticias utilizando Zappa a través de la plataforma de Amazon Web Services (AWS). Se eligieron las páginas https://www.bbc.com/ y https://www.nejm.org/. La carpeta  [lambda_parcial/](https://github.com/Colquida/bigdata2022-p2/tree/main/lambda_parcial) contiene los scripts usados para extraer el contenido de las páginas en HTML ([app.py](https://github.com/Colquida/bigdata2022-p2/blob/main/lambda_parcial/app.py)) y subirlos a un bucket. 

![image](https://user-images.githubusercontent.com/83324055/166157864-6501334f-2837-4a47-bb84-01465287e312.png)

A partir de allí se genera un trigger que ejecuta una función lambda que contiene el siguiente script: ([app2.py](https://github.com/Colquida/bigdata2022-p2/blob/main/lambda_parcial/app2.py)), el cual realiza el procesamiento del contenido almacenado en el Bucket, lo procesa y genera el correspondiente archivo csv bajo una rutina de 24 horas. 

![image](https://user-images.githubusercontent.com/83324055/166158332-de741c5d-b6ca-4838-8258-821ff8a1f2cf.png)

Ahora, note uno de los archivos .csv que se han generado tras el procesamiento del scraping.

![image](https://user-images.githubusercontent.com/83324055/166157949-8d7fc6c4-41e4-4729-94cd-da05d769add6.png)

Al poseerlo, se puede utilizar el módulo de Hive para crear remotamente la tabla desde la cual se podrán realizar consultas. 

![creación de tabla](https://user-images.githubusercontent.com/83324055/166157174-6063632a-f818-4cbf-9e84-ce98353a25d5.jpg)

Es esencial el paso de repararla, crear las particiones, referencias a columnas, tipos de columnas y el bucket desde el cual se hará la extracción.

![repair table](https://user-images.githubusercontent.com/83324055/166157178-6dfd0fc0-8961-43be-9bee-d5df268e7da4.jpg)

Finalmente, se accede al módulo de Presto y se pueden ejecutar consultas. 

![select usando presto](https://user-images.githubusercontent.com/83324055/166157185-0bf7f31e-dba7-44ad-9192-b77dacd9226d.jpg)

Si tienen alguna duda o comentario que permita mejorar, con gusto estaremos atentos. Pueden escribirnos a ruben.nunez01@correo.usa.edu.co, jonathana.torres@correo.usa.edu.co


