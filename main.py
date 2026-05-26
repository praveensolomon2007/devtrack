# DevTrack - AI-powered developer analytics and growth insights platform

# Importing necessary libraries
import requests

# Start of the application
print("DevTrack")
print("AI-powered developer analytics and growth insights platform\n")

# Functions

def make_request(url):
    return requests.get(url)

def status_code_check(status_code):
    return status_code == 200

def status_code_message(status_code):
    if status_code == 200:
        print("\nStatus Code: 200 OK")
        print("Success: The request was successful.")
    elif status_code == 404:
        print("Error: 404 Not Found")
        print("Error: User not found. Please check the username and try again.")
    elif status_code == 403:
        print("Error: 403 Forbidden")
        print("Error: API rate limit exceeded. Please try again later.")
    elif status_code == 500:
        print("Error: 500 Internal Server Error")
        print("Error: Internal server error. Please try again later.")
    else:
        print(f"Error: Unexpected status code {status_code}")
        print(f"Error: An unexpected error occurred. Status code: {status_code}")

def fetch_github_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = make_request(url)
    status_code_message(response.status_code)
    if status_code_check(response.status_code):
        return response.json()
    return None

def fetch_github_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = make_request(url)
    status_code_message(response.status_code)
    if status_code_check(response.status_code):
        return response.json()
    return []


# User input and main logic
username = input("Enter GitHub username: ")
data = fetch_github_profile(username)

# Display developer profile information
if data:

    print("\nDeveloper Profile Information:")

    print(f"Name: {data.get('name')}")
    print(f"id: {data.get('id')}")
    print(f"Username: {data.get('login')}")
    print(f"Bio: {data.get('bio')}")
    print(f"Location: {data.get('location')}")
    print(f"Account Created At: {data.get('created_at')}")
    print(f"Last Updated At: {data.get('updated_at')}")
    print(f"Followers: {data.get('followers')}")
    print(f"Following: {data.get('following')}")
    print(f"Public Repositories: {data.get('public_repos')}")
    print(f"GitHub URL: {data.get('html_url')}")
else:
    print("Failed to retrieve developer profile information.")

# Fetch and display repository analytics

# Stars analysis, total stars, and repository details
repos = fetch_github_repositories(username)

print("\nDeveloper Repository Analytics:")
print(f"\nTotal Repositories: {len(repos)}")

print(f"\nStars Analysis:\n")

total_stars = 0
for repo in repos:
    print(f"Repository: {repo.get('name')}")
    print(f"Stars: {repo.get('stargazers_count')}\n")
    total_stars += repo.get('stargazers_count', 0)

print(f"\nTotal Stars Across All Repositories: {total_stars}")

# Top repositories

print("\nTop Repositories:")

for repo in repos[:5]:  # Display top 5 repositories
    print(f"\nRepository: {repo.get('name')}")
    print(f"Stars: {repo.get('stargazers_count')}")
    print(f"Language: {repo.get('language')}")

# Language Analytics:

print("\nLanguage Analytics:")

languages = {}

""" Note: Syntax	Missing Key
repo.get("language")	Returns None
repo["language"]	Raises KeyError

When to use which?
Use .get() when the key may not exist.
Use [] when the key must exist and missing data should be treated as an error.
In this case, since we are analyzing languages and some repositories might not
have a language specified, using .get() is safer to avoid KeyError and handle
missing data gracefully.
"""

for repo in repos:
    # language = repo["language"]  # This would raise KeyError if "language" key is missing
    language = repo.get("language")

    if language:

        if language in languages:
            languages[language] += 1
        else:
            languages[language] = 1

print("\nLanguages Used:")

for language, count in languages.items():
    a = "repository" if count == 1 else "repositories"
    print(f"{language}: {count} {a}")
