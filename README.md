# determined-source-control
Simple example demonstrating pulling from github when running an experiment

## Steps to use:
#### 1. Copy over the contents of the `runner` folder somewhere on your machine. This contains 3 key files
1. `const.yaml` a placeholder yaml file, gets overwritten
2. `model_def.py` a placeholder model_def file, gets overwritten
3. `startup-hook.sh` a shell script which runs when the experiment starts, this will clone a github repo with the appropriate files and overwrite the placeholders

#### 2. Run the determined experiment with `det e create const.yaml .`
- Make sure you have defined a `DET_MASTER` environment variable, and have run `det user login` successfully. This is done for you in an interactive session.
- You still need to define the resource pool being used for resources to be assigned to the job.
