from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

# Extract

def extract(url):
    page = requests.get(url)
    return page
    

def transform(page):
    
    soup = BeautifulSoup(page.content, 'html.parser')
    data1 = soup.find_all('div', 
                          class_ = 'w-1/2 text-center break-word p-1 dark:text-white')
    data2 = soup.find_all('span', 
                          class_ = 'flex justify-center items-center h-7 w-6 rounded-md font-semibold bg-primary-green text-white mx-1')
    
    names_loc = []
    names_vis = []
    res_loc = []
    res_vis = []


    for index in range(len(data1)):
        
        texto = data1[index].text
        name = re.sub('\n+','',texto)
        if index%2 == 0:
            names_loc.append(name)
        else:
            names_vis.append(name)
            
    for index in range(len(data2)):
        res = data2[index].text        
        if res == '1':
            res_loc.append('Gana')
            res_vis.append('Pierde')
        elif res == '2':
            res_loc.append('Pierde')
            res_vis.append('Gana')
            
    return names_loc,names_vis,res_loc,res_vis
            
def load(names_loc,names_vis,res_loc,res_vis):
    
    df = pd.DataFrame({'Local':names_loc,
                       'Visitante':names_vis,
                       'Result. local': res_loc,
                       'Result. visit.':res_vis })
    print(df)
    df.to_csv('pronostico.csv')
    
    
if __name__=='__main__':
    page = extract(url = 'https://www.sportytrader.es/pronosticos/baloncesto/usa/nba-306/')
    names_loc,names_vis,res_loc,res_vis = transform(page)
    load(names_loc,names_vis,res_loc,res_vis)