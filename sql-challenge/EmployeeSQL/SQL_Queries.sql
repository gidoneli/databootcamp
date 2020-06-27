-- DATA ANALYSIS
-- Once you have a complete database, do the following:

-- Start exploring a general view of the data
SELECT * FROM employees;


-- 1. List the following details of each employee: employee number, last name, first name, sex, and salary.
SELECT  employee.emp_no,
        employee.last_name,
        employee.first_name,
        employee.sex,
        sal.salary
FROM employees as employee
    LEFT JOIN salaries as sal
    ON (employee.emp_no = sal.emp_no)
ORDER BY employee.emp_no;


-- 2. List first name, last name, and hire date for employees who were hired in 1986.
SELECT  first_name, last_name,hire_date
FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31';

-- 3. List the manager of each department with the following information: 
-- department number, department name, the manager’s employee number, last name, first name.
SELECT  dm.dept_no,
        dept.dept_name,
        dm.emp_no,
        emp.last_name,
        emp.first_name
FROM dept_manager AS dm
    INNER JOIN departments AS dept
        ON (dm.dept_no = dept.dept_no)
    INNER JOIN employees AS emp
        ON (dm.emp_no = emp.emp_no);

-- 4. List the department of each employee with the following information: employee number, 
-- last name, first name, and department name.
SELECT  employee.emp_no,
        employee.last_name,
        employee.first_name,
        dept.dept_name
FROM employees as employee
    INNER JOIN dept_emp AS depemp
        ON (employee.emp_no = depemp.emp_no)
    INNER JOIN departments AS dept
        ON (depemp.dept_no = dept.dept_no)
ORDER BY employee.emp_no;

-- 5. List first name, last name, and sex for employees whose first name is “Hercules” and last names begin with “B.”
SELECT  first_name, last_name, sex
FROM employees
WHERE first_name = 'Hercules' AND last_name LIKE 'B%';


-- 6. List all employees in the Sales department, including their employee number, 
-- last name, first name, and department name.
SELECT  employee.emp_no,
        employee.last_name,
        employee.first_name,
        dept.dept_name
FROM employees as employee
    INNER JOIN dept_emp AS depemp
        ON (employee.emp_no = depemp.emp_no)
    INNER JOIN departments AS dept
        ON (depemp.dept_no = dept.dept_no)
WHERE dept.dept_name = 'Sales'
ORDER BY employee.emp_no;


--7. List all employees in the Sales and Development departments, 
-- including their employee number, last name, first name, and department name.
SELECT  employee.emp_no,
        employee.last_name,
        employee.first_name,
        dept.dept_name
FROM employees as employee
    INNER JOIN dept_emp AS depemp
        ON (employee.emp_no = depemp.emp_no)
    INNER JOIN departments AS dept
        ON (depemp.dept_no = dept.dept_no)
WHERE dept.dept_name IN ('Sales', 'Development')
ORDER BY employee.emp_no;


--8. In descending order, list the frequency count of employee last names, 
-- i.e., how many employees share each last name.
SELECT last_name, count(last_name)
FROM employees
GROUP BY last_name
ORDER BY COUNT(last_name) DESC;

-- End of analysis