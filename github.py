from email.policy import default

from fileinput import filename

from logging import exception

from github import Github

import boto3

​

#For Github Enterprise, leave base_url as is. You can generate an access token for Github in settings

#Warning: You access token acts as your password. Please be certain it is not shared and is secured.

with open('loginToken.txt', 'r') as file:

    login = file.read()

​

g = Github(base_url="https://github.companydomain/api/v3", login_or_token=login)

repo = g.get_repo("repo")

​

with open('credentials.txt', 'r') as file:

    content = file.read()

​

git_Prefix = '/path/to'

git_file = git_Prefix + 'file-to-write-to'

bruh = "branch-name"

b = repo.get_branch(bruh)

contents = repo.get_contents(path=git_Prefix, ref=b.commit.sha)

​

if git_file in str(contents):

    contents = repo.get_contents(git_file, ref=b.commit.sha)

    repo.update_file(contents.path, "commiting files", content, contents.sha, branch=bruh)

    print(git_file + ' UPDATED')

else:

    print("File does not exist. Creating a new file")

    repo.create_file(git_file, "commiting files", content, branch=bruh)

    print(git_file + ' CREATED')

   