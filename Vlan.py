vlan = int(input("Ingrese el número de VLAN: "))



if vlan >= 1 and vlan <= 1005:
    print("Es una VLAN normal")
elif vlan >= 1006 and vlan <= 4094:
    print("Es una VLAN extendida")