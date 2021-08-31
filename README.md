# Data-extraction-from-Social-Networks

**1. Twitter (Extracción y envío del mismo hacia CouchDB)**
   - Para realizar la extracción de datos de Twitter se debe tomar en cuenta que se debe poseer credenciales, de lo contrario será un poco más complicado realizar la actividad. Además, si se desea obtener datos de algún sitio en específico se lo hará mediante la página web: https://boundingbox.klokantech.com/ . En la parte inferior izquierda existe la opción del tipo de formato que retornará la ubicación, para esta ocasión se utilizó la de formato CSV, se copiará este archivo csv y se lo pegará en la línea 45 del código twitter.py (dentro de los corchetes). Por otra parte, si se desea extraer datos de algún tema en común se debe escribir dicho tema en la línea 45. **Tomar en cuenta que es mejor realizar uno de estos a la vez**.
Una vez hallado los tuits se los enviarán hacia la base de datos de CouchDB (línea 37 hasta 41)

**2. Facebook (Extracción y envío del mismo hacia MongoDB)**
   - Se importan las bibliotecas que se requerirán para realizar dicha petición, tomar en cuenta que si se tiene enlazada la cuenta de Facebook ya sea con gmail o el numero de celular, se enviará un mensaje de confirmación de este procedimiento a realizar.
En la línea 35 se especificará el numero de paginas que en que se buscará la información, para que no exista tanta información en las paginas se colocó el número 3. Este traerá como resultado la fecha, el texto, likes, comentaros, etc., de la publicación. **Todo esta extracción se la guardará en un archivo de formato json, dado que MongoDB admite formatos Json y CSV.**

**3. Web Scraping (Extracción de datos de una pagina web en particular y envío del mismo hacia MongoDB)**
   - Cuando se hace web Scraping se debe tene runa pagina web base de donde se extraerán los datos, la pagina de "El comercio" será en esta ocasión. Además de que la información extraída será almacenada en arrays, y después guardada en un formato Json. Finalmente se lo enviará a MongoDB.

**4. Tik Tok (Extracción de datos de cuentas oficiales mediante el símbolo del sistema)**
   - Con respecto a la obtención de datos de tik tok se utilizó la consola de windows en base a algunas librería que permiten tener acceso a los datos de esta red social. La cuenta en esta ocasión será la de **steffy.aradillas**. Una vez que se ingrese a la consola y en la carpeta en donde se desea guardar la info se deberá escribir las siguientes combinaciones:
   - *Nota: Si el usuario no desea presionar Enter podría escribir a su gusto los campos necesarios allí.*
     - *npm init* , este inicializa un proyecto, la cual tendrá un servidor, archivos de configuración e inicializa el entorno. 
       - package name: (tiktok) **nombre aleatorio***
       - version: (1.0.0)g **teclear *Enter***
       - description: **teclear *Enter***
       - entry point: (index.js) **teclear *Enter***
       - test command: **teclear *Enter***
       - git repository: **teclear *Enter***
       - keywords: **teclear *Enter***
       - author: **teclear *Enter***
     - *npm install calculator*, el npm es un administrador de paquetes; posee para Word, Excel, gif, mp3, etc.(tiene página oficial para descargarlos).
     - *npm install -g calculator*, el -g significa que se instalará en todo el entorno de programación.
     - *node-calc*
     - *npm i -g tiktok-scraper*    
     - Finalmente se escribe el nombre la cuenta oficial a buscar con el tipo de formato a guardarse, dado que se lo enviará a otra base de datos se lo pondra como csv: *tiktok-scraper user olympicteamisrael -t csv*


**5. Envío de los datos de Twitter a MongoDB (CouchDB hacia MongoDB)**
   - Descripción detallada del procedimiento en *7Envío de los datos de Twitter a MongoDB (CouchDB hacia MongoDB).md*
  
**6. Envío de los datos de Tik Tok a MongoDB (MYSQL hacia MongoDB)**
   - Como ya se tenía la información de la cuenta de TikTok en csv es sencillo subirlo a MongoDB, practicamente son los mismos pasos de importación del literal anterior. Así se vería la importación del mismo:
     - ![1](https://user-images.githubusercontent.com/66731201/130114155-34148269-f4d3-4655-b7d1-a4e2c91ffa15.png) 
     - Finalizando así este apartado.
         
**7. Enviar base de datos de MongoDB a MongoDB Atlas**
   - De acuerdo a la base de datos del literal **5** se procederá a enviarlo a MongoDB Atlas. 
     - Se exportará la información dando clic en icono que permite dicha función, y se lo guarda con un nombre en específico (ya sea con filtro o toda la base en sí y un formato de csv o json).
     - Una vez que ya se haya creado un clúster en Mongo Atlas, se irá hacia *Collecions* y debajo de esto existe un *+ Create data base*, se pondrá el nombre de la collección y la base de datos.
       - 1. ![atlas2](https://user-images.githubusercontent.com/66731201/131422352-ed6a3600-109b-435b-a095-73a2eb2d5451.png)
       - 2. ![atlas](https://user-images.githubusercontent.com/66731201/131422116-1c8942cc-0dc7-4dca-9e25-e48bfd138d77.PNG)
       - clic en *INSERT DOCUMENT*, mediante un editor de texto se abre el documento exportado de MongoDB, se copia aquel archivo y se lo pegará.
         - ![twitter1](https://user-images.githubusercontent.com/66731201/131422852-cbb5c685-be99-45ab-bc57-aa329b7bee75.PNG)
         - Finalmente se habrá culminado el procedimiento y presentando en pantalla la misma base de datos
           - ![fin](https://user-images.githubusercontent.com/66731201/131423047-d508fbfd-0385-4129-be01-d374407fbe19.PNG)


  
