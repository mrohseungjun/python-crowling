import csv
with open("singer2.csv","r")as inFp:
    csvReadr = csv.reader(inFp)
    header_list = next(csvReadr)
    print(header_list[1],header_list[6])
    for row_list in csvReadr:
        youtube = int(row_list[6].replace(',',''))
        youtube = int(youtube/10000)
        print(row_list[1],str(youtube)+"만")
        