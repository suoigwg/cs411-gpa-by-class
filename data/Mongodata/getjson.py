import pandas as pd
import json
"""
info.csv is generated by sqlite
sqlite query:
sqlite >.headers on
sqlite >.mode csv
sqlite >.output info.csv
sqlite >. SELECT AVG(value) as avgVal, C.Subject, C.CourseNo, C.CourseId
sqlite >. FROM GPA
sqlite >. JOIN Course C on GPA.CourseId = C.CourseId
sqlite >. GROUP BY C.CourseId
info.csv schema:
avgVal subject CourseNo CourseId
"""
gpa_df=pd.read_csv('info.csv')
gpa_df= gpa_df\
    .drop_duplicates(['Subject', 'CourseNo'],keep='last')
gpa_df['CourseNo']=gpa_df['CourseNo'].astype('str')
gpa_df['Course']=gpa_df['Subject']+' '+gpa_df['CourseNo']
avg_gpa=pd.Series(gpa_df.avgVal.values,index=gpa_df.Course).to_dict()
with open ("avg_gpa.json","w") as f:
    json.dump(avg_gpa,f)

    