create table Sensor
(
    id            int auto_increment,
    herstellerId  int          not null,
    serverCabinId int          not null,
    sensorAddress varchar(255) not null,
    maxTemp       double       not null,
    constraint id
        primary key (id),
    constraint herstellerId
        foreign key (herstellerId) references hersteller (id),
    constraint serverCabinId
        foreign key (serverCabinId) references servercabin (id)
);

