-- Initial
DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(255) NOT NULL,
    score INT default 0,
    last_meeting DATE NULL 
);

INSERT INTO students (name, score) VALUES ("Bob", 80);
INSERT INTO students (name, score) VALUES ("Sylvia", 120);
INSERT INTO students (name, score) VALUES ("Jean", 60);
INSERT INTO students (name, score) VALUES ("Steeve", 50);
INSERT INTO students (name, score) VALUES ("Camilia", 80);
INSERT INTO students (name, score) VALUES ("Alexa", 130);
-- cat 11-init.sql | sudo mysql -uroot -p Trying_Hassan
-- cat 11-main.sql | sudo mysql -uroot -p Trying_Hassan
-- cat 11-need_meeting.sql | sudo mysql -uroot -p Trying_Hassan