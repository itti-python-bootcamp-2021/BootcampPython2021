tele1 = "CHiQ Televisor Smart TV LED 32, Android 9.0, HD, WiFi, Bluetooth, Google Play Store, Google Assistant, Netflix, Prime Video, HDMI, USB"
tele2 = "Philips 70PUS7855/12 Ambilight Televisor 4K UHD de 70 Pulgadas (P5 Picture Engine, Asistente Alexa integrada, Smart TV"
tele3 = "Xiaomi Smart TV P1 50 Pulgadas (Frameless, UHD, Sintonizador Triple, Android 10.0, Prime Video, Netflix, Google Assistant, Compatible"
tele4 = "Sony BRAVIA KE-55XH90/P - Smart TV 55 pulgada, Full Array LED, 4K Ultra HD, Alto Rango dinámico (HDR), Android TV"
tele5 = "Samsung HD TV 24N4305 - Smart TV de 24, HDR, Ultra Clean View, PurColor, Micro Dimming Pro y Color Negro."
tele6 = "Samsung 4K UHD 2021 55AU8005- Smart TV de 55 con Resolución Crystal UHD, Procesador Crystal UHD, HDR10+, Motion Xcelerator"

#Solicitar al usuario un texto libre referente a la televisión que desea: "Quiero una televisión 4K con UHD y que tenga Netflix"
#Mostrar la televisión que más se aproxima a lo que está buscando.
#Nota la función set(lista) devuelve un conjunto a partir de la lista que se le pasa como parámetro
teles = [tele1, tele2, tele3, tele4, tele5, tele6]
lista_conjuntos_teles = [set(tele.replace(",","").upper().split()) for tele in teles]
#print(lista_conjuntos_teles)
deseo = input("Introduce cómo quieres que sea tu televisor:")




#tele6_set = {"Samsung","4K","UHD","2021","55AU8005","Smart", "de", "55", "con", "Resolución", "Crystal", "UHD"}
#palabras_clave = {"TV","UHD","4K"}

#print(tele6_set.intersection(palabras_clave))
