# Data-extraction-from-Social-Networks
**1. Twitter(extracción y envío del mismo hacia CouchDB)**
   - Para realizar la extracción de datos de Twitter se debe tomar en cuenta que se debe poseer credenciales, de lo contrario será un poco más complicado realizar la actividad. Además, si se desea obtener datos de algún sitio en específico se lo hará mediante la página web: https://boundingbox.klokantech.com/ . En la parte inferior izquierda existe la opción del tipo de formato que retornará la ubicación, para esta ocasión se utilizó la de formato CSV, se copiará este archivo csv y se lo pegará en la línea 45 del código twitter.py (dentro de los corchetes). Por otra parte, si se desea extraer datos de algún tema en común se debe escribir dicho tema en la línea 45. **Tomar en cuenta que es mejor realizar uno de estos a la vez**.
Una vez hallado los tuits se los enviarán hacia la base de datos de CouchDB (línea 37 hasta 41)



**2. Facebook(extracción y envío del mismo hacia MongoDB)**
   - Se importan las bibliotecas que se requerirán para realizar dicha petición, tomar en cuenta que si se tiene enlazada la cuenta de Facebook ya sea con gmail o el numero de celular, se enviará un mensaje de confirmación de este procedimiento a realizar.
En la línea 35 se especificará el numero de paginas que en que se buscará la información, para que no exista tanta información en las paginas se colocó el número 3. Este traerá como resultado la fecha, el texto, likes, comentaros, etc., de la publicación. **Todo esta extracción se la guardará en un archivo de formato json, dado que MongoDB admite formatos Json y CSV.**

**3. Web Scraping(Extracción de datos de una pagina web en particular y envío del mismo hacia MongoDB)**

Cuando se hace web Scraping se debe tene runa pagina web base de donde se extraerán los datos, la pagina de "El comercio" será en esta ocasión. Además de que la información extraída será almacenada en arrays, y después guardada en un formato Json. Finalmente se lo enviará a MongoDB.

**4. Tik Tok(Extracción y envío del mismo hacia MySQL)**

Con respecto a la obtención de datos de tik tok se utilizó la consola de windows en base a algunas librería que permiten tener acceso a los datos de esta red social. La cuenta en esta ocasión será la de **olympicteamisrael**.
Una vez que se ingrese a la consola y en la carpeta en donde se desea guardar la info se deberá escribir las siguientes combinaciones:
- *npm init*, este inicializa un proyecto, la cual tendrá un servidor, archivos de configuración e inicializa el entorno.
package name: (tiktok) **nombre aleatorio***
version: (1.0.0)g **teclear *Enter***
description: **teclear *Enter***
entry point: (index.js) **teclear *Enter***
test command: **teclear *Enter***
git repository: **teclear *Enter***
keywords: **teclear *Enter***
author: **teclear *Enter***
Si el usuario no desea presionar *Enter* podría escribir a su gusto los campos necesarios allí.
- *npm install calculator*, el npm es un administrador de paquetes; posee para Word, Excel, gif, mp3, etc.(tiene página oficial para descargarlos).
- *npm install -g calculator*, el -g significa que se instalará en todo el entorno de programación.
- *node-calc*
- *npm i -g tiktok-scraper*    
- Finalmente se escribe el nombre la cuenta oficial a buscar con el tipo de formato a guardarse, dado que se lo enviará a otra base de datos se lo pondra como csv *tiktok-scraper user olympicteamisrael -t csv*

6. a


  
