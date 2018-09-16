CREATE TABLE Departments (
   Code INTEGER PRIMARY KEY NOT NULL,
   Name TEXT NOT NULL ,
   Budget REAL NOT NULL
 );

 CREATE TABLE Employees (
   SSN INTEGER PRIMARY KEY NOT NULL,
   Name TEXT NOT NULL ,
   LastName TEXT NOT NULL ,
   Department INTEGER NOT NULL ,
   CONSTRAINT fk_Departments_Code FOREIGN KEY(Department)
   REFERENCES Departments(Code)
 );

 INSERT INTO Departments(Code,Name,Budget) VALUES(14,'IT',65000);
INSERT INTO Departments(Code,Name,Budget) VALUES(37,'Accounting',15000);
INSERT INTO Departments(Code,Name,Budget) VALUES(59,'Human Resources',240000);
INSERT INTO Departments(Code,Name,Budget) VALUES(77,'Research',55000);

INSERT INTO Employees(SSN,Name,LastName,Department) VALUES('123234877','Michael','Rogers',14);
INSERT INTO Employees(SSN,Name,LastName,Department) VALUES('152934485','Anand','Manikutty',14);
INSERT INTO Employees(SSN,Name,LastName,Department) VALUES('222364883','Carol','Smith',37);
INSERT INTO Employees(SSN,Name,LastName,Department) VALUES('326587417','Joe','Stevens',37);
INSERT INTO Employees(SSN,Name,LastName,Department) VALUES('332154719','Mary-Anne','Foster',14);
INSERT INTO Employees(SSN,Name,LastName,Department) VALUES('332569843','George','O''Donnell',77);
INSERT INTO Employees(SSN,Name,LastName,Department) VALUES('546523478','John','Doe',59);
INSERT INTO Employees(SSN,Name,LastName,Department) VALUES('631231482','David','Smith',77);
INSERT INTO Employees(SSN,Name,LastName,Department) VALUES('654873219','Zacary','Efron',59);
INSERT INTO Employees(SSN,Name,LastName,Department) VALUES('745685214','Eric','Goldsmith',59);
INSERT INTO Employees(SSN,Name,LastName,Department) VALUES('845657245','Elizabeth','Doe',14);
INSERT INTO Employees(SSN,Name,LastName,Department) VALUES('845657246','Kumar','Swamy',14);


---7. Select all the data of employees whose last name begins with an "S".
SELECT * FROM Employees
  WHERE LastName LIKE 'S%';

---8. Select the sum of all the departments' budgets.
SELECT SUM(Budget) FROM Departments;


---9. Select the number of employees in each department (you only need to show the department code and the number of employees).
SELECT Department, COUNT(SSN) FROM EmpLoyees
GROUP BY Department;

---10. Select all the data of employees, including each employee's department's data.
SELECT *, Departments.Name FROM Employees
JOIN Departments
ON Departments.Code = Employees.Department
ORDER BY Employees.LastName;

---13. Select the departments with a budget larger than the average budget of all the departments.
SELECT Name, Budget FROM Departments
WHERE Budget > (SELECT AVG(Budget) FROM Departments);

---14. Select the names of departments with more than two employees.
SELECT Departments.Name FROM Employees
JOIN Departments ON Departments.Code = Employees.Department
GROUP BY Departments.Name
HAVING COUNT(Employees.SSN) > 2;

---15. Select the name and last name of employees working for departments with second lowest budget.
SELECT a.Name, a.LastName FROM Employees a
WHERE a.Department = (
  SELECT b.Code FROM
    (SELECT * FROM Departments d ORDER BY d.Budget LIMIT (2)) b
  ORDER BY b.Budget DESC LIMIT (1));

---20. Delete from the table all employees who work in departments with a budget greater than or equal to $60,000.
DELETE FROM Employees
WHERE Department IN (
  SELECT Code FROM Departments
  WHERE Budget >= 60000);





