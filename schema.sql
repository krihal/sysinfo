drop table if exists sys_stat;
create table sys_stat (
       time timestamp default (strftime('%s', 'now')) not null,
       label text not null,
       value float not null
);     
