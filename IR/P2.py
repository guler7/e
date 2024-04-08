# BOOLEAN RETRIEVAL

###################
## METHOD - 1
###################

def bitwise_operation(a, b):
    #BIT AND result
    bit_and_result = a & b

    #BIT OR result 
    bit_or_result = a | b

    #BIT XOR result
    bit_xor_result = a ^ b

    #BIT NOT result
    bit_not_result = ~a, ~b

    #BIT Left Shift
    bit_lshift_result = a << 1

    #BIT Right Shift
    bit_rshift_result = b >> 1

    print('Bitwise AND Result: ', bit_and_result)
    print('Bitwise OR Result: ', bit_or_result)
    print('Bitwise XOR Result: ', bit_xor_result)
    print('Bitwise NOT Result: ', bit_not_result)
    print('Bitwise Left Shift Result: ', bit_lshift_result)
    print('Bitwise Right Shift Result: ', bit_rshift_result)


a = int(input('Enter a binary Number: '))
b = int(input('Enter another binary Number: '))

bitwise_operation(a, b)


###################
## METHOD - 2
###################

import pandas as pd 
from sklearn.featudre_extraction.text import CountVectorizer 
print("Boolean Retrivel ModelUsing Bitwise operations on Term Document Incidence Matrix") 
corpus={'this is the first documnent', 'this document is the second document','and is the third document','Is This Is The First Document?'} 
print("The Corpus is:\n",corpus) 
vecsftorizer=CountVectorizer() 
x12=vectorizer.fit_transform(corpus) 
ddf=pd.DataFrame(x.toarray(),columns=vecctorizer.get_feature_names_out()) 
print("the generated data frame") 
print(df) 
print("query processing on term document incidence matrix ") 
#AND 
print("1.find all document ids for query 'this' AND 'first'") 
alldasdfa=df[(df['this']==1)&(df['first']==1)] 
print("document ids where either 'this' AND 'first'are present are:",alldata.index.tolist()) 
#OR 
print("2.find all document ids for query 'this' OR 'first'") 
alldsdfata=df[(df['this']==1)|(df['first']==1)] 
print("document ids where either 'this' OR 'first'are present are:",alldata.index.tolist()) 
#NOT 
print("3.find all document ids for query NOT 'and'") 
alldasdfata=df[(df['and']!=1)] 
print("document ids where 'and' term is not present are: ",alldata.index.tolist())
