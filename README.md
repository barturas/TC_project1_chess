# Chessboard Simulator README

## Overview

This Chessboard Simulator is a Python project developed as part of the Turing College curriculum. It allows users to create a visual representation of a chessboard, place white and black chess pieces on the board, and simulate capturing movements. The project is designed to help learners understand basic programming concepts, including data structures, loops, and user input handling in Python.

## Features

- **Chessboard Creation**: Generates an 8x8 chessboard with coordinates for each cell.
- **Visual Representation**: Displays the chessboard in the terminal with clear boundaries between cells, making it easy to visualize.
- **Piece Placement**: Users can place white (rook or bishop) and black (pawn) pieces on the board. The placement is flexible, allowing for a dynamic setup before simulation.
- **Capture Simulation**: After placing the pieces, the program calculates and displays the black pawns that can be captured by the white rook or bishop, based on their positions on the board.

## Installation

To run this project, you need Python installed on your system. This code is compatible with Python 3.x. No additional libraries are required to run the program. Simply clone the repository, navigate to the directory containing the project, and execute the script using the Python interpreter.

```bash
git clone <repository-url>
cd <project-directory>
python chess.py
```

## Usage

Follow the on-screen instructions to place the white and black pieces on the chessboard. The program will then display the chessboard with your placements and calculate any captures based on the positions of the pieces.

1. **Start the Program**: Run the script in your terminal or command line.

    ```bash
    python chess.py
    ```

2. **Place a White Piece**: At the prompt, choose between placing a rook or a bishop on the board. Specify your choice along with the position in the format `<piece> <position>`. For example, to place a rook at position a1, you would enter:

    ```
    rook a1
    ```

3. **Place Black Pawns**: Next, you will place black pawns on the board. Enter the positions for black pawns one at a time. Use the coordinate system to specify the position, for example, `e4`. After placing each pawn, press enter to input the next position. When you have finished placing all desired black pawns, type `done` and press enter to proceed.

    Example input for placing a black pawn at position e4:

    ```
    e4
    ```

    To finish placing black pawns:

    ```
    done
    ```

4. **View Simulation Results**: After all pieces are placed, the program will simulate the chessboard and calculate the captures. The results, including the positions of captured black pawns, will be displayed on the screen.

5. **Review Output**: The final output will include the chessboard with all pieces placed as specified, along with a list of black pawns that can be captured by the white piece(s) you placed.

By following these steps, you can simulate different chessboard setups and understand the potential captures based on the pieces' positions.


## Contributing

As this is a learning project developed as part of the Turing College curriculum, contributing is not required. The project is intended to serve as an educational tool for understanding basic programming concepts in Python, including data structures, loops, and user input handling. I encourage learners to fork and experiment with the project for their personal learning and development, but no formal contributions are sought.

## License

This project is licensed under the MIT License. This means it is free to use, modify, and distribute, including for commercial purposes, provided that the original authorship is credited and the source code remains open source.

The full text of the license can be found in the LICENSE file in the project repository. Here is a summary of the key points:

- **Permission** is granted to anyone to use, copy, modify, and distribute this software and its documentation for any purpose.
- **No Warranty**: The software is provided "as is", without warranty of any kind.
- **Conditions**: Redistribution must include the original license and copyright notice.

Please review the full license for more detailed information.

