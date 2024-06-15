-- Lists all dbs

CREATE TABLE student(
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    email VARCHAR(60) NULL,
    phone_number VARCHAR(20) NOT NULL,
    state VARCHAR(20) NOT NULL,
    country VARCHAR(15) NOT NULL,
    d_o_b DATE NOT NULL,
    sex ENUM('M', 'F') NOT NULL,
    CGPA FLOAT NULL,
    start_date TIMESTAMP,
    student_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY);

SHOW TABLES;

DESCRIBE student;
