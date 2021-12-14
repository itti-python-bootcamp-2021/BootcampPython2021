#**kwargs construye un diccionario a partir de los parámetros 'nominales' que recibe.
def construir_select_sql(nombre_tabla, **kwargs):
    sql="SELECT * FROM "+nombre_tabla
    i=0
    for k,v in kwargs.items():
        if i==0:
            sql+=" WHERE " + k + "=" + v
        else:
            sql+=" AND " +  k + "=" + v
        i=i+1
    return sql

sentencia_sql1 = construir_select_sql("EMPLEADOS", nombre="Fernando",ciudad="Alcorcon")
sentencia_sql2 = construir_select_sql("EMPLEADOS", nombre="Fernando",ciudad="Alcorcon",edad="48")
sentencia_sql3 = construir_select_sql("EMPLEADOS", nombre="Julian",ciudad="Mataró",vehiculo="VW")
print(sentencia_sql1)
print(sentencia_sql2)
print(sentencia_sql3)