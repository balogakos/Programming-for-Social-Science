# -*- coding: utf-8 -*-
'''
Created on Mon Oct 10 10:57:21 2022

@author: Akos
'''
import requests
import bs4

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html', verify=False)
content = r.text

soup = bs4.BeautifulSoup(content, 'html.parser')

td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

