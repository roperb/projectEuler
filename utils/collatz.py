def collatzStepNumber(n):
    step = 1
    while n > 1:
        if n%2 == 0:
            n = n/2
            step += 1
        else:
            n = (3*n+1)/2
            step+=2
    return step
