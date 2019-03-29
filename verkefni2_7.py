#verkefni2_7
import csv
import datetime
def release_days(cast_file, dates_file, actors):
    

    with open(cast_file, 'r', encoding = 'utf-8') as f:
        read = csv.reader(f, delimiter= ",")
        cast_list = list(read)
    
    dates_list = [] #dates_list = list(read) still thought everything else was valid
    with open(dates_file, 'r', encoding = 'utf-8') as f:
        read = csv.reader(f, delimiter= ",")
        for x in read:
            if 'USA' in x[2]:
                dates_list.append(x)

    movie_actor_match = []
    for title in cast_list:
        for star in actors:
            if star in title[2]:
                movie_actor_match.append(title)

    res = {}
    l = []
    days = set()
    for title in movie_actor_match:
        for release_day in dates_list:
            if title[0] == release_day[0] and title[1] == release_day[1]:
                total_date = release_day[3]
                #get the weekday value from datetime as key for dict of movies and release days, 0 based so +1
                day_key = datetime.datetime(int(total_date[0:4]), int(total_date[5:7]), int(total_date[8:10])).weekday()+1
                days.add(day_key)
                l.append([title[0], day_key])
    

    for day in days:
        res[day] = []

    for movie in sorted(l, key=lambda x: x[0]): #sort the titles by their name 
        print(movie[0])
        res[movie[1]].append(movie[0])

    for day in days:
        res[day] = set(res[day])

    print(res)
    return res

#release_days('cast.csv', 'dates.csv', ['Meg Ryan', 'Tom Hanks']) 