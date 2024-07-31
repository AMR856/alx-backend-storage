-- The script is killing
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
    END IF;
    INSERT INTO corrections (user_id, project_id, score) 
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END$$
DELIMITER ;
