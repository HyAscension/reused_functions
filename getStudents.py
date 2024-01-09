import pandas as pd

def enrolled_only(df, year):
    df = df[df['SCHOOL_YR'] == year]
    df = df[(df['SIMPLE_ENROLL_STATUS'] == 'Enrolled') | (df['SIMPLE_ENROLL_STATUS'] == 'Pending')]
    return df

def current_year(path, cols, cols_renamed, current_yr):
    df = pd.read_csv(path, usecols=cols)
    df = enrolled_only(df, current_yr)
    df = df[
        (df['OFFICIAL_GRADE'] == '9') 
        | (df['OFFICIAL_GRADE'] == '10') 
        | (df['OFFICIAL_GRADE'] == '11') 
        | (df['OFFICIAL_GRADE'] == '12') 
        | (df['OFFICIAL_GRADE'] == 'PG')]
    df.columns = cols_renamed
    #df.to_excel('Path.xlsx', index=False)
    return df

path = ''
cols = []
cols_renamed = []
current_year(path, cols, cols_renamed, '')