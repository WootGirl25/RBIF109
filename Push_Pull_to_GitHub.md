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
