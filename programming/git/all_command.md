
---

### 1. Checking Your Setup
Commands to see what is going on with your remotes and branches.

```bash
# See all connected remote repositories (e.g., origin, src, github)
git remote -v 

# See all local branches (the asterisk * shows the branch you are currently on)
git branch
```

---

### 2. Managing Remotes (Adding & Removing)
How to connect to a new server (like GitHub) or remove a connection.

```bash
# Connect to a remote using SSH (best for GitHub)
git remote add github git@github.com:lelectronicien/2026-2-study-practical-scientific-writing.git

# Remove a remote connection entirely
git remote remove github 
```

---

### 3. Pushing (Uploading your work)
How to send your local branches and tags to a remote repository (`github` in this case).

```bash
# Push ALL local branches to the remote
git push github --all

# Push ALL local tags to the remote
git push github --tags

# Push a specific branch (e.g., master) and set it to track the remote
git push -u github master

# Delete a branch on the remote server
git push github --delete release/v6.0.0
```

---

### 4. Releases & Git Flow (Merging and Tagging)
The core steps to finish a release after you have finished coding on your `release/` branch.

```bash
# 1. Merge your release branch into your main branch (e.g., master or develop)
git merge --no-ff release/v6.0.0 -m "Merge branch 'v6.0.0'"

# 2. Create the annotated tag
git tag -a v6.0.0 -m "Release v6.0.0"
```

---

### 5. Cleaning Up (Branch Management)
After a release is fully merged and pushed, you delete the temporary release branch.

```bash
# Switch to a safe branch (you cannot delete the branch you are currently on)
git checkout develop

# Delete the branch locally
git branch -d release/v6.0.0
```

---

### 6. Initializing & Syncing (The GitHub Template)

```bash
# If you were starting from scratch (which you aren't, but for reference):
git init
git add README.md
git commit -m "feat: first commit"

# If you ever need to rename your current branch to 'main' or 'master'
git branch -M main

# If you need to pull the latest updates from the original server (GitVerse)
git pull origin develop
```


### 7. tag

```bash
git tag -a v1.4 -m 'v1.4'

git tag ## list tag

git tag -d list

git status -s #check modified files.


git diff # Pour visualiser ce qui a été modifié mais pas encore indexé, tapez git diff sans autre argument :

find . -name .DS_Store -delete

git log --pretty=oneline


```

```markdown

[livre de git](https://git-scm.com/book/fr/v2)
```
