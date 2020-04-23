from __future__ import print_function

import numpy as np
import csv

input_texts = []
target_texts = []
input_words = set()
target_words = set()

for i in range(300,385):
    #print(i)
    try:
        with open('DAIC/' + str(i) + '_TRANSCRIPT.csv') as csvfile:
            prev_speaker = "NoOne"
            value = ""
            conversation = csv.reader(csvfile, delimiter='\t')
            next(conversation)
            for row in conversation:
                if row:
                    line_value = '\t' + row[3] + '\n'
                    cur_speaker = row[2]
                    if cur_speaker == prev_speaker or prev_speaker == "NoOne":
                        value += line_value
                    else: # new speaker
                        # we add this in
                        if prev_speaker == "Ellie":
                            input_texts.append(value)
                            for word in value.split():
                                if word not in input_words:
                                    input_words.add(word)
                        elif prev_speaker == "Participant":
                            target_texts.append(value)
                            for word in value.split():
                                if word not in target_words:
                                    target_words.add(word)
                        # set the value to the new thing
                        value = line_value
                    prev_speaker = cur_speaker
            if prev_speaker == "Ellie":
                        input_texts.append(value)
                        for word in value.split():
                            if word not in input_words:
                                input_words.add(word)
            elif prev_speaker == "Participant":
                target_texts.append(value)
                for word in value.split():
                    if word not in target_words:
                        target_words.add(word)
    except:
        print("missing transcript " + str(i))

with open("Ellie_data.txt", 'w') as output:
    for row in input_texts:
        output.write(str(row) + '\n')
with open("Participant_data.txt", 'w') as output:
    for row in target_texts:
        output.write(str(row) + '\n')