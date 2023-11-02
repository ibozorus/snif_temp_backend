create table User
(
    id          INT                not null auto_increment,
    username    varchar(255)            not null,
    password    varchar(255)            not null,
    isAdmin     bool default false not null,
    phoneNumber varchar(255)            null,
    loginTries  int                null,
    firstName   varchar(255)            not null,
    lastName    varchar(255)            not null,
    primary key (id)
);

