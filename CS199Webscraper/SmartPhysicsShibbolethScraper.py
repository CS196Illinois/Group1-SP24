import sys 
import urllib.request 
import requests
from bs4 import BeautifulSoup

# Opening the html file. If the file 
# is present in different location,  
# exact location need to be mentioned 
HTMLFileToBeOpened = open("/home/imanengineer2/CS199Webscraper/Physics 211 Spring 2024.html", "r") 
  
# Reading the file and storing in a variable 
contents = HTMLFileToBeOpened.read() 
  
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(contents, 'html.parser')

# Find the parent element containing all assignment information
parent_element = soup.find('div', class_='rc-smallcontent-panel')

# Check if the parent element is found
if parent_element:
    # Find all assignment items within the parent element
    assignment_items = parent_element.find_all('div', class_='planneritem')

    # Initialize a list to store assignment details
    assignments = []

    # Loop through each assignment item to extract title and due date
    for item in assignment_items:
        # Extract assignment title
        title_element = item.find('span', class_='pit-title').find('a')
        title = title_element.text.strip()

        # Extract due date
        due_date_element = item.find('div', class_='planneritem-time')
        due_date = due_date_element.text.strip()

        # Store assignment details in a dictionary
        assignment = {'title': title, 'due_date': due_date}

        # Append the assignment details to the list
        assignments.append(assignment)

    # Print the extracted assignments and their due dates
    for assignment in assignments:
        print(f"Assignment: {assignment['title']}, Due Date: {assignment['due_date']}")
else:
    print("Parent element containing assignment information not found.")