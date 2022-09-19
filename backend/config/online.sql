drop database db_online;
create database db_online;
use db_online;

create table Usuario(
ID_usuario int (11) primary key not null auto_increment,
Nombre_usuario varchar (20) not null,
Apellido_Paterno varchar (20) not null,
Apellido_Materno varchar (20) not null,
Pais varchar (20) not null,
Correo varchar (30) not null,
Contraseña varchar(30) not null,
Telefono int not null
);

create table Administrador(
ID_Admin int (11) primary key not null auto_increment,
Nickname varchar (30) not null,
ID_usuario int not null,
FOREIGN KEY (ID_usuario) REFERENCES Usuario(ID_usuario)
);

create table Categoria (
Cod_categoria int (11) primary key not null auto_increment,
Nom_cateogoria varchar (15) not null,
Deta_categoria TinyText not null,
Publico set ('+18', '+12', '+7')
);

create table Producto(
Cod_producto int (11) primary key not null auto_increment,
Nom_producto varchar (20) not null,
Precio_producto float not null,
Descripcion TinyText not null,
Fecha_lanzamiento date not null,
Cod_categoria int not null,
FOREIGN KEY (Cod_categoria) REFERENCES Categoria(Cod_categoria)
);
create table Recibo(
Num_recibo int (11) primary key not null auto_increment,
Num_cuenta int not null,
Detalle varchar (20) not null,
Tipo_moneda varchar (20),
Total float not null,
Descuento set ('0%','20%','50%','75%')
);
create table Compra(
ID_compra int (11) not null primary key auto_increment,
Cod_producto int not null,
FOREIGN KEY (Cod_producto) REFERENCES Producto(Cod_producto),
ID_usuario int not null,
FOREIGN KEY (ID_usuario) REFERENCES Usuario(ID_usuario),
Num_recibo int not null,
FOREIGN KEY (Num_recibo) REFERENCES Recibo(Num_recibo)
);

insert into  Usuario (Nombre_usuario,Apellido_Paterno,Apellido_Materno,Pais,Correo,Contraseña,Telefono) values
('Diego','Hurtado','Silva','Bolivia','diego@gmail.com','12345678','79348124'),
('Josue','Estrada','Apaza','Bolivia','josue@gmail.com','holas123','79323123'),
('Juan Gustavo','Bravo','Ibañez','Bolivia','juan@gmail.com','2361de23','73340956');

insert into  Administrador (Nickname,ID_usuario) values
('Admin_bolivia','3');

insert into Categoria (Nom_cateogoria,Deta_categoria,Publico)values 
('Terror','Este tipo de juegos contiene contenido fuerte','+18'),
('Creativo','Este tipo de juegos contiene contenido para expresar creativida','+7'),
('Shooter','Este tipo de juegos contiene contenido armas','+12');

insert into Producto (Nom_producto,Precio_producto,Descripcion,Fecha_lanzamiento,Cod_categoria) values
('Resident Evil V','134.99','Juego de terror','2022/08/12','1'),
('Minecraft','69.99','Juego de creativor','2022/09/11','2'),
('Fornite','89.99','Juego de disparos online','2022/07/25','3');

insert into Recibo (Num_cuenta,Detalle,Tipo_moneda,Total,Descuento)values
('1000023321','Compra de MInecraft','Pesos Bolivianos','69.99','0%');

insert into Compra (Cod_producto,ID_usuario,Num_recibo) values
('2','2','1');


