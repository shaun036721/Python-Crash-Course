guest_list = ['Cristiano Ronaldo', 'Lionel Messi', 'Paul Pogba', 'Michael Essien', 'Luis Nani']

#Informing my guests that I have found a new dinner table. 
print(f'Hello, everyone! I have found a bigger dinner table.\n')

#Adding one new guest to the beginning of the guest list.
guest_list.insert(0, 'Sergio Aguero')

#Adding one new guest to the middle of the guest list.
guest_list.insert(3, 'Asamoah Gyan')

#Adding one new guest to the end of my guest list.
guest_list.append('Samuel Eto')

#Resending invitations to my guests. 
print(f"Hello, {guest_list[0]}! You are invited to my dinner party.")
print(f"Hello, {guest_list[1]}! You are invited to my dinner party.")
print(f"Hello, {guest_list[2]}! You are invited to my dinner party.")
print(f"Hello, {guest_list[3]}! You are invited to my dinner party.")
print(f"Hello, {guest_list[4]}! You are invited to my dinner party.")
print(f"Hello, {guest_list[5]}! You are invited to my dinner party.")
print(f"Hello, {guest_list[6]}! You are invited to my dinner party.")
print(f"Hello, {guest_list[7]}! You are invited to my dinner party.\n")

#Priting the updated guest list.
print(f"Here is the updated guest list:\n{guest_list}")