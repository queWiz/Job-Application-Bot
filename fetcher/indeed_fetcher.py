import requests
from datetime import datetime
from dataclasses import dataclass

@dataclass
class JobListing:
    title: str
    company: str
    url: str
    date_posted: datetime.date
    salary: int
    easy_apply: bool

class IndeedFetcher:
    URL = "https://api.indeed.com/v2/jobs"

    def __init__(self, api_key=None):
        self.api_key = api_key

    def search(self, keywords, locations):
        params = {
            "q": " OR ".join(keywords),
            "l": ",".join(locations),
            "publisher": self.api_key,
            "limit": 50,
        }
        resp = requests.get(self.URL, params=params).json()
        listings = []
        for jd in resp.get("results", []):
            listings.append(JobListing(
                title=jd.get("jobtitle"),
                company=jd.get("company"),
                url=jd.get("url"),
                date_posted=datetime.strptime(jd.get("date", ""), "%Y-%m-%d").date(),
                salary=int(jd.get("salary", 0)) or 0,
                easy_apply=jd.get("easy_apply", False)
            ))
        return listings
