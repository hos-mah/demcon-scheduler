# demcon-scheduler
The code schedules a list of shows to minimize the number of stages required, ensuring that no overlapping shows are scheduled on the same stage. It outputs a detailed schedule and the minimum number of stages used.


## Plan
#### Sort the Shows: 
Sort the shows based on their start times. If two shows have the same start time, we can sort them by their end times.

#### Allocate Stages: 
Use a priority queue (min-heap) to track the end times of shows currently using stages. Iterate through the sorted shows, and for each show:

- If the show starts after the earliest ending show, reuse that stage by updating the end time in the heap.
- If the show starts before the earliest ending show finishes, allocate a new stage.

#### Count the Stages: 
The maximum size of the heap at any point will give us the minimum number of stages required.

#### Output Schedule: 
Assign shows to stages and print the schedule.



## How to Run the Code

Ensure you have Python3 installed on your machine.

Run the script using a terminal or command prompt:

_python festival_scheduler.py_

