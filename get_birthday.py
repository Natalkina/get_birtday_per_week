from datetime import datetime, timedelta
from collections import defaultdict

users_dict_list = [
                      {"name": "Sat", "birthday":  datetime.strptime("17 December 2022", "%d %B %Y")},
                      {"name": "Sun", "birthday":  datetime.strptime("18 December 2022", "%d %B %Y")},
                      {"name": "Thur", "birthday":  datetime.strptime("22 December 2022", "%d %B %Y")},
                      {"name": "Mon", "birthday": datetime.strptime("19 December 2022", "%d %B %Y")},
                      {"name": "Tue", "birthday": datetime.strptime("20 December 2022", "%d %B %Y")},
                      {"name": "Wed", "birthday": datetime.strptime("21 December 2022", "%d %B %Y")},
                      {"name": "Wed", "birthday": datetime.strptime("21 December 2022", "%d %B %Y")},
                      {"name": "Thur", "birthday": datetime.strptime("22 December 2022", "%d %B %Y")},
                      {"name": "Fri", "birthday": datetime.strptime("23 December 2022", "%d %B %Y")}
                    ]


def find_next_day_by_weekday(day, weekday, weeks_from_now):
    shift_day = - day.weekday() + 7 * weeks_from_now + weekday
    return day + timedelta(shift_day)

def get_next_birtday(birthday):
    now = datetime.now()
    this_year_birthday = birthday.replace(year=now.year)
    if this_year_birthday < now:
        return birthday.replace(year=now.year+1)
    else:
        return this_year_birthday

def get_birthday_per_week(users):
    found_users = {}
    left_bound = find_next_day_by_weekday(datetime.now(), 5, 0)
    right_bound = left_bound + timedelta(7)
    range = tuple((left_bound, right_bound))
    weekday_map = ["Monday", "Tuesday", "Wednersday", "Thursday", "Friday", "Monday", "Monday"]
    for user in users:
        user_next_birthday = get_next_birtday(user["birthday"])
        if user_next_birthday >= range[0] and user_next_birthday <=range[1]:
            key = weekday_map[user_next_birthday.weekday()]
            if key not in found_users:
                found_users[key] = []

            found_users[key].append(user["name"])
    for key, value in found_users.items():
        print(f"{key}:", " ".join(value))


get_birthday_per_week(users_dict_list)





