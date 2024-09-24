import requests
import json
from tabulate import tabulate
from colorama import Fore, Style, init

# Initialize colorama for color support in the terminal
init(autoreset=True)

# Function to get user repositories
def get_user_repos(username, token=None):
    url = f"https://api.github.com/users/{username}/repos"
    
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json() 
    else:
        print(f"Error: {response.status_code}")
        return None

# Function to display repository data
def display_repos(repo_data):
    table = []
    for repo in repo_data:
        repo_name = repo['name']
        stars = repo['stargazers_count']
        forks = repo['forks_count']
        repo_url = repo['html_url']
        
        colored_repo_name = f"{Fore.CYAN}{repo_name}{Style.RESET_ALL}"
        colored_stars = f"{Fore.YELLOW}{stars}{Style.RESET_ALL}"
        colored_forks = f"{Fore.GREEN}{forks}{Style.RESET_ALL}"
        colored_repo_url = f"{Fore.MAGENTA}{repo_url}{Style.RESET_ALL}"
        
        table.append([colored_repo_name, colored_stars, colored_forks, colored_repo_url])

    headers = ["Repository Name", "Stars", "Forks", "URL"]
    
    column_widths = [30, 10, 10, 50] 

    print(tabulate(table, headers, tablefmt="fancy_grid", colalign=("left", "center", "center", "left")))

# Main function
def main():
    username = input("Enter GitHub username: ")
    token = input("Enter GitHub token (optional): ").strip() or None
    
    repo_data = get_user_repos(username, token)
    
    if repo_data:
        display_repos(repo_data)

if __name__ == "__main__":
    main()
