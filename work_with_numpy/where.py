import numpy as np

shape = (6, 9)
maze = np.zeros(shape, dtype=int)
V_WALL = 1
# Mark wall for maze
maze[2:5,2] = V_WALL
maze[1,5] = V_WALL
maze[3:6,7] = V_WALL

# Get wall index
wall_index = np.where(maze == V_WALL)
wall_indexlist = list(zip(wall_index[0], wall_index[1]))
wall_index_pair = np.argwhere(maze == V_WALL)

print(maze)

# print(wall_index[0])
# print(np.concatenate(wall_index))
print(wall_index_pair)
print("\n", wall_index_pair[0])
print(maze[wall_index_pair[0]])
