-- SENTENCIAS DML (DATA MANIPULATION LANGUAGE)
-- CRUD
-- C(CREATE) - INSERT
-- R(READ) - SELECT
-- U(UPDATE) - UPDATE
-- D (DELETE) - DELETE

-- INSERTAR DATOS A LA TABLA
insert into alumno(nombre,email,celular)
values('Jorge Perez','jperez@gmail.com','993467456');

insert into alumno(nombre,email)
VALUES
('Ana Lopez','alopez@gmail.com'),
('Luis Llerena','lllerena@gmail.com'),
('Carlos Aguilar','caguilar@gmail.com'),
('Maritza Rodriguez','mrodriguez@gmail.com');

-- SELECCIONAR DATOS DE LA TABLA
select * from alumno;
select nombre from alumno;


insert into alumno(nombre,email,celular)
values('Jorge Perez','jperez@gmail.com','993467456');
select * from alumno
where id=1;
-- ACTUALIZAR DATOS DE UN REGISTRO
UPDATE alumno
set celular='333444555'
where id = 1;

-- ELIMINAR UN REGISTRO DE LA TABLA
DELETE from alumno
where id = 6;

