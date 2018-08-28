SET NAMES utf-8;

create database mvctest;
use 

drop table if exists users;

create table users(
id int auto_increment primary key,
name varchar(20),
password varchar(20)
);

begin;
insert into users(name,password) values('liuxv','1234');
commit;

