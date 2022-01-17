class Animal:
    """
    #NO EXISTE LA SOBRECARGA (overload) DE MÉTODOS, NI DE CONSTRUCTORES EN PYTHON
    def comer(self):
        print("Comiendo cualquier cosa")
    def comer(self, carne):
        print(f"Comiendo {carne} kilos de carne")
    def comer(self, carne, patatas):
        print(f"Comiendo {carne} kilos de carne y {patatas} kilos de patatas")
    """
    def comer(self, carne=None, patatas=None):
        if (carne!=None and patatas!=None):
            print(f"Comiendo {carne} kilos de carne y {patatas} kilos de patatas")
        elif (carne!=None and patatas==None):
            print(f"Comiendo {carne} kilos de carne")
        else:
           print("Comiendo cualquier cosa") 

Animal().comer()
Animal().comer(5)
Animal().comer(5,-8)