def preparar_panqueque(ingredientes, sarten):
    print("||___________Preparando el panqueque____________||")
    print("Ingredientes:", ingredientes)
    print("Sartén:", sarten)
    print("Mezclando los ingredientes...")
    print("Cocinando el panqueque en la sartén...")
    print("Listo! Tu panqueque está listo.")

ingredientes = ["harina",
                "huevo",
                "leche",
                "azúcar",
                "aceite"]
sarten = "Sartén antiadherente"
preparar_panqueque(ingredientes, sarten)


# Nueva funcion
def cocinar_panqueque(tamaño_panqueque, tiempo_cocción):
    print(f"Cocinando un panqueque de {tamaño_panqueque} pulgadas durante {tiempo_cocción} minutos...")
    print("El panqueque está cocinándose...")
    print("El panqueque está listo!")
    return f"Tu panqueque de {tamaño_panqueque} pulgadas está listo para servir!"

print(cocinar_panqueque(10, 5))