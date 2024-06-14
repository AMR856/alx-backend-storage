-- First function
DELIMITER $$
CREATE FUNCTION SafeDiv (first_number INT, second_number INT) RETURNS INT
BEGIN
    IF second_number = 0
    THEN
        RETURN 0;
    ELSE
        RETURN first_number / second_number;
    END IF;
END$$
DELIMITER ;
