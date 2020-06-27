--SQL Homework - Employee Database: A Mystery in Two Parts

-- DROP PREVIOUS VERSIONS OF TABLES

DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS dept_emp;
DROP TABLE IF EXISTS dept_manager;
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS titles;

-- Create departments table
CREATE TABLE departments (
  dept_no VARCHAR(32) NOT NULL,
  dept_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (dept_no)
);

-- Create employees table
CREATE TABLE employees (
  emp_no INT NOT NULL,
  emp_title VARCHAR(255) NOT NULL,
  birth_date DATE NOT NULL,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  sex VARCHAR(16) NOT NULL,
  hire_date DATE NOT NULL,
  PRIMARY KEY (emp_no)
);

-- Create dept_emp table
CREATE TABLE dept_emp (
  emp_no INT NOT NULL,
  dept_no VARCHAR(32) NOT NULL,
  FOREIGN KEY (dept_no) REFERENCES departments (dept_no),
  FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
  PRIMARY KEY (emp_no, dept_no)
);

-- Create dept_manager table
CREATE TABLE dept_manager (
  dept_no VARCHAR(32) NOT NULL,
  emp_no INT NOT NULL,
  FOREIGN KEY (dept_no) REFERENCES departments (dept_no),
  FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
  PRIMARY KEY (dept_no, emp_no)
);

-- Create salaries table
CREATE TABLE salaries (
  emp_no INT NOT NULL,
  salary INT NOT NULL,
  FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
  PRIMARY KEY (emp_no)
);

-- Create titles table
CREATE TABLE titles (
  title_id VARCHAR(32) NOT NULL,
  title VARCHAR(64) NOT NULL
);

-- END CREATING TABLES
