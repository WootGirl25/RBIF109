Once local repository is initialized on home computer (if not skip to bottom):
1. Pull from GitHub & edit from home:
   In terminal:
   cd ~/Documents/RBIF109/Notebooks    #Or wherever git repo & notebooks are stored from setup instructions
   
   git pull origin main

   jupyter lab       #opens jupyter
   
   #save on jupyter browser

   ctrl c #terminates jupyter
3. Push to github
   #makesure in same directory
   git add Assignment1.ipynb     #or "git add ." if you want to push everything in the folder
   git commit -m "add comment"
   git push origin main

4. To access on anaconda cloud from work:
   Open cloud, open new terminal window, navigate to repository directory on cloud (if not already there)
   cd RBIF109
   git pull origin main     #this will update local repo with latest changes from GitHub

5. Push back to GitHub
   git add Assignment1.ipynb
   git commit -m "updated from work"
   git push origin branch_name  ## REALLY IMPORTANT YOU SPECIFY WHICH BRANCH YOURE IN. OTHERWISE COULD PUSH TO MAIN, OR A BRANCH YOURE NOT INTENDING. See note below
   WootGirl25
   <paste personal access token>

** To check which branch you're currently in:
    git branch --show-current
** To change branches
    git switch branch_name
    
_______________________________________________________________________________
**Step-by-Step Guide to Push to GitHub (For each new class)**
1. ON MAC
Install Git:
If you don’t have Git installed on your laptop, you can download and install it from here.

Create a GitHub Account:
If you don’t already have a GitHub account, sign up at GitHub.

Create a New Repository on GitHub:
Go to your GitHub account.
Click on the “+” icon in the top right corner and select “New repository”.
Give your repository a name (e.g., my-jupyter-notebooks).
Optionally, add a description.
Choose whether you want the repository to be public or private.
Click on “Create repository”.

Initialize a Git Repository Locally:
Open a terminal or command prompt on your laptop.
Navigate to the directory where your Jupyter notebooks are stored:
cd path/to/your/notebooks
Initialize a new Git repository:
git init

Add Your Notebooks to the Repository:
Add all your files to the staging area:
git add .
Commit the files with a message:
git commit -m "Initial commit"

Connect Your Local Repository to GitHub:
Add the remote repository URL. Replace <your-repo-url> with the URL of your GitHub repository (you can find this on the main page of your repository on GitHub):
git remote add origin <your-repo-url>

Push Your Changes to GitHub:
Push your committed changes to the GitHub repository:
git push -u origin main

2. On conda
Step-by-Step Guide to Clone and Work on Your Repository
Step 1: Push Your Repository to GitHub from Home Computer
Push Your Repository to GitHub:
Follow the steps you’ve already completed to push your entire repository to GitHub.
Step 2: Access and Work on Your Repository via Anaconda Cloud

Log In to Anaconda Cloud:
Open a web browser on your work computer and go to Anaconda Cloud.
Log in with your Anaconda Cloud account.

Create a New Project:
In Anaconda Cloud, go to the “Projects” section.
Click on “Create a New Project” and follow the prompts to create a new project.

Open the Terminal:
In your new project, click on the “Terminal” option to open a terminal window.

Clone Your GitHub Repository:
In the terminal, clone your GitHub repository using the following command:
git clone https://github.com/WootGirl25/RBIF109.git
This will download the entire repository to your Anaconda Cloud project.

Navigate to Your Repository:
Change directory to your cloned repository:
cd RBIF109
Edit the Notebook:
In the Anaconda Cloud file browser, navigate to the directory where your repository was cloned.
Click on the notebook file (e.g., your-notebook.ipynb) to open it.
Make the necessary changes to your notebook.
Save and Commit Changes:
After editing, save your notebook.
In the terminal, add and commit your changes:
git add your-notebook.ipynb
git commit -m "Updated notebook"
Push the changes back to GitHub:
git push


__________________________________________________
Closing a branch
Got it! Merging branches across multiple platforms can feel a bit daunting, but I'm here to guide you through it step by step.

Merging Branches in GitHub
Switch to Branch1 and Push Changes:

Make sure you're on branch1 on your home computer, and push any final changes to GitHub:

bash
git checkout branch1
git add .
git commit -m "Final changes on branch1"
git push origin branch1
Create a Pull Request (PR):

Go to your GitHub repository on the GitHub website.

Click on the "Pull requests" tab.

Click "New pull request."

Select branch1 as the compare branch and main as the base branch.

Click "Create pull request."

Add a title and description if necessary and click "Create pull request" again.

Merge the pull request by clicking "Merge pull request" and then "Confirm merge."

Updating Local Repositories
Update Main Branch on Home Computer:

On your home computer, switch to the main branch and pull the latest changes:

git checkout main
git pull origin main

Update Main Branch on Work Computer:
On your work computer, do the same as above.
By following these steps, you'll have successfully merged branch1 into main and updated the main branch on GitHub, your home computer, and your work computer.

I have now deleted branch1 on github. Does this automatically remove branch1 on my local machienes?
Deleting a branch on GitHub doesn't automatically remove it from your local machines. You'll need to manually delete the branch1 branch from your local repositories. Here's how you can do it:

List All Branches:
This will help you confirm that branch1 is still present in your local repository:
git branch

Delete the Local Branch:
To delete branch1 locally, run:
git branch -d branch1

If you get an error saying that the branch is not fully merged, and you are sure you want to delete it, you can force-delete it with:
git branch -D branch1
You'll need to run these commands on both your home and work computers.