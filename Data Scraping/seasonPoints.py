# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv

year_list = [2018,2017,2016,2015,2014,2013,2012,2011,2010]

# Create and write headers to a list
rows = []
rows.append(['Player Name', 'Events','Points', '# of Wins', '# of Top 10','Year'])
#print(rows)

# Loop through all the different years
for i in year_list:
    i = str(i)
    # defining the url page
    urlpage = 'https://www.pgatour.com/stats/stat.02394.' + i + '.html'

    # Query the website and return the html to the variable 'page'
    page = urllib.request.urlopen(urlpage)

    # Parse the html using beautiful osup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')
    #print(soup)

    # Find results within table
    table = soup.find('table', attrs={'class': 'table-styled'})
    results = table.find_all('tr')
    #print('Number of results', len(results))
    #print(results)

    # The columns you want: RANK THIS WEEK, PLAYER NAME, ROUNDS, AVG., TOTAL DISTANCE, TOTAL DRIVES, YEAR

    # Year of data collected
    year = i

    # Loop over results
    for result in results:
        # find all columns per result
        data = result.find_all('td')

        # check that columns have data
        if len(data) == 0:
            continue

        # assign columns to variables
        rank_week = data[0].getText()
        rank_last = data[1].getText()
        name = data[2].getText()
        event = data[3].getText()
        points = data[4].getText()
        num_win = data[5].getText()
        num_10 = data[6].getText()

        # Removing \n and spaces in rank_week and rank_last
        rank_week = rank_week.replace('\n','')
        rank_week = rank_week.strip()

        rank_last = rank_last.replace('\n','')
        rank_last = rank_last.strip()

        # Remove \n in name
        name = name.replace('\n','')

        #write each result to rows
        rows.append([name, event, points, num_win, num_10, year])

    print(rows)

# Create a csv file and write rows to the file
with open('seasonPoints.csv', 'w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)
