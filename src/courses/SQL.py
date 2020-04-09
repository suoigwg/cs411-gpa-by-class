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
