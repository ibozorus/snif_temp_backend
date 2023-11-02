create table Temperature
(
    id        int auto_increment,
    sensorFK  int                                   not null,
    timestamp timestamp default CURRENT_TIMESTAMP() not null,
    value     double                                not null,
    constraint id
        primary key (id),
    constraint sensorFK
        foreign key (sensorFK) references sensor (id)
);

