import random
import uuid
from PIL import Image, ImageDraw
import math
import os
from reportlab.pdfgen import canvas as pdf_canvas

def create_background_canvas(width=128, height=128, background_color='white'):
    canvas = Image.new('CMYK', (width, height), background_color)
    return canvas

def rule1(canvas):
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(5)]
    first_color, *colors = colors

    amount_of_first_color = round((canvas.size[0] * canvas.size[1]) / random.randint(5, 8) * random.randint(1, 2))
    first_positions = set()
    while len(first_positions) < amount_of_first_color:
        x, y = random.randint(0, canvas.size[0] - 1), random.randint(0, canvas.size[1] - 1)
        first_positions.add((x, y))
        canvas.putpixel((x, y), first_color)

    list_of_first_positions = list(first_positions)

    subrules = ["LEFT", "RIGHT", "ABOVE", "BELOW"]
    random_subrule = random.choice(subrules)

    if random_subrule == 'ABOVE':
        list_of_above_first_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            if y > 0:
                above_pos = (x, y - 1)
                if above_pos[1] >= 0 and above_pos not in list_of_first_positions:
                    list_of_above_first_positions.append(above_pos)

                    random_distance = random.randint(1, 2)

                    for i in range(1, random_distance + 1):
                        left_pos = (x - i, y - 1)
                        right_pos = (x + i, y - 1)
                        if (left_pos[0] >= 0 and left_pos[0] < canvas.size[0] and
                                left_pos[1] >= 0 and left_pos[1] < canvas.size[1] and
                                left_pos not in list_of_first_positions):
                            list_of_above_first_positions.append(left_pos)
                        if (right_pos[0] >= 0 and right_pos[0] < canvas.size[0] and
                                right_pos[1] >= 0 and right_pos[1] < canvas.size[1] and
                                right_pos not in list_of_first_positions):
                            list_of_above_first_positions.append(right_pos)

        for i in list_of_above_first_positions:
            canvas.putpixel(i, colors[1])

    if random_subrule == 'BELOW':
        list_of_below_first_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            if y < canvas.size[1] - 1:
                below_pos = (x, y + 1)
                if below_pos[1] < canvas.size[1] and below_pos not in list_of_first_positions:
                    list_of_below_first_positions.append(below_pos)

                    random_distance = random.randint(1, 2)

                    for i in range(1, random_distance + 1):
                        left_pos = (x - i, y + 1)
                        right_pos = (x + i, y + 1)
                        if (left_pos[0] >= 0 and left_pos[0] < canvas.size[0] and
                                left_pos[1] >= 0 and left_pos[1] < canvas.size[1] and
                                left_pos not in list_of_first_positions):
                            list_of_below_first_positions.append(left_pos)
                        if (right_pos[0] >= 0 and right_pos[0] < canvas.size[0] and
                                right_pos[1] >= 0 and right_pos[1] < canvas.size[1] and
                                right_pos not in list_of_first_positions):
                            list_of_below_first_positions.append(right_pos)

        for i in list_of_below_first_positions:
            canvas.putpixel(i, colors[1])

    if random_subrule == 'RIGHT':
        list_of_right_first_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            if x < canvas.size[0] - 1:
                right_pos = (x + 1, y)
                if right_pos[0] < canvas.size[0] and right_pos not in list_of_first_positions:
                    list_of_right_first_positions.append(right_pos)

                    random_distance = random.randint(1, 2)

                    for i in range(1, random_distance + 1):
                        above_pos = (x + 1, y - i)
                        below_pos = (x + 1, y + i)
                        if (above_pos[0] < canvas.size[0] and above_pos[0] >= 0 and
                                above_pos[1] < canvas.size[1] and above_pos[1] >= 0 and
                                above_pos not in list_of_first_positions):
                            list_of_right_first_positions.append(above_pos)
                        if (below_pos[0] < canvas.size[0] and below_pos[0] >= 0 and
                                below_pos[1] < canvas.size[1] and below_pos[1] >= 0 and
                                below_pos not in list_of_first_positions):
                            list_of_right_first_positions.append(below_pos)

        for i in list_of_right_first_positions:
            canvas.putpixel(i, colors[1])

    if random_subrule == 'LEFT':
        list_of_left_first_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            if x > 0:
                left_pos = (x - 1, y)
                if left_pos[0] >= 0 and left_pos not in list_of_first_positions:
                    list_of_left_first_positions.append(left_pos)

                    random_distance = random.randint(1, 2)

                    for i in range(1, random_distance + 1):
                        above_pos = (x - 1, y - i)
                        below_pos = (x - 1, y + i)
                        if (above_pos[0] >= 0 and above_pos[0] < canvas.size[0] and
                                above_pos[1] >= 0 and above_pos[1] < canvas.size[1] and
                                above_pos not in list_of_first_positions):
                            list_of_left_first_positions.append(above_pos)
                        if (below_pos[0] >= 0 and below_pos[0] < canvas.size[0] and
                                below_pos[1] >= 0 and below_pos[1] < canvas.size[1] and
                                below_pos not in list_of_first_positions):
                            list_of_left_first_positions.append(below_pos)

        for i in list_of_left_first_positions:
            canvas.putpixel(i, colors[1])

    amount_of_third_color = round((canvas.size[0] * canvas.size[1]) / random.randint(4, 6) * random.randint(1, 2))
    third_positions = set()
    max_iterations = canvas.size[0] * canvas.size[1]  # Maximum number of iterations
    iteration_count = 0

    while len(third_positions) < amount_of_third_color and iteration_count < max_iterations:
        x, y = random.randint(0, canvas.size[0] - 1), random.randint(0, canvas.size[1] - 1)
        if canvas.getpixel((x, y)) == (255, 255, 255, 255):
            third_positions.add((x, y))
            canvas.putpixel((x, y), colors[2])
        iteration_count += 1

    try:
        for x in range(canvas.size[0]):
            for y in range(canvas.size[1]):
                if canvas.getpixel((x, y)) == (255, 255, 255, 255):
                    canvas.putpixel((x, y), colors[3])
    except KeyboardInterrupt:
        print("Program interrupted by the user.")

def rule2(canvas):
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(5)]
    first_color, *colors = colors

    amount_of_first_color = round((canvas.size[0] * canvas.size[1]) / random.randint(4, 7) * random.randint(1, 3))
    first_positions = set()
    while len(first_positions) < amount_of_first_color:
        x, y = random.randint(0, canvas.size[0] - 1), random.randint(0, canvas.size[1] - 1)
        first_positions.add((x, y))
        canvas.putpixel((x, y), first_color)

    list_of_first_positions = list(first_positions)

    subrules = ["DIAGONAL_UP_RIGHT", "DIAGONAL_UP_LEFT", "DIAGONAL_DOWN_RIGHT", "DIAGONAL_DOWN_LEFT"]
    random_subrule = random.choice(subrules)

    if random_subrule == 'DIAGONAL_UP_RIGHT':
        list_of_diagonal_up_right_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            if x < canvas.size[0] - 1 and y > 0:
                diagonal_pos = (x + 1, y - 1)
                if diagonal_pos[0] < canvas.size[0] and diagonal_pos[1] >= 0 and diagonal_pos not in list_of_first_positions:
                    list_of_diagonal_up_right_positions.append(diagonal_pos)

        for i in list_of_diagonal_up_right_positions:
            canvas.putpixel(i, colors[0])

    if random_subrule == 'DIAGONAL_UP_LEFT':
        list_of_diagonal_up_left_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            if x > 0 and y > 0:
                diagonal_pos = (x - 1, y - 1)
                if diagonal_pos[0] >= 0 and diagonal_pos[1] >= 0 and diagonal_pos not in list_of_first_positions:
                    list_of_diagonal_up_left_positions.append(diagonal_pos)

        for i in list_of_diagonal_up_left_positions:
            canvas.putpixel(i, colors[0])

    if random_subrule == 'DIAGONAL_DOWN_LEFT':
        list_of_diagonal_down_left_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            if x > 0 and y < canvas.size[1] - 1:
                diagonal_pos = (x - 1, y + 1)
                if diagonal_pos[0] >= 0 and diagonal_pos[1] < canvas.size[1] and diagonal_pos not in list_of_first_positions:
                    list_of_diagonal_down_left_positions.append(diagonal_pos)

        for i in list_of_diagonal_down_left_positions:
            canvas.putpixel(i, colors[0])

    if random_subrule == 'DIAGONAL_DOWN_RIGHT':
        list_of_diagonal_down_right_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            if x < canvas.size[0] - 1 and y < canvas.size[1] - 1:
                diagonal_pos = (x + 1, y + 1)
                if diagonal_pos[0] < canvas.size[0] and diagonal_pos[1] < canvas.size[1] and diagonal_pos not in list_of_first_positions:
                    list_of_diagonal_down_right_positions.append(diagonal_pos)

        for i in list_of_diagonal_down_right_positions:
            canvas.putpixel(i, colors[0])

    for x in range(canvas.size[0]):
        for y in range(canvas.size[1]):
            if canvas.getpixel((x, y)) == (255, 255, 255, 255):
                canvas.putpixel((x, y), colors[1])

    noise_positions = set()
    max_noise_iterations = round((canvas.size[0] * canvas.size[1]) / random.randint(10, 20))
    while len(noise_positions) < max_noise_iterations:
        x, y = random.randint(0, canvas.size[0] - 1), random.randint(0, canvas.size[1] - 1)
        if (x, y) not in noise_positions:
            noise_positions.add((x, y))
            canvas.putpixel((x, y), colors[2])

    border_color = colors[3]
    for x in range(canvas.size[0]):
        canvas.putpixel((x, 0), border_color)
        canvas.putpixel((x, canvas.size[1] - 1), border_color)
    for y in range(canvas.size[1]):
        canvas.putpixel((0, y), border_color)
        canvas.putpixel((canvas.size[0] - 1, y), border_color)

def rule3(canvas):
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(5)]
    first_color, *colors = colors

    amount_of_first_color = round((canvas.size[0] * canvas.size[1]) / random.randint(5, 8) * random.randint(1, 2))
    first_positions = set()
    while len(first_positions) < amount_of_first_color:
        x, y = random.randint(0, canvas.size[0] - 1), random.randint(0, canvas.size[1] - 1)
        first_positions.add((x, y))
        canvas.putpixel((x, y), first_color)

    list_of_first_positions = list(first_positions)

    subrules = ["DIAGONAL_UP_LEFT", "DIAGONAL_UP_RIGHT", "DIAGONAL_DOWN_LEFT", "DIAGONAL_DOWN_RIGHT"]
    random_subrule = random.choice(subrules)

    if random_subrule == 'DIAGONAL_UP_LEFT':
        list_of_diagonal_up_left_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            if x > 0 and y > 0:
                diagonal_up_left_pos = (x - 1, y - 1)
                if diagonal_up_left_pos[0] >= 0 and diagonal_up_left_pos[1] >= 0 and diagonal_up_left_pos not in list_of_first_positions:
                    list_of_diagonal_up_left_positions.append(diagonal_up_left_pos)

                    random_distance = random.randint(1, 2)

                    for i in range(1, random_distance + 1):
                        up_left_pos = (x - i, y - i)
                        if (up_left_pos[0] >= 0 and up_left_pos[0] < canvas.size[0] and
                                up_left_pos[1] >= 0 and up_left_pos[1] < canvas.size[1] and
                                up_left_pos not in list_of_first_positions):
                            list_of_diagonal_up_left_positions.append(up_left_pos)

        for i in list_of_diagonal_up_left_positions:
            canvas.putpixel(i, colors[1])

    if random_subrule == 'DIAGONAL_UP_RIGHT':
        list_of_diagonal_up_right_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            if x < canvas.size[0] - 1 and y > 0:
                diagonal_up_right_pos = (x + 1, y - 1)
                if diagonal_up_right_pos[0] < canvas.size[0] and diagonal_up_right_pos[1] >= 0 and diagonal_up_right_pos not in list_of_first_positions:
                    list_of_diagonal_up_right_positions.append(diagonal_up_right_pos)

                    random_distance = random.randint(1, 2)

                    for i in range(1, random_distance + 1):
                        up_right_pos = (x + i, y - i)
                        if (up_right_pos[0] < canvas.size[0] and up_right_pos[0] >= 0 and
                                up_right_pos[1] >= 0 and up_right_pos[1] < canvas.size[1] and
                                up_right_pos not in list_of_first_positions):
                            list_of_diagonal_up_right_positions.append(up_right_pos)

        for i in list_of_diagonal_up_right_positions:
            canvas.putpixel(i, colors[1])

    if random_subrule == 'DIAGONAL_DOWN_LEFT':
        list_of_diagonal_down_left_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            if x > 0 and y < canvas.size[1] - 1:
                diagonal_down_left_pos = (x - 1, y + 1)
                if diagonal_down_left_pos[0] >= 0 and diagonal_down_left_pos[1] < canvas.size[1] and diagonal_down_left_pos not in list_of_first_positions:
                    list_of_diagonal_down_left_positions.append(diagonal_down_left_pos)

                    random_distance = random.randint(1, 2)

                    for i in range(1, random_distance + 1):
                        down_left_pos = (x - i, y + i)
                        if (down_left_pos[0] >= 0 and down_left_pos[0] < canvas.size[0] and
                                down_left_pos[1] >= 0 and down_left_pos[1] < canvas.size[1] and
                                down_left_pos not in list_of_first_positions):
                            list_of_diagonal_down_left_positions.append(down_left_pos)

        for i in list_of_diagonal_down_left_positions:
            canvas.putpixel(i, colors[1])

    if random_subrule == 'DIAGONAL_DOWN_RIGHT':
        list_of_diagonal_down_right_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            if x < canvas.size[0] - 1 and y < canvas.size[1] - 1:
                diagonal_down_right_pos = (x + 1, y + 1)
                if diagonal_down_right_pos[0] < canvas.size[0] and diagonal_down_right_pos[1] < canvas.size[1] and diagonal_down_right_pos not in list_of_first_positions:
                    list_of_diagonal_down_right_positions.append(diagonal_down_right_pos)

                    random_distance = random.randint(1, 2)

                    for i in range(1, random_distance + 1):
                        down_right_pos = (x + i, y + i)
                        if (down_right_pos[0] < canvas.size[0] and down_right_pos[0] >= 0 and
                                down_right_pos[1] < canvas.size[1] and down_right_pos[1] >= 0 and
                                down_right_pos not in list_of_first_positions):
                            list_of_diagonal_down_right_positions.append(down_right_pos)

        for i in list_of_diagonal_down_right_positions:
            canvas.putpixel(i, colors[1])

    amount_of_third_color = round((canvas.size[0] * canvas.size[1]) / random.randint(4, 6) * random.randint(1, 2))
    third_positions = set()
    max_iterations = canvas.size[0] * canvas.size[1]  # Maximum number of iterations
    iteration_count = 0

    while len(third_positions) < amount_of_third_color and iteration_count < max_iterations:
        x, y = random.randint(0, canvas.size[0] - 1), random.randint(0, canvas.size[1] - 1)
        if canvas.getpixel((x, y)) == (255, 255, 255, 255):
            third_positions.add((x, y))
            canvas.putpixel((x, y), colors[2])
        iteration_count += 1

    try:
        for x in range(canvas.size[0]):
            for y in range(canvas.size[1]):
                if canvas.getpixel((x, y)) == (255, 255, 255, 255):
                    canvas.putpixel((x, y), colors[3])
    except KeyboardInterrupt:
        print("Program interrupted by the user.")

def rule4(canvas):
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(5)]
    first_color, *colors = colors

    amount_of_first_color = round((canvas.size[0] * canvas.size[1]) / random.randint(3, 5) * random.randint(1, 2))
    first_positions = set()
    while len(first_positions) < amount_of_first_color:
        x, y = random.randint(0, canvas.size[0] - 1), random.randint(0, canvas.size[1] - 1)
        first_positions.add((x, y))
        canvas.putpixel((x, y), first_color)

    list_of_first_positions = list(first_positions)

    subrules = ["EXPLOSION", "SPIRAL", "RIPPLE", "GALAXY"]
    random_subrule = random.choice(subrules)

    if random_subrule == 'EXPLOSION':
        list_of_explosion_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            for i in range(1, random.randint(2, 5)):
                explosion_pos = (x + random.randint(-i, i), y + random.randint(-i, i))
                if (explosion_pos[0] >= 0 and explosion_pos[0] < canvas.size[0] and
                        explosion_pos[1] >= 0 and explosion_pos[1] < canvas.size[1] and
                        explosion_pos not in list_of_first_positions):
                    list_of_explosion_positions.append(explosion_pos)

        for i in list_of_explosion_positions:
            canvas.putpixel((int(i[0]), int(i[1])), colors[1])

    if random_subrule == 'SPIRAL':
        list_of_spiral_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            for i in range(1, random.randint(2, 5)):
                spiral_pos = (x + i * math.cos(i * math.pi / 4), y + i * math.sin(i * math.pi / 4))
                if (spiral_pos[0] >= 0 and spiral_pos[0] < canvas.size[0] and
                        spiral_pos[1] >= 0 and spiral_pos[1] < canvas.size[1] and
                        spiral_pos not in list_of_first_positions):
                    list_of_spiral_positions.append(spiral_pos)

        for i in list_of_spiral_positions:
            canvas.putpixel((int(i[0]), int(i[1])), colors[1])

    if random_subrule == 'RIPPLE':
        list_of_ripple_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            for i in range(1, random.randint(2, 5)):
                ripple_pos = (x + i * math.cos(i * math.pi / 2), y + i * math.sin(i * math.pi / 2))
                if (ripple_pos[0] >= 0 and ripple_pos[0] < canvas.size[0] and
                        ripple_pos[1] >= 0 and ripple_pos[1] < canvas.size[1] and
                        ripple_pos not in list_of_first_positions):
                    list_of_ripple_positions.append(ripple_pos)

        for i in list_of_ripple_positions:
            canvas.putpixel((int(i[0]), int(i[1])), colors[1])

    if random_subrule == 'GALAXY':
        list_of_galaxy_positions = list()
        for pos in list_of_first_positions:
            x, y = pos
            for i in range(1, random.randint(2, 5)):
                galaxy_pos = (x + i * math.cos(i * math.pi / 3), y + i * math.sin(i * math.pi / 3))
                if (galaxy_pos[0] >= 0 and galaxy_pos[0] < canvas.size[0] and
                        galaxy_pos[1] >= 0 and galaxy_pos[1] < canvas.size[1] and
                        galaxy_pos not in list_of_first_positions):
                    list_of_galaxy_positions.append(galaxy_pos)

        for i in list_of_galaxy_positions:
            canvas.putpixel((int(i[0]), int(i[1])), colors[1])

    amount_of_third_color = round((canvas.size[0] * canvas.size[1]) / random.randint(4, 6) * random.randint(1, 2))
    third_positions = set()
    max_iterations = canvas.size[0] * canvas.size[1]  # Maximum number of iterations
    iteration_count = 0

    while len(third_positions) < amount_of_third_color and iteration_count < max_iterations:
        x, y = random.randint(0, canvas.size[0] - 1), random.randint(0, canvas.size[1] - 1)
        if canvas.getpixel((x, y)) == (255, 255, 255, 255):
            third_positions.add((x, y))
            canvas.putpixel((x, y), colors[2])
        iteration_count += 1

    try:
        for x in range(canvas.size[0]):
            for y in range(canvas.size[1]):
                if canvas.getpixel((x, y)) == (255, 255, 255, 255):
                    canvas.putpixel((x, y), colors[3])
    except KeyboardInterrupt:
        print("Program interrupted by the user.")

def rule5(canvas):
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(7)]

    primary_color = colors[0]
    secondary_color = colors[1]

    num_seed_pixels = round((canvas.size[0] * canvas.size[1]) / random.randint(10, 20))

    seed_pixels = set()
    while len(seed_pixels) < num_seed_pixels:
        x = random.randint(0, canvas.size[0] - 1)
        y = random.randint(0, canvas.size[1] - 1)
        seed_pixels.add((x, y))
        canvas.putpixel((x, y), primary_color)

    num_iterations = random.randint(3, 6)
    for _ in range(num_iterations):
        new_pixels = set()
        for x in range(canvas.size[0]):
            for y in range(canvas.size[1]):
                if (x, y) not in seed_pixels:
                    neighbor_count = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if (x + dx, y + dy) in seed_pixels:
                                neighbor_count += 1
                    if neighbor_count >= 2:
                        new_pixels.add((x, y))
                        canvas.putpixel((x, y), secondary_color)
        seed_pixels.update(new_pixels)

    for x in range(canvas.size[0]):
        for y in range(canvas.size[1]):
            if (x, y) in seed_pixels:
                neighbor_count_primary = 0
                neighbor_count_secondary = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if (x + dx, y + dy) in seed_pixels:
                            if canvas.getpixel((x + dx, y + dy)) == primary_color:
                                neighbor_count_primary += 1
                            elif canvas.getpixel((x + dx, y + dy)) == secondary_color:
                                neighbor_count_secondary += 1
                if neighbor_count_primary >= 2 and neighbor_count_secondary >= 2:
                    canvas.putpixel((x, y), random.choice(colors[2:]))

    for x in range(canvas.size[0]):
        for y in range(canvas.size[1]):
            if canvas.getpixel((x, y)) == (255, 255, 255, 255):
                canvas.putpixel((x, y), random.choice(colors))

def rule6(canvas):
    colors = [(random.randint(0, 1) * 255, random.randint(0, 1) * 255, random.randint(0, 1) * 255, random.randint(0, 1) * 255) for _ in range(5)]
    first_color, *colors = colors

    amount_of_first_color = round((canvas.size[0] * canvas.size[1]) / random.randint(5, 8) * random.randint(1, 2))
    first_positions = set()
    while len(first_positions) < amount_of_first_color:
        x, y = random.randint(0, canvas.size[0] - 1), random.randint(0, canvas.size[1] - 1)
        first_positions.add((x, y))
        canvas.putpixel((x, y), first_color)

    list_of_first_positions = list(first_positions)

    submodes = ["DIAGONAL_UP_RIGHT", "DIAGONAL_UP_LEFT", "DIAGONAL_DOWN_RIGHT", "DIAGONAL_DOWN_LEFT", "CROSS", "SQUARE"]
    random_submode = random.choice(submodes)

    if random_submode == "DIAGONAL_UP_RIGHT":
        list_of_diagonal_up_right_positions = []
        for pos in list_of_first_positions:
            x, y = pos
            if x < canvas.size[0] - 1 and y > 0:
                diagonal_pos = (x + 1, y - 1)
                if diagonal_pos not in list_of_first_positions:
                    list_of_diagonal_up_right_positions.append(diagonal_pos)
        for pos in list_of_diagonal_up_right_positions:
            canvas.putpixel(pos, colors[1])

    elif random_submode == "DIAGONAL_UP_LEFT":
        list_of_diagonal_up_left_positions = []
        for pos in list_of_first_positions:
            x, y = pos
            if x > 0 and y > 0:
                diagonal_pos = (x - 1, y - 1)
                if diagonal_pos not in list_of_first_positions:
                    list_of_diagonal_up_left_positions.append(diagonal_pos)
        for pos in list_of_diagonal_up_left_positions:
            canvas.putpixel(pos, colors[1])

    elif random_submode == "DIAGONAL_DOWN_RIGHT":
        list_of_diagonal_down_right_positions = []
        for pos in list_of_first_positions:
            x, y = pos
            if x < canvas.size[0] - 1 and y < canvas.size[1] - 1:
                diagonal_pos = (x + 1, y + 1)
                if diagonal_pos not in list_of_first_positions:
                    list_of_diagonal_down_right_positions.append(diagonal_pos)
        for pos in list_of_diagonal_down_right_positions:
            canvas.putpixel(pos, colors[1])

    elif random_submode == "DIAGONAL_DOWN_LEFT":
        list_of_diagonal_down_left_positions = []
        for pos in list_of_first_positions:
            x, y = pos
            if x > 0 and y < canvas.size[1] - 1:
                diagonal_pos = (x - 1, y + 1)
                if diagonal_pos not in list_of_first_positions:
                    list_of_diagonal_down_left_positions.append(diagonal_pos)
        for pos in list_of_diagonal_down_left_positions:
            canvas.putpixel(pos, colors[1])

    elif random_submode == "CROSS":
        list_of_cross_positions = []
        for pos in list_of_first_positions:
            x, y = pos
            cross_positions = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
            for cross_pos in cross_positions:
                if (
                    0 <= cross_pos[0] < canvas.size[0]
                    and 0 <= cross_pos[1] < canvas.size[1]
                    and cross_pos not in list_of_first_positions
                ):
                    list_of_cross_positions.append(cross_pos)
        for pos in list_of_cross_positions:
            canvas.putpixel(pos, colors[1])

    elif random_submode == "SQUARE":
        list_of_square_positions = []
        for pos in list_of_first_positions:
            x, y = pos
            square_positions = [
                (x - 1, y - 1),
                (x, y - 1),
                (x + 1, y - 1),
                (x - 1, y),
                (x + 1, y),
                (x - 1, y + 1),
                (x, y + 1),
                (x + 1, y + 1),
            ]
            for square_pos in square_positions:
                if (
                    0 <= square_pos[0] < canvas.size[0]
                    and 0 <= square_pos[1] < canvas.size[1]
                    and square_pos not in list_of_first_positions
                ):
                    list_of_square_positions.append(square_pos)
        for pos in list_of_square_positions:
            canvas.putpixel(pos, colors[1])

    amount_of_third_color = round((canvas.size[0] * canvas.size[1]) / random.randint(4, 6) * random.randint(1, 2))
    third_positions = set()
    max_iterations = canvas.size[0] * canvas.size[1]  # Maximum number of iterations
    iteration_count = 0

    while len(third_positions) < amount_of_third_color and iteration_count < max_iterations:
        x, y = random.randint(0, canvas.size[0] - 1), random.randint(0, canvas.size[1] - 1)
        if canvas.getpixel((x, y)) == (255, 255, 255, 255):
            third_positions.add((x, y))
            canvas.putpixel((x, y), colors[2])
        iteration_count += 1

    for x in range(canvas.size[0]):
        for y in range(canvas.size[1]):
            if canvas.getpixel((x, y)) == (255, 255, 255, 255):
                canvas.putpixel((x, y), colors[3])

def rule7(canvas):
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(4)]

    first_positions = set()
    amount_of_first_color = round((canvas.size[0] * canvas.size[1]) / random.randint(5, 8) * random.randint(1, 2))
    for _ in range(amount_of_first_color):
        x, y = random.randint(0, canvas.size[0] - 1), random.randint(0, canvas.size[1] - 1)
        first_positions.add((x, y))
        canvas.putpixel((x, y), colors[0])

    above_first_positions = []
    for pos in first_positions:
        x, y = pos
        if y > 0:
            above_pos = (x, y - 1)
            if above_pos[1] >= 0 and above_pos not in first_positions:
                above_first_positions.append(above_pos)

    below_first_positions = []
    for pos in first_positions:
        x, y = pos
        if y < canvas.size[1] - 1:
            below_pos = (x, y + 1)
            if below_pos[1] < canvas.size[1] and below_pos not in first_positions:
                below_first_positions.append(below_pos)

    right_first_positions = []
    for pos in first_positions:
        x, y = pos
        if x < canvas.size[0] - 1:
            right_pos = (x + 1, y)
            if right_pos[0] < canvas.size[0] and right_pos not in first_positions:
                right_first_positions.append(right_pos)

    left_first_positions = []
    for pos in first_positions:
        x, y = pos
        if x > 0:
            left_pos = (x - 1, y)
            if left_pos[0] >= 0 and left_pos not in first_positions:
                left_first_positions.append(left_pos)

    for pos in above_first_positions:
        canvas.putpixel(pos, colors[1])
    for pos in below_first_positions:
        canvas.putpixel(pos, colors[1])
    for pos in right_first_positions:
        canvas.putpixel(pos, colors[1])
    for pos in left_first_positions:
        canvas.putpixel(pos, colors[1])

    third_positions = set()
    amount_of_third_color = round((canvas.size[0] * canvas.size[1]) / random.randint(4, 6) * random.randint(1, 2))
    for _ in range(amount_of_third_color):
        x, y = random.randint(0, canvas.size[0] - 1), random.randint(0, canvas.size[1] - 1)
        if canvas.getpixel((x, y)) == (255, 255, 255, 255):
            third_positions.add((x, y))
            canvas.putpixel((x, y), colors[2])

    fourth_positions = set()
    for x in range(canvas.size[0]):
        for y in range(canvas.size[1]):
            if canvas.getpixel((x, y)) == (255, 255, 255, 255):
                fourth_positions.add((x, y))
                canvas.putpixel((x, y), colors[3])

    return canvas

# This part of code for getting all the images pixels pixel by pixel and their positions
# def generate_pixel_matrix(canvas):
#     width, height = canvas.size
#     pixel_matrix = []
#     for y in range(height):
#         row = []
#         for x in range(width):
#             color = canvas.getpixel((x, y))
#             row.append(((x, y), color))
#         pixel_matrix.append(row)
#     return pixel_matrix

# pixel_matrix = generate_pixel_matrix(some_canvas)

# Single generation
# resize is using because it's faster and easier to generate an image
# of smaller size and then upscale it and sometime less is more

# c_width, c_height = 124, 68
# some_canvas = create_background_canvas(c_width, c_height, 'white')
# rule3(some_canvas)
# scale_factor = round(1980 / c_width)  # Adjust the scale factor as needed for FULL HD size
# resized_image = some_canvas.resize((some_canvas.width * scale_factor, some_canvas.height * scale_factor), resample=Image.NEAREST)

# # Save the resized image
# resized_image.show()

# Set the output directory
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def generate_images(amount, width, height, rule_index):
    for i in range(amount):
        canvas = create_background_canvas(width, height, 'white')
        rules[rule_index](canvas)
        scale_factor = round(1980 / width)
        canvas = canvas.resize((canvas.width * scale_factor, canvas.height * scale_factor), resample=Image.NEAREST)
        
        unique_id = uuid.uuid4()
        filename_pdf = f"{unique_id}_{width}x{height}_{rule_index+1}.pdf"
        output_path_pdf = os.path.join(output_dir, filename_pdf)

        # Convert to PDF and save
        pdf = pdf_canvas.Canvas(output_path_pdf, pagesize=(canvas.width, canvas.height))
        temp_img_path = f"{unique_id}_{width}x{height}_{rule_index+1}_temp.png"
        canvas.convert("RGB").save(temp_img_path, "PNG")
        pdf.drawImage(temp_img_path, 0, 0, width=canvas.width, height=canvas.height)
        pdf.save()
        os.remove(temp_img_path)  # Remove the temporary PNG file
        print(f"Image '{filename_pdf}' saved successfully as PDF.")

# Generate any amount of images with different rules and sizes
# rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7]
# width_height = [(31, 17), (62, 34), (93, 51), (124, 68)]


rules = [rule1]
width_height = [(42, 60)]

for i in range(10):
    rule = random.choice(rules)
    size = random.choice(width_height)
    width = size[0]
    height = size[1]
    canvas = create_background_canvas(width, height, 'white')
    rule(canvas)
    scale_factor = round(3960 / width)
    canvas = canvas.resize((canvas.width * scale_factor, canvas.height * scale_factor), resample=Image.NEAREST)
    rule_index = rules.index(rule)
    generate_images(1, width, height, rule_index)
