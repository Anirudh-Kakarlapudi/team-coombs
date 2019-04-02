#Make Directory
import os
extractPathTest = "D:\\Sushanth\\UGA Notes\\Sem2-DSP,DM,DCS\\DSP\\Projects\\Project 3\\project3\\extractedZipTest"
extractPathTrain = "D:\\Sushanth\\UGA Notes\\Sem2-DSP,DM,DCS\\DSP\\Projects\\Project 3\\project3\\extractedZipTrain"
if not os.path.isdir(extractPathTest):
    os.mkdir(extractPathTest)
if not os.path.isdir(extractPathTrain):
    os.mkdir(extractPathTrain)

#Extracting Zip files
import zipfile
extractPathTest = "D:\\Sushanth\\UGA Notes\\Sem2-DSP,DM,DCS\\DSP\\Projects\\Project 3\\project3\\extractedZipTest"
extractPathTrain = "D:\\Sushanth\\UGA Notes\\Sem2-DSP,DM,DCS\\DSP\\Projects\\Project 3\\project3\\extractedZipTrain"
#extract test files
for testFile in testFiles:
    filePath = "D:\\Sushanth\\UGA Notes\\Sem2-DSP,DM,DCS\\DSP\\Projects\\Project 3\\project3\\" + testFile
    zip_ref = zipfile.ZipFile(filePath, 'r')
    zip_ref.extractall(extractPathTest)
    zip_ref.close()

for trainFile in trainFiles:
    filePath = "D:\\Sushanth\\UGA Notes\\Sem2-DSP,DM,DCS\\DSP\\Projects\\Project 3\\project3\\" + trainFile
    zip_ref = zipfile.ZipFile(filePath, 'r')
    zip_ref.extractall(extractPathTrain)
    zip_ref.close()

#deleting the zip files from the extracted folder
import os
extractPathTest = "D:\\Sushanth\\UGA Notes\\Sem2-DSP,DM,DCS\\DSP\\Projects\\Project 3\\project3\\extractedZipTest"
extractPathTrain = "D:\\Sushanth\\UGA Notes\\Sem2-DSP,DM,DCS\\DSP\\Projects\\Project 3\\project3\\extractedZipTrain"
#extract test files
for testFile in testFiles:
    os.remove(extractPathTest + testFile)

for trainFile in trainFiles:
    os.remove(extractPathTrain + trainFile )
