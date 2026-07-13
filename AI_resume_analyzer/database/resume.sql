CREATE DATABASE IF NOT EXISTS resume;

USE resume;

DROP TABLE IF EXISTS resume_analysis;

CREATE TABLE resume_analysis
(
    id INT PRIMARY KEY AUTO_INCREMENT,

    name VARCHAR(100) NOT NULL,

    email VARCHAR(100),

    phone VARCHAR(20),

    job_role VARCHAR(100),

    ats_score INT,

    matched_skills TEXT,

    missing_skills TEXT,

    suggestions TEXT
);