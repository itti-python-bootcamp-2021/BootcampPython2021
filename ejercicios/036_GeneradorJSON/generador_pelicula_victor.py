import json

peliculas = {
    "El Resplandor": {
        "Director": "Kubrick",
        "Anyo": 1980,
        "Reparto": [
            {"Nombre": "Jack Nicholson"},
            {"Nombre": "Shelley Duvall"},
            {"Nombre": "DannyLloyd"},
            {"Nombre": "Scatman Crothers"},
        ],
    },
    "The Unforgivable": {
        "Director": "Nora Fingscheidt",
        "Anyo": 2021,
        "Reparto": [
            {"Nombre": "Sandra Bullock"},
            {"Nombre": "Jon Bernthal"},
            {"Nombre": "Aisling Franciosi"},
        ],
    }
}

with open("peliculas_victor.json", "w", encoding="UTF-8") as fichero:
    fichero.write(json.dumps(peliculas))