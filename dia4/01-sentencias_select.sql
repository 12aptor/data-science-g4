-- SENTENCIAS SELECT
select * from empleado;
select nombre,pais from empleado;
-- ordernar los resultados
select * from empleado order by nombre asc;
select * from empleado order by salario desc;
-- limites de resultados
select * from empleado order by salario desc limit 10;
-- condiciones con where
select * from empleado where pais = 'Peru';
select * from empleado where salario > 1000;
select * from empleado where salario > 1000 and pais = 'Peru';
select * from empleado where salario > 1000 or pais = 'Peru';
select * from empleado where salario > 1000 and (pais = 'Peru' or pais = 'Chile');
select * from empleado where salario BETWEEN 1000 and 2000;
select * from empleado where pais in ('Peru','Chile','Colombia');