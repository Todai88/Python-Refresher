#Learning moments

### Git:
`git rm -r --cached .` removes all cached files in a directory. So if you have already pushed up files that shouldn't be a part of the repository and have added said files / directories to `.gitignore` they will be removed.

### venv:
In Python3.6 you should use `python3 -m venv <path to virtual environment>`.
This creates a virtual environment where python is bundled in it, otherwise access to `pip` may be denied.

Follow this procedure:
```
$ > mkdir <name of venv> && cd <name of venv>
    .... Create directory
$ > python3 -m venv <name of venv>
    .... Create virtual environment with Python presets
$ > source <name of venv>/bin/activate
    .... Activate the environment
$ > pip install flask
    .... Install flask or what you need
$ > pip freeze > requirements.txt
    .... Add a snapshot of the pip libraries into a txt file
$ > deactivate
    .... leave the virtual shell
```