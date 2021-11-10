"""
Ricardo
    - Torrelodones
    - Saab
        - 2000cc
        - 150cv
Mohamed
    - Barcelona
    - Peugeot
        - 1800cc
        - 125cv
Fernando
    - Alcorcón
    - Kia
        - 1400cc
        - 74cv
"""
flota = [["Ricardo", "Torrelodones",["Saab",2000,150]], ["Mohamed","Barcelona",["Peugeot",1800,125]], ["Fernando","Alcorcón",["Kia",1400,74]]]
print("CC del coche de Mohamed:",flota[1][2][1])
print("Marca del coche de Ricardo:",flota[0][2][0])
