import matplotlib.pyplot as plt
from math import pi, sin, cos
class BOOM:
    def __init__(self, mass, v0, angle, gravity, dt):
        self.mass = mass
        self.v0 = v0
        self.v_x = v0 * cos(angle * pi / 180)
        self.v_y = v0 * sin(angle * pi / 180)
        self.a_x = 0
        self.a_y = -1 * gravity
        self.angle = angle * pi / 180
        self.gravity = gravity
        self.dt = dt
        self.pos_x = 0
        self.pos_y = 0

    def nextState(self):
        nv_x = self.v_x + (self.a_x * self.dt)
        nv_y = self.v_y + (self.a_y * self.dt)
        self.v_x = nv_x
        self.v_y = nv_y

        self.pos_x += nv_x * self.dt
        self.pos_y += nv_y * self.dt

        return (self.pos_x, self.pos_y)

    def nowState(self):
        return (self.pos_x, self.pos_y)

class FORCEBOOM(BOOM):
    def __init__(self, mass, v0, angle, gravity, dt, cd):
        super().__init__(mass, v0, angle, gravity, dt)
        self.cd = cd
        
    def nextState(self):
        nv_x = self.v_x + (self.a_x * self.dt)
        nv_y = self.v_y + (self.a_y * self.dt)

        if self.v_x != 0 and self.v_y !=0:
            air_resistance_x = -0.5 * self.mass * nv_x**2 * self.cd * (nv_x**2 + nv_y**2) / (nv_x**2 + nv_y**2) * self.dt
            air_resistance_y = -0.5 * self.mass * nv_y**2 * self.cd * (nv_x**2 + nv_y**2) / (nv_x**2 + nv_y**2) * self.dt

        self.v_x = nv_x + air_resistance_x
        self.v_y = nv_y + air_resistance_y

        self.pos_x += self.v_x * self.dt
        self.pos_y += self.v_y * self.dt

        return (self.pos_x, self.pos_y)
    
if (__name__ == '__main__'):
    forceboom1 = FORCEBOOM(1.0, 100.0, 30.0, 9.8, 0.1, 0.01)
    #forceboom1 = FORCEBOOM(1.0, 100.0, 60.0, 9.8, 0.1, 0.01)
    x_log = [0]
    y_log = [0]
    time = 0
    while forceboom1.pos_x >= 0 and forceboom1.pos_y >= 0:
        forceboom1.nowState()
        print(f"boom1's now state x: {forceboom1.pos_x:.2f}, y: {forceboom1.pos_y:.2f} at {time:.1f}s")
        forceboom1.nextState()
        print(f"boom1's next state x: {forceboom1.pos_x:.2f}, y: {forceboom1.pos_y:.2f} at {time:.1f}s")
        print(f"{forceboom1.dt:.1f} later...\n")

        x_log.append(forceboom1.pos_x)
        y_log.append(forceboom1.pos_y)

        time += forceboom1.dt

    # Plot the trajectory
    plt.xlim(0, 300)
    plt.ylim(0, 300)
    plt.plot(x_log, y_log)

    # Set labels and title
    plt.xlabel('X-Position (m)')
    plt.ylabel('Y-Position (m)')
    plt.title('Projectile Trajectory')

    # Add grid
    plt.grid(True)

    # Show the plot
    plt.show()