import numpy as np


def preprocess_annotations():
    annots = []
    new_lines = []
    with open('flickr_logos_27_dataset_training_set_annotation.txt','r') as infile:
        for line in infile:
            params = line.split(' ')
            new_lines.append(params[0]+' '+params[1]+' '+params[3]+' '+params[4]+' '+params[5]+' '+params[6])

    for line in new_lines:
        with open('flickr_logos_27_dataset_training_set_annotation_no_subsets.txt','a') as new_file:
            new_file.write(line+'\n')

    lines_seen = set()
    outfile = open('preprocessed_flickr_logos_27_training_set_annotation.txt','a')
    for line in open('flickr_logos_27_dataset_training_set_annotation_no_subsets.txt', 'r'):
        if line not in lines_seen:
            outfile.write(line+'\n')
            annots.append(line)
            lines_seen.add(line)
    outfile.close()
    return annots

def divide_train_val(annots):
    traindir = 'train_annotations.txt'
    valdir = 'val_annotations.txt'
    trainfile = open(traindir,'a')
    valfile = open(valdir,'a')
    np.random.shuffle(annots)
    num_train = int(len(annots)*0.8)
    for annot in annots[:num_train]:
        trainfile.write(annot)
    num_val = 0
    for annot in annots[num_train:]:
        valfile.write(annot)
        num_val += 1

    print('Num of annotations: {}(training), {}(validation)'.format(num_train,num_val))


if __name__ == '__main__':
    annots = preprocess_annotations()
    divide_train_val(annots)
