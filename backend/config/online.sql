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
Telefono int not null,
Admin bit,
CreationDate DateTime not null,
DeleteDate DateTime null
);

create table Categoria (
Cod_categoria int (11) primary key not null auto_increment,
Nom_cateogoria varchar (15) not null,
Deta_categoria TinyText not null,
Publico set ('+18', '+12', '+7'),
CreationDate DateTime not null,
DeleteDate DateTime null,
DeleteUserId int null
);

create table Producto(
Cod_producto int (11) primary key not null auto_increment,
Nom_producto varchar (20) not null,
Precio_producto float not null,
Descripcion TinyText not null,
Fecha_lanzamiento date not null,
Cod_categoria int not null,
FOREIGN KEY (Cod_categoria) REFERENCES Categoria(Cod_categoria),
CreationDate DateTime not null,
DeleteDate DateTime null,
DeleteUserId int null
);

create table Factura(
Num_recibo int (11) primary key not null auto_increment,
ID_usuario int not null,
FOREIGN KEY (ID_usuario) REFERENCES Usuario(ID_usuario),
Productos varchar(100),
Tipo_moneda varchar (20),
Total float not null,
CreationDate DateTime not null
);

create table Compra(
ID_compra int (11) not null primary key auto_increment,
Cod_producto int not null,
FOREIGN KEY (Cod_producto) REFERENCES Producto(Cod_producto),
ID_usuario int not null,
FOREIGN KEY (ID_usuario) REFERENCES Usuario(ID_usuario),
CreationDate DateTime not null
);

insert into  Usuario (Nombre_usuario,Apellido_Paterno,Apellido_Materno,Pais,Correo,Contraseña,Telefono, Admin, CreationDate) values
('Diego','Hurtado','Silva','Bolivia','diego@gmail.com','12345678','79348124', 1, now()),
('Josue','Estrada','Apaza','Bolivia','josue@gmail.com','holas123','79323123', 1, now()),
('Juan Gustavo','Bravo','Ibañez','Bolivia','juan@gmail.com','2361de23','73340956', 1, now()),
('Wilfredo','Lopez','Perez','Bolivia','wilfredo@gmail.com','123456','73340956', 1, now());


insert into Categoria (Nom_cateogoria,Deta_categoria,Publico, CreationDate)values 
('Terror','Este tipo de juegos contiene contenido fuerte','+18', now()),
('Creativo','Este tipo de juegos contiene contenido para expresar creativida','+7', now()),
('Shooter','Este tipo de juegos contiene contenido armas','+12',now());

insert into Producto (Nom_producto,Precio_producto,Descripcion,Fecha_lanzamiento,Cod_categoria, CreationDate) values
('Resident Evil V','134.99','Juego de terror','2022/08/12','1',now()),
('Minecraft','69.99','Juego de creativor','2022/09/11','2',now()),
('Fornite','89.99','Juego de disparos online','2022/07/25','3',now());




