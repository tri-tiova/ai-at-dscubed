CREATE SCHEMA IF NOT EXISTS project_two;

CREATE TABLE IF NOT EXISTS project_two.trinity(
    id INT, 
    task VARCHAR(50),
    urgency BOOLEAN,
    completed BOOLEAN,
    duration INT
);