CREATE TABLE Manufacturers (
    Code INTEGER PRIMARY KEY NOT NULL,
    Name TEXT NOT NULL
);

CREATE TABLE Products (
    Code INTEGER PRIMARY KEY NOT NULL,
    Name TEXT NOT NULL ,
    Price REAL NOT NULL ,
    Manufacturer INTEGER NOT NULL
        CONSTRAINT fk_Manufacturers_Code REFERENCES MANUFACTURERS(Code)
);

INSERT INTO Manufacturers(Code,Name) VALUES(1,'Sony');
INSERT INTO Manufacturers(Code,Name) VALUES(2,'Creative Labs');
INSERT INTO Manufacturers(Code,Name) VALUES(3,'Hewlett-Packard');
INSERT INTO Manufacturers(Code,Name) VALUES(4,'Iomega');
INSERT INTO Manufacturers(Code,Name) VALUES(5,'Fujitsu');
INSERT INTO Manufacturers(Code,Name) VALUES(6,'Winchester');

INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(1,'Hard drive',240,5);
INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(2,'Memory',120,6);
INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(3,'ZIP drive',150,4);
INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(4,'Floppy disk',5,6);
INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(5,'Monitor',240,1);
INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(6,'DVD drive',180,2);
INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(7,'CD drive',90,2);
INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(8,'Printer',270,3);
INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(9,'Toner cartridge',66,3);
INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(10,'DVD burner',180,2);
INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(11,'Floppy disk1',5,6);


---7. Compute the average price of all products with manufacturer code equal to 2.
--select avg(Price) from Products where Manufacturer = 2;

---8. Compute the number of products with a price larger than or equal to $180.
--select count(*) from Products where Price >= 180;

---9. Select the name and price of all products with a price larger than or equal to $180, and sort first by price (in descending order), and then by name (in ascending order).
--select Name, Price from Products where Price >= 180 order by Price desc, Name asc;

---10. Select all the data from the products, including all the data for each product's manufacturer.
--select * from Products inner join Manufacturers on Products.Manufacturer = Manufacturers.Code;
--SELECT * FROM Products, Manufacturers
--  WHERE Products.Manufacturer = Manufacturers.Code;

---11. Select the product name, price, and manufacturer name of all the products.
--select Products.Name, Price, Manufacturers.Name from Products
--  inner join Manufacturers on Products.Manufacturer = Manufacturers.Code;

---12. Select the average price of each manufacturer's products, showing only the manufacturer's code.
--select avg(Products.Price), Manufacturer from Products
--  group by Manufacturer;


---13. Select the average price of each manufacturer's products, showing the manufacturer's name.
--select avg(Price), Manufacturers.Name from Products
--  inner join Manufacturers on Products.Manufacturer = Manufacturers.Code
--  group by Manufacturers.Name;


---14. Select the names of manufacturer whose products have an average price larger than or equal to $150.
--select avg(Price) as x, Manufacturers.Name from Products
--  inner join Manufacturers on Products.Manufacturer = Manufacturers.Code
--  group by Manufacturers.Name
--  having x >= 150;

---15. Select the name and price of the cheapest product.
--select min(Price), Name from Products;
---wybierze tylko jeden produkt

-- SELECT Name,Price
--  FROM Products
--  ORDER BY Price ASC
--  LIMIT 2;
---wybierze tylko jeden produkt, jeśli nie ustawimy odpowiedniego limitu

-- SELECT Name, Price
--   FROM Products
--   WHERE Price = (SELECT MIN(Price) FROM Products);
---wybierze wszystko, najlepsze rozwiązanie
-- select 2 from ; - jeden wiersz
-- select 2, Name from Products; - wiele wierszy


---16. Select the name of each manufacturer along with the name and price of its most expensive product.
select P.Price, P.Name, M.Name from Products P
join Manufacturers M
on P.Manufacturer = M.Code
and P.Price =
(
  select max(P.Price) from Products P
  where P.Manufacturer = M.Code
);

---17. Add a new product: Loudspeakers, $70, manufacturer 2.
INSERT INTO Products(Code, Name, Price, Manufacturer)VALUES(11, 'Loudspeakers',70, 2);

---18. Update the name of product 8 to "Laser Printer".
UPDATE Products
SET Name = 'Laser printer'
Where Code = 8;

---19. Apply a 10% discount to all products.
UPDATE Products
SET Price = 0.9*Price;


---20. Apply a 10% discount to all products with a price larger than or equal to $120.
UPDATE Products
SET Price = 0.9*Price
Where Price >= 120;

