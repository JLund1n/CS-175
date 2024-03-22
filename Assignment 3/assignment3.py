from bqueue import ChemicalQueue
from bstack import Flask
import os
import sys

def clear_screen():
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

def move_cursor(line, column):
    print(f"\033[{line};{column}H", end='')

def print_at(line, message, erase_line=True):
    if erase_line:
        move_cursor(line, 0)
        print("\033[2K", end='')  # Erase the line
    move_cursor(line, 0)
    print(message, end='')
    sys.stdout.flush()

class Game:
    def __init__(self, file_path):
        self.flasks = []
        self.chemical_queue = ChemicalQueue(4)
        self.read_initial_setup(file_path)

    def read_initial_setup(self, file_path):
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
            num_flasks, _ = map(int, first_line.split())
            self.flasks = [Flask() for _ in range(num_flasks)]

            for line_number, line in enumerate(file, start=2):  # Start at 2 considering the first line is already read
                line = line.strip()
                if 'F' in line:
                    parts = line.split('F')
                    if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                        num_to_dequeue, flask_index = map(int, parts)
                        for _ in range(num_to_dequeue):
                            chemical = self.chemical_queue.dequeue()
                            if chemical:
                                self.flasks[flask_index - 1].add_chemical(chemical)
                    else:
                        print(f"Warning: Line {line_number} in file '{file_path}' is not properly formatted and will be skipped.")
                elif line:  # Ensure the line is not empty before enqueuing
                    self.chemical_queue.enqueue(line)
                else:
                    print(f"Warning: Empty line at {line_number} in file '{file_path}' will be skipped.")

    def run_game(self):
        clear_screen()
        print_at(1, "Magical Flask Game")
        while not self.check_win_condition():
            self.display_flasks()

            source = self.get_valid_input("Select source flask: ", 2)
            if source == "exit":
                print_at(4, "Game exited.")
                return

            destination = self.get_valid_input("Select destination flask: ", 3)
            if destination == "exit":
                print_at(4, "Game exited.")
                return

            self.make_pour(int(source), int(destination))
            if self.check_win_condition():
                self.display_flasks()  # Display final state of flasks
                print_at(4, "You win!")
                return

    def get_valid_input(self, prompt, line):
        valid_input = False
        input_value = ""
        while not valid_input:
            print_at(line, prompt + " ", False)
            input_value = input()
            if self.validate_input(input_value):
                valid_input = True
                print_at(4, " " * 50)  # Clear any error message
            else:
                print_at(4, "Invalid Input. Try Again.")
        return input_value
    
    def validate_input(self, input_str):
        if not input_str.isdigit():
            return False
        input_num = int(input_str)
        if 1 <= input_num <= len(self.flasks):
            return True
        return False


    def display_flasks(self):
        start_line = 6
        move_cursor(start_line, 0)
        print("\033[J", end='')  # Clear from cursor to the end of the screen
        # Define the number of flasks per row for display, assuming a fixed layout for simplicity
        flasks_per_row = min(4, len(self.flasks))  # Adjust based on your terminal size or preferences
        for i, flask in enumerate(self.flasks, start=1):
            # Adjust line based on flask index
            line = start_line + (i - 1) // flasks_per_row * Flask.CAPACITY + (i - 1) // flasks_per_row * 2  # Additional space between rows
            column = ((i - 1) % flasks_per_row) * (Flask.CAPACITY + 3)  # Adjust spacing based on your layout preferences
            flask_representation = str(flask).split('\n')
            for j, layer in enumerate(flask_representation):
                print_at(line + j, " " * column + layer)
        sys.stdout.flush()


    def display_flasks(self):
        # Define the number of flasks per row for display
        if len(self.flasks) < 4:
            flasks_per_row = len(self.flasks)
        else:
            flasks_per_row = 4
        # Define empty space and flask width
        empty_space = "|  |"
        
        # move cursor to first row
        print("\033[H", end='')
        # Start the display string
        flask_display = "\n\n\n\n\n"

        for i in range(0, len(self.flasks), flasks_per_row):
            # Display for each row
            content_lines = [["|  |" for _ in range(flasks_per_row)] for _ in range(Flask.CAPACITY)]
            bottom_line = []
            number_line = []

            for j in range(flasks_per_row):
                if i + j < len(self.flasks):
                    flask = self.flasks[i + j]
                    for k in range(Flask.CAPACITY - len(flask.stack), Flask.CAPACITY):
                        content_lines[k][j] = f"|{Flask.COLORS[flask.stack[-(k - Flask.CAPACITY + len(flask.stack)) - 1]]}{flask.stack[-(k - Flask.CAPACITY + len(flask.stack)) - 1]}{Flask.COLORS['RESET']}|"

                    bottom_line.append("+--+" if flask.stack else "    ")
                    number_line.append(f" {i+j+1} " if flask.stack else "   ")
                else:
                    bottom_line.append("+--+")
                    number_line.append("   ")

            # Join the content lines and bottom line for the full flask representation
            for line in content_lines:
                flask_display += " ".join(line) + "\n"
            flask_display += " ".join(bottom_line) + "\n"
            flask_display += " ".join(number_line) + "\n"

            # Add an extra line of space after each row of flasks for separation
            if i + flasks_per_row < len(self.flasks):
                flask_display += "\n"
        
        print(flask_display)


    def handle_user_input(self):
        while True:
            source = input("Select source flask: ").strip()
            if source.lower() == 'exit':
                return "exit", "exit"
            destination = input("Select destination flask: ").strip()
            if destination.lower() == 'exit':
                return "exit", "exit"

            if not source.isdigit() or not destination.isdigit():
                print("Invalid input. Try again.")
                continue
            source, destination = int(source), int(destination)
            if source < 1 or source > len(self.flasks) or destination < 1 or destination > len(self.flasks):
                print("Invalid input. Try again.")
                continue
            if source == destination:
                print("Cannot pour into the same flask. Try again.")
                continue
            return source, destination

    def make_pour(self, source, destination):
        RED = '\033[91m'  # ANSI escape code for red
        GREEN = '\033[92m'  # ANSI escape code for green
        RESET = '\033[0m'  # ANSI escape code to reset color
        print("\r", end='')

        source_flask = self.flasks[source - 1]
        destination_flask = self.flasks[destination - 1]

        if source_flask.is_sealed() or not source_flask.stack:
            print(f"Cannot pour from that flask. Try again.")
            return
        if destination_flask.is_sealed() or destination_flask.is_full():
            print(f"Cannot pour into that flask. Try again.")
            return

        chemical = source_flask.remove_top_chemical()
        destination_flask.add_chemical(chemical)

        # Use RED for the source and GREEN for the destination in the message
        print(f"Moved {chemical} from flask {RED}{source}{RESET} to flask {GREEN}{destination}{RESET}.")

        # Check if destination flask should seal
        if destination_flask.is_sealed():
            print(f"Flask {GREEN}{destination}{RESET} is now sealed.")



    def check_win_condition(self):
        return all(flask.is_sealed() or not flask.stack for flask in self.flasks)


def main():
    game_file_path = "chemicals.txt"  # Make sure to replace this with the correct path to your file
    game = Game(game_file_path)
    game.run_game()

if __name__ == "__main__":
    main()