def direction(facing, turn):
    """Return a new direction of compass."""
    compass = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']  # Create a list of compass directions
    full_turn = int(turn / 360)  # Convert a number of turn onto a single turn
    # Calculate the offset number inside the compass
    # This calculation takes into account clockwise and counterclockwise rotation
    index_turn = int((turn - 360 * full_turn) / 45)
    if compass.index(facing) + index_turn >= len(compass):
        # Case one :sum of start position and turn number more
        # than the length of the list
        return compass[compass.index(facing) + index_turn - len(compass)]
    else:
        # Case one :sum of start position and turn number less
        # than the length of the list
        return compass[compass.index(facing) + index_turn]
