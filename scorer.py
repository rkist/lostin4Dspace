def score_medium(yTest, y):
    numSamplesTest = len(y)

    sum = 0
    for i in range(numSamplesTest):
        sum += abs(yTest[i] - y[i])
    media = sum/numSamplesTest

    return media