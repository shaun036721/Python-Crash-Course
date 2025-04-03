guest_list = ['Cristiano Ronaldo', 'Lionel Messi', 'Paul Pogba', 'Carlos Tevez', 'Michael Essien']

#Carlos Tevez is unable to make it to the dinner party.
unable_to_come = guest_list.pop(3)
print(f"{unable_to_come}, is unable to make it to the dinner party.\n")

#Adding a new guest to the list, to take Carlos Tevez's spot. 
guest_list.append('Luis Nani')

#Sending out new invitations with my new guest list.
print(f"Hello, {guest_list[0]}! You are invited to my dinner party.")
print(f"Hello, {guest_list[1]}! You are invited to my dinner party.")
print(f"Hello, {guest_list[2]}! You are invited to my dinner party.")
print(f"Hello, {guest_list[3]}! You are invited to my dinner party.")
print(f"Hello, {guest_list[4]}! You are invited to my dinner party.")

#Printing the updated guest list.
print(guest_list)