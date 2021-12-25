# Exercise 4.2 - Ah Boy's PSLE score

import numpy as np

def tScoreSubjectCalculator(CandidateMark, Average, StandardDeviation):
    
    TScore = int( 50 + 10 * (CandidateMark - Average) / StandardDeviation ) # Use int to round off
    return TScore

def main():
    # Given Data
    English = [60, 90, 35, 85, 70, 50]
    MotherTongue = [70, 50, 55, 75, 60, 40]
    Math = [90, 85, 70, 85, 70, 75]
    Science = [80, 75, 60, 95, 55, 65]
    
    CandidateMarkList = [60, 70, 90, 80]
    
    MarkList = [English, MotherTongue, Math, Science]
    MeanList, StandardDeviationList, TScoreList = [], [], []
    
    for count, x in enumerate(MarkList):
        
        StandardDeviationList.append(np.std(x))
        MeanList.append(np.mean(x))
    
    for count, x in enumerate(CandidateMarkList):
    
        TScoreList.append(
            tScoreSubjectCalculator(
                x, MeanList[count], StandardDeviationList[count]
                )
            )
        
    TScore = np.sum(TScoreList)
        
    print(TScore)
    
if __name__ == "__main__":
    
    main()
    