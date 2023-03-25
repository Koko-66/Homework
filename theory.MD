### Question 1
Fill in the blank:
Git is an example of a _version control_ system.

### Question 2
Name a code hosting service that uses Git.

e.g. GitHub, GitLab, BitBucket

### Question 3
There are 3 states in Git that files can be in. What are these states?

The three stages are:
- __MODIFIED__: when you have made changes to the file but these changes are still only in your local repository and have not yet been committed to your git database.

- __STAGED__: this means that the file that you have changed has been marked as to be included in the next commit for saving in the database.

- __COMMITTED__: the file has been saved in the local git database

## Question 4
PR and repo are common abbreviations in the world of Git. What do they mean?

__PR__ => Pull Request<br>
__Repo__ => Repository

### Question 5
What is the git command that updates the local repository with changes from the remote repository?

`git pull`

### Question 6
What is the git command that gets the changes from the remote repository but doesn’t update your local repository?

`git fetch`

### Question 7
What is the git command that updates the remote repository with local repository code?

`git push`

### Question 8
What does the git commit command need to work?

It requires at least one file to be staged for commit as well as a message describing what kind of changes have been made to the code to be attached to the commit, e.g.: 
<br>
`git commit -m "Initial commit."`