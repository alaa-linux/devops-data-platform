-- Étape 124.10
-- TOP erreurs / incidents

SELECT
    description AS error,
    COUNT(*) AS error_count
FROM incidents
GROUP BY description
ORDER BY error_count DESC;
