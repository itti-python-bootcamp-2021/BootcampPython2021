#Esta clase 'equivale' al siguiente diccionario:
#columna1 = {"NAME":"id","TYPE":"INTEGER","PK":True,"AI":True,"NOT_NULL":False}

class ColumnaDB:
    name: None
    type: None
    pk: None
    ai: None
    not_null: None
    
    def __init__(self, name, type, pk, ai, not_null):
        self.name = name
        self.type = type
        self.pk = pk
        self.ai = ai
        self.not_null = not_null