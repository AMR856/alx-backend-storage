-- This script is killing
DELIMITER $$
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus(
    IN user_id INT, 
    IN project_name VARCHAR(255), 
    IN score INT
)
BEGIN
    DECLARE temp_project_id INT;
    SELECT id INTO temp_project_id
    FROM projects
    WHERE name = project_name;
    IF temp_project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SELECT LAST_INSERT_ID() INTO temp_project_id;
        INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, temp_project_id, score);
    ELSE
        UPDATE corrections
        SET score = score
        WHERE user_id = user_id AND project_id = temp_project_id;
    END IF;
END$$
DELIMITER ;
