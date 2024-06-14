-- This script is killing
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE Average FLOAT;
    SELECT AVG(score) INTO Average FROM corrections
    WHERE corrections.user_id = user_id;
    UPDATE users
        SET average_score = Average
        WHERE id = user_id;
END$$
DELIMITER ;
