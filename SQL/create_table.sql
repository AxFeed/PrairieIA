CREATE TABLE people(id SERIAL PRIMARY KEY, city integer NOT NULL, name varchar(256) NOT NULL, height float NOT NULL, date_of_birth date NOT NULL, place_of_birth integer NOT NULL);

CREATE TABLE city(id SERIAL PRIMARY KEY, name varchar(256) NOT NULL, lat float NOT NULL, lon float NOT NULL);





















