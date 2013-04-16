drop table if exists sys_stat;
create table sys_stat (
       time timestamp default (strftime('%s', 'now')) not null,
       label text not null,
       value float not null
);     

drop table if exists sys_aggregated_hourly;
create table sys_aggregated_hourly {
       time timestamp default (strftime('%s', 'now')) not null,
       label text not null,
       value float not null
};

drop table if exists sys_aggregated_daily;
create table sys_aggregated_daily {
       time timestamp default (strftime('%s', 'now')) not null,
       label text not null,
       value float not null
};

drop table if exists sys_aggregated_weekly;
create table sys_aggregated_weekly {
       time timestamp default (strftime('%s', 'now')) not null,
       label text not null,
       value float not null
};

drop table if exists sys_aggregated_monthly;
create table sys_aggregated_monthly {
       time timestamp default (strftime('%s', 'now')) not null,
       label text not null,
       value float not null
};