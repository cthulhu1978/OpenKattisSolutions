from datetime import date

day,month = map(int, input().split())
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dayOfWeek = date(2009,month,day).weekday()
print(weekday[dayOfWeek])
