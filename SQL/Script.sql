CREATE TABLE people(id SERIAL PRIMARY KEY, city integer NOT NULL, name varchar(256) NOT NULL, height float NOT NULL, date_of_birth date NOT NULL, place_of_birth integer NOT NULL);

CREATE TABLE city(id SERIAL PRIMARY KEY, name varchar(256) NOT NULL, lat float NOT NULL, lon float NOT NULL);

INSERT INTO city VALUES (1, 'Toulouse', 43.604652, 1.444209);

INSERT INTO people VALUES (1, 1, 'Gregory', 1.75, '1995-11-13', 2);

INSERT INTO people(city, name, height, date_of_birth, place_of_birth) VALUES
(1, 'Gregory', 1.75, '1995-11-13', 2),
(2, 'Alice', 1.62, '1998-04-22', 1),
(1, 'Thomas', 1.80, '1993-09-10', 1),
(2, 'Emma', 1.68, '2000-01-05', 2),
(1, 'Lucas', 1.77, '1997-06-18', 1),
(2, 'Sarah', 1.65, '1996-12-30', 2),
(1, 'Julien', 1.82, '1992-03-14', 1),
(2, 'Camille', 1.70, '1999-08-27', 2),
(1, 'Nicolas', 1.78, '1994-05-09', 1),
(2, 'Laura', 1.60, '2001-02-11', 2),
(1, 'Antoine', 1.83, '1991-10-03', 1),
(2, 'Manon', 1.67, '1997-07-21', 2),
(1, 'Maxime', 1.76, '1995-01-16', 1),
(2, 'Chloe', 1.64, '1998-11-08', 2),
(1, 'Kevin', 1.79, '1993-04-25', 1),
(2, 'Julie', 1.69, '1996-09-02', 2),
(1, 'Benjamin', 1.81, '1992-12-19', 1),
(2, 'Sophie', 1.66, '1999-06-06', 2),
(1, 'Alexandre', 1.84, '1990-08-15', 1);

SELECT * FROM people;

SELECT * FROM people ORDER BY date_of_birth;

SELECT * FROM people ORDER BY height asc;

SELECT p.name, c.name as villeNaissance FROM people as p JOIN city c ON c.id = p.place_of_birth;

SELECT c.name as ville, array_agg(p.name) as personne FROM people p JOIN city c ON p.city = c.id GROUP BY c.name ORDER BY c.name;

SELECT 
    p.name,
    c.name AS ville_naissance,
    ((c.lat - c_toulouse.lat)^2 + (c.lon - c_toulouse.lon)^2) AS distance_approx
FROM people p
JOIN city c ON p.place_of_birth = c.id
JOIN city toulouse ON toulouse.id = 1
ORDER BY distance_approx ASC;




