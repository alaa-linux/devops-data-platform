# SQL Views Results — Étape 123

## Objectif

Ce rapport documente les vues SQL analytiques créées dans PostgreSQL.

---

## Vue 1 — vw_sales_global_kpi

| total_sales | total_quantity | total_revenue | avg_revenue_per_sale | min_revenue | max_revenue |
|---:|---:|---:|---:|---:|---:|
| 10 | 38 | 9175.00 | 917.50 | 125.00 | 3600.00 |

---

## Vue 2 — vw_revenue_by_product

| Product | Total Quantity | Total Revenue | Avg Revenue |
|---|---:|---:|---:|
| Laptop | 6 | 7200.00 | 2400.00 |
| Monitor | 3 | 900.00 | 450.00 |
| Mouse | 22 | 550.00 | 183.33 |
| Keyboard | 7 | 525.00 | 262.50 |

---

## Vue 3 — vw_revenue_by_city

| City | Sales Count | Total Quantity | Total Revenue | Avg Revenue |
|---|---:|---:|---:|---:|
| Bordeaux | 1 | 3 | 3600.00 | 3600.00 |
| Marseille | 2 | 12 | 2650.00 | 1325.00 |
| Nice | 1 | 1 | 1200.00 | 1200.00 |
| Lille | 1 | 2 | 600.00 | 600.00 |
| Paris | 2 | 9 | 425.00 | 212.50 |
| Toulouse | 1 | 1 | 300.00 | 300.00 |
| Lyon | 1 | 3 | 225.00 | 225.00 |
| Nantes | 1 | 7 | 175.00 | 175.00 |

---

## Vue 4 — vw_sales_daily

| Date | Sales Count | Total Quantity | Total Revenue | Avg Revenue |
|---|---:|---:|---:|---:|
| 2026-05-01 | 2 | 7 | 2525.00 | 1262.50 |
| 2026-05-02 | 2 | 4 | 525.00 | 262.50 |
| 2026-05-03 | 2 | 11 | 1450.00 | 725.00 |
| 2026-05-04 | 2 | 6 | 900.00 | 450.00 |
| 2026-05-05 | 2 | 10 | 3775.00 | 1887.50 |

---

## Analyse

- Les ventes sont concentrées sur les laptops en chiffre d'affaires.
- Mouse est le produit le plus vendu en volume.
- Bordeaux possède la transaction la plus élevée.
- Marseille combine volume important et revenu élevé.
- Le 2026-05-05 est le jour le plus performant en revenu.

---

## Conclusion

Les vues SQL analytiques ont été créées, appliquées et validées dans PostgreSQL.

Statut : Étape 123 validée.
