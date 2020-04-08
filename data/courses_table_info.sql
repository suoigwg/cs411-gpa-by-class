INSERT INTO Courses(CourseNo, Subject, Title)
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM fa2010
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM fa2011
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM fa2012
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM fa2013
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM fa2014
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM fa2015
UNION
SELECT DISTINCT Course, Subject, CourseTitle
FROM fa2016
UNION
SELECT DISTINCT Course, Subject, CourseTitle
FROM fa2017
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM fa2018
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM sp2010
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM sp2011
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM sp2012
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM sp2013
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM sp2014
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM sp2015
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM sp2016
UNION
SELECT DISTINCT Course, Subject, CourseTitle
FROM sp2017
UNION
SELECT DISTINCT Course, Subject, CourseTitle
FROM sp2018
UNION
SELECT DISTINCT Course, Subject, CourseTitle
FROM sp2019
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM su2010
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM su2011
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM su2012
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM su2013
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM su2014
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM su2015
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM su2016
UNION
SELECT DISTINCT Course, Subject, CourseTitle
FROM su2017
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM su2018
UNION
SELECT DISTINCT Course, Subject, CourseTitle
FROM su2019
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM wi2014_2015
UNION
SELECT DISTINCT CourseNumber, CourseSubject, CourseTitle
FROM wi2015_2016
UNION
SELECT DISTINCT Course, Subject, CourseTitle
FROM wi2016_2017
UNION
SELECT DISTINCT Course, Subject, CourseTitle
FROM wi2017_2018
UNION
SELECT DISTINCT Course, Subject, CourseTitle
FROM wi2018_2019