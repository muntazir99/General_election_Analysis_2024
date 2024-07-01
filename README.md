# General_election_Analysis_2024

![Alt text](graphs/India-Election-Results-2024-Live--scaled.jpg)

## Introduction 
Recently we concluded the most awaited festivel of the democracy which is Indian General Election, after the election ECI released the data of each constituency and each candidate which contain information such as Candidate Name, Party, Total Votes, % of Votes and Postal Votes.
Here We are scrapping the data from the ECI website using BeautifulSoup, this repo contain :
1. scraper.py : This send the request to ECI website and from there it scrape data of all candidate based on there state and constituency.
2. data : This folder contain all data in structured way which can be further used for analysis of each state and constituency and make their seperate reports.
3. process.ipynb : After scraping there are few column which we dont require and few columns we need to add this process file is handeling all basic structure fixing of csv files.
4. analysis.ipynb : Here we are doing all the analysis possible and generating a basic report from our analysis.

## Report
1.  Total number of candidates: 8360
    This contain all candidate as well as NOTA as a Individual candidate from each constituency.

    Total number of candidates including NOTA: 8902
    This contain all candidate as well as NOTA as a single candidate from overall country.

    Total number of parties: 4664
    This count includes Independent candidates as a party

    Total number of registered parties: 744
    This count excludes Independent candidates

2.  Total Votes by State/Union Territory
    ![Alt text](graphs/total_votes_by_state.png)

