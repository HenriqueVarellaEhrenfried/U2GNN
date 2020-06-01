import glob
import pandas as pd
import sys


def build_csv(experiment, data):
    # epoch 1 mean: 66.12040113791208 std: 2.4849236053914434
    #   0   1  2            3          4           5 
    current_experiment = experiment.split(EXPERIMENT)[1]
    results = []
    for d in data:
        temp = []
        aux = d.split(' ')
        temp.append(aux[1])
        temp.append(aux[3])
        temp.append(aux[5])
        temp.append(str(current_experiment))
        results.append(temp)
    return results

if len(sys.argv) < 2:
    print("Missing dataset: Try to run python extract_data.py <DATASET_NAME>")
    exit(1)

EXPERIMENT = str(sys.argv[1])
PATH = "/checkpoints/model_acc.txt"
MAX_EPOCH = 100

directories = glob.glob(EXPERIMENT+'*')


results = {}

for d in directories:
    with open(d+PATH) as file:
        result = file.read().splitlines() 
        results[d] = result

header = ['epoch', 'mean', 'std', 'experiment']
data = []

for key,value in results.items():
    data = data + build_csv(key,value)

df = pd.DataFrame(data, columns = header) 

df["epoch"] = pd.to_numeric(df["epoch"])
df["mean"] = pd.to_numeric(df["mean"])
df["std"] = pd.to_numeric(df["std"])
df["experiment"] = pd.to_numeric(df["experiment"])

df = df.sort_values(['experiment','epoch'])

experiments_dfs = []
plotting = {}
plotting_std = {}
for i in range(0,len(directories)):
  experiments_dfs.append(df.loc[df['experiment'] == i])
  index = 'Experiment ' + str(i) 
  plotting[index] = experiments_dfs[i]['mean'].tolist()
  plotting_std[index] = experiments_dfs[i]['std'].tolist()
  while len(plotting[index]) < MAX_EPOCH:
    plotting[index].append(0)
    plotting_std[index].append(0)

df1 = pd.DataFrame(plotting)  
df2 = pd.DataFrame(plotting_std)

df.to_csv('CSV/'+EXPERIMENT+'.csv', index=False, sep=";", decimal=",")
df1.to_csv('CSV/'+EXPERIMENT+'_mean.csv', index=False, sep=";", decimal=",")
df2.to_csv('CSV/'+EXPERIMENT+'_std.csv', index=False, sep=";", decimal=",")