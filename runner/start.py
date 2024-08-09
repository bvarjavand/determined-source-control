import io, urllib.request, yaml

mydict = yaml.safe_load(urllib.request.urlopen("https://raw.githubusercontent.com/bvarjavand/determined-source-control/main/const.yaml"))

from determined.experimental import client

exp = client.create_experiment(config=mydict, model_dir=".")

print(exp)