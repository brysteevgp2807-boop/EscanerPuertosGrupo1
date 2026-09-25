# Escáner de Puertos de Red

## Descripción

Este proyecto consiste en el desarrollo de un escáner de puertos de red utilizando Python y la biblioteca `socket`. La aplicación permite ingresar una dirección IP, establecer un rango de puertos y realizar un análisis para identificar cuáles se encuentran abiertos.

El programa fue desarrollado con fines educativos para comprender conceptos básicos de redes, comunicación mediante sockets y reconocimiento de servicios activos.

## Tecnologías utilizadas

* Python
* PyCharm
* Biblioteca `socket`
* GitHub

## Funcionalidades

El programa permite:

1. Ingresar una dirección IP.
2. Ingresar un puerto inicial.
3. Ingresar un puerto final.
4. Realizar el escaneo del rango seleccionado.
5. Mostrar los puertos abiertos.
6. Mostrar un resumen de los resultados.

## Requisitos

Para ejecutar el programa se necesita:

* Python 3.x.
* PyCharm o cualquier otro entorno de desarrollo compatible con Python.
* Una máquina propia, máquina virtual o laboratorio autorizado para realizar las pruebas.

No es necesario instalar `socket`, debido a que forma parte de la biblioteca estándar de Python.

## Instalación

### 1. Descargar o clonar el proyecto

El proyecto puede descargarse desde GitHub o clonarse mediante:

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Abrir el proyecto

Abrir la carpeta del proyecto utilizando PyCharm.

### 3. Ejecutar el programa

Abrir el archivo:

```text
main.py
```

y seleccionar:

```text
Run → Run 'main'
```

## Uso del programa

Al iniciar la aplicación se solicitarán los siguientes datos:

```text
IP: 127.0.0.1
Desde: 1
Hasta: 100
```

La dirección IP corresponde al equipo que se desea analizar y el rango establece los puertos que serán revisados.

Después de ingresar los datos, el programa inicia automáticamente el escaneo.

## Ejemplo de ejecución

```text
================================
       ESCÁNER DE PUERTOS
================================
IP: 127.0.0.1
Desde: 1
Hasta: 100

Escaneando...

Puerto 80 - ABIERTO
Puerto 86 - ABIERTO

================================
          RESUMEN
================================
Puertos analizados: 100
Puertos abiertos: 2
```

## Registro de prueba

| Elemento         | Resultado                                                                                                                                     |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| IP utilizada     | 127.0.0.1                                                                                                                                     |
| Rango de puertos | 1 – 100                                                                                                                                       |
| Puertos abiertos | 80, 86                                                                                                                                        |
| Observaciones    | Se realizó el escaneo sobre el equipo propio mediante la dirección IP local. Se analizaron 100 puertos y se identificaron 2 puertos abiertos. |

## Interpretación de resultados

Un puerto identificado como **ABIERTO** indica que el equipo respondió al intento de conexión realizado por el programa y que existe un servicio escuchando en dicho puerto.

La cantidad de puertos abiertos puede variar dependiendo de los servicios que se encuentren activos en el equipo analizado.

## Consideraciones de seguridad

El escáner debe utilizarse únicamente sobre:

* Equipos propios.
* Máquinas virtuales propias.
* Laboratorios autorizados.

No se debe realizar el escaneo sobre equipos o redes de terceros sin autorización.

## Estructura del proyecto

```text
EscanerPuertos/
│
├── main.py
└── README.md
```

## Autor

Proyecto académico desarrollado para el estudio de redes y programación en Python.
