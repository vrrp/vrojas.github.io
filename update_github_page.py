"""
source: 
    https://steadylearner.com/blog/read/How-to-automatically-commit-files-to-GitHub-with-Python
    https://realpython.com/python-git-github-intro/
    https://git-scm.com/book/en/v2

    https://www.fullstackpython.com/blog/first-steps-gitpython.html
    https://gitpython.readthedocs.io/en/stable/tutorial.html
    https://stackoverflow.com/questions/7119452/git-commit-from-python
    
# Create a new repository on the command line
    $ echo " algun mensaje" >> READE.md
    $ git init
    $ git add README.md
    $ git commit -m "first commit"
    $ git remote add origin https://github.com/vrrp/vrrp.github.io.git
    $ git push -u origin master

# Push an existing repository from the command line
    $ git remote  add origin https://github.com/vrrp/vrrp.github.io.git
    $ git push -u origin master

# Import code from another repository
"""

import os
import subprocess as cmd


path_now = os.getcwd()
path_img = "/home/proyectos/pyprojects/coronavirus2020_api/"

cmd.run("echo 'hello world'", check=True, shell=True)

cp = cmd.run("git add .", check=True, shell=True)
print(cp)