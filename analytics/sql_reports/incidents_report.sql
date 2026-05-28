-- Étape 125.2
-- Rapport SQL incidents

SELECT
    incident_date,
    severity,
    source,
    description,
    COUNT(*) AS incidents_count
FROM incidents
GROUP BY incident_date, severity, source, description
ORDER BY incident_date, severity;
