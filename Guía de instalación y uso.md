# Guía de instalación y uso 
Tecnológico de Costa Rica
Campus Tecnológico Central Cartago
Escuela de Ingeniería en Computación
IC4302 – Bases de datos II
Profesor: Gerardo Nereo Campos Araya
Estudiantes: 
Kendall Fabián Guzmán Ramírez - 2019076561
Carlos Eduardo Leiva Medaglia - 2021032973
Kenneth Palacios Molina       - 2020035407
Jose Pablo Quesada            - 2020211670
Iván Solís Ávila              - 2018209698
Primer semestre del 2023
Entrega: viernes 24 de febrero del 2023 – Semana 3



## Sección 1: Iniciar el cluster de Minikube
Pasos:
 - Asegurarse de tener instalado minikube y kubectl en el sistema. Si no se tiene, se puede descargar desde los respectivos sitios oficiales.
 - Iniciar Minikube en la terminal ejecutando  el comando "minikube start".
## Sección 2: Entrar a Lens
Pasos:
 - Se debe ejecutar lens y entrar en la sección de clusters, específicamente en el cluster de minikube.
 - En esta aplicación se puede monitorear el estado de pods, charts, servicios, contraseñas por medio de secrets, etcétera.
## Sección 3: Configurar detalles dependiendo de los recursos disponibles (opcional)
Pasos:
 - Si se poseen recursos limitados para el procesamiento de los pods, es recomendable deshabilitar las bases de datos que no se vayan a monitorear en esa prueba en específico.
 - Se deshabilitan los servicios de la base de datos por medio del values.yaml que se encuentra en la carpeta databases la cual se encuentra en la carpeta charts de la tarea, colocando "enabled:false" en la indentación del servicio que se desea deshabilitar.
## Sección 4: Instalar los Helm charts y construir sus dependencias
Pasos:
- Para esta sección se debe ubicar el kernel en el path "Tarea_corta_1_BDII\charts\" de la carpeta de la tarea. 
- Cuando se encuentre en la carpeta "charts" se debe otorgar los permisos de ejecución al archivo "install_charts.sh" por medio del comando "chmod +x install_charts.sh".
- Con los permisos otorgados se debe llamar al archivo de instalación de los charts y de construcción de sus dependencias llamado "install_charts.sh" escribiendo lo siguiente: "./install_charts.sh", este archivo se encarga de por medio de helm construir las dependencias para los diferentes charts que se utilizarán en este proyecto y de instalar los charts generando servicios hospedados localmente.
## Sección 5: Verificar detección de la base de datos desde el API de Prometheus
Pasos:
- Ingresar a Lens.
- Ingresar a la sección de  "services".
- Realizar una operación de forward en el servicio "monitoring-stack--prometheu-prometheus".
- Desde el navegador en la API de prometheus se debe ingresar a "status" y aquí se observaran las bases de datos que se están monitoreando.
## Sección 6: Ingresar al dashboard de la base de datos que se desee monitorear
Pasos:
- Ingresar a Lens.
- Ingresar a la sección de  "services".
- Realizar una operación de forward en el servicio "grafana-service".
- Desde el API de grafana se debe hacer click en los cuadrados ubicados en la parte izquierda, esto abrirá una ventana con los dashboards disponibles.
- Se debe elegir el dashboard de la base de datos que se desea monitorear y que anteriormente se verificó que prometheus estaba monitoreandola.
## Sección 7: Ingresar queries a la base de datos por medio de Gatling
Pasos:  
- Ingresar a la carpeta de descarga de gatling
- Tomar el archivo Prueba.scala del documento enviados e insertarlo dentro de la ruta  ./user-files/simulations
- Ejecutar el archivo Gatling.sh en el caso de ejecutarse en linux o gatling.bat en el caso de ser windows
- Presionar el boton numero 1 (opcion: run the simulation locally)


## Sección 8: Observación de métricas

