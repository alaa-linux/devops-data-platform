-- Étape 124.8
-- GROUP BY incidents par date

SELECT
    incident_date,
    COUNT(*) AS incidents_count
FROM incidents
GROUP BY incident_date
ORDER BY incident_date;
