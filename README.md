# Entregas de los Alpes - Monolito Solutions

Este repositorio es parte del proyecto "Entregas de los Alpes", el cual está diseñado para manejar el inventario y las entregas de una empresa ficticia de productos alpinos. Este repositorio principal reúne los diferentes microservicios que componen el sistema.

## Estructura del Repositorio

El repositorio está organizado en carpetas para cada uno de los microservicios que componen el sistema:

- **inbound**: servicio encargado de recibir los pedidos del cliente
- **inventory**: servicio encargado de actualizar los inventarios disponibles
- **outbound**: servicio encargado de la entrega de los productos
- **notifications-ui**: servicio encargado de notificar a los clientes sobre el estado de sus pedidos

Cada microservicio se desarrolló en su propio repositorio y se integra en este repositorio principal como submódulos de Git. Si necesita trabajar en uno de los microservicios individualmente, puede hacer clic en el enlace del repositorio correspondiente a continuación:

- **inbound**: https://github.com/monolito-solutions/inbound
- **inventory**: https://github.com/monolito-solutions/inventory
- **outbound**: https://github.com/monolito-solutions/outbound
- **notifications-ui**: https://github.com/monolito-solutions/notifications-ui

## Despliegue

El proyecto "Entregas de los Alpes" utiliza Apache Pulsar como sistema de mensajería y bases de datos descentralizadas y únicas para cada microservicio. Estos se despliegan con Docker Compose en sus respectivos servidores.

### Recomendaciones

Se sugiere clonar los repositorios de los microservicios individualmente y trabajar en ellos de forma independiente en sus respectivos servidores.

Por lo tanto, es importante tener en cuenta que los microservicios no se despliegan en Docker y deben iniciarse individualmente con el comando ```python main.py``` en su respectiva carpeta.

Los archivos con la configuración de la base de datos y apache pulsar son los siguientes:
- **Pulsar**: ```[servicio]/config/utils.py```
- **MySQL**: ```[servicio]/config/db.py```


#### Despliegue en servidores independientes
Si desea desplegar cada microservicio en un servidor diferente, puede hacerlo siguiendo los siguientes pasos:

1. Clonar el repositorio respectivo en cada servidor.
2. Desplegar Apache Pulsar en un servidor central con docker-compose.
3. Desplegar la base de datos MySQL en cada servidor con docker-compose.
4. Cambiar la configuración de los microservicios para que apunten al host de Apache Pulsar en el servidor central.
5. Ejecutar el comando ```python main.py``` en cada servidor.

#### Despliegue en único servidor
Si a pesar de lo descrito anteriormente desea desplegar todos los microservicios en un único servidor, puede hacerlo siguiendo los siguientes pasos:

1. Clonar el repositorio principal en el servidor
2. Desplegar Apache Pulsar y la base de datos MySQL con Docker Compose
3. Cambiar la configuración de los microservicios para que apunten a la base de datos MySQL del servidor
4. Entrar en la carpeta de cada microservicio y ejecutar el comando ```python main.py```

# Video de Explicación - Entrega 1

Video: https://youtu.be/eovWf5dlkoQ

## Abrir en GitPod
<a href="https://gitpod.io/#https://github.com/monolito-solutions/project" style="padding: 10px;">
    <img src="https://gitpod.io/button/open-in-gitpod.svg" width="150" alt="Push" align="center">
</a>
