# Entregas de los Alpes - Monolito Solutions

Repositorio del Proyecto Principal: https://github.com/monolito-solutions/project

Este repositorio es parte del proyecto "Entregas de los Alpes", el cual está diseñado para manejar el inventario y las entregas de una empresa ficticia de productos alpinos. Este repositorio principal solo contiene un README, los microservicios actuales se encuentran en sus respectivos repositorios.

## Estructura del Repositorio

El repositorio está organizado en carpetas para cada uno de los microservicios que componen el sistema:

- **inbound**: servicio encargado de recibir los pedidos del cliente
- **inventory**: servicio encargado de actualizar los inventarios disponibles
- **outbound**: servicio encargado de la entrega de los productos
- **notifications-ui**: servicio encargado de notificar a los clientes sobre el estado de sus pedidos

Cada microservicio se desarrolló en su propio repositorio, por lo tanto puede encontrar los enlaces de los repositorios correspondientes a continuación:

- **inbound**: https://github.com/monolito-solutions/inbound
- **inventory**: https://github.com/monolito-solutions/inventory
- **outbound**: https://github.com/monolito-solutions/outbound
- **notifications-ui**: https://github.com/monolito-solutions/notifications-ui
- **bff**: https://github.com/monolito-solutions/bff
- **sagas**: https://github.com/monolito-solutions/sagas

### Contribuciones
Para este proyecto, cada integrante del grupo trabajó en un microservicio aparte. Las contribuciones de cada integrante se encuentra en la tabla a continuación:

|Nombre|Microservicios|Usuario Github|
|---|---|---|
|Juan Andrés Romero|Inbound, BFF, Sagas|ElReyZero|
|Andrés López|Inventory|alnodp|
|Juan Sebastián Alegría|Notifications UI, Sagas|zejiran|
|Johan Carvajal|Outbound|johanCarvajalAndes|

## Videos de Explicación
### - Entrega 1

- Explicación completa (Es el mismo video):
    - Youtube: https://youtu.be/eovWf5dlkoQ
    - Google Drive: https://drive.google.com/file/d/1cX5VKM-m-yrjy72Xhnx3cl9VAaH3pBrf/view?usp=sharing
- Tutorial de cómo correr el proyecto en un único ambiente (único servidor): https://youtu.be/1AatCaZghes

### - Entrega 2
- Video Completo:
    - Youtube: https://youtu.be/i9Xq85r8xDQ
    - Google Drive: https://drive.google.com/file/d/1cX5VKM-m-yrjy72Xhnx3cl9VAaH3pBrf/view?usp=sharing

## Despliegue

El proyecto "Entregas de los Alpes" utiliza Apache Pulsar como sistema de mensajería y bases de datos descentralizadas y únicas para cada microservicio. Estos se despliegan con Docker Compose en sus respectivos servidores.

### Recomendaciones

Se sugiere clonar los repositorios de los microservicios individualmente y trabajar en ellos de forma independiente en sus respectivos servidores.

Por lo tanto, es importante tener en cuenta que los microservicios no se despliegan en Docker y deben iniciarse individualmente con el comando ```python main.py``` en su respectiva carpeta.

Los archivos con la configuración de la base de datos y apache pulsar en cada microservicio son los siguientes:
- **Pulsar**: ```[servicio]/config/utils.py```
- **MySQL**: ```[servicio]/config/db.py```

#### Despliegue en servidores independientes
Si desea desplegar cada microservicio en un servidor diferente, puede hacerlo siguiendo los siguientes pasos:

1. Clonar el repositorio respectivo en cada servidor.
2. Desplegar Apache Pulsar en un servidor central con docker-compose.
3. Desplegar la base de datos MySQL en cada servidor con docker-compose.
4. Cambiar la configuración de los microservicios para que apunten al host de Apache Pulsar en el servidor central.
5. Ejecutar el comando ```python main.py``` o ```python3 main.py``` en cada servidor.


### Escenarios de Calidad
Los escenarios de calidad se explican en el video explicativo de la entrega 1. Alrededor del minuto 19:42