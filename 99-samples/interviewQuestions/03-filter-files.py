from os import walk


dirPath = './samples/interviewQuestions'


onlyPythonFiles = []
_, _, fileNames =  next(walk(dirPath))


for fileName in fileNames:
  if fileName.split('.')[-1] == 'py':
    onlyPythonFiles.append(fileName)


print(onlyPythonFiles)