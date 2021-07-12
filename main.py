from github import Github
import json
import requests

key = json.loads(open("config.json", 'r').read())
g = Github(key["githubKey"])

user = g.get_user()
for repo in user.get_repos():
    archiveLink = repo.get_archive_link(archive_format="zipball")
    
    r = requests.get(archiveLink)
    open(f"Repositories/{repo.name}.zip", 'wb').write(r.content)