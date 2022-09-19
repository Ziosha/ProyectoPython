from flask import Flask, jsonify,request
from flask_mysqldb import MySQL
from flask_cors import CORS
#_________________________________________________________________
app=Flask(__name__)
cors=CORS(app,resources={r'/*':{'origins':'*'}})
#_________________________________________________________________
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='12345678'
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
            reader={'ID_usuario': dato[0],'Nombre_usuario': dato[1],'Apellido_Paterno':dato[2],'Apellido_Materno':dato[3],'Pais':dato[4],'Correo':dato[5],'Contraseña':dato[6],'Telefono':dato[7]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
        return('Error al observar los Usuarios')

#GET ADMINISTRADOR

@app.route('/administrador',methods=['GET'])
def administrador_get():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('select * from  Administrador')
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'ID_Admin': dato[0],'Nickname': dato[1],'ID_usuario':dato[2]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
        return('Error al observar los Administradores')

#GET CATEGORIA
@app.route('/categoria',methods=['GET'])
def categoria_get():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('select * from  Categoria')
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'Cod_categoria': dato[0],'Nom_cateogoria': dato[1],'Deta_categoria':dato[2],'Publico':dato[3]}
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
            reader={'Cod_producto': dato[0],'Nom_producto': dato[1],'Precio_producto':dato[2],'Descripcion':dato[3],'Fecha_lanzamiento':dato[4],'Cod_categoria':dato[5]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
        return('Error al observar los Productos')

#GET RECIBO
@app.route('/recibo',methods=['GET'])
def recibo_get():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('select * from  Recibo')
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'Num_recibo': dato[0],'Num_cuenta': dato[1],'Detalle':dato[2],'Tipo_moneda':dato[3],'Total':dato[4],'Descuento':dato[5]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
        return('Error al observar los Recibos')

#GET COMPRA
@app.route('/compra',methods=['GET'])
def compra_get():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('select * from  Compra')
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'ID_compra': dato[0],'Cod_producto':dato[1],'ID_usuario':dato[2],'Num_recibo':dato[3]}
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
        cursor=mysql.connection.cursor()
        sql="""Insert into Usuario(Nombre_usuario, Apellido_Paterno, Apellido_Materno,Pais,Correo,Contraseña,Telefono)
        values('{0}','{1}','{2}','{3}','{4}','{5}',{6})""".format(nom,ape,apm,pa,co,cont,tel)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Usuario añadido'})
    except Exception as ex:
     return jsonify({'Mensaje': 'Error al añadir al usuario'})

#POST ADMIN
@app.route('/administrador',methods=['POST'])
def administrador_add():
    try:        

        nick=request.json['Nickname']
        id=request.json['ID_usuario']
        
        cursor=mysql.connection.cursor()
        sql="""Insert into Administrador(Nickname, ID_usuario)
        values('{0}',{1})""".format(nick,id)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Administrador añadido'})
    except Exception as ex:
     return jsonify({'Mensaje': 'Error al añadir al administrador'})

#POST CATEGORIA

@app.route('/categoria',methods=['POST'])
def categoria_add():
    try:        

        no=request.json['Nom_cateogoria']
        de=request.json['Deta_categoria']
        pu=request.json['Publico']
        
        
        cursor=mysql.connection.cursor()
        sql="""Insert into Categoria(Nom_cateogoria, Deta_categoria,Publico)
        values('{0}','{1}','{2}')""".format(no,de,pu)
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
        
        
        cursor=mysql.connection.cursor()
        sql="""Insert into Producto(Nom_producto, Precio_producto,Descripcion,Fecha_lanzamiento,Cod_categoria)
        values('{0}',{1},'{2}','{3}',{4})""".format(no,pre,des,fe,co)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Producto añadido'})
    except Exception as ex:
     return jsonify({'Mensaje': 'Error al añadir el producto'})

#POST RECIBO
@app.route('/recibo',methods=['POST'])
def recibo_add():
    try:        

        nu=request.json['Num_cuenta']
        de=request.json['Detalle']
        ti=request.json['Tipo_moneda']
        to=request.json['Total']
        des=request.json['Descuento']
        
        
        cursor=mysql.connection.cursor()
        sql="""Insert into Recibo(Num_cuenta, Detalle,Tipo_moneda,Total,Descuento)
        values({0},'{1}','{2}','{3}','{4}')""".format(nu,de,ti,to,des)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Recibo añadido'})
    except Exception as ex:
     return jsonify({'Mensaje': 'Error al añadir el Recibo'})

#POST COMPRA
@app.route('/compra',methods=['POST'])
def compra_add():
    try:        

        co=request.json['Cod_producto']
        id=request.json['ID_usuario']
        num=request.json['Num_recibo']
        
        
        cursor=mysql.connection.cursor()
        sql="""Insert into Compra(Cod_producto, ID_usuario,Num_recibo)
        values({0},{1},{2})""".format(co,id,num)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Compra añadida'})
    except Exception as ex:
     return jsonify({'Mensaje': 'Error al añadir la Compra'})


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
        cursor=mysql.connection.cursor()
        sql="""Update Usuario set Nombre_usuario='{0}'
        ,Apellido_Paterno='{1}',Apellido_Materno='{2}',Pais='{3}',Correo='{4}',Contraseña='{5}',Telefono={6}
        where ID_usuario={7}""".format(nom,apepa,apema,pai,cor,con,tel,codigo)  
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Se actualizo con exito'})

    except Exception as ex:
        return jsonify({'Mensaje':'Error al actualizar'})
#ADMIN
@app.route('/admin/<codigo>',methods=['PUT'])
def admin_up(codigo):
    try:

        nic=request.json['Nickname']
        id=request.json['ID_usuario']
        cursor=mysql.connection.cursor()
        sql="""Update Administrador set Nickname='{0}',ID_usuario={1}
        where ID_Admin={2}""".format(nic,id,codigo)  
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
        cursor=mysql.connection.cursor()
        sql="""Update Producto set Nom_producto='{0}'
        ,Precio_producto={1},Descripcion='{2}',Fecha_lanzamiento='{3}',Cod_categoria={4}
        where Cod_producto={5}""".format(nom,pre,des,fec,cod,codigo)  
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
        cursor=mysql.connection.cursor()
        sql="""Update Categoria set Nom_cateogoria='{0}'
        ,Deta_categoria='{1}',Publico='{2}'
        where Cod_categoria={3}""".format(nom,det,pub,codigo)  
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
        cursor=mysql.connection.cursor()
        sql="""Update Compra set Cod_producto={0}
        ,ID_usuario={1},Num_recibo={2}
        where ID_compra={3}""".format(cod,id,num,codigo)  
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Se actualizo con exito'})

    except Exception as ex:
        return jsonify({'Mensaje':'Error al actualizar'})
#RECIBO
@app.route('/recibo/<codigo>',methods=['PUT'])
def recibo_up(codigo):
    try:

        num=request.json['Num_cuenta']
        det=request.json['Detalle']
        tip=request.json['Tipo_moneda']
        tot=request.json['Total']
        des=request.json['Descuento']
        cursor=mysql.connection.cursor()
        sql="""Update Usuario set Num_cuenta={0}
        ,Detalle='{1}',Tipo_moneda='{2}',Total={3},Descuento='{4}'
        where ID_usuario={5}""".format(num,det,tip,tot,des,codigo)  
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
#ADMIN
@app.route('/admin/<codigo>',methods=['DELETE'])
def admin_del(codigo):
    try:
        
        cursor=mysql.connection.cursor()
        sql="""Delete from Administrador where ID_Admin={0}""".format(codigo)
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
#RECIBO
@app.route('/recibo/<codigo>',methods=['DELETE'])
def recibo_del(codigo):
    try:
        
        cursor=mysql.connection.cursor()
        sql="""Delete from Recibo where Num_recibo={0}""".format(codigo)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'Mensaje':'Se elimino'})

    except Exception as ex:
        return jsonify({'Mensaje':'error'})
if(__name__ == '__main__'):
    app.run( debug = True, port=3000)