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
The list of pending features are in a file called **todo**, feel free to grab one, to suggest a new feature create a pull request modifying this file and describe the feature in the description of the pull request. To report new issues use the issue tracker instead. 

The project use pipenv to manage the dependecies,  mac users can use brew to install pipenv
```brew install pipenv``` or just ```pip install --user pipenv```, to install the software's dependecies ```pipenv install ``` and to build the software use ```pipenv run build```. To run the system your are going to run it inside a the virtual environemnt ```pipenv shell``` or you can do aswell ```pipenv run python viking/main.py```. For more about pipenv visit [the official site](https://pipenv.readthedocs.io/en/latest/)