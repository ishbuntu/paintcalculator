# prints the list of paints as a menu and ensure valid inoput

def select(prompt, values):
    if len(values) == 0: return
    while True:
        for i, v in enumerate(values):
            print(f'{i + 1}. {v}')
        s = int(input(prompt))
        if s < 1 or s > len(values):
            print(f'Invalid selection. Choose between 1 and {len(values)}')
        else:
            return (s - 1)


def calc_area(wall):
    return wall['length'] * wall['height'] - sum(a[0] * a[1] for a in wall['exclude'])


def get_walls():
    num_walls = int(input('How many walls would you like to paint? '))
    walls = []  # stores wall data

    for index in range(num_walls):
        wall = {}
        print(f'Enter Details of Wall No. {str(index + 1)}')

        wall['length'] = float(input('What is the length of your wall in metres?: '))
        wall['height'] = float(input('What is the height of your wall in metres?: '))

        color = select('Choose the number corresponding to the color you would like to paint the wall: ', paints)
        wall['color'] = list(paints.keys())[color]

        num_excl = int(input('Enter number of doors, windows, and sockets: '))
        exclude = []
        for i in range(num_excl):
            print(f'Exclude item No. {str(i + 1)}')
            length = float(input('Length of obstacle: '))
            height = float(input('Height of obstacle: '))
            exclude.append((length, height))
        wall['exclude'] = exclude

        walls.append(wall)

    return walls


def summarize(walls):
    summary = {}
    for wall in walls:
        wall['area'] = calc_area(wall)
        if wall['color'] not in summary:
            summary[wall['color']] = {'area': 0}

        summary[wall['color']]['area'] += wall['area']

    for color in summary:
        # # convert area in square meter then divide by six to get liters required
        summary[color]['quantity'] = summary[color]['area'] / 12.764 / 6
        summary[color]['cost'] = summary[color]['quantity'] * paints.get(color, 0)
    return summary


paints = {'White': 120, 'SkyBlue': 200, 'Ivy': 300, 'Peach': 250}

# sample walls data
# walls = [
#     {'length': 15.0, 'height': 15.0, 'color': 'Ivy', 'exclude': [(3.0, 7.0), (6.0, 6.0), (4.0, 4.0), (4.0, 4.0)]},
#     {'length': 14.0, 'height': 14.0, 'color': 'Ivy', 'exclude': [(3.0, 7.0), (2.0, 3.0), (5.0, 5.0), (4.0, 4.0), (4.0, 4.0)]},
#     {'length': 15.0, 'height': 15.0, 'color': 'White', 'exclude': [(3.0, 7.0), (6.0, 6.0), (4.0, 4.0), (4.0, 4.0)]},
#     {'length': 16.0, 'height': 16.0, 'color': 'White', 'exclude': [(3.0, 7.0), (2.0, 3.0), (5.0, 5.0), (4.0, 4.0), (4.0, 4.0)]},
#     {'length': 18.0, 'height': 20.0, 'color': 'SkyBlue', 'exclude': [(3.0, 7.0), (3.0, 7.0), (6.0, 6.0), (4.0, 4.0), (4.0, 4.0), (4.0, 4.0)]}
#     ]
# print('Sample Walls Data')
# for wall in walls:
#     print(wall)

walls = get_walls()
summary = summarize(walls)

print()
print(f"{'Color':12} {'Area':>12} {'Quantity':>12} {'Cost':>12}")
print(f"-" * 51)
total = {'area': 0, 'quantity': 0, 'cost': 0}
for paint in summary:
    print(
        f"{paint:12} {summary[paint]['area']:>12.2f} {summary[paint]['quantity']:>12.2f} {summary[paint]['cost']:>12.2f}")
    total['area'] += summary[paint]['area']
    total['quantity'] += summary[paint]['quantity']
    total['cost'] += summary[paint]['cost']

print(f"-" * 51)
print(f"{'Total':12} {total['area']:>12.2f} {total['quantity']:>12.2f} {total['cost']:>12.2f}")
print()
