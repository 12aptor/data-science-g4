DROP TABLE IF EXISTS alumno;
CREATE TABLE alumno(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nro_documento VARCHAR(10) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);
insert into alumno(nro_documento,nombre,email)
VALUES
('100','cesar','cesar@gmail.com'),
('200','cesar','cesar@gmail.com');

select * from alumno;

CREATE TABLE curso(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL
);

insert into curso(nombre) values('PYTHON'),('MYSQL');

CREATE TABLE matricula(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    alumno_id int NOT NULL,
    curso_id int NOT NULL,
    FOREIGN KEY (alumno_id) REFERENCES alumno(id),
    FOREIGN KEY (curso_id) REFERENCES curso(id)
);

insert into matricula(alumno_id,curso_id) values(1,1),(1,2),(2,1),(2,2);

select * from matricula;