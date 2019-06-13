#!/usr/bin/env python

import math
import csv
from collections import Counter

def is_tree(thing):
    if isinstance(thing, list) and (len(thing)==3) and isinstance(thing[0],tuple):
        return True
    else : False

def classify(tree, data):
    if is_tree(tree) is True:
        if data[tree[0][0]]>tree[0][1] : 
            return classify(tree[2],data)
        else : 
            return classify(tree[1],data)
    else : 
        return tree

def tree_accuracy(tree,x,y):
    correct = 0
    for x_i,y_i in zip(x,y) : 
        if classify(tree,x_i) == y_i :
            correct += 1
    return float(correct)/len(y)

# --- entropy ---

def entropy(class_probabilities):
    return sum(-p*math.log2(p) for p in class_probabilities if p)

def class_probabilities(labels):
    total_count = len(labels) 
    return [count / total_count for count in Counter(labels).values()] 

def data_entropy(labeled_data):
    labels = [y for x,y in labeled_data]
    return entropy(class_probabilities(labels))

def partition_entropy(subsets):
    total_count = sum(len(subset) for subset in subsets)
    return sum(data_entropy(subset)*len(subset)/total_count 
               for subset in subsets)

def partition_by(inputs, attribute,threshold):
    right = []
    left = []
    for input_ in inputs:
        key = input_[0][attribute]
        if key > threshold:
            right.append(input_)
        else : left.append(input_)
    return tuple([left]+[right])

def partition_entropy_by(inputs,attribute,threshold):
    partitions = partition_by(inputs,attribute,threshold)
    return partitions, partition_entropy(partitions)

def best_partition_entropy(inputs):
    attribute_len = len(inputs[0][0])
    mini = 1
    attribute_new =0
    index = 0
    for attribute in range(attribute_len):
        for i in range(len(inputs)):                        
            threshold = inputs[i][0][attribute]
            entro = partition_entropy_by(inputs,attribute,threshold)[1]
            if entro < mini :
                mini = entro
                attribute_new = attribute
                threshold_ = threshold
    return ((attribute_new, threshold_), entro)       

def build_tree_id3(inputs,max_height,current_height=0):
    labels = [label for item, label in inputs]
    labels_key = set(labels)
    
    if len(labels_key)==1:
        return labels[0]
    
    elif current_height == max_height:
        label_counts = dict()
        for key in labels_key:
            label_counts[key] = labels.count(key)
        return  max(label_counts, key=label_counts.get)
    
    else :
        att_thre, entropy = best_partition_entropy(inputs)
        partitions = partition_by(inputs,att_thre[0],att_thre[1])   
        left = build_tree_id3(partitions[0], max_height, current_height+1)
        right = build_tree_id3(partitions[1], max_height, current_height+1)
        subtrees = [att_thre, left, right]
        return (subtrees)


if __name__ == "__main__":
    iris = csv.reader(open('Fisher.txt'), delimiter='\t')
    header = iris.__next__()  # change to iris.next() for python2!
    data_ = list(d for d in iris)
    data = list([[float(di) for di in d[1:]] for d in data_])
    label = list([int(d[0]) for d in data_]) 
    datas = []
    for d,i in zip(data,label):
        d = tuple(d)
        datas.append(((d),i))
    for i in range(10):
        tree = build_tree_id3(datas,i)   
        tree_accuracy(tree,data,label)
        print(tree_accuracy(tree,data,label))
