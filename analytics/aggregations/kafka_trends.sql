-- Étape 124.12
-- Tendances Kafka

SELECT
    stat_date,
    topic_name,
    SUM(messages_count) AS total_messages,
    ROUND(AVG(consumer_lag), 2) AS avg_consumer_lag,
    MAX(consumer_lag) AS max_consumer_lag
FROM kafka_stats
GROUP BY stat_date, topic_name
ORDER BY stat_date, topic_name;
