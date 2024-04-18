import matplotlib.pyplot as plt
from math import pi, sin, cos

class BORDERBOOM:
    def __init__(self, x_border, y_border, mass, v0, angle, gravity, dt, cd):
        self.x_border = x_border
        self.y_border = y_border
        self.mass = mass
        self.v0 = v0
        self.v_x = v0 * cos(angle * pi / 180)
        self.v_y = v0 * sin(angle * pi / 180)
        self.a_x = 0
        self.a_y = -1 * gravity
        self.angle = angle * pi / 180
        self.gravity = gravity
        self.dt = dt
        self.cd = cd

        self.pos_x = 0
        self.pos_y = 0

    def nextState(self):
        nv_x = self.v_x + (self.a_x * self.dt)
        nv_y = self.v_y + (self.a_y * self.dt)

        if self.v_x != 0 and self.v_y !=0:
            air_resistance_x = -0.5 * self.mass * nv_x**2 * self.cd * (nv_x**2 + nv_y**2) / (nv_x**2 + nv_y**2) * self.dt
            air_resistance_y = -0.5 * self.mass * nv_y**2 * self.cd * (nv_x**2 + nv_y**2) / (nv_x**2 + nv_y**2) * self.dt

        self.v_x = nv_x + air_resistance_x
        self.v_y = nv_y + air_resistance_y

        if abs(nv_x - self.v_x) < 0.1 and self.pos_x <= 0:
            self.v_x = 0

        if self.pos_x > self.x_border:
            self.pos_x = self.x_border
            self.v_x *= -0.7

        if self.pos_x < 0:
            self.pos_x = 0
            self.v_x *= -0.7

        if abs(nv_y - self.v_y) < 0.1 and self.pos_y <= 0:
            self.v_y = 0

        if self.pos_x > self.y_border:
            self.pos_x = self.y_border
            self.v_x *= -0.7

        if self.pos_y < 0 :
            self.pos_y = 0
            self.v_y *= -0.7

        self.pos_x += self.v_x * self.dt
        self.pos_y += self.v_y * self.dt

        return (self.pos_x, self.pos_y)
    
    def nowState(self):
        return (self.pos_x, self.pos_y)
    
if (__name__ == '__main__'):
    #borderboom1 = BORDERBOOM(250.0, 250.0, 1.0, 100.0, 60.0, 9.8, 0.1, 0.01)
    borderboom1 = BORDERBOOM(500.0, 500.0, 1.0, 100.0, 60.0, 9.8, 0.1, 0.01)
    x_log = [0]
    y_log = [0]
    time = 0
    while borderboom1.v_x != 0 and borderboom1.v_y != 0:
        borderboom1.nowState()
        print(f"boom1's now state x: {borderboom1.pos_x:.2f}, y: {borderboom1.pos_y:.2f} at {time:.1f}s, vx: {borderboom1.v_x:.2f}, vy: {borderboom1.v_y:.2f}")
        borderboom1.nextState()
        print(f"boom1's next state x: {borderboom1.pos_x:.2f}, y: {borderboom1.pos_y:.2f} at {time:.1f}s")
        print(f"{borderboom1.dt:.1f} later...\n")

        x_log.append(borderboom1.pos_x)
        y_log.append(borderboom1.pos_y)

        time += borderboom1.dt

    # Plot the trajectory
    plt.xlim(-1, borderboom1.x_border)
    plt.ylim(0, borderboom1.y_border)
    plt.plot(x_log, y_log)

    # Set labels and title
    plt.xlabel('X-Position (m)')
    plt.ylabel('Y-Position (m)')
    plt.title('Projectile Trajectory')

    # Add grid
    plt.grid(True)

    # Show the plot
    plt.show()