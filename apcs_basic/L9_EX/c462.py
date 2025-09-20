#
# c462 交錯字串
#

while True:
    try:
        #start
        K = int(input())
        string = input()

        upper = 0
        lower = 0

        lenTemp = 0
        maxLen = 0

        prevChar = ''

        if string[0].isupper() == True:
            prevChar = 'u'
            upper = 1
            
            if K == 1:
                lenTemp = K
                maxLen = lenTemp
        else:
            prevChar = 'l'
            lower = 1
            if K == 1:
                lenTemp = K
                maxLen = lenTemp


        for i in range(1, len(string)):
            # 大 -> 大
            if string[i].isupper() and prevChar == 'u':
                upper += 1
                lower = 0

                if upper == K:
                    lenTemp += K
                    maxLen = max(lenTemp, maxLen)

                if upper > K:
                    lenTemp = K
            
            # 小 -> 小
            elif string[i].islower() and prevChar == 'l':
                upper = 0
                lower +=1

                if lower == K:
                    lenTemp += K
                    maxLen = max(lenTemp, maxLen)

                if lower > K:
                    lenTemp = K

            # 小 -> 大
            elif prevChar == 'l' and string[i].isupper():
                if lower < K:
                    lenTemp = 0

                upper = 1
                lower = 0
                
                if K == 1:
                    lenTemp += K
                    maxLen = max(lenTemp, maxLen)

                prevChar = 'u'

            # 大 -> 小
            elif prevChar == 'u' and string[i].islower():
                if upper < K:
                    lenTemp = 0

                upper = 0
                lower = 1
                
                if K == 1:
                    lenTemp += K
                    maxLen = max(lenTemp, maxLen)

                prevChar = 'l'

        print(maxLen)
    except:
        break
