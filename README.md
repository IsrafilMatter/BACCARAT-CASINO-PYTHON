# Baccarat Casino Simulator

A Python-based Baccarat casino game simulator with a graphical interface.

## Features
- Realistic Baccarat table layout with professional design
- Player and Banker hand display
- Multiple save game slots (3 slots available)
- Results tracking for Player/Banker wins
- Interactive betting system using mouse control
- Card dealing and score calculation
- Victory celebration for big wins

## Requirements
- Python 3.7+
- Pygame 2.5.2
- Numpy 1.26.3

## Installation
1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Standalone Setup
1. Create an `assets` folder in the game directory
2. Copy the following files to the `assets` folder:
   - BaccaratTable.jpg (background)
   - SHOE-removebg-preview.png (shoe image)
   - WIN sound effect no copyright.mp3 (win sound)
   - Las Vegas Casino Music.mp3 (background music)
   - pokerchip1.png (red chip)
   - pokerchip3.png (blue chip)
   - pokerchip4.png (yellow chip)
3. Create a `cards` folder inside the `assets` folder
4. Copy all playing card images (PNG format) to the `assets/cards` folder
   - Card images should be named in the format: `value_of_suit.png`
   - Example: `ace_of_hearts.png`, `king_of_spades.png`

The game will automatically create a `saves` directory to store your game progress.

## How to Play
1. Run the game:
```bash
python baccarat_simulator.py
```

### Controls
- **Mouse**: Click and drag up/down to adjust bet amount
- **SPACE**: Switch between betting on Player or Banker
- **ENTER**: Deal cards
- **R**: Reset the game
- **ESC**: Pause menu (Save/Load/Exit)

### Save/Load System
- Three save game slots available
- Access through the pause menu (ESC)
- Each save includes:
  - Player balance
  - Current bet
  - Win/loss statistics

## Game Rules
- Cards 2-9 are worth face value
- 10, J, Q, K are worth 0
- Ace is worth 1
- Hand total is the right digit of the sum (e.g., 15 becomes 5)
- Natural 8 or 9 wins automatically
- Complex drawing rules for third cards are implemented according to standard Baccarat rules

## Statistics Tracking
- View Player and Banker win counts
- Track number of ties
- Statistics are saved with game progress
