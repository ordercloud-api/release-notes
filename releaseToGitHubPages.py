import requests
import requests.codes

ghAPI = 'https://api.github.com'

repoName = 'ordercloud-api/release-notes'

outputFiles = Path('output')

params = {
    'message': "TEST MESSAGE",
    'content': "TEST MESSAGE",
    'branch': "Dev",
    'committer': {
        "name": "Azure DevOps Pipeline",
        "email": "azure@four51.com"
    },
    'author': {
        "name": "Kate Reeher",
        "email": "kreeher@four51.com"
    },
}

updateBranch = requests.get(ghAPI + '/repos/' + repoName + '/contents')
print(updateBranch)
