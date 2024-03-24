select W1.id from Weather as W1, Weather as W2 where DATEDIFF(W1, W2) = 1 and W1.temperature > W2.temperature; -- Unknown column 'W1' in 'where clause'

select W1.id from Weather W1, Weather W2 where DATEDIFF(W1, W2) = 1 and W1.temperature > W2.temperature; -- Unknown column 'W1' in 'where clause'
select W1.id FROM Weather W1, Weather W2 WHERE DATEDIFF(W1, W2) = 1 AND W1.temperature > W2.temperature; -- Unknown column 'W1' in 'where clause'
select W1.id from Weather W1, Weather W2 where DATEDIFF(W1, W2) = 1 and W1.temperature > W2.temperature; -- Unknown column 'W1' in 'where clause'

SELECT w1.id FROM Weather w1, Weather w2 WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature;