import pandas as pd
# Given values from the table as lists
arrival_r = [10.72, 8.493, 11.68, 10.74, 9.095, 9.972, 11.35, 10.74, 9.19, 8.542]
service_r = [7.37, 10.77, 9.021, 9.469, 9.905, 9.988, 9.161, 7.081, 10.53, 10.85]

# Initialize lists to store computed values
IAT = []
CAT = []
SB = []
ST = []
SE = []
WT = []
IT = []

# Initialize variables
previous_CAT = 0
previous_SE = 0

for i in range(len(arrival_r)):
    # Inter-Arrival Time
    iat = arrival_r[i]
    IAT.append(iat)
    
    # Cumulative Arrival Time
    cat = previous_CAT + iat
    CAT.append(cat)
    previous_CAT = cat

    # Service Time (same as service_r)
    st = service_r[i]
    ST.append(st)

    # Service Begins: max of CAT or previous SE
    sb = max(cat, previous_SE)
    SB.append(sb)

    # Service Ends
    se = sb + st
    SE.append(se)
    previous_SE = se

    # Waiting Time
    wt = sb - cat
    WT.append(round(wt, 3))

    # Idle Time
    if i == 0:
        it = sb  # For first customer, idle time is equal to time before their arrival
    else:
        it = max(0, sb - SE[i-1])
    IT.append(round(it, 3))

# Create DataFrame to display the table similar to the one in the image
df = pd.DataFrame({
    "i": list(range(1, 11)),
    "r' (Arrival)": arrival_r,
    "IAT": IAT,
    "CAT": CAT,
    "SB": SB,
    "r' (Service)": service_r,
    "ST": ST,
    "SE": SE,
    "WT": WT,
    "IT": IT
})

df.round(3)  # Round values for cleaner display similar to the table