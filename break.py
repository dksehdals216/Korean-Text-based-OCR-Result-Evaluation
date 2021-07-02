
import math
import random
import csv

import numpy as np
import pandas as pd
from sklearn.metrics import f1_score
from konlpy.tag import Okt


def analyze_token(_original, _tess_file):
    accuracy = 0
    original = 'data/' + _original
    tess_file = 'data/' + _tess_file

    with open(original) as f:
            
        orig_list = [word for line in f for word in line.split()]
        with open(tess_file) as tes_f:
            tess_list = [tess for lines in tes_f for tess in lines.split()]

            with open('data/data_by_line/' + _original + '_line') as _f:
                with open('data/data_by_line/' + _tess_file + '_line') as _tes_f:
                    orig_line = _f.readlines()
                    tess_line = _tes_f.readlines()

                    # create vocab dictionary
                    vocab_list = orig_list + tess_list
                    tok_list = [line for line in vocab_list]
                    

                    word2index = {}

                    for vocab in tok_list:
                        if vocab not in word2index.keys():
                            word2index[vocab]=len(word2index)
                    

                    orig_list = [line[:-1] for line in orig_list]
                    tess_list = [line[:-1] for line in tess_list]
                    orig_line = [line[:-1] for line in orig_line]
                    tess_line = [line[:-1] for line in tess_line]

                    for index, data in enumerate(orig_list):
                        for key, value in word2index.items():
                            if key == data:
                                orig_list[index] = data.replace(str(key), str(word2index[key]))

                    for index, data in enumerate(tess_list):
                        for key, value in word2index.items():
                            if key == data:
                                tess_list[index] = data.replace(str(key), str(word2index[key]))
        
                    # padding
                    diff = abs(len(orig_list) - len(tess_list))

                    if len(orig_list) > len(tess_list):
                        for i in range(diff):
                            tess_list.append("")

                        for i in range(len(orig_list)):
                            if orig_list[i] == tess_list[i]:
                                accuracy +=1
                    else:
                        for i in range(diff):
                            orig_list.append("")

                        for i in range(len(tess_list)):
                            if tess_list[i] == orig_list[i]:
                                accuracy +=1

                    line_diff = abs(len(orig_line) - len(tess_line))
                    score_sum = 0

                    if len(orig_line) > len(tess_line):
                        for i in range(line_diff):
                            tess_line.append("")

                        for index in range(len(orig_line)):
                            orig_line[index] = orig_line[index].split()

                        for index in range(len(orig_line)):
                            tess_line[index] = tess_line[index].split()

                        for _index in orig_line:
                            for index, data in enumerate(_index):
                                for key, value in word2index.items():
                                    if key == data:
                                        _index[index] = data.replace(str(key), str(word2index[key]))
                        for _index in tess_line:
                            for index, data in enumerate(_index):
                                for key, value in word2index.items():
                                    if key == data:
                                        _index[index] = data.replace(str(key), str(word2index[key]))
                        for i in range(len(orig_line)):
                            line_diff = len(orig_line[i]) - len(tess_line[i])
                            #print(line_diff)
                            
                            if line_diff > 0:
                                for i in range(abs(line_diff)):
                                    tess_line[i].append("")
                            elif line_diff < 0:
                                for i in range(abs(line_diff)):
                                    orig_line[i].append("")
                                    #print(orig_line[i])



                        #print(orig_line)
                        #print(tess_line)

                        #print("\t F1 total method")
                        #print("F1 Score: ", f1_score(orig_list, tess_list, average='weighted'))



                    else:
                        for i in range(line_diff):
                            orig_line.append("")

                        for index in range(len(tess_line)):
                            orig_line[index] = orig_line[index].split()

                        for index in range(len(tess_line)):
                            tess_line[index] = tess_line[index].split()

                        for _index in orig_line:
                            for index, data in enumerate(_index):
                                for key, value in word2index.items():
                                    if key == data:
                                        _index[index] = data.replace(str(key), str(word2index[key]))
                        for _index in tess_line:
                            for index, data in enumerate(_index):
                                for key, value in word2index.items():
                                    if key == data:
                                        _index[index] = data.replace(str(key), str(word2index[key]))




            print("accuracy: ", float((accuracy)/len(orig_list)))
            print("F1 Score: ", f1_score(orig_list, tess_list, average='weighted'))


def analyze_sentance(original, tess_file):
    accuracy = 0
    original = 'data/data_by_line/' + original + '_line'
    tess_file = 'data/data_by_line/' + tess_file + '_line'

    with open(original) as f:
        with open(tess_file) as tes_f:
            orig_list = f.readlines()
            tess_list = tes_f.readlines()

            # create vocab dictionary
            vocab_list = orig_list + tess_list
            tok_list = [line[:-1] for line in vocab_list]
            
            #print(tok_list)

            word2index = {}

            for vocab in tok_list:
                if vocab not in word2index.keys():
                    word2index[vocab]=len(word2index)

            orig_list = [line[:-1] for line in orig_list]
            tess_list = [line[:-1] for line in tess_list]

            for index, data in enumerate(orig_list):
                for key, value in word2index.items():
                    if key == data:
                        orig_list[index] = data.replace(str(key), str(word2index[key]))

            for index, data in enumerate(tess_list):
                for key, value in word2index.items():
                    if key == data:
                        tess_list[index] = data.replace(str(key), str(word2index[key]))

            diff = abs(len(orig_list) - len(tess_list))

            if len(orig_list) > len(tess_list):
                for i in range(diff):
                    tess_list.append("")

                for i in range(len(orig_list)):
                    if orig_list[i] == tess_list[i]:
                        accuracy +=1
            else:
                for i in range(diff):
                    orig_list.append("")

                for i in range(len(tess_list)):
                    if tess_list[i] == orig_list[i]:
                        accuracy +=1

            print("accuracy: ", float((accuracy)/len(orig_list)))
            print("F1 Score: ", f1_score(orig_list, tess_list, average='weighted'))
'''
def f1_manual(orig_index, tess_index):

    diff = sum(i != j for i, j in zip(orig_index, tess_index))
    print(dff)

    
    if len(orig_index) > len(tess_index):
        false_n = 0
    else:
        false_n = abs(len(orig_index) - len(tess_index))

    # Precision
    # Recall

   # return (2 * (precision * recall) / (precision + recall))
'''
def main():

    print("By Word, total method")
    print("\nResults for Prof: ")
    analyze_token('prof_orig', 'prof_tess') 
    print("\nResults for mine: ")
    analyze_token('mine_orig', 'mine_tess')
    print("\nResults for dudu1: ")
    analyze_token('dudu1_orig', 'dudu1_tess')
    print("\nResults for dudu2: ")
    analyze_token('dudu2_orig', 'dudu2_tess')
    
    '''
    print('\n\nBy Sentence')
    print("\nResults for Prof: ")
    analyze_sentance('prof_orig', 'prof_tess') 
    print("\nResults for mine: ")
    analyze_sentance('mine_orig', 'mine_tess')
    print("\nResults for dudu1: ")
    analyze_sentance('dudu1_orig', 'dudu1_tess')
    print("\nResults for dudu2: ")
    analyze_sentance('dudu2_orig', 'dudu2_tess')
    '''

if __name__ == "__main__":
    main()


