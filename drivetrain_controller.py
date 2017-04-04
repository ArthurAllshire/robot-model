from drivetrain_plant import DriveTrainPlant
import numpy as np
import matplotlib.pyplot as plt

dt = 0.02
sp = 5

drivebase = DriveTrainPlant(dt)

positions = []
velocities = []
times = np.arange(0, 10, dt)
setpoints = [sp]* len(times)
for tm in times:
    positions.append(drivebase.get_pos())
    velocities.append(drivebase.get_vel())
    output = 12 # voltage, between +/- 12; what the pid loop is controlling
    drivebase.predict(output)

plt.figure(1)

plt.plot(times, positions, "b-", times, setpoints, "r-")
plt.show()
