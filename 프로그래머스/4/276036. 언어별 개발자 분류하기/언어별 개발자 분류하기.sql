# SELECT SUM(CODE) 
# FROM SKILLCODES
# WHERE CATEGORTY = 'Front End'

# SELECT SUM(CODE) 
# FROM SKILLCODES
# WHERE NAME = 'Python'

# SELECT SUM(CODE) 
# FROM SKILLCODES
# WHERE NAME = 'C#'
SELECT *
FROM (
    SELECT CASE
        WHEN SKILL_CODE & (
            SELECT SUM(CODE) 
            FROM SKILLCODES
            WHERE CATEGORY = 'Front End'
        ) > 0 AND SKILL_CODE & (
            SELECT CODE 
            FROM SKILLCODES
            WHERE NAME = 'Python'
        ) > 0 THEN 'A'
        WHEN SKILL_CODE & (
            SELECT CODE 
            FROM SKILLCODES
            WHERE NAME = 'C#'    
        ) > 0 THEN 'B'
        WHEN SKILL_CODE & (
            SELECT SUM(CODE) 
            FROM SKILLCODES
            WHERE CATEGORY = 'Front End'
        ) > 0 THEN 'C'
        ELSE NULL
        END AS GRADE, ID, EMAIL
    FROM DEVELOPERS
) AS A
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID

