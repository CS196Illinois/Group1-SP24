import sys 
import urllib.request  
import requests
import time
from bs4 import BeautifulSoup

HTMLFileToBeOpened = open("/home/imanengineer2/CS199Webscraper/Physics 211 Spring 2024.html", "r") 
contents = HTMLFileToBeOpened.read() 
soup = BeautifulSoup(contents, 'html.parser')

# Find the assignments pannel in smartphysics
parent_element = soup.find('div', class_='rc-smallcontent-panel')

if parent_element:
    # Extract rows representing individual assignments or schedule entries
    rows = parent_element.find_all('div', class_='rc-row')

    # Initialize variables to store extracted data
    planner_date = None
    assignments = []

    # Process each row
    for row in rows:
        # Find the date associated with this row of assignments
        planner_date_element = row.find('div', class_='plannerdate')
        planner_date = planner_date_element.text.strip()

        # Find assignment items within the row
        assignment_items = row.find_all('div', class_='planneritem')

        # Process each assignment item
        for item in assignment_items:
            # assignment title
            title_element = item.find('span', class_='pit-title')
            if title_element is not None:
                title = title_element.text.strip()

                # due date
                due_date_element = item.find('div', class_='planneritem-time')
                due_date = due_date_element.text.strip()

                # Create a dictionary to represent this assignment
                assignment = {
                    'planner_date': planner_date, 
                    'title': title, 
                    'due_date': due_date
                    }
                assignments.append(assignment)

    # Print info
    for assignment in assignments:
        print(f"Due Date: {assignment['planner_date']}, Assignment: {assignment['title']}, Time Due: {assignment['due_date']}") 
        time.sleep(.01)  # delay to make it look cool printing
def get_homework():
    return assignments