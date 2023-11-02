create table changelog
(
    id       int auto_increment,
    userId   int                                   not null,
    sensorId int                                   not null,
    datum    timestamp default CURRENT_TIMESTAMP() not null,
    constraint id
        primary key (id),
    constraint sensorId
        foreign key (sensorId) references sensor (id)
            ON DELETE CASCADE,
    constraint userId
        foreign key (userId) references user (id)
            ON DELETE CASCADE
);

