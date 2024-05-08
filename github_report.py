import os
import requests
from datetime import datetime, timedelta

def get_pr(owner, repo):

    repo_url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    
    # Get 1 week ago date
    week_ago = datetime.now() - timedelta(days=7)
    week_ago = week_ago.isoformat()
    
    params = {
        "state": "all",
        "since": week_ago
    }
    
    response = requests.get(repo_url, params=params)
    pr_info = response.json()
    
    return pr_info

def generate_report(pr_info):
    open_prs = [pr for pr in pr_info if pr['state'] == 'open']
    closed_prs = [pr for pr in pr_info if pr['state'] == 'closed']
    in_progress_prs = [pr for pr in pr_info if pr['state'] == 'in-progress']
    
    report = []
    report.append("Weekly Pull Requests Report:\n")
    
    report.append(f"Open Pull Requests: {len(open_prs)}")
    for pr in open_prs:
        report.append(f" - #{pr['number']} {pr['title']} by {pr['user']['login']}")

    report.append(f"\nClosed Pull Requests: {len(closed_prs)}")
    for pr in closed_prs:
        report.append(f" - #{pr['number']} {pr['title']} by {pr['user']['login']}")

    report.append(f"\nIn Progress Pull Requests: {len(in_progress_prs)}")
    for pr in in_progress_prs:
        report.append(f" - #{pr['number']} {pr['title']} by {pr['user']['login']}")
    
    return '\n'.join(report)

def main():
    owner = os.getenv('OWNER')
    repo = os.getenv('REPO')
    
    pr_info = get_pr(owner, repo)

    report = generate_report(pr_info)
    
    email = {
        "From": "user@gmail.com",
        "To": "manager@gmail.com",
        "Subject": f"Weekly PR Report for {repo} Github Repository",
        "Body": report
    }
    
    print("From:", email['From'])
    print("To:", email['To'])
    print("Subject:", email['Subject'])
    print("\n", email['Body'])

if __name__ == "__main__":
    main()