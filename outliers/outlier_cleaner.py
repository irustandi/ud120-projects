#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []
    import math
    import numpy

    ### your code goes here
    residuals = sorted(numpy.fabs(predictions - net_worths))
    refIdx = int(0.9 * len(residuals))
    refValue = residuals[refIdx]

    for idx in range(0, len(ages)):
        errorValue = predictions[idx] - net_worths[idx]
        if math.fabs(errorValue) < refValue:
            tupleValue = (ages[idx], net_worths[idx], errorValue)
            cleaned_data.append(tupleValue)

    return cleaned_data

