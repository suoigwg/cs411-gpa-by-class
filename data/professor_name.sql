INSERT INTO Professor(Name)
SELECT DISTINCT PrimaryInstructor
FROM fa2010
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM fa2011
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM fa2012
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM fa2013
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM fa2014
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM fa2015
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM fa2016
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM fa2017
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM fa2018
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM sp2010
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM sp2011
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM sp2012
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM sp2013
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM sp2014
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM sp2015
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM sp2016
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM sp2017
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM sp2018
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM sp2019
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM su2010
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM su2011
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM su2012
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM su2013
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM su2014
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM su2015
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM su2016
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM su2017
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM su2018
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM su2019
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM wi2014_2015
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM wi2015_2016
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM wi2016_2017
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM wi2017_2018
WHERE PrimaryInstructor IS NOT NULL
UNION
SELECT DISTINCT PrimaryInstructor
FROM wi2018_2019
WHERE PrimaryInstructor IS NOT NULL
ORDER BY PrimaryInstructor