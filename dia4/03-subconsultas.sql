-- salario promedio
select avg(salario) from empleado;
-- empleados que gana mas que el salario promedio
select * from empleado 
where salario > (select avg(salario) from empleado);
select nombre,salario,(select avg(salario) from empleado) as promedio
from empleado;

-- consultas con columnas calculadas
SELECT 
    nombre,
    salario,
    (SELECT AVG(salario) FROM empleado) AS salario_promedio,
    CASE 
        WHEN salario > (SELECT AVG(salario) FROM empleado) THEN 'Mayor al promedio'
        WHEN salario = (SELECT AVG(salario) FROM empleado) THEN 'Igual al promedio'
        ELSE 'Menor al promedio'
    END AS comparacion
FROM empleado;
