SELECT CASE
WHEN G.Grade < 8 THEN NULL
ELSE S.Name
END AS Name, G.Grade, S.Marks
FROM Students S
LEFT JOIN Grades G ON
S.Marks >= G.Min_Mark AND S.Marks <= G.Max_Mark
ORDER BY G.Grade DESC, S.Name;
