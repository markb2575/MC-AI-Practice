import cv2
import numpy as np

data = np.load("C:/Users/markb/OneDrive/Desktop/FCbot/data/training_data.npy", allow_pickle=True)
targets = np.load("C:/Users/markb/OneDrive/Desktop/FCbot/data/target_data.npy", allow_pickle=True)

print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')

# Lets see how many of each type of move we have.
unique_elements, counts = np.unique(targets, return_counts=True)
print(np.asarray((unique_elements, counts)))

# Store both data and targets in a list.
# We may want to shuffle down the road.

holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])

count_up = 0
count_left = 0
count_back = 0
count_right = 0
count_attack = 0

for data in holder_list:
    #print(data[1])
    if data[1] == 'W':
        count_up += 1
        cv2.imwrite(f"C:/Users/markb/OneDrive/Desktop/FCbot/GC/Forward/H7-u{count_up}.png", data[0])
    if data[1] == 'A':
        count_left += 1
        cv2.imwrite(f"C:/Users/markb/OneDrive/Desktop/FCbot/GC/Left/H7-l{count_left}.png", data[0]) 
    if data[1] == 'S':
        count_back += 1
        cv2.imwrite(f"C:/Users/markb/OneDrive/Desktop/FCbot/GC/Back/H7-b{count_back}.png", data[0]) 
    if data[1] == 'D':
        count_right += 1
        cv2.imwrite(f"C:/Users/markb/OneDrive/Desktop/FCbot/GC/Right/H7-r{count_right}.png", data[0]) 
    if data[1] == 'M':
        count_attack += 1
        cv2.imwrite(f"C:/Users/markb/OneDrive/Desktop/FCbot/GC/Attack/H7-a{count_attack}.png", data[0]) 
