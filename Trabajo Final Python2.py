import pickle, sys, os, random


tickets = {}

def menu_principal():
    print("\n--Hola bienvenidos al sistema de Tickets--")
    while True:
        #print("/n--Hola bienvenidos al sistema de Tickets--")
        print("----------------")
        print("Menú Principal")
        print("----------------")
        print("1. Generar Ticket")
        print("2. Leer Ticket")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            alta_ticket()
        elif opcion == '2':
            leer_ticket()
        elif opcion == '3':
            if input("¿Estás seguro que deseas salir? (si/no): ").lower() == 'si':
                print("\nSaliendo del sistema...")
                print("-------------------------------------------")
                print("Gracias por utilizar el sistema de Tickets.")
                print("-------------------------------------------")
                break 
                   

def alta_ticket():
    print("---------------------------------------------------")
    print("--ingrese sus datos para Generar un nuevo Tickets--")
    print("---------------------------------------------------")
    nombre = input("ingrese su nombre :")
    sector = input("ingrese el sector de su servicio : ")
    asunto = input("ingrese su asunto : ")
    problema = input("ingrese su problema : ")
    numero_ticket = random.randint(1000, 9999)

    tickets[numero_ticket] = {
        'nombre': nombre,
        'sector': sector,
        'asunto': asunto,
        'problema': problema
    }

    print(f"\nTicket generado: {numero_ticket}")
    print(f"Nombre: {nombre}, Sector: {sector}, Asunto: {asunto}, Problema: {problema}")
    print("--Recuerda tu número de ticket--")

    if input("¿Deseas crear otro ticket? (si/no): ").lower() == 'si':
        alta_ticket()

def leer_ticket():
    numero_ticket = int(input("Introduce el número de ticket: "))
    print("---------------------------------------------------")
    print("--Se Genero el siguiente Tickets--")
    print("---------------------------------------------------")
    
    
    if numero_ticket in tickets:
        ticket = tickets[numero_ticket]
        print(f"\nTicket encontrado: {numero_ticket}")
        print(f"Nombre: {ticket['nombre']}, Sector: {ticket['sector']}, Asunto: {ticket['asunto']}, Problema: {ticket['problema']}")
    else:
        print("Ticket no encontrado.")

    if input("¿Deseas leer otro ticket? (si/no): ").lower() == 'si':
        leer_ticket()

# Iniciar el programa
menu_principal()