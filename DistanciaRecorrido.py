from geopy.geocoders import Nominatim
from geopy.distance import geodesic


geolocator = Nominatim(user_agent="distancias")
transportes = {"auto": 100, "bus": 80, "avion": 800}
while True:
   o = input("Ciudad origen (s para salir): ")
   if o.lower() == "s": break
   d = input("Ciudad destino: ")
   mo = geolocator.geocode(o + ", Chile")
   md = geolocator.geocode(d + ", Argentina")
   if not mo or not md:
       print("Ciudad no encontrada.\n")
       continue
   print("Medios: auto, bus, avión")
   t = input("Transporte: ").lower()
   if t not in transportes:
       print("Medio no válido.\n")
       continue
   dist = geodesic((mo.latitude, mo.longitude), (md.latitude, md.longitude)).km
   dur = dist / transportes[t]
   print(f"\nDe {o} a {d}:")
   print(f"{dist:.2f} km | {dist * 0.621:.2f} mi | {dur:.2f} h en {t}\n")
