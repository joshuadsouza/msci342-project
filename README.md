# Team-4-2019-Project

Install Repo:
Go to directory where you want to install the project (i.e. `cd <dirName>`)
`git clone https://github.com/UWaterlooMSCI342/Team-4-2019-Project.git`
`cd Team-4-2019-Project`

Install Anaconda:
`conda create --name schedulePrinter python=3.6`
`conda activate schedulePrinter`
`conda env update --file env.yaml` (this will also be used to update our env as new dep are added)

In VSCode make sure you interpreter is set to schedulePrinter:

- install Python for vscode: View > Extensions > search for Python
- CMD + SHIFT + P > select python interpreter
  Check by running `python --version` and make sure it is Python 3.6

When we are adding new dep in python:
`conda install <thing>`
`conda env export > env.yaml`

Convert python to js:
`pip install transcrypt` first to install - one time!
`transcrypt hello.py`

Run project:
`python3 -m http.server`
Note this is only for local dev. As this is a static page we do not need a server however CORs does not enable access to local file system (which is good) and so we spin up a server to rep the server it will be hosted on.
