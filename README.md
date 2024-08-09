# determined-source-control
Simple example demonstrating pulling from github when running an experiment

## Steps to use:
#### 1. Copy over the contents of the `runner` folder somewhere on your machine. This contains 2 key files
1. `start.py` pulls the correct yaml file to run the experiment with
2. `startup-hook.sh` a shell script which runs when the experiment starts, this will clone a github repo with the appropriate files

#### 2. Run the determined experiment with `python start.py`
- Make sure you have defined a `DET_MASTER` environment variable, and have run `det user login` successfully. This is done for you in an interactive session
