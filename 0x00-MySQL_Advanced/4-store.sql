-- Writing a trigger
DROP TRIGGER IF EXISTS DECRESING_TRIGGER;
DELIMITER $$
CREATE TRIGGER DECRESING_TRIGGER AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END $$
DELIMITER ;