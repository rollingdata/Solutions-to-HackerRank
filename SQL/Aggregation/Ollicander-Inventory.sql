SELECT W.id, P.age, W.coins_needed, W.power
FROM Wands W, Wands_Property P
WHERE W.code = P.code AND P.is_evil = 0
AND W.coins_needed = (SELECT min(W1.coins_needed) FROM Wands W1
                      WHERE W1.power = W.power and W1.code = W.code)
ORDER BY W.power DESC, P.age DESC
