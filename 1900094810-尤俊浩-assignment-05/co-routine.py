import asyncio
import time
import csv
res = []
async def readfile():
    global res
    csv_reader = csv.reader(open("IBM_2006-01-01_to_2018-01-01.csv", "r"), delimiter=',')
    cnt = 0
    for row in csv_reader:
        cnt += 1
        if cnt % 2:
            res.append(row)

async def writefile():
    global res
    writer = csv.writer(open('new.csv', mode='w',newline=""), delimiter=",")
    for i in res:
        writer.writerow(i)
    
async def main():
    print(f"start at {time.strftime('%X')}")
    await readfile()
    await writefile()
    print(f"finish at {time.strftime('%X')}")

asyncio.run(main())
