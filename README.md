# Tercera_Pre_Entrega_GutierrezRafaella
Tercera pre-entrega de curso de Python en CoderHouse Comision 54955

# Consigna
Desarrollar una WEB Django con patrón MVT subida a Github.

1. Herencia de HTML.
Se observa en el VSC, carpeta templates/AppOne el archivo padre.html que realizara la herencia a los hijos inicio.html, productos.html, servicios.html y clientes.html

2. Por lo menos 3 clases en models.
Se trabajo con 3 clases: Productos, Servicios y Clientes.

3. Un formulario para insertar datos a todas las clases de tu models.
En la barra de navegacion de la plataforma podras encontrar botones, del mismo nombre de las clases, que llevaran a un formulario donde podras ingresar informacion.

4. Un formulario para buscar algo en la BD
Podras acceder a este formulario mediante un boton encontrado visualmente en el centro de la plataforma que indica 'Busca por categoria!'
Alli podras buscar un listado de productos o servicios que se encuentren dentro de la categoria ingresada.

5. Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades

# Uso de la plataforma
Superuser: rafaella
pass: rafa12345

limited user: User1
pass: user12345

Una vez corriendo el server ingresar a http://127.0.0.1:8000/AppOne/

Hacer click en 'Productos' - Ingresar nombre de cualquier producto y su categoria en el formulario - Click en 'Guardar'

Hacer click en 'Servicios' - Ingresar nombre de cualquier servicio y su categoria en el formulario -  Click en 'Guardar'

Hacer click en 'Clientes' - Ingresar nombre completo, DNI, email y fecha de compra en el formulario - Click en 'Guardar'

*Importante: la fecha de compra se debe añadir de la siguiente manera 'yyyy-mm-dd', es decir, año completo guion medio mes guion medio y dia segun la estructura.

Para realizar una busqueda, hacer click en 'Busca por categoria!', puedes ingresar una el nombre de una categoria que hayas ingresado o alguna de las siguientes:

Para desplegar productos ingresa las siguiente categorias:
- Tecnologia
- Hogar
- Deco
- Cocina

Para desplegar servicios ingresa las siguientes categorias:
- Digital Marketing
- Management
- Consulting
- Data

Estos son unos ejemplos de informacion ya ingresada, con el fin de cumplir con la idea de la plataforma:

'One Space, productos y servicios On-demand en un solo lugar'

