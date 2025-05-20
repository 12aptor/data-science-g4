-- FUNCIONES DE AGRUPACIÓN
-- 1. Contar el número de empleados
SELECT count(*) FROM empleado;
select count(*) from empleado where salario > 5000;
-- 2. Maximos y minimos
SELECT max(salario) FROM empleado;
SELECT min(salario) FROM empleado;
-- 3. Sumar salarios
SELECT sum(salario) FROM empleado;
-- 4. Promedio de salarios
SELECT avg(salario) FROM empleado;

-- VALORES DISTINTOS
select pais from empleado;
select distinct pais from empleado;
-- AGRUPACIONES POR CATEGORIAS
-- 1. Agrupación por país
select pais,count(*) from empleado
group by pais;
-- 2 salario minimo,promedio y maximo por pais
select pais,area,min(salario) as minimo,avg(salario)as promedio,max(salario) as maximo from empleado
group by pais,area order by pais;
--- filtros en agrupaciones

select pais,area,min(salario) as minimo,avg(salario)as promedio,max(salario) as maximo from empleado
group by pais,area
having avg(salario) > 5000 order by pais;