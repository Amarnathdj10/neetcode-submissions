-- Write your query below
SELECT e.*,
    CASE
        WHEN e.operator = '>' AND lv.value > rv.value THEN 'true'
        WHEN e.operator = '<' AND lv.value < rv.value THEN 'true'
        WHEN e.operator = '=' AND lv.value = rv.value THEN 'true'
        ELSE 'false'
    END AS value
FROM expressions e
JOIN variables lv ON e.left_operand = lv.name
JOIN variables rv ON e.right_operand = rv.name;