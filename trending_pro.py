import requests
from tabulate import tabulate
from termcolor import colored

# گرفتن ترندترین ریپوزیتوری‌ها
url = "https://api.github.com/search/repositories?q=stars:>1000&sort=stars&order=desc"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    table = []
    for i, repo in enumerate(data['items'][:10], 1):  # 10 ریپوزیتوری اول
        name = colored(repo['full_name'], 'cyan')
        stars = colored(repo['stargazers_count'], 'yellow')
        desc = repo['description'] or "No description"
        table.append([i, name, stars, desc])

    print(colored("🔥 Top 10 Trending GitHub Repositories 🔥", 'green', attrs=['bold']))
    print(tabulate(table, headers=["#", "Repository", "Stars", "Description"], tablefmt="fancy_grid"))
else:
    print(colored("❌ Failed to fetch data from GitHub API", 'red'))
