-- Hee Ji Park (USC ID: 4090715830)
-- CSCI 585 HW3

-- Create table
CREATE TABLE geometries (name varchar, location geometry);

-- Insert locations
INSERT INTO geometries VALUES
    ('Troy Hall','POINT(-118.2818054 34.0260208)'),
    ('USC Bookstores','POINT(-118.286183 34.0207388)'),
    ('Viterbi school of Engineering','POINT(-118.2880679 34.0200566)'),
    ('Jefferson Boulevard Structure','POINT(-118.2887621 34.0248966)'),
    ('Leavey Library','POINT(-118.282985 34.021633)'),
    ('USC Hotel','POINT(-118.281233 34.019296)'),
    ('Marshall Business School','POINT(-118.285406 34.018841)'),
    ('USC School of Cinematic Arts','POINT(-118.286415 34.023465)'),
    ('Target','POINT(-118.2842542 34.0256988)'),
    ('Ray R. Irani Hall','POINT(-118.2897672 34.0222983)'),
    ('Doheny Memorial Library','POINT(-118.2841286 34.0203388)'),
    ('Chase Bank','POINT(-118.2803439 34.0222549)'),
    ('USC Korean Studies Institute','POINT(-118.2843231 34.0228976)');

-- Check database
SELECT name, ST_AsText(location) FROM geometries;

-- For Convex Hull
SELECT ST_AsText(ST_ConvexHull(ST_Collect(location))) FROM geometries;

-- For 4 Nearest Neighbors of Troy Hall (my dorm)
SELECT name, ST_AsText(location), ST_Distance(location,'POINT(-118.2818054 34.0260208)') as distance  
FROM geometries 
WHERE name <> 'Troy Hall'
ORDER BY ST_Distance(location, 'POINT(-118.2818054 34.0260208)')
LIMIT 4;




