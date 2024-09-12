import numpy as np
from stl import mesh

# Cube size in millimeters (30 mm)
cube_size = 30.0

# Define the vertices of a cube (8 vertices for a cube)
# These coordinates define a cube centered at the origin
half_size = cube_size / 2
vertices = np.array([
    [-half_size, -half_size, -half_size],
    [+half_size, -half_size, -half_size],
    [+half_size, +half_size, -half_size],
    [-half_size, +half_size, -half_size],
    [-half_size, -half_size, +half_size],
    [+half_size, -half_size, +half_size],
    [+half_size, +half_size, +half_size],
    [-half_size, +half_size, +half_size]
])

# Define the 12 triangles composing the cube
faces = np.array([
    [0, 3, 1], [1, 3, 2],  # Bottom face
    [0, 4, 7], [0, 7, 3],  # Left face
    [4, 5, 6], [4, 6, 7],  # Top face
    [5, 1, 2], [5, 2, 6],  # Right face
    [2, 3, 7], [2, 7, 6],  # Front face
    [0, 1, 5], [0, 5, 4]   # Back face
])

# Create the mesh
cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))

# Assign the vertices to the mesh
for i, face in enumerate(faces):
    for j in range(3):
        cube.vectors[i][j] = vertices[face[j], :]

# Save the cube as an STL file
cube.save('30mm_cube.stl')

print("STL file '30mm_cube.stl' created successfully.")