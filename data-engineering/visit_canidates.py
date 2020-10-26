import math
import csv


def Distance(Lat0, Long0, Lat1, Long1):
    RadiusEarth = 3958.8 #miles
    Lat0 = math.radians(Lat0)
    Long0 = math.radians(Long0)
    Lat1 = math.radians(Lat1)
    Long1 = math.radians(Long1)
    # had to look this one up, "great circle distance"
    ArcDistance = math.acos(math.sin(Lat0)*math.sin(Lat1) + math.cos(Lat0)*math.cos(Lat1)*math.cos(Long0-Long1))

    return ArcDistance * RadiusEarth

Solutions = []
with open('./Stores.csv', newline='') as StoreFile:
    Stores = csv.DictReader(StoreFile)

    for Store in Stores:
        with open('./Team.csv', newline='') as TeamFile:
            Members = csv.DictReader(TeamFile)

            Canidates = []
            for Member in Members:
                Canidates.append([Member['EMAIL'], Distance(
                float(Store['LAT']), float(Store['LONG']),
                float(Member['LAT']), float(Member['LONG']))])

            Canidates.sort(key = lambda t: t[1])
            CanidatesList = [Store['NUMBER']] + Canidates[0] + Canidates[1] + Canidates[2]
            Solutions.append(CanidatesList)

with open('./Answers.csv', 'w', newline='') as OutFile:
    writer = csv.writer(OutFile)
    writer.writerow(['Store Number',
                     'First Canidate', 'Distance',
                     'Second Canidate', 'Distance',
                     'Third Canidate', 'Distance'])
    writer.writerows(Solutions)
