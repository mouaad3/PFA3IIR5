create database SitePFA;
use SitePFA;

create table Clientt(
	id int not null primary  key auto_increment,
	 username varchar(30) not null,
	 age varchar(10) CHECK(CAST(age AS UNSIGNED) > 0),
	 email varchar(50) check(email like('%@%')), 
     pass varchar(50),
	 telephone varchar(30)
 );
create table adminn(
	id int not null primary key auto_increment,
	 nom varchar(30) not null unique,
	 prenom varchar(30) not null,
	 age varchar(10) CHECK(CAST(age AS UNSIGNED) > 0),
	 email varchar(50) check(email like('%@%')), 
     pass varchar(50),
	 telephone varchar(30)
 );
create table voyage(id int primary key unique,
	 destination varchar(30) not null,
	 nbrAdult int CHECK(nbrAdult > 0),
	 nbrChild int CHECK(nbrChild > 0),
	 checkIn date,
	 checkOut date, 
	 CHECK(checkIn<checkOut)
 );
create table agence(id int primary key unique,
	 nom varchar(30) not null,
	 localPlace varchar(30) not null
 );

insert into adminn values(7, "Ahmed", "ROUITA",20,"email@gmail.com","123","0612345");

insert into adminn values(3, "Mouaad", "AAJMI", 21, "email@gmail.com","root", "0612345");

insert into clientt(username,age,email,pass,telephone)values( "MOUAAD","21","email@gmail.com","1231","0612345");
insert into clientt(username,age,email,pass,telephone)values( "Ahmed","20","ahmed.rouita@gmail.com","12345678","061234554");
insert into clientt(username,age,email,pass,telephone)values( "Youness","26","Youness.Gaghou@gmail.com","12345678","063546846");
insert into clientt(username,age,email,pass,telephone)values( "Mouaad","21","Mouaad.Aajmi@gmail.com","123678","075644167");
insert into clientt(username,age,email,pass,telephone)values( "Oumaima","27","Oumaima.Douski@gmail.com","1065423678","0758855167");
insert into clientt(username,age,email,pass,telephone)values( "Rachid","30","Rachid.Igeunfer@gmail.com","10544184","065748448");
insert into clientt(username,age,email,pass,telephone)values( "Tarik","24","Tarik.Benlahbib@gmail.com","1231","074846871");

drop table adminn;
drop table clientt;
drop table agence;
drop table voyage;


select * from adminn;
select * from clientt;

select max(id) as '' from clientt;



DELETE FROM clientt WHERE id = 4;

update clientt set pass = '1231' where id = 1;