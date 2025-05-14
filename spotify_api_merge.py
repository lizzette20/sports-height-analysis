import requests
import base64 #this library is used to encode our spotify cilent credentials
import json
import pandas as pd 
from urllib.parse import quote

#Spotify client credentials (required to authorize API access)
client_id = 'c4edcf1c104a42578afc2347bb8896c8'
client_secret = 'fe74831ff9a543de811f9112ba9a9128'

#Encoded client credentials in Base64 as required by Spotify
client_credentials = f"{client_id}:{client_secret}"
client_credentials_b64 = base64.b64encode(client_credentials.encode()).decode()

#Token request endpoint
token_url = "https://accounts.spotify.com/api/token"

#Request headers and body for access token
headers = {
    'authorization': f'basic {client_credentials_b64}',
    'content-type': 'application/x-www-form-urlencoded' #tells spotify we're sending form data
}
data = {
    'grant_type': 'client_credentials'
}

#Request access token
response = requests.post(token_url, headers=headers, data=data)


#Validating the token request and extracting access token if successful
if response.status_code == 200: 
    token_info = response.json()
    access_token = token_info['access_token']
    print (f'Access token recieved successfully')
    print (f'Access token: {access_token}')

else: 
    #Handle failed token request by logging the status and error details
    print(f'Failed to retrieve access token.')
    print(f'Status code: {response.status_code}')
    print(f'Error message: {response.text}')


#Loading DF1/ scrapped billboard data
df1 = pd.read_csv('Billboard_Year-End_Hot_100_singles_of_2023.csv')
print(df1.head()) #printing first few rows to confirm successful loading

#Initializing an empty list to store track details returned from spotify
spotify_data=[]

#Looping through each song title in the Billboard dataset to query Spotify's API
for x in range(len(df1)):
    title = df1['Title'][x]
    #print(f'Searching spotify for: {title}')
    encoded_title = quote(title)

#Setting our url
    url = f'https://api.spotify.com/v1/search?q={encoded_title}&type=track&limit=1'

    #Providing our access token for authentication
    headers = {
    'Authorization': 'Bearer BQDZP3KHIUX_gs8_5RlNUECDVIKxpTUfBzPI75yqpgiks28bS4iqeVzAkBKUMyBtwcj1v246WHzvEoL93O3YOG9yIvkZkTrYqVjZHQW-YL5ShksrPmt5tSeM5ma1QghWHxVtrzVuaPI'
    }

    #Send GET request to Spotify API
    r = requests.get(url, headers=headers)
    print(r.status_code)

    #If the request is successful, proceed to parse the response
    if r.status_code == 200:
        data = r.json()

    #Formating raw json for readability
    formatted_json = json.dumps(data, sort_keys = True, indent = 5)
    #print(formatted_json)

    #Checking if the search returned at least one track
    if data['tracks']['items']:
        track = data['tracks']['items'][0]
        #Extract relevant track details from the JSON response
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        album_name = track['album']['name']
        popularity = track['popularity']
        spotify_url = track['external_urls']['spotify']

        # Optional (for debugging or reviewing as the loop runs):
        # print(f'Track name: {track_name}')
        # print(f'Artist name: {artist_name}')
        # print(f'Album name: {album_name}')
        # print(f'Popularity ranking: #{popularity}')
        # print(f'Spotify URL: {spotify_url}')  

        #Append extracted data to our list as a dictionary
        spotify_data.append({
            'Track name': track_name,
            'Spotify Artist': artist_name,
            'Album': album_name,
            'Popularity ranking #': popularity,
            'Spotify URL': spotify_url

        })

    else: 
        #If no track data is returned, log it and append None placeholders
        print(f'Error requesting song: {title}')
        spotify_data.append({
            'Track name': None,
            'Artist': None, 
            'Album': None,
            'Popularity ranking #': None,
            'Spotify URL': None,
        })

#Converting the list of dictionaries into a DataFrame (DF2)
df2 = pd.DataFrame(spotify_data)

#Resetting indexes for both DataFrames to ensure proper alignment during concatenation
df2 = df2.reset_index(drop=True)
df1 = df1.reset_index(drop=True)

#Renaming 'Artist' column in DF1 to avoid column name conflict during merge
df1 = df1.rename(columns={'Artist': 'Billboard Artist'})

#Concatenating Billboard and Spotify dataframes horizontally
df3 = pd.concat([df1, df2], axis=1)

#Saving the merged dataframe to a CSV file and displaying summary statistics
df3.to_csv('Billboard_Spotify_Merged.csv', index=False)
print("CSV file exported as 'Billboard_Spotify_Merged.csv'")
print(df3.head()) #Preview first few rows of merged data
print(df3.describe(include='all')) #Displaying summary statistics

#Optional: reloading the CSV to confirm final export worked
df = pd.read_csv('Billboard_Spotify_Merged.csv')
