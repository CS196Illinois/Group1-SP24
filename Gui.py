import tkinter as tk
import csv
import os
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk 
from SmartPhysicsShibbolethScraperwithDate import get_homework

def update_assignments():
    for item in tree.get_children():
        tree.delete(item)
    assignments = get_homework()
    for assignment in assignments:
        tree.insert("", tk.END, values=(assignment['title'], assignment['planner_date'] + '|' + assignment['due_date']))



window = ThemedTk(theme='adapta')  # Theme
window.title("SmartPhysics Assignments")


#Column GUI
tree = ttk.Treeview(window, columns=("name", "date"), show="headings", style="mystyle.Treeview")
tree.heading("name", text="Assignment Name")
tree.heading("date", text="Date Due")

tree.heading("name", text="Assignment Name", anchor=tk.N)
tree.heading("date", text="Date Due", anchor=tk.N)

tree.column("name", width = 390, stretch=tk.YES, anchor=tk.W) 
tree.column("date", width = 200, stretch=tk.YES, anchor=tk.E)  

style = ttk.Style(window)
style.configure("mystyle.Treeview", background="#15BF73", foreground="#060270")  # Style
tree.pack()

# Export to CSV
def export_assignments():
    if not messagebox.askyesno("Confirm Export", "Do you want to export assignments to /home/imanengineer2/CS199Webscraper/CSV Files?"):
        return
    
    csv_folder = "/home/imanengineer2/CS199Webscraper/CSV Files" 
    now = datetime.now()
    filename = now.strftime("%Y-%m-%d_%H-%M-%S_assignments.csv")

    with open(os.path.join(csv_folder, filename), 'w', newline='') as csvfile:
        fieldnames = ['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'All Day Event', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        assignments = get_homework()

        for assignment in assignments:
            # Extract date 
            date_parts = assignment['planner_date'].split(', ')[1].split(' ')
            month, day = date_parts[0], date_parts[1]

            year = 2024  # Assuming this year for now this will need to be modified down the line

            # Reformat date
            due_date_formatted = datetime.strptime(f"{year}-{month}-{day}", '%Y-%B-%d').strftime('%Y-%m-%d')

            writer.writerow({
                'Subject': assignment['title'],
                'Start Date': due_date_formatted, 
                'All Day Event': 'TRUE',
                'Description': ''  # Possibly add notes
            })

# Button Layout and Styling
button_frame = tk.Frame(window)
refresh_button = tk.Button(button_frame, text="Refresh", command=update_assignments)
refresh_button.pack(side=tk.LEFT, padx=5) 
export_button = tk.Button(button_frame, text="Export to Calendar", command=export_assignments)
export_button.pack(side=tk.LEFT, padx=5)
button_frame.pack()

#initial setup
update_assignments()

window.mainloop()