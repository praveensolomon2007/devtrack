import requests

print("DevTrack")
print("AI-powered developer analytics and growth insights platform\n")

username = input("Enter your GitHub username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

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

elif response.status_code == 404:
    print("User not found. Please check the username and try again.")

elif response.status_code == 403:
    print("API rate limit exceeded. Please try again later.")

elif response.status_code == 500:
    print("Internal server error. Please try again later.")

else:
    print(f"An error occurred. Status code: {response.status_code}")