import heapq
from collections import defaultdict
from typing import List, Tuple, Dict

def schedule_shows(shows: List[Tuple[str, int, int]]) -> Tuple[Dict[int, List[str]], List[str], int]:
    """
    Schedule shows to minimize the number of stages needed.
    
    Parameters:
    shows (List[Tuple[str, int, int]]): A list of tuples representing shows with their names, start times, and end times.
    
    Returns:
    Tuple[Dict[int, List[str]], List[str], int]: A tuple containing:
        - A dictionary mapping stage numbers to lists of scheduled shows.
        - A list of formatted strings representing the schedule.
        - The minimum number of stages required.
    """
    # Sort shows by their start times, then by end times as a tiebreaker
    shows.sort(key=lambda show: (show[1], show[2]))
    
    # Min-heap to track end times of stages
    stage_end_times = []  # Stores tuples of (end_time, stage_number)
    show_to_stage = {}    # Maps each show to its assigned stage
    next_stage_number = 1 # Counter to assign new stage numbers

    for show_name, start, end in shows:
        # Reuse the earliest available stage if its end time is before the current show's start time
        if stage_end_times and stage_end_times[0][0] < start:
            _, stage_number = heapq.heappop(stage_end_times)
        else:
            # Allocate a new stage if no stages are available
            stage_number = next_stage_number
            next_stage_number += 1
        
        # Push the current show into the heap with its end time and stage number
        heapq.heappush(stage_end_times, (end, stage_number))
        
        # Assign the show to the stage
        show_to_stage[show_name] = stage_number
    
    # Prepare the output schedule
    stage_shows = defaultdict(list)
    schedule_output = []
    for show_name, start, end in shows:
        stage_number = show_to_stage[show_name]
        show_info = f"{show_name}: Stage {stage_number}, Time {start} - {end}"
        schedule_output.append(show_info)
        stage_shows[stage_number].append(f"{show_name} (Time {start} - {end})")
    
    return stage_shows, schedule_output, next_stage_number - 1

# Example Input
shows = [
    ("show_1", 29, 33),
    ("show_2", 2, 9),
    ("show_3", 44, 47),
    ("show_4", 26, 30),
    ("show_5", 15, 20),
    ("show_6", 8, 15),
    ("show_7", 2, 9),
    ("show_8", 30, 34),
    ("show_9", 1, 9),
    ("show_10", 20, 28),
    ("show_11", 1, 4),
    ("show_12", 2, 11),
    ("show_13", 26, 29),
    ("show_14", 5, 10),
    ("show_15", 37, 44),
    ("show_16", 27, 35),
    ("show_17", 36, 39),
    ("show_18", 4, 10),
    ("show_19", 35, 44),
    ("show_20", 22, 30),
    ("show_21", 15, 20),
    ("show_22", 42, 46),
    ("show_23", 6, 9),
    ("show_24", 19, 23),
    ("show_25", 31, 38),
    ("show_26", 37, 41),
    ("show_27", 30, 36),
    ("show_28", 14, 21),
    ("show_29", 5, 13),
    ("show_30", 33, 36)
]

# Execute the scheduling function
stage_shows, schedule, num_stages = schedule_shows(shows)

# Output the results
print(f"Minimum number of stages required: {num_stages}")
print("Schedule:")
for show_info in schedule:
    print(show_info)

print("\nSchedule by Stage:")
for stage_number in sorted(stage_shows.keys()):
    print(f"\nStage {stage_number}:")
    for show_info in stage_shows[stage_number]:
        print(f"  {show_info}")
