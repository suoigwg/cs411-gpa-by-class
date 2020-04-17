GPA_BY_YEAR_AND_DEPT = """select *
from GPA
         join Course C on GPA.CourseId = C.CourseId
         join Professor P on GPA.ProfessorId = P.ProfessorId
where Year = %s
  and Subject = %s;
"""

GET_ALL_DEPT_ABBR = """
SELECT distinct (Subject) FROM Course;
"""

GET_COURSE_GPA = """
select *
from GPA
         join Course C on GPA.CourseId = C.CourseId
         join Professor P on GPA.ProfessorId = P.ProfessorId
where Subject = %s
  and CourseNo = %s
group by Term, Year, CourseNo, Subject, Name, Title
;
"""

GET_GPA_BY_YEAR = """
select *
from GPA
         join Course C on GPA.CourseId = C.CourseId
         join Professor P on GPA.ProfessorId = P.ProfessorId
where Year = %s
group by Term, Year, CourseNo, Subject, Name, Title
;"""

GET_AVG_GPA = """
select Subject, avg(Value) as Average
from GPA
         join Course C on GPA.CourseId = C.CourseId
         join Professor P on GPA.ProfessorId = P.ProfessorId
where Year = %s
group by Subject
;
"""

GET_INSTRUCTOR_AVG_GPA = """
select distinct *
from GPA
         join Course C on GPA.CourseId = C.CourseId
         join Professor P on GPA.ProfessorId = P.ProfessorId
where P.Name = %s
group by Term, Year, CourseNo, Subject, Name, Title
;
"""

GET_PROF_NAME = """
select name
from Professor
where Name like %s
"""
