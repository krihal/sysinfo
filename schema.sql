drop table if exists sys_stat;
create table sys_stat (
       id integer primary key autoincrement not null,
       time timestamp default (strftime('%s', 'now')) not null,
       cpu float,
       mem float,
       net float,
       users integer,
       load_one float,
       load_five float,
       load_fifteen float
);     
