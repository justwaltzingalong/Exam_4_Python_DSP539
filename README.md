# Exam_4_Python_DSP539

Included in this repository is a python script, python test script, a data file, and output files with the express purpose of aiding indivduals in genetic analysis tasks.


This python script is a script used to read each line in a text file containing DNA sequences. 
The script has 3 main functions:
1)  Calculate possible combinations of strings (should be larger or equal to tha observed)
2)  Calculate observed combinations of strings
3)  Calcualte the linguistic complexity which is a measure of the total number of strings observed/ sum of the totoal possible strings.
4)  The script outputs possible and observed combinations of strings ,also calculates linguistic complexity of each line of the text file.
5)  The information is presented in dataframe style via the useage of pandas with the columns being in order K value, observed kmers and possible kmers.
6)  Linguistic Complexity appears at the bottom of each dataframe per sequence analyzed.

To run this script in python: use Test_4main.py
In order to read in a file to this script, you must create a text file containing DNA sequences and name it listofstrings2.txt This script will create the outputs stated above for each line of the text file.

To test this script in python: py.test Test_CasesExam4.py
This script contains a series of tests to ensure all fucntions run as they should.

If you have any questions or diffculty with the script please email:
Nicholaswaltz33@gmail.com for assistance.
