create database if not exists LiveScore;
use LiveScore;
create table if not exists users(
    ID int not null,
    username varchar(50),
    birthdate date,
    mail varchar(50),
    passwd varchar(50),
    gender varchar(50)
);
insert into users values(111, "Juan Bocanegra", "2022-02-27", "111@mail.com", "111", "Male");
insert into users values(112, "Angely Ballesteros", "2022-02-27", "112@mail.com", "112", "Female");

CREATE USER 'AdminLS'@'localhost' IDENTIFIED BY 'Admin'; 
GRANT ALL PRIVILEGES ON LiveScore.* TO 'AdminLS'@'localhost';
CREATE USER 'UserLS'@'localhost' IDENTIFIED BY 'user'; 
GRANT SELECT,INSERT,UPDATE,DELETE ON LiveScore.* TO 'UserLS'@'localhost';