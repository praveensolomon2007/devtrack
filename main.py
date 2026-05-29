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

def calculate_total_stars(repositories):
    total_stars = 0
    for repo in repositories:
        total_stars += repo.get('stargazers_count', 0)

    return total_stars

def get_most_starred_repositories(repositories):
    if not repositories:
        return None
    return max(
        repositories,
        key=lambda repo: repo.get('stargazers_count', 0)
    )

def get_top_repositories(repositories, top_n=5):
    sorted_repos = sorted(
        repositories,
        key=lambda repo: repo.get('stargazers_count', 0),
        reverse=True
    )
    return sorted_repos[:top_n]

def calculate_languages_used(repositories):
    
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

    for repo in repositories:
        # language = repo["language"]  # This would raise KeyError if "language" key is missing
        language = repo.get("language")

        if language:

            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1

    return languages

def most_used_language(languages):
    if not languages:
        return None
    return max(languages, key=languages.get)

# --------------------------------------------------------------
    # main function to run the application
def main():
    # User input and main logic
    username = input("Enter GitHub username: ")
    data = fetch_github_profile(username) # fetch developer profile information function call

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
    
    # Fetch and display repository analytics:

    # Stars analysis, total stars, and repository details

    repos = fetch_github_repositories(username) # fetch github repositories function call
    # fetched repositories stored in repos variable for further analysis

    print("\nDeveloper Repository Analytics:")

    print(f"\nTotal Repositories: {len(repos)}")

    print(f"\nStars Analysis:")
    total_stars = calculate_total_stars(repos) # calculate total stars function call
    print(f"\nTotal Stars Across All Repositories: {total_stars}")

    # Most starred repositories
    print("\nMost Starred Repositories:")
    most_starred_repo = get_most_starred_repositories(repos) # get most starred repositories function call
    if most_starred_repo:
        print(f"\nMost Starred Repository: {most_starred_repo.get('name')}")
        print(f"Stars: {most_starred_repo.get('stargazers_count')}")
        print(f"Language: {most_starred_repo.get('language')}")

    # Language Analytics:
    print("\nLanguage Analytics:")
    print("\nLanguages Used:")
    languages = calculate_languages_used(repos) # calculate languages function call
    for language, count in languages.items():
        a = "repository" if count == 1 else "repositories"
        print(f"{language}: {count} {a}")

    most_used_lang = most_used_language(languages) # most used language function call
    if most_used_lang:
        a = "repository" if languages[most_used_lang] == 1 else "repositories"
        print(f"\nMost Used Language: {most_used_lang} ({languages[most_used_lang]} {a})")

    print("\nTop 5 Repositories by Stars:") 
    top_repos = get_top_repositories(repos) # get top repositories function call
    for repo in top_repos:
        print(f"\nRepository: {repo.get('name')} || Stars: {repo.get('stargazers_count')}")
        print(f"Language: {repo.get('language')}")
# --------------------------------------------------------------

if __name__ == "__main__":
    main()

# --------------------------------------------------------------