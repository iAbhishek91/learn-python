import pandas as pd


def isModuleTestCoverageAccepted(line):
  if (float(line[1].Cover[:-1])) >= 65:
    print(f'{line[1].Name} have good coverage')
  else:
    print(f'{line[1].Name} have not been properly covered')




filepath = './samples/interviewQuestions/02-test-result.txt'

# read space based file
dataframe = pd.read_csv(filepath, delim_whitespace=True) 

# extract the rows using chaining method
dataframe = dataframe.iloc[1:].iloc[:-2]

# iterate over each rows
for x in dataframe.iterrows():
  # each x is a tuple or number and values are class
  isModuleTestCoverageAccepted(x)
