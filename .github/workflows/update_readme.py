import os
import requests

def fetch_user_icons(organization, token):
    headers = {"Authorization": f"Bearer {token}"}
    url = f"https://api.github.com/orgs/{organization}/members"
    response = requests.get(url, headers=headers)
    members = response.json()
    user_icons = []
    for member in members:
        user_icons.append(member["avatar_url"])
    return user_icons

def generate_readme_content(organization, user_icons):
    content = f"# {organization} Members\n\n"
    for icon in user_icons:
        content += f"![User Icon]({icon}) "
    return content

def main():
    organization = "embraceemacs"
    token = os.environ.get('GH_TOKEN')
    user_icons = fetch_user_icons(organization, token)
    readme_content = generate_readme_content(organization, user_icons)
    with open(".github/README.md", "w") as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    main()
