CREATE DATABASE IF NOT EXISTS test_library;

USE test_library;

CREATE TABLE IF NOT EXISTS test_books( 
id INT NOT NULL AUTO_INCREMENT , 
title VARCHAR(255) NOT NULL , 
price VARCHAR(31) NOT NULL , 
rating TINYINT NOT NULL , 
availability VARCHAR(255) NOT NULL , 
img_url TEXT NOT NULL , 
date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
PRIMARY KEY (id)
)