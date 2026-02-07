# Configure Multiple Git Accounts
1. Create a New SSH Key
    - ssh-keygen -t rsa -b 4096 -C "your-email-address"

2. Attach the New Key
    - Next, log in to your second GitHub account, click on the drop-down next to the profile picture at the top right, select Settings, and click on SSH and GPG keys.

3. Create a Config File
    - Example:
    ```bash
    # Work Account
    Host github.com-work
        HostName github.com
        User git
        IdentityFile ~/.ssh/id_ed25519_github_work

    # Personal Accout
    Host github.com
        HostName github.com
        User git
        IdentityFile ~/.ssh/id_ed25519_github_personal
    4. Try
    - ssh -vT git@github.com-work

5. Clone repository
    - This time, rather than pushing to git@github.com, we're using the custom host we created in the config file: git@github.com-work
    - git clone git@github.com-work:RepoName/RepoName.git