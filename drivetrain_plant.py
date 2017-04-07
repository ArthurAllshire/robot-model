import numpy as np

class DriveTrainPlant:
    max_voltage = 12

    G = 10.71

    n_motors = 4

    stall_current = 133*n_motors
    stall_torque = 2.42*G*n_motors
    free_current = 2.7*n_motors
    free_speed = 556/G

    R = max_voltage / stall_current

    Kv = free_speed/(max_voltage - free_current*R)

    Kt = stall_torque/stall_current

    r = 6*0.0254/2

    J = r**2 * 30 / G

    D = 1.8*10e-0

    def __init__(self, dt):
        self.x_hat = np.array([0,0,0]).reshape(-1, 1)
        self.A = np.array([
            [1, dt, dt**2],
            [0, 1, dt],
            [0, self.r*(((-self.Kt/(self.Kv*self.R*self.J*self.G)))-self.D), 0]
            ]).reshape(3,3)
        self.B = self.r*(self.Kt/(self.R*self.J*self.G**2))*np.array([dt**2,dt,1]).reshape(-1,1)

    def predict(self, voltage):
        # cap voltage to +/- 12
        voltage = max(min(12, voltage), -12)
        self.x_hat = np.dot(self.A, self.x_hat) + self.B*voltage

    def get_pos(self):
        return self.x_hat[0][0]

    def get_vel(self):
        return self.x_hat[1][0]
