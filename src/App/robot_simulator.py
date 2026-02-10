"""
Simple Robot Simulator

Prompts for robot name, distance to target, and obstacle presence.
Makes movement decisions using if/elif/else and nested ifs, records
checkpoints in a list, allows adding/removing checkpoints, and
shows a trip summary using f-strings.
"""
import random
import time


def decide_speed(distance_remaining):
    """Decide speed based on remaining distance."""
    if distance_remaining > 100:
        return 'fast', 10
    elif distance_remaining > 50:
        return 'medium', 5
    else:
        return 'slow', 2


def handle_obstacle(speed_label, speed_val):
    """Nested decision-making for obstacle handling.

    Returns (action, speed_val_delta)
    """
    if speed_label == 'fast':
        # if going fast and obstacle, must brake and turn
        return 'brake_and_turn', - int(speed_val * 0.8)
    elif speed_label == 'medium':
        # medium speed: slow down and carefully pass
        return 'slow_and_pass', - int(speed_val * 0.5)
    else:
        # slow: attempt small detour
        return 'detour', 0


def simulate_trip(name, total_distance, obstacle_ahead):
    checkpoints = []
    distance_travelled = 0
    step = 0
    direction = 'forward'

    print(f"Starting trip for {name}. Target {total_distance} units away.")

    while distance_travelled < total_distance:
        remaining = total_distance - distance_travelled
        speed_label, speed_val = decide_speed(remaining)

        # chance of unexpected direction change
        if random.random() < 0.15:
            old_direction = direction
            direction = random.choice(['left', 'right', 'forward'])
            note = f'unexpected_turn_from_{old_direction}_to_{direction}'
        else:
            note = ''

        # chance of seeing humans and needing to stop until they pass
        if random.random() < 0.12:
            humans_waiting = random.randint(1, 4)
            print(f"Human(s) detected ahead: {humans_waiting}. Stopping until they pass...")
            # robot stops until all humans pass; record wait checkpoints
            while humans_waiting > 0:
                step += 1
                cp_wait = {
                    'step': step,
                    'moved': 0,
                    'total_so_far': distance_travelled,
                    'speed': 'stopped',
                    'note': f'stopped_for_humans_remaining_{humans_waiting}'
                }
                checkpoints.append(cp_wait)
                print(f"Waiting... {humans_waiting} human(s) still passing.")
                time.sleep(0.4)
                humans_waiting -= 1
            # after all pass, add a checkpoint note
            step += 1
            cp_clear = {
                'step': step,
                'moved': 0,
                'total_so_far': distance_travelled,
                'speed': 'stopped',
                'note': 'humans_cleared'
            }
            checkpoints.append(cp_clear)
            print('Humans have passed. Resuming movement.')
            # continue loop to next iteration with updated step/checkpoints
            continue

        # obstacle handling (nested if)
        if obstacle_ahead:
            action, speed_delta = handle_obstacle(speed_label, speed_val)
            speed_val = max(0, speed_val + speed_delta)
            checkpoint_note = f"{action}{('-' + note) if note else ''}"
        else:
            checkpoint_note = f"moving_{direction}{('-' + note) if note else ''}"

        # if robot is close enough to 'see' the objective, move left or right
        see_distance = 5
        if remaining <= see_distance:
            direction = random.choice(['left', 'right'])
            checkpoint_note = f'see_objective_and_move_{direction}'

        # simulate movement step
        moved = min(speed_val, remaining) if speed_val > 0 else 0
        # if stopped or zero speed, try a small recovery move
        if moved == 0:
            # recovery: take a small careful step
            moved = 1
            checkpoint_note += '_recovery'

        distance_travelled += moved
        step += 1

        cp = {
            'step': step,
            'moved': moved,
            'total_so_far': distance_travelled,
            'speed': speed_label,
            'note': checkpoint_note,
        }
        checkpoints.append(cp)

        # brief console feedback
        print(f"Step {step}: moved {moved} units ({speed_label}). Remaining: {total_distance - distance_travelled}")
        time.sleep(0.05)

        # small chance the obstacle clears or appears dynamically
        if random.random() < 0.1:
            obstacle_ahead = not obstacle_ahead

    return distance_travelled, obstacle_ahead, checkpoints


def manage_checkpoints(checkpoints):
    """Allow user to add or remove checkpoints after the trip."""
    while True:
        print('\nCheckpoint manager:')
        print(' - a: add a checkpoint')
        print(' - r: remove a checkpoint by index')
        print(' - l: list checkpoints')
        print(' - q: quit manager')
        choice = input('Choice (a/r/l/q): ').strip().lower()
        if choice == 'a':
            desc = input('Enter checkpoint description: ').strip()
            idx = len(checkpoints) + 1
            cp = {'step': idx, 'moved': 0, 'total_so_far': checkpoints[-1]['total_so_far'] if checkpoints else 0, 'speed': 'manual', 'note': desc}
            checkpoints.append(cp)
            print('Added checkpoint.')
        elif choice == 'r':
            if not checkpoints:
                print('No checkpoints to remove.')
                continue
            try:
                i = int(input(f'Enter index 1..{len(checkpoints)} to remove: ').strip())
                if 1 <= i <= len(checkpoints):
                    removed = checkpoints.pop(i-1)
                    print(f"Removed checkpoint {i}: {removed['note']}")
                    # reindex steps
                    for j, c in enumerate(checkpoints, start=1):
                        c['step'] = j
                else:
                    print('Index out of range.')
            except ValueError:
                print('Invalid number.')
        elif choice == 'l':
            for c in checkpoints:
                print(f"{c['step']}: {c['moved']}u, total {c['total_so_far']}, speed={c['speed']}, note={c['note']}")
        elif choice == 'q':
            break
        else:
            print('Unknown choice.')


def print_summary(name, total_travelled, obstacle_final, checkpoints):
    print('\n---- Trip Summary ----')
    print(f'Robot: {name}')
    print(f'Total distance travelled: {total_travelled} units')
    print(f'Obstacle present at end: {obstacle_final}')
    print('Final checkpoints:')
    for c in checkpoints:
        print(f" - step {c['step']}: moved {c['moved']}u, total {c['total_so_far']}, note={c['note']}")


def main():
    print('Robot Trip Simulator')
    name = input('Enter robot name: ').strip() or 'Robo'
    # validate numeric distance
    while True:
        try:
            distance = int(input('Enter distance to target (positive integer): ').strip())
            if distance <= 0:
                print('Please enter a positive integer.')
                continue
            break
        except ValueError:
            print('Invalid number. Try again.')

    obs_in = input('Is there an obstacle ahead? (y/n): ').strip().lower()
    obstacle = obs_in == 'y'

    travelled, obstacle_final, checkpoints = simulate_trip(name, distance, obstacle)

    # allow user to manage checkpoints
    manage = input('\nWould you like to manage checkpoints now? (y/n): ').strip().lower()
    if manage == 'y':
        manage_checkpoints(checkpoints)

    print_summary(name, travelled, obstacle_final, checkpoints)


if __name__ == '__main__':
    main()
