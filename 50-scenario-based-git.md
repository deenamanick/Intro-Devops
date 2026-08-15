# 🚀 50 Scenario-Based Git Interview & Practice Questions

A comprehensive collection of real-world Git scenarios, commands, and practical examples for DevOps engineers, developers, and system administrators.

---

### 🔰 **Basic Repository & Commit Scenarios**

1. **Scenario: You just installed Git on a new machine and need to configure your identity for commits.**
   
   ➤ *Goal:* Set your global username and email address.
   
   ➤ *Command:*
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```
   
   *Example:*
   ```bash
   git config --global user.name "Sanjay Kanth"
   git config --global user.email "sanjay@devops.com"
   # Verify your configuration:
   git config --list
   ```

2. **Scenario: You are starting a brand new project locally and want to place it under version control.**
   
   ➤ *Goal:* Initialize a new Git repository in the current folder.
   
   ➤ *Command:* `git init`
   
   *Example:*
   ```bash
   mkdir payment-service && cd payment-service
   git init
   # Output: Initialized empty Git repository in /payment-service/.git/
   ```

3. **Scenario: You want to download an existing team project from GitHub into a custom folder name.**
   
   ➤ *Goal:* Clone a remote repository to a specific local directory.
   
   ➤ *Command:* `git clone <repo_url> <custom_folder>`
   
   *Example:*
   ```bash
   git clone https://github.com/spring-projects/spring-boot.git my-spring-app
   cd my-spring-app
   ```

4. **Scenario: You want to check which files have been modified, staged, or untracked before committing.**
   
   ➤ *Goal:* Inspect the current state of the working directory and staging area.
   
   ➤ *Command:* `git status`
   
   *Example:*
   ```bash
   git status
   # Output:
   # Changes not staged for commit:
   #   modified:   server.js
   # Untracked files:
   #   new_feature.py
   ```

5. **Scenario: You edited multiple files, but only want to stage `app.py` for the next commit.**
   
   ➤ *Goal:* Add an individual file to the staging area.
   
   ➤ *Command:* `git add app.py`
   
   *Example:*
   ```bash
   git add database.py
   git status  # Shows database.py in green (staged) and other files in red (unstaged)
   ```

6. **Scenario: You created multiple new files and modified existing ones; stage everything at once.**
   
   ➤ *Goal:* Stage all tracked and untracked changes in the current directory.
   
   ➤ *Command:* `git add .`
   
   *Example:*
   ```bash
   # Add all changes across all subdirectories:
   git add .
   git status  # All modified and new files are now staged in green
   ```

7. **Scenario: You have staged your changes and want to commit them with a meaningful message.**
   
   ➤ *Goal:* Record changes to the repository history.
   
   ➤ *Command:* `git commit -m "feat: add user authentication endpoint"`
   
   *Example:*
   ```bash
   git commit -m "feat(auth): implement JWT token verification middleware"
   # [main 4f8b21c] feat(auth): implement JWT token verification middleware
   #  2 files changed, 45 insertions(+), 3 deletions(-)
   ```

8. **Scenario: You need to review recent commits in a concise, one-line format.**
   
   ➤ *Goal:* Display commit history briefly.
   
   ➤ *Command:* `git log --oneline -n 10`
   
   *Example:*
   ```bash
   git log --oneline -n 5
   # e4a1b2c feat(auth): add JWT login
   # 9c3d4e5 fix(db): fix connection pool timeout
   # 1b2a3c4 chore: update npm dependencies
   ```

---

### 🌿 **Branching & Merging Scenarios**

9. **Scenario: You want to see all branches available locally as well as on the remote.**
   
   ➤ *Goal:* List both local and remote-tracking branches.
   
   ➤ *Command:* `git branch -a`
   
   *Example:*
   ```bash
   git branch -a
   # * main
   #   feature/login
   #   remotes/origin/HEAD -> origin/main
   #   remotes/origin/main
   #   remotes/origin/feature/api
   ```

10. **Scenario: You are assigned a new feature ticket `feature/login` and need to create and switch to it immediately.**
    
    ➤ *Goal:* Create and checkout a new branch in a single command.
    
    ➤ *Command:* `git checkout -b feature/login` *(or modern `git switch -c feature/login`)*
    
    *Example:*
    ```bash
    git switch -c feature/cart-checkout
    # Switched to a new branch 'feature/cart-checkout'
    ```

11. **Scenario: You are done with your feature branch and need to switch back to the `main` branch.**
    
    ➤ *Goal:* Switch branches.
    
    ➤ *Command:* `git switch main` *(or `git checkout main`)*
    
    *Example:*
    ```bash
    git switch main
    # Switched to branch 'main'
    # Your branch is up to date with 'origin/main'.
    ```

12. **Scenario: You tested your `feature/login` branch and want to merge it into `main`.**
    
    ➤ *Goal:* Merge changes from a feature branch into the active branch.
    
    ➤ *Command:*
    ```bash
    git checkout main
    git merge feature/login
    ```
    
    *Example:*
    ```bash
    git switch main
    git merge feature/cart-checkout
    # Updating 3a4b5c6..7d8e9f0
    # Fast-forward
    #  cart.py | 120 ++++++++++++++++++++++++++++++
    #  1 file changed, 120 insertions(+)
    ```

13. **Scenario: During a merge, Git reports a merge conflict in `config.py`. You need to resolve it and finish the merge.**
    
    ➤ *Goal:* Resolve merge conflicts, stage resolved files, and complete the merge.
    
    ➤ *Command:*
    ```bash
    git add config.py
    git commit -m "merge: resolve conflict in config.py"
    ```
    
    *Example:*
    ```bash
    # 1. Inspect config.py and remove conflict markers:
    # <<<<<<< HEAD
    # PORT = 8080
    # =======
    # PORT = 9000
    # >>>>>>> feature/port-update
    
    # 2. Keep the desired line (e.g. PORT = 9000), save file, then:
    git add config.py
    git commit -m "merge: resolve port conflict with feature/port-update"
    ```

14. **Scenario: A feature branch has already been merged into `main`. Clean up the local branch.**
    
    ➤ *Goal:* Safely delete a merged local branch.
    
    ➤ *Command:* `git branch -d feature/login`
    
    *Example:*
    ```bash
    git branch -d feature/cart-checkout
    # Output: Deleted branch feature/cart-checkout (was 7d8e9f0).
    ```

15. **Scenario: You decided to abandon an experimental branch that was never merged, but Git warns you with `-d`.**
    
    ➤ *Goal:* Force delete an unmerged local branch.
    
    ➤ *Command:* `git branch -D experiment-branch`
    
    *Example:*
    ```bash
    git branch -D spike-prototype
    # Output: Deleted branch spike-prototype (was 8a9b0c1).
    ```

16. **Scenario: You made a typo while creating your branch `feat-paymnt` and want to rename it to `feat-payment`.**
    
    ➤ *Goal:* Rename the current active branch.
    
    ➤ *Command:* `git branch -m feat-payment`
    
    *Example:*
    ```bash
    git branch -m feat-stripe-integration
    # Renames current active branch to 'feat-stripe-integration'
    ```

---

### 🔄 **Remote Repositories & Collaboration Scenarios**

17. **Scenario: You initialized a local project and created a GitHub repo. Connect your local repo to GitHub.**
    
    ➤ *Goal:* Add a remote repository pointer.
    
    ➤ *Command:* `git remote add origin https://github.com/your-username/your-repo.git`
    
    *Example:*
    ```bash
    git remote add origin https://github.com/sanjaykanth/Intro-Devops.git
    ```

18. **Scenario: You want to verify the exact remote URLs configured for fetch and push.**
    
    ➤ *Goal:* List configured remotes with URLs.
    
    ➤ *Command:* `git remote -v`
    
    *Example:*
    ```bash
    git remote -v
    # Output:
    # origin  https://github.com/sanjaykanth/Intro-Devops.git (fetch)
    # origin  https://github.com/sanjaykanth/Intro-Devops.git (push)
    ```

19. **Scenario: You created a new local branch `feature/auth` and want to push it to remote while setting tracking.**
    
    ➤ *Goal:* Push branch to remote and set upstream tracking (`-u`).
    
    ➤ *Command:* `git push -u origin feature/auth`
    
    *Example:*
    ```bash
    git push -u origin feature/auth
    # Output: Branch 'feature/auth' set up to track remote branch 'feature/auth' from 'origin'.
    ```

20. **Scenario: You want to download all branches and commits from remote without merging them into your working files.**
    
    ➤ *Goal:* Fetch latest remote objects and metadata safely.
    
    ➤ *Command:* `git fetch origin`
    
    *Example:*
    ```bash
    git fetch origin
    # Output:
    # From https://github.com/sanjaykanth/Intro-Devops
    #  * [new branch]      staging    -> origin/staging
    #  * [new tag]         v2.1.0     -> v2.1.0
    ```

21. **Scenario: Your teammates pushed updates to `main`. Update your local `main` branch with the latest changes.**
    
    ➤ *Goal:* Fetch and integrate remote changes into the current branch.
    
    ➤ *Command:* `git pull origin main`
    
    *Example:*
    ```bash
    git pull origin main
    # Fast-forwarding local branch to match remote updates seamlessly
    ```

22. **Scenario: A feature branch `feature/old-search` was merged via Pull Request. Delete the branch on GitHub.**
    
    ➤ *Goal:* Delete a branch from the remote repository.
    
    ➤ *Command:* `git push origin --delete feature/old-search`
    
    *Example:*
    ```bash
    git push origin --delete feature/jira-402-search-fix
    # Output: - [deleted] feature/jira-402-search-fix
    ```

23. **Scenario: Multiple remote branches were deleted by teammates, but they still appear in your local `git branch -r`.**
    
    ➤ *Goal:* Prune stale remote tracking references.
    
    ➤ *Command:* `git fetch --prune` *(or `git remote prune origin`)*
    
    *Example:*
    ```bash
    git fetch -p
    # Output:
    #  x [deleted]         (none)     -> origin/feature/old-login
    #  x [deleted]         (none)     -> origin/feature/deprecated-api
    ```

24. **Scenario: You created release tags locally and want to publish all tags to the remote repository.**
    
    ➤ *Goal:* Push all local tags to remote.
    
    ➤ *Command:* `git push origin --tags`
    
    *Example:*
    ```bash
    git push origin --tags
    # Output:
    #  * [new tag]         v1.0.0 -> v1.0.0
    #  * [new tag]         v1.1.0 -> v1.1.0
    ```

---

### ⏪ **Undoing Changes, Reset & Revert Scenarios**

25. **Scenario: You accidentally ran `git add .` and staged sensitive credentials `secrets.env`. Unstage it without losing edits.**
    
    ➤ *Goal:* Remove a file from the staging area while keeping changes in working directory.
    
    ➤ *Command:* `git restore --staged secrets.env` *(or legacy `git reset HEAD secrets.env`)*
    
    *Example:*
    ```bash
    git restore --staged .env
    git status  # .env is now unstaged (safe from accidental commit)
    ```

26. **Scenario: You made unwanted edits to `index.html` and want to discard all local changes to match the last commit.**
    
    ➤ *Goal:* Discard uncommitted changes in a specific file.
    
    ➤ *Command:* `git restore index.html` *(or legacy `git checkout -- index.html`)*
    
    *Example:*
    ```bash
    git restore app/views.py
    # Reverts all local uncommitted modifications in app/views.py back to HEAD
    ```

27. **Scenario: You just committed changes but forgot to include `utils.py` and had a typo in your commit message.**
    
    ➤ *Goal:* Amend the last commit without creating a duplicate commit.
    
    ➤ *Command:*
    ```bash
    git add utils.py
    git commit --amend -m "feat: complete user auth module and add utils"
    ```
    
    *Example:*
    ```bash
    git add src/helper.js
    git commit --amend -m "fix(auth): correct token expiry and add helper"
    # Replaces the previous commit with the updated files and message
    ```

28. **Scenario: A commit that was pushed to production contains a critical bug. Undo its changes safely in public history.**
    
    ➤ *Goal:* Revert an existing commit by creating a new forward-facing inverse commit.
    
    ➤ *Command:* `git revert <commit_hash>`
    
    *Example:*
    ```bash
    git revert 9c3d4e5
    # Creates a new commit: "Revert 'fix(db): fix connection pool timeout'"
    ```

29. **Scenario: You made the last commit by mistake. You want to undo the commit but keep all modified code staged for rework.**
    
    ➤ *Goal:* Soft reset the HEAD by 1 commit.
    
    ➤ *Command:* `git reset --soft HEAD~1`
    
    *Example:*
    ```bash
    git reset --soft HEAD~1
    git status  # Last commit is undone; modified files remain staged in green
    ```

30. **Scenario: You want to undo the last 2 commits and unstage the files, but keep the modifications in your working files.**
    
    ➤ *Goal:* Mixed reset (default reset) to keep changes unstaged in working directory.
    
    ➤ *Command:* `git reset HEAD~2`
    
    *Example:*
    ```bash
    git reset HEAD~2
    git status  # Last 2 commits are undone; files remain on disk unstaged in red
    ```

31. **Scenario: Your local workspace is completely messed up. You want to throw away ALL uncommitted changes and match `origin/main`.**
    
    ➤ *Goal:* Hard reset working directory and index to match remote state.
    
    ➤ *Command:*
    ```bash
    git fetch origin
    git reset --hard origin/main
    ```
    
    *Example:*
    ```bash
    git fetch origin
    git reset --hard origin/main
    # Output: HEAD is now at 8b7c6d5 Merge pull request #42 from team/master
    ```
    > ⚠️ *Warning:* `git reset --hard` permanently deletes uncommitted changes.

32. **Scenario: You ran `git reset --hard` by accident and lost a valuable commit hash. Recover it.**
    
    ➤ *Goal:* Use the reference log to find and recover lost commits.
    
    ➤ *Command:*
    ```bash
    git reflog
    git reset --hard HEAD@{2}
    ```
    
    *Example:*
    ```bash
    git reflog
    # 7f2a1b9 HEAD@{0}: reset: moving to HEAD~1
    # 3c4d5e6 HEAD@{1}: commit: add production payment key
    # Restore the lost commit:
    git reset --hard 3c4d5e6
    ```

33. **Scenario: Build tools generated numerous untracked temporary files and directories. Remove all of them in one command.**
    
    ➤ *Goal:* Clean untracked files (`-f`) and directories (`-d`).
    
    ➤ *Command:* `git clean -fd`
    
    *Example:*
    ```bash
    # Preview what would be deleted:
    git clean -nd
    # Force delete all untracked files and directories:
    git clean -fd
    # Output: Removing temp_build/
    #         Removing debug.log
    ```

---

### 🧰 **Stashing, Diffing & Inspection Scenarios**

34. **Scenario: You are in the middle of a feature, but an urgent hotfix is needed on `main`. Save your uncommitted work temporarily.**
    
    ➤ *Goal:* Stash working directory and staged changes with a descriptive message.
    
    ➤ *Command:* `git stash push -m "WIP: working on payment gateway integration"`
    
    *Example:*
    ```bash
    git stash push -m "WIP: redis caching logic"
    # Output: Saved working directory and index state WIP: redis caching logic
    ```

35. **Scenario: You want to check all saved stashes to decide which one to resume.**
    
    ➤ *Goal:* List all items in the stash stack.
    
    ➤ *Command:* `git stash list`
    
    *Example:*
    ```bash
    git stash list
    # Output:
    # stash@{0}: On feature/redis: WIP: redis caching logic
    # stash@{1}: On main: WIP: navbar redesign
    ```

36. **Scenario: The hotfix is done. You are back on your feature branch and want to restore and remove the latest stash.**
    
    ➤ *Goal:* Apply the top stash and drop it from the stash list.
    
    ➤ *Command:* `git stash pop`
    
    *Example:*
    ```bash
    git stash pop
    # Output:
    # Auto-merging src/cache.js
    # Dropped refs/stash@{0} (a1b2c3d...)
    ```

37. **Scenario: You edited `server.py` and want to inspect the exact line-by-line differences before staging.**
    
    ➤ *Goal:* View unstaged differences in the working directory against the index.
    
    ➤ *Command:* `git diff server.py`
    
    *Example:*
    ```bash
    git diff src/index.js
    # Output:
    # - const PORT = 3000;
    # + const PORT = process.env.PORT || 8080;
    ```

38. **Scenario: You ran `git add .` and want to inspect exactly what changes are currently in the staging area.**
    
    ➤ *Goal:* View staged differences against the last commit.
    
    ➤ *Command:* `git diff --staged` *(or `git diff --cached`)*
    
    *Example:*
    ```bash
    git add app.py
    git diff --staged
    # Displays line-by-line colored diff of what is currently staged to be committed
    ```

39. **Scenario: Compare differences between your branch `feature/api` and the `main` branch.**
    
    ➤ *Goal:* Diff two branches.
    
    ➤ *Command:* `git diff main..feature/api`
    
    *Example:*
    ```bash
    git diff main..feature/payment-v2
    # Shows all code differences introduced between main and the feature branch
    ```

40. **Scenario: A production bug was traced to line 85 of `auth.py`. Find out who wrote that line and in which commit.**
    
    ➤ *Goal:* Show file annotations and commit authorship per line.
    
    ➤ *Command:* `git blame -L 80,90 auth.py`
    
    *Example:*
    ```bash
    git blame -L 12,14 server.py
    # Output:
    # 4f8b21c5 (Sarah Dev 2026-04-10 14:32:10 +0000 12) def authenticate_user(token):
    # 4f8b21c5 (Sarah Dev 2026-04-10 14:32:10 +0000 13)     if not token:
    # 4f8b21c5 (Sarah Dev 2026-04-10 14:32:10 +0000 14)         return None
    ```

41. **Scenario: You want a visual, colored terminal graph showing all branches, merges, and tags.**
    
    ➤ *Goal:* Render an ASCII commit history graph.
    
    ➤ *Command:* `git log --graph --oneline --decorate --all`
    
    *Example:*
    ```bash
    git log --graph --oneline --decorate --all
    # Output:
    # * 7f3a9e1 (HEAD -> main, origin/main) Merge branch 'feat/auth'
    # |\  
    # | * 1b8d2a4 (feat/auth) add jwt login validation
    # | * 5c9e2b1 add auth models
    # |/  
    # * a1b2c3d Initial commit
    ```

---

### ⚡ **Advanced Workflows: Rebase, Cherry-Pick & Maintenance**

42. **Scenario: Your feature branch fell behind `main`. You want a clean linear history instead of a messy merge commit.**
    
    ➤ *Goal:* Rebase current feature branch onto the latest `main`.
    
    ➤ *Command:*
    ```bash
    git checkout feature/api
    git fetch origin
    git rebase origin/main
    ```
    
    *Example:*
    ```bash
    git checkout feature/checkout
    git fetch origin
    git rebase origin/main
    # Output: Successfully rebased and updated refs/heads/feature/checkout.
    ```

43. **Scenario: You made 4 small "fix typo" and "wip" commits locally. Squash them into 1 clean commit before opening a PR.**
    
    ➤ *Goal:* Perform an interactive rebase to squash the last 4 commits.
    
    ➤ *Command:* `git rebase -i HEAD~4`
    
    *Example:*
    ```text
    # Run git rebase -i HEAD~3, then update the editor commands:
    pick a1b2c3d feat: add notification service
    squash b2c3d4e fix typo in notification templates
    squash c3d4e5f add email fallback mechanism
    # Save and close; Git squashes all three into one clean commit!
    ```

44. **Scenario: An interactive rebase or merge went wrong with too many conflicts. Cancel it and restore original state.**
    
    ➤ *Goal:* Abort an in-progress rebase or merge safely.
    
    ➤ *Command:* `git rebase --abort` *(or `git merge --abort`)*
    
    *Example:*
    ```bash
    # When encountering unwanted conflicts during merge:
    git merge --abort
    # Repository immediately returns to the clean pre-merge state
    ```

45. **Scenario: A critical bugfix commit `a1b2c3d` was made on `develop`. You need to apply only that single commit into `main`.**
    
    ➤ *Goal:* Cherry-pick a specific commit onto the current branch.
    
    ➤ *Command:* `git cherry-pick a1b2c3d`
    
    *Example:*
    ```bash
    git switch production
    git cherry-pick 9f4e2a1
    # Output: [production 8c2d1e0] fix: prevent SQL injection in search query
    #         1 file changed, 4 insertions(+), 1 deletion(-)
    ```

46. **Scenario: A bug was introduced somewhere among the last 100 commits. Automatically pinpoint the breaking commit.**
    
    ➤ *Goal:* Use Git binary search (`bisect`) to find the faulty commit.
    
    ➤ *Command:*
    ```bash
    git bisect start
    git bisect bad
    git bisect good v1.0.0
    ```
    
    *Example:*
    ```bash
    git bisect start
    git bisect bad                     # Current HEAD has the crash
    git bisect good v1.4.0             # Release v1.4.0 was working
    # Git automatically checks out middle commit:
    npm test                           # Tests pass -> git bisect good
    # ... after a few steps:
    # 7b9c1d2 is the first bad commit
    git bisect reset
    ```

47. **Scenario: You are releasing version `1.2.0` of your application and need to create an annotated tag with release notes.**
    
    ➤ *Goal:* Create an annotated tag.
    
    ➤ *Command:* `git tag -a v1.2.0 -m "Release version 1.2.0"`
    
    *Example:*
    ```bash
    git tag -a v2.0.0 -m "Release v2.0.0: major architecture upgrade with microservices support"
    git tag -n  # List tags with their annotation messages
    ```

48. **Scenario: You need to urgently work on a hotfix branch without stashing or switching your current workspace branch.**
    
    ➤ *Goal:* Use Git Worktrees to check out multiple branches simultaneously in separate folders.
    
    ➤ *Command:*
    ```bash
    git worktree add ../hotfix-folder hotfix/security-patch
    git worktree remove ../hotfix-folder
    ```
    
    *Example:*
    ```bash
    # Create a separate folder working on the hotfix branch:
    git worktree add ../hotfix-work hotfix/memory-leak
    cd ../hotfix-work  # Work on hotfix here independently
    # Once merged and done:
    cd ../Intro-Devops
    git worktree remove ../hotfix-work
    ```

49. **Scenario: You added `logs/app.log` to `.gitignore`, but Git continues tracking it because it was committed earlier.**
    
    ➤ *Goal:* Untrack a file from Git index without deleting it from your local filesystem.
    
    ➤ *Command:*
    ```bash
    git rm --cached logs/app.log
    git commit -m "chore: stop tracking logs/app.log"
    ```
    
    *Example:*
    ```bash
    # Add .env to .gitignore first:
    echo ".env" >> .gitignore
    # Untrack .env from git while leaving the file on your local machine:
    git rm --cached .env
    git commit -m "chore: stop tracking .env secret file"
    ```

50. **Scenario: You cloned a project that relies on external Git submodules (e.g. shared libraries), but the submodule folders are empty.**
    
    ➤ *Goal:* Initialize, fetch, and check out nested submodules.
    
    ➤ *Command:* `git submodule update --init --recursive`
    
    *Example:*
    ```bash
    # In a newly cloned project with submodules:
    git submodule update --init --recursive
    # Output: Submodule 'libs/utils' (https://github.com/org/shared-utils.git) registered
    #         Submodule path 'libs/utils': checked out 'e3f1a2b...'
    ```

---
