import socket


def escanear_puerto(ip, puerto):
    try:
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.settimeout(0.5)

        resultado = socket_obj.connect_ex((ip, puerto))
        socket_obj.close()

        return resultado == 0

    except socket.error:
        return False


print("================================")
print("       ESCÁNER DE PUERTOS")
print("================================")

ip = input("IP: ")
puerto_inicial = int(input("Desde: "))
puerto_final = int(input("Hasta: "))

print("\nEscaneando...\n")

puertos_abiertos = 0
puertos_analizados = 0

for puerto in range(puerto_inicial, puerto_final + 1):

    if escanear_puerto(ip, puerto):
        print(f"Puerto {puerto} - ABIERTO")
        puertos_abiertos += 1

    puertos_analizados += 1

print("\n================================")
print("          RESUMEN")
print("================================")
print(f"Puertos analizados: {puertos_analizados}")
print(f"Puertos abiertos: {puertos_abiertos}")