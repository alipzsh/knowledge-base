# lamp

# apache

`apt install apache2`

to access it inside lxc, be sure that it's allowed in firewall.
to access it over ssh, use ssh proxy.

status: `systemctl status apache2`

# relational database (mysql)

a tool for organizing data into tables made up of columns and rows

The data contained within an individual row is known as a record, which is
referenced by a key.

The Structured Query Language (SQL) is a standardized syntax for managing data
on relational databases.

A *database engine* is software for managing relational database data and
exposing it to administrators and automated processes using SQL syntax.

`
apt install mariadb-server
systemctl status mysql
`

`
MariaDB> CREATE DATABASE companydb;
MariaDB> use companydb
MariaDB> CREATE TABLE Contacts (
    ID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
MariaDB> INSERT INTO Contacts (ID, LastName, FirstName, Address, City)
VALUES ('001', 'Torvalds', 'Linus', '123 Any St.', 'Newtown');
MariaDB> select * from Contacts;
`
creating a new user with privileges:
`
mysql> CREATE DATABASE wikidb;
Query OK, 1 row affected (0.01 sec)
mysql> CREATE USER 'mw-admin'@'localhost' IDENTIFIED BY 'mypassword';
Query OK, 0 rows affected (0.00 sec)
mysql> GRANT ALL PRIVILEGES ON wikidb.* TO 'mw-admin'@'localhost'
IDENTIFIED BY 'mypassword';
mysql> FLUSH PRIVILEGES; # to enable the new settings
Query OK, 0 rows affected (0.00 sec)
mysql> exit
`

show database:

`SHOW DATABASES;`


# PHP

`
# apt install php
# apt install libapache2-mod-php
# systemctl restart apache2   # restart whenever chainging a web server's configuration.
`
