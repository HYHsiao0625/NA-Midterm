import matplotlib.pyplot as plt
from math import pi, sin, cos


class Boom:
    def __init__(self, mass, v0, angle, gravity, dt):
        self.mass = mass
        self.v0 = v0
        self.v_x = v0 * cos(angle * pi / 180)
        self.v_y = v0 * sin(angle * pi / 180)
        self.a_x = 0.0
        self.a_y = -1 * gravity
        self.angle = angle * pi / 180
        self.gravity = gravity
        self.dt = dt
        self.pos_x = 0
        self.pos_y = 0

    def nextState(self):
        self.pos_x += self.v_x * self.dt
        self.pos_y += self.v_y * self.dt

        nv_x = self.v_x + (self.a_x * self.dt)
        nv_y = self.v_y + (self.a_y * self.dt)  

        self.v_x = nv_x
        self.v_y = nv_y
        return (self.pos_x, self.pos_y)

    def nowState(self):
        return (self.pos_x, self.pos_y)


if __name__ == "__main__":
    boom1 = Boom(1.0, 100.0, 30.0, 9.8, 0.1)
    x_log = [0]
    y_log = [0]
    time = 0

    while boom1.pos_x >= 0 and boom1.pos_y >= 0:
        boom1.nowState()
        print(f"boom1's now state x: {boom1.pos_x:.2f}, y: {boom1.pos_y:.2f} at {time:.1f}s")
        boom1.nextState()
        print(f"boom1's next state x: {boom1.pos_x:.2f}, y: {boom1.pos_y:.2f} at {time:.1f}s")
        print(f"{boom1.dt:.1f} later...\n")

        x_log.append(boom1.pos_x)
        y_log.append(boom1.pos_y)

        time += boom1.dt

# Plot the trajectory
plt.xlim(0, 1000)
plt.ylim(0, 1000)
plt.plot(x_log, y_log)

# Set labels and title
plt.xlabel('X-Position (m)')
plt.ylabel('Y-Position (m)')
plt.title('Projectile Trajectory')

# Add grid
plt.grid(True)

# Show the plot
plt.show()
