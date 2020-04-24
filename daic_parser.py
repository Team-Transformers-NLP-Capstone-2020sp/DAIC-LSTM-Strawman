import pandas as pd, numpy as np
import re, os

def parse_conversation(df):
    drop_rows = []
    for i in range(1, len(df)):
        # check for consecutive rows with same speaker
        if df.loc[i, "speaker"] == df.loc[i - 1, "speaker"]:
            df.loc[i, "value"] = str(df.loc[i - 1, "value"]) + " " + str(df.loc[i, "value"])
            drop_rows.append(i - 1)
    df = df.drop(drop_rows)
    #df = df[df.speaker == 'Participant']["value"].apply(lambda x: re.sub("<.*>", "", x))
    df = df[df != ""]
    return df

convs = []
for i in range(300,305):
    try:
        df = pd.read_csv('DAIC/' + str(i) + '_TRANSCRIPT.csv', delimiter="\t")
        convs.append(parse_conversation(df))
    except:
        pass
convs_full = pd.concat(convs).reset_index(drop=True)
#print(convs_full)

data_set = open("test.txt", "w")
ellie = True
for _, row in convs_full.iterrows():
    if ellie:
        data_set.write(row['value'] + '\t')
        ellie=False
    else:
        data_set.write(row['value'] + '\t' + "PLACEHOLDER\n")
        ellie=True



