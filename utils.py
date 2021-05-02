import datetime
import pandas as pd



def validate_date(date):
    # Validate date given by user
    error = {'error': 'Invalid date format must "/stat DD.MM.YYYY"'}

    splited = date.split('.')

    if len(splited) != 3:
        return error

    try:
        type_checked_date = list(map(int, splited))
        d = datetime.date(type_checked_date[2], type_checked_date[1], type_checked_date[0])
    except:
        return error

    return d

def save_to_csv(data, file_path):
    confirmeds = [i['Confirmed'] for i in data]
    deaths = [i['Deaths'] for i in data]
    recovered = [i['Recovered'] for i in data]
    active = [i['Active'] for i in data]
    date = [i['Date'] for i in data]

    df = pd.DataFrame(list(zip(confirmeds, deaths, recovered, active, date)),
               columns =['Confirmed', 'Death', 'Recovered', 'Active', 'Date'])
    df.to_csv(file_path)

