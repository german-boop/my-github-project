import requests

# این API لیست ترندهای GitHub را می‌گیرد
url = "https://api.github.com/search/repositories?q=stars:>1000&sort=stars"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Top 5 Trending Repositories on GitHub:")
    for i, repo in enumerate(data["items"][:5], 1):
        print(f"{i}. {repo['full_name']} - ⭐ {repo['stargazers_count']}")
else:
    print("Failed to fetch data from GitHub API")
