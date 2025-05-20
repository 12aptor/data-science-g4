-- A ALUMNO
-- B MATRICULA
-- C CURSO

update alumno set nombre = 'Juanito Alvarado' where id = 1;
update alumno set nombre = 'Anita' where id = 2;
insert into alumno(nro_documento,nombre,email) values('300','cesar','cesar@gmail.com');

select * from alumno;
-- LEFT JOIN
select alumno.nombre,curso.nombre
from alumno LEFT JOIN matricula ON matricula.alumno_id = alumno.id
LEFT JOIN curso ON curso.id = matricula.curso_id;

-- RIGHT JOIN
insert into curso(nombre) values('JAVA');
select alumno.nombre,curso.nombre
from alumno RIGHT JOIN matricula ON matricula.alumno_id = alumno.id
RIGHT JOIN curso ON curso.id = matricula.curso_id;

-- INNER JOIN
select alumno.nombre,alumno.email,alumno.nro_documento,curso.nombre
from alumno INNER JOIN matricula ON matricula.alumno_id = alumno.id
INNER JOIN curso ON curso.id = matricula.curso_id;