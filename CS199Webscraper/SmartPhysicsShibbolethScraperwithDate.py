import sys 
import urllib.request 
import requests
from bs4 import BeautifulSoup

HTMLFileToBeOpened = open("/home/imanengineer2/CS199Webscraper/Physics 211 Spring 2024.html", "r") 
contents = HTMLFileToBeOpened.read() 
soup = BeautifulSoup(contents, 'html.parser')
parent_element = soup.find('div', class_='rc-smallcontent-panel')
if parent_element:
    rows = parent_element.find_all('div', class_='rc-row')
    planner_date = None
    assignments = []
    for row in rows:
        planner_date_element = row.find('div', class_='plannerdate')
        if planner_date_element:
            planner_date = planner_date_element.text.strip()
        assignment_items = row.find_all('div', class_='planneritem')
        for item in assignment_items:
            title_element = item.find('span', class_='pit-title').find('a')
            title = title_element.text.strip()
            due_date_element = item.find('div', class_='planneritem-time')
            due_date = due_date_element.text.strip()
            assignment = {'planner_date': planner_date, 'title': title, 'due_date': due_date}
            assignments.append(assignment)

    for assignment in assignments:
        print(f"Planner Date: {assignment['planner_date']}, Assignment: {assignment['title']}, Due Date: {assignment['due_date']}")
