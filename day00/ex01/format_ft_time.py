import datetime as dt
import time

start_date = dt.datetime(1970, 1, 1)

total_seconds = time.time()

print(f"Seconds since {start_date.strftime("%B %d, %Y")}: \
{total_seconds:,.4f} or {total_seconds:.2e} in scientific notation")