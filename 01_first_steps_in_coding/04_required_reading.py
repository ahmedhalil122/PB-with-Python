pages_count = int(input())
pages_per_hour = int(input())
days = int(input())

total_time_required = pages_count//pages_per_hour
total_time_per_day_required = total_time_required//days

print(total_time_per_day_required)
