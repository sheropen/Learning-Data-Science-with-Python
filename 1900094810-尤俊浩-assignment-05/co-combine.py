import asyncio
import time
import csv

async def readfile(filename):
    res = []
    csv_reader = csv.reader(open(filename, "r"), delimiter=',')
    for row in csv_reader:
        res.append(row)
    return res

async def writefile(lst):
    writer = csv.writer(open('combine.csv', mode='w',newline=""), delimiter=",")
    for i in lst:
        writer.writerow(i)
    
async def main():
    print(f"start at {time.strftime('%X')}")
    task1 = asyncio.create_task(readfile("AMZN_2006-01-01_to_2018-01-01.csv"))
    task2 = asyncio.create_task(readfile("IBM_2006-01-01_to_2018-01-01.csv"))
    lst1 = await task1
    lst2 = await task2
    lst2.pop(0)
    await writefile(lst1+lst2)
    print(f"finish at {time.strftime('%X')}")

asyncio.run(main())
