use project;
CREATE TABLE Product (
    prod_id CHAR(10),
    pname VARCHAR(30),
    price FLOAT
);
ALTER TABLE Product ADD CONSTRAINT pk_product PRIMARY KEY (prod_id);

INSERT INTO Product (prod_id, pname, price)
VALUES ('p1', 'tape', 2.5),
                  ('p2', 'tv', 250),
                  ('p3', 'vcr', 80);

CREATE TABLE Depot (
    dep_id CHAR(10),
    addr VARCHAR(50),
    volume FLOAT
);
ALTER TABLE Depot ADD CONSTRAINT pk_depot PRIMARY KEY (dep_id);

INSERT INTO Depot (dep_id, addr, volume)
VALUES ('d1', 'NewYork', 9000),
       ('d2', 'Syracuse', 6000),
       ('d4', 'NewYork', 2000);

CREATE TABLE Stock (
    prod_id CHAR(10),
    dep_id CHAR(10),
    quantity INT
);

ALTER TABLE Stock ADD CONSTRAINT pk_stock PRIMARY KEY (prod_id, dep_id);

ALTER TABLE Stock ADD CONSTRAINT fk_stock_product FOREIGN KEY (prod_id)
REFERENCES Product(prod_id) ON UPDATE CASCADE;

ALTER TABLE Stock ADD CONSTRAINT fk_stock_depot FOREIGN KEY (dep_id)
REFERENCES Depot(dep_id) ON UPDATE CASCADE;

INSERT INTO Stock (prod_id, dep_id, quantity)
VALUES ('p1', 'd1', 1000),
       ('p1', 'd2', -100),
       ('p1', 'd4', 1200),
       ('p3', 'd1', 3000),
       ('p3', 'd4', 2000),
       ('p2', 'd4', 1500),
       ('p2', 'd1', -400),
       ('p2', 'd2', 2000);

