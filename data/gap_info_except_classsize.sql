INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2010, "fa"
FROM fa2010 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2011, "fa"
FROM fa2011 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2012, "fa"
FROM fa2012 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2013, "fa"
FROM fa2013 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2014, "fa"
FROM fa2014 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2015, "fa"
FROM fa2015 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT Course, ProfessorId, CAST(AverageGrade as REAL), 2016, "fa"
FROM fa2016 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT Course, ProfessorId, CAST(AverageGrade as REAL), 2017, "fa"
FROM fa2017 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2018, "fa"
FROM fa2018 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2010, "sp"
FROM sp2010 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2011, "sp"
FROM sp2011 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2012, "sp"
FROM sp2012 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2013, "sp"
FROM sp2013 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2014, "sp"
FROM sp2014 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2015, "sp"
FROM sp2015 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2016, "sp"
FROM sp2016 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT Course, ProfessorId, CAST(AverageGrade as REAL), 2017, "sp"
FROM sp2017 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT Course, ProfessorId, CAST(AverageGrade as REAL), 2018, "sp"
FROM sp2018 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT Course, ProfessorId, CAST(AverageGrade as REAL), 2019, "sp"
FROM sp2019 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2010, "su"
FROM su2010 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2011, "su"
FROM su2011 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2012, "su"
FROM su2012 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2013, "su"
FROM su2013 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2014, "su"
FROM su2014 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2015, "su"
FROM su2015 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2016, "su"
FROM su2016 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT Course, ProfessorId, CAST(AverageGrade as REAL), 2017, "su"
FROM su2017 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2018, "su"
FROM su2018 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT Course, ProfessorId, CAST(AverageGrade as REAL), 2019, "su"
FROM su2019 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2014, "wi"
FROM wi2014_2015 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT CourseNumber, ProfessorId, CAST(AverageGrade as REAL), 2015, "wi"
FROM wi2015_2016 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT Course, ProfessorId, CAST(AverageGrade as REAL), 2016, "wi"
FROM wi2016_2017 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT Course, ProfessorId, CAST(AverageGrade as REAL), 2017, "wi"
FROM wi2017_2018 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";

INSERT INTO GPA(CourseId, ProfessorId, Value, Year, Term)
SELECT Course, ProfessorId, CAST(AverageGrade as REAL), 2018, "wi"
FROM wi2018_2019 JOIN Professor
ON PrimaryInstructor = Name 
WHERE AverageGrade <> "N/A";
