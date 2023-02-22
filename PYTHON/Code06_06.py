import re
# 오류 발생 코드
with open("singer2.csv","r")as inFp:
    header = inFp.readline()
    header = header.strip()
    header_list = header.split(',')
    print(header_list[1],header_list[6])

    for inStr in inFp:
        inStr = re.sub('"','',inStr)
        inStr = inStr.strip()
        row_list = inStr.split(',')
        youtube = int(row_list[6])
        youtube = int(youtube/10000)
        print(row_list[0],str(youtube)+"만")
        