#!/usr/bin/env python3


from __future__ import print_function

import argparse
import csv
import sys
import os
import statistics
import collections


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def detectTaskType(value):
    if value.isdigit():
        return "YearBasedTask"
    elif value.startswith("Class"):
        return "CoarseGrainedTask"
    elif value.isdigit() is not True:
        if len(value) > 4 and value[4] == "-":
            return "FineGrainedTask"
    else:
        raise Exception("Unidentified type of task")


class ClassificationOutput:
    def checkDataStructure(self):
        filledCol = -1
        rowCount = 1
        self.rows = []
        self.taskTypeInTheRow = []
        self.valueForEachTypeTask = {}
        self.retrievedResultsForEachTask = {}
        self.rowsById = {}
        self.distinctId = set()
        for row in self.csv_rows:
            self.distinctId.add(row[0])
            # check cells            
            if len(row) > 4:
                eprint("Too many columnsat row " + str(rowCount))
                sys.exit()

            taskTypeInCurrentLine = []
            colNumber = 0
            for col in row:
                if colNumber > 0:
                    taskTypeInCurrentLine.append(detectTaskType(col))
                    if detectTaskType(col) not in self.valueForEachTypeTask:
                        self.valueForEachTypeTask[detectTaskType(col)] = set()
                    self.valueForEachTypeTask[detectTaskType(col)].add(col)
                    if col not in self.retrievedResultsForEachTask:
                        self.retrievedResultsForEachTask[col] = 0
                    self.retrievedResultsForEachTask[col] += 1

                if (len(col) > 0):
                    colNumber += 1
                    
            if filledCol > -1 and filledCol != colNumber:
                eprint("Inconsistency in data file: variable number of columns at row " + str(rowCount))
                sys.exit()
            if len(self.taskTypeInTheRow) > 0 and self.taskTypeInTheRow != taskTypeInCurrentLine:
                eprint("Inconsistency in data file: different type of task at row " + str(rowCount))
                sys.exit()
            else:
                filledCol = colNumber
                if (len(self.taskTypeInTheRow) == 0):
                    for x in range(1, len(row)):
                        self.taskTypeInTheRow.append(detectTaskType(row[x]))
            rowCount += 1
            self.rows.append(row)
            self.rowsById[row[0]] = row


    def checkIfValueOfATaskIsAllowed(self, task, value):
        if value in self.valueForEachTypeTask[task]:
            return True
        else:
            return False

    def getRowsCount(self):
        return len(self.distinctId)

    def getRowWithId(self, id):
        return self.rowsById[id]

    def getRowAtIndex(self, n):
        return self.rows[n]

    def __init__(self, filePath):
        #print("Loading " + filePath + " file...")
        self.filePath = filePath
        tsv_file = open(self.filePath)
        read_tsv = csv.reader(tsv_file, delimiter="\t")
        self.csv_rows = read_tsv
        self.checkDataStructure()


class Results:
    def __init__(self, taskType, goldRetrieved, runRetrieved):
        self.taskType = taskType
        self.runRetrievedResults = 0
        self.goldRetrieved = goldRetrieved
        self.runRetrieved = runRetrieved
        self.valuesDeviation = []
        self.positive = 0
        self.negative = 0
        self.positiveByTask = {}



    def compareResults(self, goldValue, runValue):
        self.runRetrievedResults += 1
        if goldValue == runValue:
            self.positive += 1
        if (self.taskType == "YearBasedTask"):
            self.valuesDeviation.append(abs(int(goldValue) - int(runValue)))
        
        if goldValue not in self.positiveByTask:
            self.positiveByTask[goldValue] = 0
        if runValue not in self.positiveByTask:
            self.positiveByTask[runValue] = 0
        if goldValue == runValue: 
            self.positiveByTask[runValue] += 1


    def printResults(self):
        if (self.runRetrievedResults > 0):
            f1s = []
            print(self.taskType+":\n")
            print("Overall precision: " + str(round((self.positive / self.runRetrievedResults), 6)) + "\n")
            if (self.taskType == "YearBasedTask"):
                print("Standard Deviation of sample is "+ str(round(statistics.stdev(self.valuesDeviation), 3))+ "\n")

            for key in sorted(self.positiveByTask.keys()) :
                if key not in self.runRetrieved:
                    precision = 0
                else:
                    precision = (self.positiveByTask[key] / self.runRetrieved[key])

                if key not in self.goldRetrieved:
                    recall = 0
                else:
                    recall = (self.positiveByTask[key] / self.goldRetrieved[key])

                try:
                    f1 = 2 * ((precision * recall) / (precision + recall))
                except:
                    f1 = 0.0
                f1s.append(f1)
                print(key + " Precision: " + str(round(precision, 3)) + " Recall: "+ str(round(recall, 3))+  " F1:" + str(round(f1, 3)))
            
            print("\nF1 Mean: " + str(round(statistics.mean(f1s),3)))
            print("-----------------------------------------------------")



def evaluate(gold, run):
    if gold.getRowsCount() != run.getRowsCount():
        eprint("Run file has a different number of results compared to gold file")
        sys.exit()

    goldTaskTypeMapping = {}
    resultsByTask = {}

    for goldColIndex in range(1, len(gold.getRowAtIndex(0))):
        goldTaskType = detectTaskType(gold.getRowAtIndex(0)[goldColIndex])
        goldTaskTypeMapping[goldTaskType] = goldColIndex
        resultsByTask[goldTaskType] = Results(goldTaskType, gold.retrievedResultsForEachTask, run.retrievedResultsForEachTask)

    for lineIndex in range(0, run.getRowsCount()):
        
        runResult = run.getRowAtIndex(lineIndex)
        try:
            goldResult = gold.getRowWithId(runResult[0])
        except KeyError:
            eprint("Id not found in goldstandard data.")
            sys.exit()

        for runColIndex in range(1, len(runResult)):
            resultOfTheRun = runResult[runColIndex]
            typeOfResult = detectTaskType(resultOfTheRun)

            if typeOfResult != "YearBasedTask":
                if not gold.checkIfValueOfATaskIsAllowed(typeOfResult, resultOfTheRun):
                    eprint("The value " + resultOfTheRun + " is not allowed")
                    sys.exit()
                
            goldResultValue = goldResult[goldTaskTypeMapping.get(typeOfResult)]
            resultsByTask[typeOfResult].compareResults(goldResultValue, resultOfTheRun)

    return resultsByTask


def processFile(goldData,testData):
    print("\n-----------------------------------------------------")
    print("Evaluation of file: " + testData.filePath)
    print("-----------------------------------------------------")
    results = evaluate(goldData, testData)
    for resultTask in results:
        results[resultTask].printResults()


def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--gold_file", type=str, required=True, 
                        help="Path to the TSV file with the gold data.")
    parser.add_argument("--system_file", type=str, required=True,
                        help="Path to the TSV file or folder containig TSV files with the predicated data.")
    args = parser.parse_args()
    

    goldData = ClassificationOutput(args.gold_file)
    
    if os.path.isfile(args.system_file):
        testData = ClassificationOutput(args.system_file)
        processFile(goldData, testData)
    elif os.path.isdir(args.system_file):
        for file in os.listdir(args.system_file):
            if file.endswith(".tsv"):
                testData = ClassificationOutput(os.path.join(args.system_file, file))
                processFile(goldData, testData)


if __name__ == "__main__":
    main()
