import requests
from bs4 import BeautifulSoup
import pandas as pd

url= 'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2023'

def process_data(url):
  '''

  Purpose: This program scrapes a website to extract Billboard Hot 100 songs chart position,
  song title and artist and stores it in a datafram
  parameters: url (string): The URL of the webpage to scrape the Billboard Hot 100 data from.
  Returns: A csv dataframe containing the extracted data called DF1 or None if
  an error occurs during the scraping process.
  
  '''
  #list to store the number the song was on the billboard
  Position_on_chart=[]
  #list to store song titles
  Title=[]
  #list to store heights
  Artist=[]
  page=requests.get(url)

  #only process data on a website if the request is successful
  if page.status_code==200:
      
    #import raw html into beautful soup
    soup=BeautifulSoup(page.content,'html.parser')
    table=soup.find('table',{'class':'wikitable'})

    #looping through each row in the table and skipping the header
    for row in table.find_all('tr')[1:]:
      column=row.find_all('td') #extract the columns in each row
      if len(column)>=3: #makes sure the row has enough columns to extract the data 
        #adding data to the respected list 
        Position_on_chart.append(column[0].text.strip())
        Title.append(column[1].text.strip())
        Artist.append(column[2].text.strip())

    #creating a datafram from the data stored in the lists 
    data={'Position on chart':Position_on_chart,'Title':Title,'Artist':Artist}

    #convert the data into a dataframe
    df1=pd.DataFrame(data)

    #save dataframe into a CSV file
    df1.to_csv('Billboard_Year-End_Hot_100_singles_of_2023.csv',index=False)
    print('CSV file has been created')

    #displays the dataframe
    return df1
  else:
    print(f"Error: Failed to retrieve URL ({url}). Status code: {page.status_code}")
    return None

df1=process_data(url)
df1
