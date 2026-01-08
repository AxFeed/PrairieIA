SELECT 
    p.name,
    c.name AS ville_naissance,
    ((c.lat - toulouse.lat)^2 + (c.lon - toulouse.lon)^2) AS distance_approx
FROM people p
JOIN city c ON p.place_of_birth = c.id
JOIN city toulouse ON toulouse.id = 1
ORDER BY distance_approx ASC;