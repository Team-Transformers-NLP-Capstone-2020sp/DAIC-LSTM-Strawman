import csv

data_set = open("test.txt", "w")

for i in range(300,305):
    try:
        with open('DAIC/' + str(i) + '_TRANSCRIPT.csv') as csvfile:
            prev_speaker = ""
            value = ""
            conversation = csv.reader(csvfile, delimiter='\t')
            next(conversation)
            for row in conversation:
                if row:
                    line_value = row[3]
                    cur_speaker = row[2]
                    if cur_speaker == prev_speaker or prev_speaker == "":
                        if value == "":
                            value = line_value
                        else:
                            value += ' ' + line_value
                    else: # new speaker
                        # we add this in
                        if prev_speaker == "Ellie":
                            data_set.write(value + '\t')
                        elif prev_speaker == "Participant":
                            data_set.write(value + '\n')
                        # set the value to the new thing
                        value = line_value
                    prev_speaker = cur_speaker
            if prev_speaker == "Ellie":
                data_set.write(value + '\t')
            elif prev_speaker == "Participant":
                data_set.write(value + '\n')
    except:
        pass