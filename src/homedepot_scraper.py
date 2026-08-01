import requests
import pandas as pd

url = "https://careers.homedepot.ca/job-search/jobs"
headers = {
    "user-agent" : "Mozilla/5.0",
    "Accept" : "application/json, text/javascript, */*; q=0.01",
    "Conten-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin" : "https://careers.homedepot.ca",
    "referer": "https://careers.homedepot.ca/job-search",
    "X-Requested-With": "XMLHttpRequest"
}
payload = {
    "saved_jobs": "",
    "saved_jobs_only": "false",
    "new_search": "1",
    "keyword": "",
    "sortBy": "Proximity",
    "page": "1",
    "limit": "10",
    "lat": "43.7439",
    "long": "-79.5882",
    "sr": "1360x768"
}

response = requests.post(url = url, headers=headers, data = payload)
print(response.status_code)
print(response.headers.get('Content-Type'))
# print(response.text[:500])

# print("Final URL",response.url)
# print("Redirect history:", response.history)

# for item in response.history:
#     print("Redirect status", item.status_code)
#     print("Redirect location", item.headers.get("Location"))

# print("History Length",len(response.history))
# print("Request method:", response.request.method)
# print("Request URL:", response.request.url)

data = response.json()

print(type(data))
print(data.keys())

# Printing only the jobs
jobs = data["jobs"]
print(type(jobs))
print(len(jobs))

# Printing only first job

first_job = jobs[0]
print(first_job["title"])
print(first_job["jobId"])
print(first_job["city"])
print(first_job["salary"])
# print(type(first_job))
# print(first_job.keys())

# for job in jobs:
#     print(jobs[job])

# We use pandas to create the dataframe and to store all the jobs details
df = pd.DataFrame(jobs)
print(df.head())
print(df.columns)
print(df[["title","city"]])

# Select required columns out of all the columns and stored in to the list because its not key-value pairs so can not be stored in dictionary
selected_columns = ["reqId","title","location","city","state","type","salary","date","company","desc","applyUrl"]
selected_columns

# Mapped the selected columns to actual dataframe df and stored in to new_df that has only selected columns values
new_df = df[selected_columns]
new_df
print(new_df.head())
print(new_df.shape) # Shape function gives total row and column value

# Rename the columns name for easy understanding 
column_names = {
    "reqId": "requisition_id",
    "title": "job_title",
    "location": "location",
    "city": "city",
    "state": "province",
    "type": "employment_type",
    "salary": "salary",
    "date": "posting_date",
    "company": "company",
    "desc": "job_description",
    "applyUrl": "apply_url"
}

# rename function will rename the column names in new_df
new_df = new_df.rename(columns=column_names)
print(new_df.columns)

# info() function will give info of the dataset. How many rows and columns,if row has non numm or null values datatypes  and memory usage
new_df.info()
print(new_df["salary"].unique()) # unique function will give only unique values of salaries. Not includes duplicates

# compare the salary to empty string and generate output as row1 = True and row 2 = False
new_df["salary"] == ""
print(new_df)

# count how many salary has empty string.(sum of True count 1+0+1+1 = 3)
(new_df["salary"] == "").sum()

# To find how many percentage of the jobs has emptystring means no values in the salary columns.(Missing salary values)
missing_salary_percentage = ((new_df["salary"] == "").sum() / len(new_df)) * 100
print(round(missing_salary_percentage,2))


# To check the duplicated records on Requisition id. If the two jobs have same reqId means the jobs are duplicated
new_df["requisition_id"].duplicated().sum()