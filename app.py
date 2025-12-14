import time
from datetime import datetime

print("🚀 Python Docker App Started")

for i in range(1, 6):
    print(f"Count: {i} | Time: {datetime.now()}")
    time.sleep(1)

print("✅ App Finished Successfully")
