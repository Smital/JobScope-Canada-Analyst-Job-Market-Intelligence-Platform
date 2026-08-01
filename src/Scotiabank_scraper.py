import requests
from bs4 import BeautifulSoup

# Get the URl for all active jobs in all categories
url = 'https://careers.homedepot.ca/job-search'

#header is use to tell the scotibank website that the request is from the actual crome,safari or mozilla
#browser not from bot or hackers are trying get the content
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/150.0 Safari/537.36"
}
#get the html page content using .get requests method
response = requests.get(url, headers=headers)

#Check the stattus code
print(response.status_code)
#print the actual content of html
print(response.text)

#Create a soup obeject to parse the html content and get the title 
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)

#Create a page.html file and write the whole html content to this file using write command
with open("page.html","w") as file:
    file.write(response.text)

print("Analyst" in response.text)
print("Toronto" in response.text)
print("/job/" in response.text)