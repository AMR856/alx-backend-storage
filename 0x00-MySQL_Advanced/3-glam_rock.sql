-- Glam Rock Fr
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan FROM metal_bands
WHERE style LIKE '%glam rock%' AND (split <= 2022 OR split IS NULL)
ORDER BY fans DESC;