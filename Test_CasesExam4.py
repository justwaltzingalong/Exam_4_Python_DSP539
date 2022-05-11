# Test Cases for the Main Files Functions:

from Test_4main.py import*

#observed tests
def test_obs_sub_k_is_9(): #when k value is the same as string length
    result=observed_substrings('ATTTGGATT',9)
    expected=1
    assert result==expected
    
def test_obs_sub_k_is_10(): #when k value is larger than string length
    result=observed_substrings('ATTTGGATT',10)
    expected=0
    assert result==expected 

def test_obs_sub_k_is_14(): #when k value is shorther than string length
    result=observed_substrings('ATATATATATATATATA',14)
    expected=4
    assert result==expected 

def test_obs_sub_k_is_30():
    result=observed_substrings('ACTGCAGCGCGATGATGAGAGAGATTTCAGGACACACATTGCCAAATTGAGGCAT',30)
    expected=26
    assert result==expected 
                               
#possible tests
def test_pos_k_is_2(): #when k value is shorter than string length
    result=sub_str_possible('ATTTGGATT',2)
    expected=8
    assert result==expected

def test_pos_k_is_19():
    result=sub_str_possible('ATATATATATATATATA',19) #when K is larher
    expected=
    assert result==expected

def test_pos_k_is_17(): #when k value is the same as string length
    result=sub_str_possible('ATATATATATATATATA',17)
    expected=1
    assert result==expected

# Test Cases for LC:

#ling complx tests
def test_ling_complx_1(): #correct linguistic complexity
    result=ling_complx('ATATATATATATATATA')
    expected= 0.2357142857142857
    assert result==expected

def test_ling_complx_2(): #correct linguistic complexity
    result=ling_complx('ATTTGGATT')
    expected=0.875
    assert result==expected
    
def test_ling_complx_3(): #correct linguistic complexity
    result=ling_complx('ACTGCAGCGCGATGATGAGAGAGATTTCAGGACACACATTGCCAAATTGAGGCAT')
    expected=0.9738111647139903
    assert result==expected
