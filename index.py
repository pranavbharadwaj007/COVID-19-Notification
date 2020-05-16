from plyer import notification
import requests
from bs4 import BeautifulSoup
import pandas as pd
from prettytable import PrettyTable

def note(title,mess):
    notification.notify(
        title=title,
        message=mess,
        app_icon="cori.ico",
        timeout=24,
    )
def data(url):
    updat=requests.get(url)
    return updat.text
if __name__ == "__main__":
    #note("india","corona varriorooo")
    gdata=data('https://www.mohfw.gov.in/')
    #print(gdata)
    soup=BeautifulSoup(gdata,'html.parser')
    extract = lambda row: [x.text.replace('\n', '') for x in row]
    stats = []
    all_rows = soup.find_all('tr')
    for row in all_rows:
        stat = extract(row.find_all('td')) 
        
        if len(stat) == 5:
            stats.append(stat)
            
    new_cols = ["Sr.No", "States/UT","Confirmed","Recovered","Deceased"]
    state_data = pd.DataFrame(data = stats, columns = new_cols)
    state_data['Confirmed'] = state_data['Confirmed'].map(int)
    state_data['Recovered'] = state_data['Recovered'].map(int)
    state_data['Deceased']  = state_data['Deceased'].map(int)
    #select id for states
    x=state_data[14:15]
    print(x)
    y=f"\ncases::{x['Confirmed']}\n recovery::{x['Recovered']}"
    note("covid 19",y)
    table = PrettyTable()
    table.field_names = (new_cols)
    for i in stats:
        table.add_row(i)
    table.add_row(["","Total", 
                sum(state_data['Confirmed']), 
                sum(state_data['Recovered']), 
                sum(state_data['Deceased'])])
    print(table)

        

    
