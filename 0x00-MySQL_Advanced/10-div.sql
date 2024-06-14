-- First function
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv (first_number INT, second_number INT) RETURNS FLOAT DETERMINISTIC 
BEGIN
    IF second_number = 0
    THEN
        RETURN (0);
    ELSE
        RETURN (first_number / second_number);
    END IF;
END$$
DELIMITER ;

-- cat 10-init.sql | sudo mysql -uroot -p Trying_Hassan
-- cat 10-div.sql | sudo mysql -uroot -p Trying_Hassan
-- echo "SELECT (a / b) FROM numbers;" | sudo mysql -uroot -p Trying_Hassan