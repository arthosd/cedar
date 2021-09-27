DROP DATABASE TEMP;
CREATE DATABASE TEMP;

USE TEMP;

CREATE TABLE ARTICLE
(
    article_id      INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    article_date    VARCHAR(255),
    category		VARCHAR(255),
    title           TEXT,
    text			LONGTEXT,
    link            TEXT NOT NULL,
    image_link      TEXT,
    author_name     TEXT,
    tweeted         TINYINT DEFAULT 0,
    website         VARCHAR(255),
    resume_sentence TEXT
);