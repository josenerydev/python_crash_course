alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

del alien_0['points']
print(alien_0)
