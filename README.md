# Viking
Command line interface tool to manage passwords

## Usage
- Add new password:
```viking  -a www.mysite.com myusername```
- Show a specific password:
``` viking -s www.mysite.com```
- Show all: ``` viking -s ```
- Delete password: ```viking -d www.mysite.com ```

## How to contribute
There is a todo file with the list of features to add, you can pick one and start working on it or just suggest new features, to report issues please use the issue tracker. To run the application locally is necessary to create a virtual environment and activate it, the virtual environment should be called "viking-env" in that way it is going to be ignored.
[How to create a virtual environment](https://docs.python.org/3/tutorial/venv.html)