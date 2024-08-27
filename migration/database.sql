CREATE DATABASE library_db;

USE library_db;

CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    bio TEXT,
    birth_date DATE
);

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    description TEXT,
    publish_date DATE,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);
