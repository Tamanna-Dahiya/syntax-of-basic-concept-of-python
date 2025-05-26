# INTRODUCTION TO PANDAS 
'''PANDAS(PANEL DATA)IS AN OPEN SOURCE PYTHON LIBRARY WHICH MAKES DATA ANALYSIS EASIER AND EFFECTIVE.
   IT WAS DEVELOPED BNY WES MECKENNY IN 2008.IT PROVIDES FLEXIBLE AND POWERFUL DATA STRUCTURES THAT MAKES DATA MANIPULATION EASIER.'''
 #FEATURES OF PANDAS
'''1.IT CAN READ OR WRITE IN DIFFERENT DATA FORMATS(INT,FLOAT,DOUBLE)
    2.SIZE MUTABILITY
    3.FUNCTIONALITY TO FIND AND FILL MISSING DATA
    4.MAKES DATA VISUALISATION EASIER
    5.ALLOWS MERGING AND JOINING OF DATA'''
# DATA STRUCTURES-WAY TO STORE OR ORGANISE DATA IN COMPUTER
#PANDAS PROVIDE THREE DATA STRUCTURE-SERIES,DATAFRAME,PANEL
                       #SERIES
'''SERIES IS ONE DIMENSIONAL DATA STRUCTURE THAT STORES HOMOGENEOUS AND MUTABLE DATA.
    SIZE OF SERIES IS IMMUTABLE BUT DATA IS MUTABLE'''
# CREATING EMPTY SERIES AND ALSO VERFYING ITS SERIES
import pandas as pd
s=pd.Series()
print(s)
print(type(s)) 
# Series creation with the help of list
import pandas as pd
s1=pd.Series([1,2,3,4,5])# by default indices starts from 0
print(s1)
#series creation with the help of two lists
import pandas as pd
months=["jan","feb","mar","apr","may"]
days_months=pd.Series([31,28,31,30,31],index=months) 
print(days_months)
#series creation using range()
import pandas as pd
s2=pd.Series(range(5))
print(s2)
#series by using concept of loop
# handling values
import pandas as pd
s4=pd.Series([1,2,3,4,5.5])
print(s4)#float is superior to int data type so interpreter will automatically convert int to float
# series with missimg values
# NaN is special floting point value indicating null values in python it is an attribute pof numpy library
import pandas as pd
import numpy as np
s5=pd.Series([1,2,3,np.nan])
print(s5)
 #to change its index
s5.index=[1,2,3,4]
print(s5)
# creating series with dictionary(keys will become indices and values will become data)
import pandas as pd
dict={"Name":"Tamanna Dahiya","Course":"Btech Cse","year":"First"}
s6=pd.Series(dict)
print(s6)
# creating series using a scalar
import pandas as pd
s7=pd.Series(50,index=[1,2,3,4,5])
print(s7)
#creating series using mathe,atical function or expression
import pandas as pd
import numpy as np
a=np.arange(10,14)
print(a)
s8=pd.Series(a*4,index=a)#using expression
print(s8)
import pandas as pd
import numpy as np
a=np.arange(10,14)
print(a)
s8=pd.Series(a**4,index=a)#using function
print(s8)
# creating series using numpy array
import pandas as pd
import numpy as np
array=np.array([1,2,3,4,5])
s9=pd.Series(array)
print(s9)
#changing the name of series and name of index
s9.name="array"
s9.index.name="index"
s9.index=[1,2,3,4,5]
print(s9)
#indexing
#to access single element
import pandas as pd
import numpy as np
a=np.arange(10,14)
print(a)
s8=pd.Series(a**4,index=a)
print(s8[10])
print(s8[11])
#to access more than one element make a list of that elements
print(s8[[11,12,13]])
#slicing
print(s1[:3])
print(s8[11:13])