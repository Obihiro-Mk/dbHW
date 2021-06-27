create table if not exists Performer (
    id serial primary key,
    name varchar(80) not null
);

create table if not exists Genre (
    id serial primary key,
    genre varchar(50) not null
);

create table if not exists Performer_Genre (
    id serial primary key,
    performer_id integer not null references Performer(id),
    genre_id integer not null references Genre(id)
);

create table if not exists Album (
    id serial primary key,
    name_album varchar(80) not null,
    year_album integer not null check(year_album >= 0)
);

create table if not exists Performer_Album (
    id serial primary key,
    performer_id integer not null references Performer(id),
    album_id integer not null references Album(id)
);

create table if not exists Track (
    id serial primary key,
    album_id integer references Album(id),
    name_track varchar(120) not null,
    time_track integer not null
);

create table if not exists Collection (
    id serial primary key,
    name_album varchar(80) not null,
    year_album integer not null check(year_album >= 0)
);

create table if not exists Track_Collection (
    id serial primary key,
    track_id integer not null references Track(id),
    collection_id integer not null references Collection(id)
);

ALTER TABLE collection RENAME COLUMN name_album TO name_collection;