#!/usr/bin/env python3

import pandas as pd  #This installs pandas function for the creation of a data table


def numberpossibleKmer(k, mystring):
  assert k > 0 and k <= len(mystring), 'k must be > 0 and ≤ string length'
  for c in mystring:
    assert c in ["A","C","T","G"], 'invalid character in string'
  return min(len(mystring) - k + 1, 4**k)

#Question 2
# return number of kmers of length k
def numberOfObservedKmers(k,string):
  strlen = len(string)
  assert k > 0 and k <= strlen, 'k must be > 0 and ≤ string length'
  for c in string:
    assert c in ["A","C","T","G"], 'invalid character in string'
  kmers = set() #set of substrings
  for i in range(strlen - k + 1):
    kmer = string[i:i+k] # substring of length k
    kmers.add(kmer)
  array_of_kmers = list(kmers)
  array_of_kmers.sort()
  return len(kmers)


def createDataFrame(string):   #The purpose of this is to allow for the creation of a data frame 
  return pd.DataFrame({'k': [i for i in range(1,len(string)+1)],
          'observed kmers': [numberOfObservedKmers(i,string) for i in range(1,len(string)+1)],
          'possible kmers': [numberpossibleKmer(i,string) for i in range(1,len(string)+1)]})


def LinguisticComplexity(s): #This function will give the linguistic complexity of certain genetic sequences.
    totalObserved = 0
    totalPossible = 0
    for L in range(1, len(s) + 1):
      totalObserved += numberOfObservedKmers(L,s)
      totalPossible += numberpossibleKmer(L,s)
    return totalObserved / totalPossible


myfile = 'listofstrings2.txt' #this is the text file with the sequences
with open(myfile, "r") as f:
    for eachline in f:
        eachline = eachline.strip() #split each line so it can be looped through the functions
        print(eachline)            #This step provides the out put of each line
        print(createDataFrame(eachline)) # This step helps organize the data into a dataframe
        print(LinguisticComplexity(eachline))
        #This step ensures the outputting of linguistic complexity value for the data set at hand.
  
''' This step will print the output of the operation that we just ran to a new file'''

outF = open("finalresultsfile.txt", "w") 
outF.writelines(all_lines)
outF.close()