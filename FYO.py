import pandas as pd
from datetime import datetime

csv_file = pd.read_excel("C:/Users/Jacinto D'Souza/Documents/Waterloo/Management Engineering/3B/MSCI 342 - Principles of Software Eng/Team-4-2019-Project/FYO Track Sessions for Portal - for MSCI group_REV1.xlsx")

res = ['ON-CAMPUS', 'SJU', 'STP', 'SJ Arts', 'Renison', 'CONRAD', 'OFF-CAMPUS']
faculty = ['Arts', 'Engineering', 'Software', 'Math', 'Science','AHS', 'Environment']


writer = pd.ExcelWriter('FYOmultiple.xlsx', engine='openpyxl')


df = csv_file.loc[(csv_file['Committee'] == 'Architecture')]
df.is_copy = False

df['Start Date'] = pd.to_datetime(df['Start Date'], format='%Y-%m-%d').dt.strftime('%Y-%m-%d')
df['Start Time'] = (pd.to_datetime(df['Start Time'].str.strip(), format='%I:%M %p')
                  .dt.strftime('%H:%M'))

df['Date Time'] = df['Start Date'].str.cat(df[['Start Time']], sep=' ')

df.sort_values(by=['Date Time'], ascending=True)
df.to_excel(writer, sheet_name= "Architecture")

for r in res:
    for f in faculty:
        df = csv_file.loc[(csv_file['Committee'] == f) | (csv_file['Committee'] == r)]
        df.is_copy = False

        df.to_excel(writer, sheet_name= f + " " + r)
writer.save()



