import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load the dataset
df = pd.read_csv("data/silver/jobs_cleaned.csv")
print(df.head())
print(df.shape)

# Check if the value is missng or NaN ,if yes then return true and no then False
print("Missing description", df["job_description"].isna().sum())

# To check if what value is in desc
print(df.loc[0,"job_description"])
print(df.loc[0,"apply_url"]) # This will give the entire URL with apply link

# To remove the apply part and keep only the job description page - Only for the first job
job_url = df.loc[0, "apply_url"].split("/apply")[0]
print(job_url)

headers = {
    "User-Agent" :"Mozilla/5.0"
}
response = requests.get(job_url, headers = headers , timeout =30)

print(response.status_code)
print(response.headers.get("Content-Type"))
print(response.text[:500])

# To check if these title are presnt in the response data then they are present in the HTML not the external API like before
print("Position Purpose" in response.text)
print("Responsibilities" in response.text)
print("Delivery Coordinator" in response.text)

# To extract the data from HTML, beautifulsoup will used
soup = BeautifulSoup(response.text, 'html.parser')

page_text = soup.get_text(" ", strip=True)
print(page_text[:1000])

print(type(soup))
print(type(page_text))
print(len(page_text))

# position = response.text.find("Position Purpose")
# print(position)
# print(response.text[position -200: position +500]) # THis means that it present in the HTML meta tag not the raw html

# description_tag = soup.find("meta", attrs= {"name" : "description"})
# # print(description_tag)

# # Extract only description text
# job_description = description_tag.get("content")
# print(job_description[0:500])

# print("SQL:", "SQL" in job_description.lower())
# print("Python:", "Python" in job_description.lower())
# print("Excel:", "Excel" in job_description.lower())
# print("Logistics:", "logistics" in job_description.lower())
# print("Customer:", "customer" in job_description.lower())


# Created an empty list to store every jobs skills result


skills = [
    "sql",
    "python",
    "excel",
    "power bi",
    "tableau",
    "azure",
    "snowflake",
    "databricks",
    "spark",
    "git"
]
# TO check every skills one by one in the job description if its match or not
# for skill in skills:
#     print(skill,":", skill in job_description.lower())

# # Store the output in the dictionary
# skills_found = {}
# for skill in skills:
#     skills_found[skill] = skill in job_description.lower()

# print(skills_found)


# all_skill_results = []
# # Loop to iterate every row in the dataframe
# for index,row in df.iterrows():
#     print(index, row["job_title"])

# # To get the job-url and then split the url to get the actual job description url
#     job_url = row["apply_url"].split("/apply")[0]
#     headers = {
#         "user-agent" : "Mozilla/5.0"
#     }
#     response = requests.get(job_url, headers =headers)
#     print(index, response.status_code)

# # To get the meta tag where the actual description lies and print first 500 characters
#     soup = BeautifulSoup(response.text, "html.parser")
#     description_tag = soup.find("meta", attrs= {"name" : "description"})
  
#     job_description =(
#         description_tag.get("content")
#         if description_tag
#         else ""
#     )
#     if job_description is None:
#        job_description = "" 
    

# # Create dictionary for skills.Each job has their own skills mentioned in the job description and we need all the skills data for each job
#     skills_found = {}
#     for skill in skills:
#         skills_found[skill] = skill in job_description.lower()

#     all_skill_results.append(skills_found)

#     # print(f"Processed {index + 1} of {len(df)} jobs")

# print(len(all_skill_results))

# # # Convert the list of dictionary into a Dataframe
# # To store the loop results in to csv file so we dont have to run the loop again for 271 rows
# skills_df = pd.DataFrame(all_skill_results)
# skills_df.to_csv("data/Gold/skills_only.csv", index = False)

# print(skills_df.head())
# print(skills_df.shape)

skills_df = pd.read_csv("data/gold/skills_only.csv")

# merge the two dataframes (Jobs and skills)
gold_df = pd.concat(
    [df.reset_index(drop =True), skills_df.reset_index(drop=True)],
    axis =1
)

print(gold_df.head())
print(gold_df.shape)

# Save the gold dataset to csv file and store in data folder
gold_df.to_csv("data/Gold/jobs_with_skills.csv",index = False)

# To check the data is store correctly.
saved_gold_df = pd.read_csv("data/Gold/jobs_with_skills.csv")
print(saved_gold_df.shape)