
#importing our libraries
import requests
from bs4  import BeautifulSoup
import pandas as pd

#organizing our urls into a dictionary
sports_teams = {
                    'mens_volleyball': ['https://ccnyathletics.com/sports/mens-volleyball/roster?view=2', 'https://lehmanathletics.com/sports/mens-volleyball/roster',
                                        'https://www.brooklyncollegeathletics.com/sports/mens-volleyball/roster','https://johnjayathletics.com/sports/mens-volleyball/roster', 'https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster?view=2',
                                        'https://lindenwoodlions.com/sports/mens-volleyball/roster?view=2','https://www.huntercollegeathletics.com/sports/mens-volleyball/roster?sort=name', 'https://yorkathletics.com/sports/mens-volleyball/roster','https://csidolphins.com/sports/mens-volleyball/roster?view=2'],
                    'mens_swimming_diving':['https://csidolphins.com/sports/mens-swimming-and-diving/roster/2023-2024?view=2','https://yorkathletics.com/sports/mens-swimming-and-diving/roster',
                                            'https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster?view=2','https://www.brooklyncollegeathletics.com/sports/mens-swimming-and-diving/roster/2019-20',
                                            'https://lindenwoodlions.com/sports/mens-swimming-and-diving/roster/2021-22','https://mckbearcats.com/sports/mens-swimming-and-diving/roster/2023-24','https://ramapoathletics.com/sports/mens-swimming-and-diving/roster','https://oneontaathletics.com/sports/mens-swimming-and-diving/roster',
                                            'https://bubearcats.com/sports/mens-swimming-and-diving/roster/2021-22','https://albrightathletics.com/sports/mens-swimming-and-diving/roster/2021-22'],
                    'womens_volleyball': ['https://athletics.baruch.cuny.edu/sports/womens-volleyball/roster/2024?view=2','https://yorkathletics.com/sports/womens-volleyball/roster','https://hostosathletics.com/sports/womens-volleyball/roster/2022-2023','https://bronxbroncos.com/sports/womens-volleyball/roster/2021',
                                          'https://queensknights.com/sports/womens-volleyball/roster','https://augustajags.com/sports/wvball/roster','https://flaglerathletics.com/sports/womens-volleyball/roster','https://pacersports.com/sports/womens-volleyball/roster','https://www.golhu.com/sports/womens-volleyball/roster'],
                    'womens_swimming_diving':['https://csidolphins.com/sports/womens-swimming-and-diving/roster/2023-2024?view=2','https://queensknights.com/sports/womens-swimming-and-diving/roster/2019-20','https://yorkathletics.com/sports/womens-swimming-and-diving/roster','https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster/2021-22?path=wswim','https://www.brooklyncollegeathletics.com/sports/womens-swimming-and-diving/roster/2022-23?view=2',
                                              'https://lindenwoodlions.com/sports/womens-swimming-and-diving/roster/2021-22?view=2','https://mckbearcats.com/sports/womens-swimming-and-diving/roster','https://ramapoathletics.com/sports/womens-swimming-and-diving/roster','https://keanathletics.com/sports/womens-swimming-and-diving/roster','https://oneontaathletics.com/sports/womens-swimming-and-diving/roster/2021-22?view=2']
                }


def webscraper1(urls,team_name):

    '''
    Purpose: This program scrapes player names and heights from a list of team roster URLs, cleans the height data, converting into inches and saves it to a CSV file.
    Parameters:
        urls (list of str): A list of URLs for team rosters to scrape player information from.
        team_name (str): The name of the team, used to name the output CSV file.
    Returns: A DataFrame containing two columns — 'Name' and 'Height' (in inches).
    '''

    # Lists to store names and heights
    names = []
    heights = []

    # Loop through each URL
    for url in urls:
        # Make a request to the server
        page = requests.get(url)

        # Only process data on a website if the request is successful
        if page.status_code == 200:

            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(page.content, 'html.parser')

            # Extracting height and name tags
            height_tags = soup.find_all('td', class_='height')
            name_tags = soup.find_all('td', class_='sidearm-table-player-name')

            #extracting the content from the td tags for names
            for name_tag in name_tags:
              names.append(name_tag.get_text().strip())

              # extracting the content from the td tags for heights
            for height_tag in height_tags:
              raw_height = height_tag.get_text()

        # extract the feet and inches from the string and converting them to floats
            for height_tag in height_tags:
              raw_height = height_tag.get_text()
        # extract the feet and inches from the string and converting them to floats
              feet = float(raw_height.split('-')[0]) * 12 # converting the feet to inches
              inches = float(raw_height.split('-')[1])

              height_in_inches = feet + inches
              heights.append(height_in_inches)
              
    # Build a pandas DataFrame from the collected data
    data = {
        'Name': names,
        'Height': heights
    }

    df = pd.DataFrame(data)

    #converts into csv files
    df.to_csv(f'{team_name}.csv', index=False)
    print(f'CSV file has been created for {team_name}')

    return df

#calls the function for each team
mens_volleyball_df = webscraper1(sports_teams['mens_volleyball'], 'mens_volleyball')
mens_swimming_diving_df = webscraper1(sports_teams['mens_swimming_diving'], 'mens_swimming_diving')
womens_volleyball_df=webscraper1(sports_teams['womens_volleyball'],'womens_volleyball')
womens_swimming_diving_df =webscraper1(sports_teams['womens_swimming_diving'], 'womens_swimming_diving')

print(mens_volleyball_df)
print(mens_swimming_diving_df)
print(womens_volleyball_df)
print(womens_swimming_diving_df)
