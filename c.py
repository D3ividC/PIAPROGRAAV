# Instancias de TV
from PIA.B import TV, Celular, Licuadora


tv_sala = TV(tamaño="Grande", peso="10kg", altura="70cm", marca="Sony", pulgadas=65)
tv_sala.encender()
tv_sala.cambiar_canal(10)
tv_sala.ajustar_volumen(30)
tv_sala.apagar()

tv_dormitorio = TV(tamaño="Mediano", peso="5kg", altura="50cm", marca="LG", pulgadas=40)
tv_dormitorio.encender()
tv_dormitorio.cambiar_canal(5)
tv_dormitorio.ajustar_volumen(20)
tv_dormitorio.apagar()

# Instancias de Licuadora
licuadora_cocina = Licuadora(tamaño="Grande", peso="3kg", altura="40cm", marca="Hamilton Beach", capacidad="2 litros")
licuadora_cocina.encender()
licuadora_cocina.mezclar(["plátano", "fresa", "leche"])
licuadora_cocina.hacer_batido("mango")
licuadora_cocina.apagar()

licuadora_bar = Licuadora(tamaño="Pequeño", peso="1.5kg", altura="25cm", marca="Black+Decker", capacidad="1 litro")
licuadora_bar.encender()
licuadora_bar.mezclar(["piña", "naranja", "hielo"])
licuadora_bar.hacer_batido("fresa")
licuadora_bar.apagar()

# Instancias de Celular
celular_juan = Celular(tamaño="Pequeño", peso="150g", altura="15cm", marca="Samsung", modelo="Galaxy S20")
celular_juan.encender()
celular_juan.llamar("987654321")
celular_juan.enviar_mensaje("Amigo", "Hola, ¿cómo estás?")
celular_juan.tomar_foto()
celular_juan.apagar()

celular_ana = Celular(tamaño="Pequeño", peso="130g", altura="14cm", marca="Xiaomi", modelo="Redmi Note 10")
celular_ana.encender()
celular_ana.llamar("123456789")
celular_ana.enviar_mensaje("Familia", "Nos vemos en casa pronto.")
celular_ana.tomar_foto()
celular_ana.apagar()
