import random
from datetime import datetime

with open("sample.log", "w") as f:
    for i in range(1000):
        f.write(
            f"2024-03-15T14:23:{i%60:02d}Z 192.168.1.{i%255} GET /api/users 200 {random.randint(10,500)}ms\n"
        )

    f.write("MALFORMED LINE\n")
    f.write('{"timestamp":"2024-03-15T14:23:01Z","ip":"10.0.0.1","method":"GET","path":"/api","status":200,"response_time":"100ms"}\n')
