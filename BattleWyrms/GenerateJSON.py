import json
import random
import os

def generate_data(i):
    # Generate data for characters
    data = {
        "id": i,
        "health": random.randint(100, 1000),
        "strength": random.randint(100, 1000),
        "defense": random.randint(1, 100),
        "crit": random.randint(1, 100)
    }
    return data

def main():
    # Directory where files will be saved
    directory = 'BattleWyrms/BattleWyrmJSON'
    
    # Create directory if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Number of files to generate
    num_files = 100
    
    for i in range(num_files):
        # Generate the data for each character
        character_data = generate_data(i)
        
        # File name pattern
        file_name = f'{directory}/{i}.json'
        
        # Save data to a JSON file
        with open(file_name, 'w') as file:
            json.dump(character_data, file, indent=4)

# Run the script
if __name__ == "__main__":
    main()
