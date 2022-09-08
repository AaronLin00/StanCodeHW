"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        tags = soup.tbody.find_all('td')
        num = []
        for tag in tags:
            new = tag.text
            if len(new) > 3 and new[0].isdigit() is True:
                new_number = str(new[:(len(new)-4)]) + str(new[(len(new)-3):])
                num.append(new_number)
        male_total = 0
        female_total = 0
        for i in range(len(num)):
            if i % 2 == 0:
                male_total += int(num[i])
            else:
                female_total += int(num[i])
        print('Male Number: '+str(male_total))
        print('Female Number: '+str(female_total))


if __name__ == '__main__':
    main()
