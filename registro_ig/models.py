from registro_ig.conexion import Conexion

def select_all():
    conectar = Conexion("SELECT * from movements order by date DESC")
    filas = conectar.res.fetchall() #(1,2023-05-05,sueldo,1600)
    columnas= conectar.res.description #columnas(id,0,0,0,0,0,0)
                                                          
    #objetivo crear una lista de diccionario con filas y columnas
    lista_diccionario=[]
    
    for f in filas:
        diccionario={}
        posicion=0
        for c in columnas:
            diccionario[c[0]] = f[posicion] 
            posicion +=1
        lista_diccionario.append(diccionario)

    conectar.con.close()
    
    return lista_diccionario

def insert(registroForm):
    conectarInsert = Conexion("insert into movements(date,concept,quantity) values(?,?,?)",registroForm)
    conectarInsert.con.commit()#funcion para validar el registro
    conectarInsert.con.close()


def select_by(id):
    conectSelectBy = Conexion(f"select * from movements where id={id}")
    resultado = conectSelectBy.res.fetchall()
    conectSelectBy.con.close()

    return resultado[0]

def delete_by(id):
    conectDeleteBy = Conexion(f"delete from movements where id={id};")
    conectDeleteBy.con.commit()#funcion para validar el registro
    conectDeleteBy.con.close()

def update_by(id,registro):
    conectUpdateBy = Conexion(f"UPDATE movements SET date=? ,concept=?, quantity=? WHERE id={id};",registro)
    conectUpdateBy.con.commit()
    conectUpdateBy.con.close()

def select_ingreso():
    conectIngreso = Conexion("SELECT sum(quantity) from movements WHERE quantity > 0")
    resultadoIngreso = conectIngreso.res.fetchall()
    conectIngreso.con.close()

    return resultadoIngreso[0][0]

def select_egreso():
    conectEgreso = Conexion("SELECT sum(quantity) from movements WHERE quantity < 0")
    resultadoEgreso = conectEgreso.res.fetchall()
    conectEgreso.con.close()

    return resultadoEgreso[0][0]