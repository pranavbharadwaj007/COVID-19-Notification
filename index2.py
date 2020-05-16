from plyer import notification
import requests
from bs4 import BeautifulSoup
import pandas as pd
from prettytable import PrettyTable
import time

def note(title,mess):
    notification.notify(
        title=title,
        message=mess,
        app_icon="cori.ico",
        timeout=4,
    )
def data(url):
    updat=requests.get(url)
    return updat.text
if __name__ == "__main__":
    while True:
        #note("india","corona varriorooo")
        gdata=data('https://www.mohfw.gov.in/')
        #print(gdata)
        states=""
        soup=BeautifulSoup(gdata,'html.parser')
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            states+=tr.get_text()
        states=states[1:]
        itemli=states.split("\n\n")
        

        favstates=['Delhi','Karnataka','Kerala']
        for item in itemli[0:32]:
            datait=item.split('\n')
            if datait[1] in favstates:
                #print(datait)
                cc="COVID-19 LIVE CASES!!!!"
                pp=f"State: {datait[1]}\t\t!!\n Total: {datait[2]}\n Cured: {datait[3]}\n Death: {datait[4]}\n"
                note(cc,pp)
        time.sleep(8)    