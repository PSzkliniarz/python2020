def fun(N):
    nZeros = 0

    binary = bin(N)
    withoutPrefix = binary[2:]

    print(N, " = ",withoutPrefix)

    rightOneBit = 1
    previousBit = 0

    #szukanie prawej jedynki
    i = 1
    for i in range(33):
        previousBit += 1


        if (N & rightOneBit) == rightOneBit:
            rightOneBit = rightOneBit << 1
            break


        rightOneBit = rightOneBit << 1



    currentBit = previousBit

    for j in range(i + 1, 33):
        currentBit += 1


        #ilość zer to różnica między jedynkami
        if (N & rightOneBit) == rightOneBit:
            #wybieramy największą
            if nZeros < (currentBit - previousBit - 1):

                nZeros = currentBit - previousBit - 1


            previousBit = currentBit

        rightOneBit = rightOneBit << 1

    return nZeros

print("Najdłuższa binarna przerwa: " , fun(1041))

