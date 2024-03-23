# Design a program that determines the award a person competing in a triathlon will receive.
# Your program should read in the times (in minutes) for all three events of a
# triathlon, namely swimming, cycling, and running, and then calculate and
# display the total time taken to complete the triathlon.
# The award a participant receives is based on the total time taken to
# complete the triathlon. The qualifying time for awards is 100 minutes.
# Display the award that the participant will receive based on the following
# criteria:
"""Qualifying Criteria Time Range Award
Within the qualifying time. 0 - 100 minutes Provincial Colours
Within 5 minutes of the
qualifying time.
101 - 105 minutes Provincial Half
Colours
Within 10 minutes of the
qualifying time.
106 - 110 minutes Provincial Scroll
More than 10 minutes off
from the qualifying time.
111+ minutes No award"""

swimming = int(input("Please enter your swimming time in minutes: "))
cycling= int(input("Please enter your cycling time in minutes: "))
running = int(input("Please enter your running time in minutes: "))

#  A direct addition here is possible but I did it this way to practice a bit 
list_triathlon = [swimming,cycling, running] 
triathlon = sum(list_triathlon)
print(f"The total time of your triathlon is {triathlon} mn")

#  mentor comment:
# covers all numbers up to 100
# so the second condition do not need to re check the previous conditions each time 

if 0< triathlon <= 100:
    print(f"Congratulation, you receive the Award of Provincial Colours with {triathlon} mn")
elif triathlon<= 105:
    print(f"Congratulation, you receive the Award of Provincial Half Colours with {triathlon} mn")
elif triathlon <= 110:
    print(f"Congratulation, you receive the Award of Provincial Scroll with {triathlon} mn")
else:
    print(f"No award, with a time of {triathlon} mn,but don't worry you'll do better next time")
    