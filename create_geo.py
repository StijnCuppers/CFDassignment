import numpy as np

# Load your airfoil data -- MAKE SURE to change the filename if yours is different!
coords = np.loadtxt("NACA0012.dat")

# Open a .geo file to write to
with open("NACA0012.geo", "w") as f:
    # Define a characteristic length for the mesh (smaller value = finer mesh)
    lc = 0.05 
    
    # Write the points to the .geo file
    point_ids = []
    for i, (x, y) in enumerate(coords):
        point_id = i + 1
        f.write(f"Point({point_id}) = {{{x}, {y}, 0, {lc}}};\n")
        point_ids.append(str(point_id))
        
    # Create a spline that connects all the points to form the airfoil
    f.write(f"Spline(1) = {{{', '.join(point_ids)}}};\n")
