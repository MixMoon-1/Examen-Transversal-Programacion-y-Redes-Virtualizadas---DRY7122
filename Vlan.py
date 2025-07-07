# Pedir el número de VLAN
vlan = int(input("Ingrese el número de Vlan: "))

# Verificar si es VLAN normal
if vlan >= 1 and vlan <= 1005:
    print("Es una Vlan normal")

# Verificar si es VLAN extendida
if vlan >= 1006 and vlan <= 4094:
    print("Es una Vlan extendida")