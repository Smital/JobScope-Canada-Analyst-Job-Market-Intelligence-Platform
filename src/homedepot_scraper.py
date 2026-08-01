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

first_job = jobs[0].
print(first_job)
print(type(first_job))
print(first_job.keys())

for job in jobs:
    print(jobs[job])
    