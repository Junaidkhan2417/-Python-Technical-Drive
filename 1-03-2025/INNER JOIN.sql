SELECT employee.id, employee.first_name, employee.last_name, employee.salary, department.department_name
FROM employee
INNER JOIN department ON employee.department_id = department.department_id;
