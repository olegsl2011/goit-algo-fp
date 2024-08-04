import matplotlib.pyplot as plt
import numpy as np

trunk_level = None


def draw_branch(x, y, length, angle, level, angle_between_branches, length_randomness, angle_randomness):
    if level == 0:
        return

    length *= 1.0 - length_randomness + 2.0 * length_randomness * np.random.rand()

    if level != trunk_level:
        angle += np.random.uniform(-angle * angle_randomness, angle * angle_randomness)

    x_end = x + length * np.cos(np.radians(angle))
    y_end = y + length * np.sin(np.radians(angle))

    plt.plot([x, x_end], [y, y_end], color='brown', lw=1)

    new_length = length * 0.7
    draw_branch(x_end, y_end, new_length, angle + angle_between_branches, level - 1, angle_between_branches,
                length_randomness, angle_randomness)
    draw_branch(x_end, y_end, new_length, angle - angle_between_branches, level - 1, angle_between_branches,
                length_randomness, angle_randomness)


def draw_pythagorean_tree(level, angle_between_branches, length_randomness, angle_randomness):
    plt.figure(figsize=(8, 8))
    plt.axis('equal')
    plt.axis('off')

    trunk_length = 1.0
    trunk_angle = 90.0

    draw_branch(0, 0, trunk_length, trunk_angle, level, angle_between_branches, length_randomness, angle_randomness)

    plt.show()


if __name__ == "__main__":
    recursion_level = int(input("Enter the level of recursion: "))
    trunk_level = recursion_level
    angle_between_branches = float(input("Enter the angle between branches in degrees: "))
    length_randomness = float(input("Enter the branch length randomness coefficient (between 0 and 1): "))
    angle_randomness = float(input("Enter the angle randomness coefficient (between 0 and 1): "))

    draw_pythagorean_tree(recursion_level, angle_between_branches, length_randomness, angle_randomness)
