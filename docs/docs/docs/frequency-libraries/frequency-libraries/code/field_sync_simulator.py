

# field_sync_simulator.py
# Simulates ideal planting times based on HLZ frequencies and moon phase

import math
import datetime

def z_n(n):
    phi = (1 + math.sqrt(5)) / 2
    return phi**n * math.sin(math.pi / n)

today = datetime.date.today()
phase = z_n(10)
print(f"Z(10) planting frequency: {phase:.2f} Hz on {today}")
