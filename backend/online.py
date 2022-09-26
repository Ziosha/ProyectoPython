from flask import Flask, jsonify,request
from flask_mysqldb import MySQL
from flask_cors import CORS
#_________________________________________________________________
app=Flask(__name__)
cors=CORS(app,resources={r'/*':{'origins':'*'}})
#_________________________________________________________________
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='123456'
app.config['MYSQL_DB']='db_online'
mysql = MySQL(app)
#_________________________________GET______________________________

#GET USUARIO
@app.route('/usuario',methods=['GET'])
def usuario_get():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('select * from Usuario')
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'ID_usuario':dato[0],'Nombre_usuario':dato[1],'Apellido_Paterno':dato[2],'Apellido_Materno':dato[3],'Pais':dato[4],'Correo':dato[5],'Contraseña':dato[6],'Telefono':dato[7]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
         return('Error al observar los Usuarios')

#GET CATEGORIA
@app.route('/categoria',methods=['GET'])
def categoria_get():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('select * from  Categoria')
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'Cod_categoria': dato[0],'Nom_cateogoria': dato[1],'Deta_categoria':dato[2],'Publico':dato[3],'CreationDate':dato[4]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
        return('Error al observar las Categorias')

#GET PRODUCTO
@app.route('/producto',methods=['GET'])
def producto_get():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('select * from  Producto')
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'Cod_producto': dato[0],'Nom_producto': dato[1],'Precio_producto':dato[2],'Descripcion':dato[3],'Fecha_lanzamiento':dato[4],'Image':dato[5], 'Cod_Categoria':dato[6]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
        return('Error al observar los Productos')

#GET FACTURA
@app.route('/factura',methods=['GET'])
def factura_get():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('select * from  Factura')
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'Num_recibo': dato[0],'ID_usuario': dato[1],'Productos':dato[2],'Tipo_moneda':dato[3],'Total':dato[4],'CreationDate':dato[5]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
        return('Error al observar la Factura')

#GET COMPRA
@app.route('/compra',methods=['GET'])
def compra_get():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('select * from  Compra')
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'ID_compra': dato[0],'Cod_producto':dato[1],'ID_usuario':dato[2],'CreationDate':dato[3]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
        return('Error al observar las compras')

#____________________POST______________________________________________
#POST USUARIO
@app.route('/usuario',methods=['POST'])
def usuario_add():
    try:        

        nom=request.json['Nombre_usuario']
        ape=request.json['Apellido_Paterno']
        apm=request.json['Apellido_Materno']
        pa=request.json['Pais']
        co=request.json['Correo']
        cont=request.json['Contraseña']
        tel=request.json['Telefono']
        cre=request.json['CreationDate']

        cursor=mysql.connection.cursor()
        sql="""Insert into Usuario(Nombre_usuario, Apellido_Paterno, Apellido_Materno,Pais,Correo,Contraseña,Telefono,CreationDate)
        values('{0}','{1}','{2}','{3}','{4}','{5}',{6},'{7}')""".format(nom,ape,apm,pa,co,cont,tel,cre)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Usuario añadido'})
    except Exception as ex:
     return jsonify({'Mensaje': 'Error al añadir al usuario'})


#POST CATEGORIA
@app.route('/categoria',methods=['POST'])
def categoria_add():
    try:        

        no=request.json['Nom_cateogoria']
        de=request.json['Deta_categoria']
        pu=request.json['Publico']
        cre=request.json['CreationDate']
        
        cursor=mysql.connection.cursor()
        sql="""Insert into Categoria(Nom_cateogoria, Deta_categoria,Publico,CreationDate)
        values('{0}','{1}','{2}','{3}')""".format(no,de,pu,cre)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Categoria añadida'})
    except Exception as ex:
     return jsonify({'Mensaje': 'Error al añadir la categoria'})

#POST PRODUCTO
@app.route('/producto',methods=['POST'])
def producto_add():
    try:        

        no=request.json['Nom_producto']
        pre=request.json['Precio_producto']
        des=request.json['Descripcion']
        fe=request.json['Fecha_lanzamiento']
        co=request.json['Cod_categoria']
        cre=request.json['CreationDate']
        
        cursor=mysql.connection.cursor()
        sql="""Insert into Producto(Nom_producto, Precio_producto,Descripcion,Fecha_lanzamiento,Cod_categoria,CreationDate)
        values('{0}',{1},'{2}','{3}',{4},'{5}')""".format(no,pre,des,fe,co,cre)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Producto añadido'})
    except Exception as ex:
     return jsonify({'Mensaje': 'Error al añadir el producto'})

#POST FACTURA
@app.route('/factura',methods=['POST'])
def factura_add():
    try:        

        nu=request.json['ID_usuario']
        pro=request.json['Productos']
        ti=request.json['Tipo_moneda']
        to=request.json['Total']
        cre=request.json['CreationDate']
        
        cursor=mysql.connection.cursor()
        sql="""Insert into Factura(ID_usuario, Productos,Tipo_moneda,Total,CreationDate)
        values({0},'{1}','{2}','{3}','{4}','{5}')""".format(nu,pro,ti,to,cre)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Factura añadida'})
    except Exception as ex:
     return jsonify({'Mensaje': 'Error al añadir la Factura'})

#POST COMPRA
@app.route('/compra',methods=['POST'])
def compra_add():
    try:        

        co=request.json['Cod_producto']
        id=request.json['ID_usuario']
        num=request.json['Num_recibo']
        cre=request.json['CreationDate']
        
        cursor=mysql.connection.cursor()
        sql="""Insert into Compra(Cod_producto, ID_usuario,Num_recibo,CreationDate)
        values({0},{1},{2},'{3}')""".format(co,id,num,cre)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Compra añadida'})
    except Exception as ex:
     return jsonify({'Mensaje': 'Error al añadir la Compra'})

#_____________________________PUT________________________________
#USUARIO
@app.route('/usuario/<codigo>',methods=['PUT'])
def usuario_up(codigo):
    try:

        nom=request.json['Nombre_usuario']
        apepa=request.json['Apellido_Paterno']
        apema=request.json['Apellido_Materno']
        pai=request.json['Pais']
        cor=request.json['Correo']
        con=request.json['Contraseña']
        tel=request.json['Telefono']
        cre=request.json['CreationDate']
        cursor=mysql.connection.cursor()
        sql="""Update Usuario set Nombre_usuario='{0}'
        ,Apellido_Paterno='{1}',Apellido_Materno='{2}',Pais='{3}',Correo='{4}',Contraseña='{5}',Telefono={6},CreationDate='{7}'
        where ID_usuario={8}""".format(nom,apepa,apema,pai,cor,con,tel,cre,codigo)  
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Se actualizo con exito'})

    except Exception as ex:
        return jsonify({'Mensaje':'Error al actualizar'})

#PRODUCTO
@app.route('/producto/<codigo>',methods=['PUT'])
def producto_up(codigo):
    try:

        nom=request.json['Nom_producto']
        pre=request.json['Precio_producto']
        des=request.json['Descripcion']
        fec=request.json['Fecha_lanzamiento']
        cod=request.json['Cod_categoria']
        cre=request.json['CreationDate']
        
        cursor=mysql.connection.cursor()
        sql="""Update Producto set Nom_producto='{0}'
        ,Precio_producto={1},Descripcion='{2}',Fecha_lanzamiento='{3}',Cod_categoria={4},CreationDate='{5}'
        where Cod_producto={6}""".format(nom,pre,des,fec,cod,cre,codigo)  
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Se actualizo con exito'})

    except Exception as ex:
        return jsonify({'Mensaje':'Error al actualizar'})
#CATEGORIA
@app.route('/categoria/<codigo>',methods=['PUT'])
def categoria_up(codigo):
    try:

        nom=request.json['Nom_cateogoria']
        det=request.json['Deta_categoria']
        pub=request.json['Publico']
        cre=request.json['CreationDate']
        cursor=mysql.connection.cursor()
        sql="""Update Categoria set Nom_cateogoria='{0}'
        ,Deta_categoria='{1}',Publico='{2}',CreationDate='{3}'
        where Cod_categoria={4}""".format(nom,det,pub,cre,codigo)  
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Se actualizo con exito'})

    except Exception as ex:
        return jsonify({'Mensaje':'Error al actualizar'})
#COMPRA
@app.route('/compra/<codigo>',methods=['PUT'])
def compra_up(codigo):
    try:

        cod=request.json['Cod_producto']
        id=request.json['ID_usuario']
        num=request.json['Num_recibo']
        cre=request.json['CreationDate']
        cursor=mysql.connection.cursor()
        sql="""Update Compra set Cod_producto={0}
        ,ID_usuario={1},Num_recibo={2},CreationDate='{3}'
        where ID_compra={4}""".format(cod,id,num,cre,codigo)  
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Se actualizo con exito'})

    except Exception as ex:
        return jsonify({'Mensaje':'Error al actualizar'})
#FACTURA
@app.route('/factura/<codigo>',methods=['PUT'])
def factura_up(codigo):
    try:

        id=request.json['ID_usuario']
        pro=request.json['Productos']
        ti=request.json['Tipo_moneda']
        to=request.json['Total']
        cre=request.json['CreationDate']
        cursor=mysql.connection.cursor()
        sql="""Update Factura set ID_usuario={0}
        ,Productos='{1}',Tipo_moneda='{2}',Total={3},CreationDate='{4}'
        where Num_recibo={5}""".format(id,pro,ti,to,cre,codigo)  
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Se actualizo con exito'})

    except Exception as ex:
        return jsonify({'Mensaje':'Error al actualizar'})
#_____________________________DELETE_______________________________
#USUARIO
@app.route('/usuario/<codigo>',methods=['DELETE'])
def usuario_del(codigo):
    try:
        
        cursor=mysql.connection.cursor()
        sql="""Delete from Usuario where ID_usuario={0}""".format(codigo)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Se elimino'})

    except Exception as ex:
        return jsonify({'Mensaje':'error'})

#CATEGORIA
@app.route('/categoria/<codigo>',methods=['DELETE'])
def categoria_del(codigo):
    try:
        
        cursor=mysql.connection.cursor()
        sql="""Delete from Categoria where Cod_categoria={0}""".format(codigo)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Se elimino'})

    except Exception as ex:
        return jsonify({'Mensaje':'error'})
#PRODUCTO
@app.route('/producto/<codigo>',methods=['DELETE'])
def producto_del(codigo):
    try:
        
        cursor=mysql.connection.cursor()
        sql="""Delete from Producto where Cod_producto={0}""".format(codigo)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Se elimino'})

    except Exception as ex:
        return jsonify({'Mensaje':'error'})
#COMPRA
@app.route('/compra/<codigo>',methods=['DELETE'])
def compra_del(codigo):
    try:
        
        cursor=mysql.connection.cursor()
        sql="""Delete from Compra where ID_compra={0}""".format(codigo)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Se elimino'})

    except Exception as ex:
        return jsonify({'Mensaje':'error'})
#FACTURA
@app.route('/factura/<codigo>',methods=['DELETE'])
def factura_del(codigo):
    try:
        
        cursor=mysql.connection.cursor()
        sql="""Delete from Factura where Num_recibo={0}""".format(codigo)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Se elimino'})

    except Exception as ex:
        return jsonify({'Mensaje':'error'})


if(__name__ == '__main__'):
    app.run( debug = True, port=3000)