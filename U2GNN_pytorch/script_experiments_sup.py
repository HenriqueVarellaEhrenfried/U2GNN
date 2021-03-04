import pandas as pd 
import os 

DATA_TYPES ={
        "run_folder":str,
        "dataset":str,
        "learning_rate":float,
        "batch_size":int,
        "num_epochs":int,
        "model_name":str,
        "sampled_num":int,
        "dropout":float,
        "num_hidden_layers":int,
        "num_self_att_layers":int,
        "ff_hidden_size":int,
        "num_neighbors":int,
        "fold_idx":int,
        "Experiment_Number":str,
        "Description":str
    }

CSV_FILE = pd.read_csv(
    'MR_Spacy.csv', 
    header= 0, 
    dtype= DATA_TYPES   
)

CSV_SIZE = len(CSV_FILE["learning_rate"])

CMD = "python train_pytorch_U2GNN_Sup.py "
# CMD = "python unsup_train_alternative.py "

for i in range(0, CSV_SIZE):
    print(">>> Processing Experiment", i, "/", (CSV_SIZE-1), "<<<" )
    command = CMD \
            + "--run_folder " + str(CSV_FILE["run_folder"][i]) + ' ' \
            + "--dataset " + str(CSV_FILE["dataset"][i]) + ' ' \
            + "--learning_rate " + str(CSV_FILE["learning_rate"][i]) + ' ' \
            + "--batch_size " + str(CSV_FILE["batch_size"][i]) + ' ' \
            + "--num_epochs " + str(CSV_FILE["num_epochs"][i]) + ' ' \
            + "--model_name " + str(CSV_FILE["model_name"][i]) + ' ' \
            + "--sampled_num " + str(CSV_FILE["sampled_num"][i]) + ' ' \
            + "--dropout " + str(CSV_FILE["dropout"][i]) + ' ' \
            + "--num_hidden_layers " + str(CSV_FILE["num_hidden_layers"][i]) + ' ' \
            + "--num_self_att_layers " + str(CSV_FILE["num_self_att_layers"][i]) + ' ' \
            + "--ff_hidden_size " + str(CSV_FILE["ff_hidden_size"][i]) + ' ' \
            + "--num_neighbors " + str(CSV_FILE["num_neighbors"][i]) + ' ' \
            + "--fold_idx " + str(CSV_FILE["fold_idx"][i]) + ' '         
    os.system(command)

print("------------ Finished Processing ------------")