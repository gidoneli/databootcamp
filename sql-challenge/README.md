# SQL Homework - Employee Database: A Mystery in Two Parts
## Date: June 2020
### By Raúl Flores Palacios


## INTRODUCTION
In this assignment, I will design the tables to hold data in the CSVs, import the CSVs into a SQL database, and answer questions about the data. In other words, you will perform:

* Data Engineering
* Data Analysis


## Data Modeling
Inspect the CSVs and sketch out an ERD of the tables. Feel free to use a tool like http://www.quickdatabasediagrams.com.
I have been provided with six CSV data source files as follow:
* departments.csv
* dept_emp.csv
* dept_manager.csv
* employees.csv
* salaries.csv
* titles.csv

Using the data modeling tool I have produced the followinf data diagram:

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/sql-challenge/EmployeeSQL/QuickDBD-Free%20Diagram.png?raw=true)


## Data Engineering
Using the information from CSV tables I created a table schema for each of the six CSV files. I specified data types, primary keys, foreign keys, and other constraints.

For the primary keys I checked if the column is unique, otherwise I created a composite key. Which takes to primary keys in order to uniquely identify a row.

I made sure to create tables in the correct order to handle foreign keys.
I imported each CSV file into the corresponding SQL table. Note be sure to import the data in the same order that the tables were created and account for the headers when importing to avoid errors.

### Source SQL File for creating the DB Schema
Please refer to the file: <B>SQL_Tables_Schema.sql</B>
https://github.com/raulfloresp/databootcamp/blob/master/sql-challenge/EmployeeSQL/SQL_Tables_Schema.sql


The following image illustrated the outcome on the PGAdmin Tool.

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/sql-challenge/EmployeeSQL/PGAdmin_db.jpg?raw=true)


## Data Analysis
I have created the following queries to analyse the data:
* List the following details of each employee: employee number, last name, first name, sex, and salary.
* List first name, last name, and hire date for employees who were hired in 1986.
* List the manager of each department with the following information: department number, department name, the manager’s employee number, last name, first name.
* List the department of each employee with the following information: employee number, last name, first name, and department name.
* List first name, last name, and sex for employees whose first name is “Hercules” and last names begin with “B.”
* List all employees in the Sales department, including their employee number, last name, first name, and department name.
* List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
* In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

### Source SQL File for queries
Please refer to the file: <B>SQL_Queries.sql</B>

SQL File here:

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/Project01/Images/Decompose_the_ask.png?raw=true)



## BONUS
Data sources are listed here:

Please refer to the Jupyter Notebook file: <B>BONUS_sqlchallenge.ipynb</B>

Jupyter Notebook File here:

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/Project01/Images/Decompose_the_ask.png?raw=true)



Please refer to the Python file: <B>BONUS_sqlchallenge.py</B>

Python File here:

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/Project01/Images/Decompose_the_ask.png?raw=true)


Image of Plot from Jupyter Notebook is here

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/Project01/Images/Decompose_the_ask.png?raw=true)


## Built With

* [Python](https://www.python.org/) - The development language used
* [Pandas](https://pandas.pydata.org/) - Oopen source data analysis and manipulation tool
* [PostgreSQL](https://www.postgresql.org/) - Postgree SQL Database
* [Visual Studio Code](https://code.visualstudio.com/) - Source Code Editor
* [GitHub](https://github.com/) - The version control software and repo


## Authors

* **Raúl Flores Palacios** - *Initial work* - [raulfloresp](https://github.com/raulfloresp/databootcamp)


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
