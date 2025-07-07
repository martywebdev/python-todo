import glob
import csv
import shutil
import webbrowser

# myfiles = glob.glob("../files/*.txt")
#
# for filepath in myfiles:
#     with open(filepath, "r") as f:
#         print(f.read())




# with open("weather.csv", mode="w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Day", "Temperature", "Condition"])
#     writer.writerow(["Monday", 23, "Sunny"])
#     writer.writerow(["Tuesday", 19, "Rainy"])


# with open("../files/weather.csv", "r") as f:
#     data = list(csv.reader(f))
#
# city = input("Enter city: ")
#
# for row in data[1:]:
#     if city.title() == row[0]:
#         print(row[1])"


# shutil.make_archive("../files/output", "zip", "../files")

search = input("Search: ")
webbrowser.open("https://google.com/search?q=" + search)