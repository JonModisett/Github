import os
import pandas as pd

#initials
df = pd.DataFrame

"""
TODO:
File Selction Process
Standardized Table
Initial Data Insights
GUI interface
"""
## Support for CSV, JSON, Excel, XML

#Grabbing filename from users documents
documents = [f for f in os.listdir()]

for idx, doc in enumerate(documents, start=1):
    print(f"{idx}, {doc}")
          
#Allow user to select file
file_choice = int(input("Please input a number for the specific file: "))
filename = documents[file_choice - 1] #Offset the initial 1 above
print(f"\nThe file selected is: {filename}")

#Initial Load, creating modular
def fileload():
    try:
        with open(filename, 'r') as file:
            content = file.read()
            contents = content
#Error Handling
    except FileNotFoundError:
        print("File not found.")
