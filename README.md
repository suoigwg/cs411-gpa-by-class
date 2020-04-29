# cs411-gpa-by-class
First activate the python virtual environment

Windows: type ".\venv\Scripts\activate"

Mac/Linux: type "source venv/Scripts/activate"

Run backend: "python manager.py runserver"

Run frontend:

Navigate to frontend folder

Run "npm run dev"


API Reference:

UserService:

POST /users/login/

Input: {username, password}

Response: 200 or 400

{username, isAdmin}

POST /users/register/

Input: {username, password, isAdmin}

Response: 200 or 400

CoursesService:

GET /api/courses/

Input: {subject}

Response: [List of courses]

http://127.0.0.1:8000/api/courses/?subject=MATH

[{"courseid": 1, "courseno": 10, "subject": "MATH", "title": "Linear Algebra"}, {"courseid": 2, "courseno": 12, "subject": "MATH", "title": "Algebra"}, {"courseid": 3, "courseno": 14, "subject": "MATH", "title": "Trigonometry"},...]

http://127.0.0.1:8000/api/courses/?subject=LING

[{"courseid": 40, "courseno": 100, "subject": "LING", "title": "Intro to Language Science"}, {"courseid": 273, "courseno": 105, "subject": "LING", "title": "Language in Daily Life"}, {"courseid": 355, "courseno": 111, "subject": "LING", "title": "Language in Globalization"},...]

Get /api/subjects/

Input: None

Response: [List of subject codes]

http://127.0.0.1:8000/api/subjects

[{"subject": "AAS"}, {"subject": "ABE"}, {"subject": "ACCY"},...]

POST /api/courses/new

POST /api/courses/updated

POST /api/courses/deleted

Input: {courses: [List]}

Response: 200 or 400

GPAService:

GET /api/coursegpa/

Input: {subject, number}

Response: [List of GPA info] + (professor_name, subject, number)

http://127.0.0.1:8000/api/coursegpa/?subject=MATH&number=415

[{"term": "fa", "value": 2.85, "courseid": 4733, "classsize": null, "year": 2010, "professorid": 2684, "gpaid": 54362}, {"term": "fa", "value": 3.08, "courseid": 4733, "classsize": null, "year": 2010, "professorid": 1204, "gpaid": 54363}, {"term": "fa", "value": 2.73, "courseid": 4733, "classsize": null, "year": 2010, "professorid": 3250, "gpaid": 54364},

POST /api/coursesgpa/new

POST /api/coursesgpa/updated

POST /api/coursesgpa/deleted

Input: {gpas: [List]}

Response: 200 or 400

Get /api/courseNumbers/

Input: None

Response: [List of course Numbers] (CS411, CS233, ..)

(Currently there are some undesired method)

ProfessorService:

Get /api/professorNames/

Input: None

Response: [List of professor names]

http://127.0.0.1:8000/api/professorNames/

[{"name": "Aadland, Matthew A"}, {"name": "Aaron, Benjamin L"}, {"name": "Abbamonte, Peter M"}, {"name": "Abbas, Ali E"}, {"name": "Abbott, Annie R"}, {"name": "Abbott, Michael O"}, {"name": "Abd El Khalick, Fouad"},...]



## nosql 
**Firstly, ensure MongoDB service is running on your PC**
 mongo

**Navigate to src file**
python3 manage.py migrate --database mongo
python3 makemigrations
python3 manage.py loaddata ./courses/fixtures/db_course_preq.json --app courses.CoursePrereqModel
python3 manage.py runsever 



