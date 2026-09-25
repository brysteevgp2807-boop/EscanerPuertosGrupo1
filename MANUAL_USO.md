Manual de uso: Escáner de Puertos de Red 
1. Requisitos para ejecutar el programa
Sistema Operativo: Windows, macOS o Linux.
Python : Descárgalo desde el sitio oficial (python.org).
Entorno de Desarrollo: Visual Studio Code (VS Code).
Git: Para clonar o subir el proyecto a GitHub.
2. Instalación 
Descarga el archivo de código o clona el repositorio de GitHub de tu grupo usando la terminal:   git clone <URL_DE_TU_ REPOSITORIO GITHUB>
Abre Visual Studio Code. 
Ve a  Archivo > Abrir carpeta y selecciona la carpeta donde guardaste el archivo scanner.py. 
El script utiliza la biblioteca socket, la cual viene preinstalada en Python, por lo que no necesitas instalar librerías externas mediante pip.
3. Cómo iniciar la aplicación 
 En VS Code, abre el archivo scanner.py. 
Abre la terminal integrada de VS Code presionando Ctrl + Ñ (o Ctrl + ~).
Ejecuta el comando: python _scanner.py 

4. Cómo ingresar la IP y seleccionar el rango de puertos. Una vez iniciado el programa, la terminal te solicitará los siguientes datos secuencialmente:
IP: Escribe la dirección IP del objetivo que deseas auditar ( TOCA COLOCAR LA IP ACTUAL  ejemplo 192.168.1.10 o 127.0.0.1 para tu propia máquina local) y presiona Enter. 
Desde: Escribe el número del puerto inicial (por ejemplo: 1) y presiona Enter. 
Hasta: Escribe el número del puerto final (por ejemplo: 100) y presiona Enter. 
  5. Cómo ejecutar el escaneo e interpretar resultados 
El escaneo se inicia automáticamente justo después de ingresar el puerto final. 
En tiempo real verás aparecer la línea Puerto X - ABIERTO únicamente para los puertos que respondan positivamente a la conexión TCP. 
Resumen final.  Al terminar el rango, el programa imprimirá el total de puertos revisados y cuántos de ellos resultaron vulnerables o abiertos. 
