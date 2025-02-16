import csv
import math
import matplotlib.pyplot as plt

def generate_track_coordinates(csv_filename, step_size=0.5, skip_header=True, tol=1e-3):
    """
    Reads a CSV file with segments and returns a list of (x, y) coordinates
    computed every step_size meters along the track.
    
    CSV Format:
      Column 1: segment type as a string:
                "straight", "left", "right", or "connect".
                The "connect" segment tells the code to draw a straight
                line from the current position back to the start.
      Column 2: segment distance in meters (a float). For "connect", this is ignored.
      Column 3: curve radius in meters (a float). For a straight or "connect", this can be empty.
    """
    # Starting position and heading (in radians; 0 means east)
    x, y = 0.0, 0.0
    heading = 0.0  # current heading in radians
    coords = [(x, y)]
    
    # Save the start (for later connection if needed)
    start_pos = (x, y)
    
    with open(csv_filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        if skip_header:
            next(reader, None)
        
        for row in reader:
            if not row or len(row) < 1:
                continue
            
            seg_type = row[0].strip().lower()
            # For "connect" we ignore any distance/radius values.
            if seg_type == "connect":
                # Compute vector from current position to start.
                dx = start_pos[0] - x
                dy = start_pos[1] - y
                distance = math.hypot(dx, dy)
                if distance < tol:
                    continue  # already connected
                # Determine number of steps so that step size is ~step_size.
                n_steps = int(math.ceil(distance / step_size))
                for i in range(1, n_steps + 1):
                    t = i / n_steps
                    new_x = x + t * dx
                    new_y = y + t * dy
                    coords.append((new_x, new_y))
                # Update current position and heading (set heading to the direction of the connect)
                x, y = start_pos
                heading = math.atan2(dy, dx)
                continue  # move to next row
            
            # Otherwise, parse the distance and (if needed) radius.
            try:
                distance = float(row[1])
            except (IndexError, ValueError):
                raise ValueError(f"Invalid distance value in row: {row}")
            try:
                radius = float(row[2]) if len(row) >= 3 and row[2].strip() else 0.0
            except ValueError:
                radius = 0.0

            if seg_type == 'straight':
                dist_covered = 0.0
                while dist_covered < distance:
                    step_length = min(step_size, distance - dist_covered)
                    x += step_length * math.cos(heading)
                    y += step_length * math.sin(heading)
                    coords.append((x, y))
                    dist_covered += step_length

            elif seg_type in ('left', 'right'):
                if radius == 0:
                    raise ValueError("A curve segment must have a non-zero radius.")
                turn_direction = 1 if seg_type == 'left' else -1
                # Compute the center of the circle for the curve.
                center_x = x - turn_direction * radius * math.sin(heading)
                center_y = y + turn_direction * radius * math.cos(heading)
                # Starting angle from the center to the current position.
                phi0 = math.atan2(y - center_y, x - center_x)
                # Total angle to turn (in radians). Positive for left, negative for right.
                total_angle = turn_direction * (distance / radius)
                angle_covered = 0.0
                while abs(angle_covered) < abs(total_angle):
                    dphi = step_size / radius
                    if abs(angle_covered + dphi) > abs(total_angle):
                        dphi = abs(total_angle) - abs(angle_covered)
                    dphi *= turn_direction
                    angle_covered += dphi
                    phi = phi0 + angle_covered
                    x = center_x + radius * math.cos(phi)
                    y = center_y + radius * math.sin(phi)
                    coords.append((x, y))
                    # Update heading so that it is tangent to the circle.
                    # For our formulation, use: heading = phi + (math.pi/2) * turn_direction.
                    heading = phi + (math.pi / 2) * turn_direction
            else:
                raise ValueError(f"Unknown segment type: {seg_type}")
    
    return coords

def plot_track(coords):
    xs, ys = zip(*coords)
    plt.figure(figsize=(8, 8))
    plt.plot(xs, ys, marker='o', markersize=3, linestyle='-')
    plt.xlabel('X (meters)')
    plt.ylabel('Y (meters)')
    plt.title('Race Track')
    plt.axis('equal')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    csv_filename = "Motorland_Aragon.csv"  # Make sure this CSV uses the modified data
    try:
        track_coords = generate_track_coordinates(csv_filename, step_size=0.5, skip_header=True)
        plot_track(track_coords)
    except Exception as e:
        print("An error occurred:", e)