def ordenador_coches_extra(coche):
    factor = coche[1]/1000 + coche[2] + coche[3]/20
    print(coche[0],"Factor:",factor)
    return factor

coche1 = ["SAAB", 15000, 100, 2000]
coche2 = ["KIA", 12000, 74, 1400]
coche3 = ["FERRARI", 200000, 300, 22000 ]

coches=[coche1, coche2, coche3]

coches.sort(key=ordenador_coches_extra)

print(coches)
