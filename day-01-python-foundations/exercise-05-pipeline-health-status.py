rows_loaded = 9900
rows_failed = 100
runtime_minutes = 30

failure_rate = rows_failed/(rows_loaded+rows_failed) * 100
print(failure_rate)

if failure_rate <= 2 and runtime_minutes <= 20:
    print("Healthy")

elif  2 < failure_rate <= 5:
    print("Warning") 

elif failure_rate > 5:
    print("Critical")

else:
    print("Warning: Runtime is too high")
