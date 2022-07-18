# Pararius-Scraper
A python script that scrapes the information of rental apartments of a particular city from multiple pages of www.pararius.com. Built using beautifulsoup library in Python.

![image](https://user-images.githubusercontent.com/105808186/179462091-65dc07db-2bd3-4391-bfe1-d73fc27652a6.png)

# Installation
Open any terminal and run the following command
```
pip install beautifulsoup4
```

# Working
Enter the desired city and no. of web pages that you want to scrape and run the script.
```
city="amsterdam/"
home_page="https://www.pararius.com/apartments/" + city
total_pages=10
 ```

# Result

![image](https://user-images.githubusercontent.com/105808186/179462934-8fd3e636-ca3e-418a-a5c3-74b6824011f6.png)

A local CSV file will be created with the following informations

![image](https://user-images.githubusercontent.com/105808186/179463251-732274ef-39ad-444a-9cdc-de7f41cb029a.png)

