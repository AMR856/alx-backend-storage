-- Some indexes
ALTER TABLE names 
ADD COLUMN score_string VARCHAR(255) AS (CONVERT(score, CHAR));
CREATE INDEX idx_name_first_score ON names (name(1), score_string(1));
