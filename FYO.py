import pandas as pd
from datetime import datetime


def process_file(filename):
    csv_file = pd.read_csv(filename, encoding='cp1252')
    res = ['ON-CAMPUS', 'SJU', 'STP', 'SJ Arts', 'Renison', 'CONRAD', 'OFF-CAMPUS']
    faculty = ['Arts', 'Engineering', 'Software', 'Math', 'Science','AHS', 'Environment']

    name = 'FYOmultiple.xlsx'
    writer = pd.ExcelWriter(name, engine='openpyxl')


    df = csv_file.loc[(csv_file['Committee'] == 'Architecture')]
    df.is_copy = False

    df['Start Date'] = pd.to_datetime(df['Start Date'], format='%Y-%m-%d').dt.strftime('%Y-%m-%d')
    try:
        df['Start Time'] = pd.to_datetime(df['Start Time'], format='%I:%M %p').dt.strftime('%I:%M %p')

    except ValueError:

        print(df['Subject'])

    df.insert(loc=10, column="Date Time", value= df['Start Date'].str.cat(df[['Start Time']], sep=' '))
    df['Date Time'] = pd.to_datetime(df['Date Time'])
    df = df.sort_values(by=['Date Time'])

    df.insert(loc=11, column="Date in Words", value= pd.to_datetime(df['Start Date'], format='%Y-%m-%d').dt.strftime('%A, %d %B, %Y'))
    df.insert(loc=12, column="Event; Location",
                    value= df['Subject'].str.strip()+ "; " + df['Location'].str.strip())

    df.insert(loc=13, column="Start time - end time",value=df['Start Time']+ " - " + df['End Time'].str.strip())
    del df['Rainplan Location']
    df.to_excel(writer, sheet_name= "Architecture")

    for r in res:
        for f in faculty:
            df = csv_file.loc[(csv_file['Committee'] == f) | (csv_file['Committee'] == r)]
            df.is_copy = False
            # df['Start Date'] = pd.to_datetime(df['Start Date'], format='%Y-%m-%d').dt.strftime('%Y-%m-%d')
            df['Start Time'] = df['Start Time'].str.strip()


            df['Start Date'] = pd.to_datetime(df['Start Date'], format='%Y-%m-%d').dt.strftime('%Y-%m-%d')

            df["Start Time"] = df["Start Time"].str.strip()

            try:
                df['Start Time'] = pd.to_datetime(df['Start Time'], format='%I:%M %p').dt.strftime('%I:%M %p')

            except ValueError:

                print(df['Subject'])

            df = df.fillna("")


            df.insert(loc=10, column="Date Time", value= df['Start Date'].str.cat(df[['Start Time']], sep=' '))
            df['Date Time'] = pd.to_datetime(df['Date Time'])
            df = df.sort_values(by=['Date Time'])

            df.insert(loc=11, column="Date in Words", value= pd.to_datetime(df['Start Date'], format='%Y-%m-%d').dt.strftime('%A, %d %B, %Y'))

            df.insert(loc=12, column="Event; Location",value= df['Subject'].str.strip() + "; " + df['Location'].str.strip())


            df.insert(loc=13, column="Start time - end time",
                    value=df['Start Time']+ " - " + df['End Time'].str.strip())
            del df['Rainplan Location']
            df.to_excel(writer, sheet_name= f + " " + r)

    writer.save()
    return name


