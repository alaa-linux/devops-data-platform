-- Étape 125.8
-- Rapport SQL Kafka

SELECT
    stat_date,
    topic_name,
    messages_count,
    consumer_lag
FROM kafka_stats
ORDER BY stat_date, topic_name;
