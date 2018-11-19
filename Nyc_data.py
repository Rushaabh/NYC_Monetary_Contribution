import numpy as np
import pandas as pd


nyc = pd.read_csv('ny.csv.csv',index_col= False,low_memory= False) # Read the CSV file

parties = {'Clinton, Hillary Rodham':'Democrat', 'Sanders, Bernard':'Democrat', 'Trump, Donald J.':'Republican',

       "O'Malley, Martin Joseph":'Democrat', "Cruz, Rafael Edward 'Ted'":'Republican',

       'Walker, Scott':'Republican', 'Bush, Jeb':'Republican', 'Rubio, Marco':'Republican', 'Kasich, John R.':'Republican',

       'Christie, Christopher J.':'Republican', 'Stein, Jill':'Green', 'Johnson, Gary':'Libertarian',

       'Graham, Lindsey O.':'Republican', 'Webb, James Henry Jr.':'Democrat',

       'Carson, Benjamin S.':'Republican', 'Paul, Rand':'Republican', 'Fiorina, Carly':'Republican',

       'Santorum, Richard J.':'Republican', 'Jindal, Bobby':'Republican', 'Huckabee, Mike':'Republican',

       'Pataki, George E.':'Republican', 'Gilmore, James S III':'Republican', 'Lessig, Lawrence':'Democrat',

       'Perry, James R. (Rick)':'Republican', 'McMullin, Evan':'Independent'}
# Defining a dictionary
       
nyc['party']=nyc.cand_nm.map(parties) # adds a new coloumn to the data and fills it with the help of deictionary


#2


df = pd.DataFrame(nyc) #converted into a Data Frame
df['contb_receipt_dt'] = pd.to_datetime(df['contb_receipt_dt']) #convert it to Date Time

#3

df2 = df.groupby('party')['tran_id'].count() # Groups the Partues & calculates the total number of Donations
df2


#4

df3 = df.groupby(['contb_receipt_dt','party'])['tran_id'].count() # Groups the Parties, Date & calculates the total number of Donations
df3


#5
pd.options.display.float_format = '{:,.2f}'.format
df['contb_receipt_amt'] = df['contb_receipt_amt'].astype(object)
df4 = df.groupby('party')['contb_receipt_amt'].sum()
df4



#6
df5 = df.groupby(['contb_receipt_dt','party'])['contb_receipt_amt'].sum()
df5


#7
df6 = df.groupby('contbr_occupation')['contb_receipt_amt'].sum()
df6 = pd.DataFrame(df6)
df7 = df6.sort_values(['contb_receipt_amt'],ascending=False)
df7
df7.head()

#8
df7.tail()

#9
df8= df.groupby('contbr_employer')['contb_receipt_amt'].sum()
df8 = pd.DataFrame(df6)
df9 = df8.sort_values(['contb_receipt_amt'],ascending=False)
df9
df9.head()




'''
#10
df10 = df[['cand_nm','contbr_occupation','contb_receipt_amt']].copy()
df11 = df10.sort_values(['contbr_occupation','contb_receipt_amt'], ascending=[1,0])
df11
df12 = df10[['cand_nm','contbr_occupation',['contb_receipt_amt'.sum()]]
'''