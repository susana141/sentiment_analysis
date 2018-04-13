import csv
import json
import pandas as pd

infile = open("reviews_Books_5.json","r")
outfile = open ("reviews_Books_5.csv","w")

writer = csv.writer(outfile)
writer.writerow(["reviewerID","asin","helpful","reviewText","overall","summary",
                 "unixReviewTime","reviewTime","reviewType"])

for row in infile:
  data = json.loads(row)
  writer.writerow([data["reviewerID"], data["asin"], data["helpful"],data["reviewText"], data["overall"], data["summary"], data["unixReviewTime"],
                   data["reviewTime"],])

dataset = pd.read_csv("reviews_Books_5.csv", dtype={"overall":str})

print(type(dataset["overall"]))

for i in dataset["overall"]:
    if i == 1.0 or 2.0:
        writer.writerow({"reviewType":"Negative"})
    if i == "3.0":
        writer.writerow({"reviewType":"Neutral"})
    if i == "4.0" or "5.0":
        writer.writerow({"reviewType":"Positive"})
