class World:
    def __init__(self):
        self.map_file = "map.txt"
        
        # Calculate the length of a row in the map file
        with open(self.map_file, "r") as f:
            self.row_length = len(f.readline())
        
        # ... (initialize locations, characters, and items) ...
    def read_map(self, x, y):
        # Calculate the byte position in the file
        byte_position = (y * self.row_length) + x
        
        # Open the file in read mode and read the character at the specific position
        with open(self.map_file, "r") as f:
            # Move the file pointer to the byte position
            f.seek(byte_position)
            
            # Read the character at the current position
            character = f.read(1)
        
        return character
    def write_map(self, x, y, value):
        # Calculate the byte position in the file
        byte_position = (y * self.row_length) + x
        
        # Open the file in read-write mode and update the specific position
        with open(self.map_file, "r+") as f:
            # Move the file pointer to the byte position
            f.seek(byte_position)
            
            # Write the value at the current position
            f.write(value)
    def update_map(self, current_location):
        # Get the coordinates of the current location
        x, y = current_location.get_coordinates()
        
        # Update the specific position in the map file using the write_map method
        self.write_map(x, y, "X")
    # ... (rest of the class) ...