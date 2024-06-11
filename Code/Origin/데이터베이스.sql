CREATE DATABASE WeeklyProject;
USE WeeklyProject;

CREATE TABLE mytable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    email VARCHAR(255)
);

GRANT ALL PRIVILEGES ON WeeklyProject.* TO 'username'@'host' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;