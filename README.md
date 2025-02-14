# Wheel of Fortune Game  

## Project Overview  
This project is a recreation of the **Wheel of Fortune** game designed for **three players**, featuring **three rounds** and a **final round**.  

The entire application is built using **PySide2 widgets**, which are stored in memory and displayed sequentially as separate screens.  

## Folder and File Structure  

### **`classes/` - Core Logic**  
- **`constants.py`** – Stores constant values used throughout the program. It contains:  
  - `Letters` – Defines the available letters in the game.  
  - `WheelPrizes` – Holds all possible prizes on the wheel.  
  - `FilePaths` – Contains file paths for external resources used in the game.  
  - `UiLabelsTexts` – Stores UI text strings used for screen updates.  
- **`exceptions.py`** – Defines custom exceptions used in the program:  
  - `NotAPositiveNumberError`  
  - `EmptyStringError`  
- **`game.py`** – Implements:  
  - `Game` – Manages game logic and flow.  
  - `Reward` – Handles the prizes players can win.  
- **`player.py`** – Implements the `Player` class, representing the players.  
- **`word.py`** – Implements the `Word` class, managing the words used in the game.  

### **`files/` - External Resources**  
- **`rewards.txt`** – Stores the prizes that players can win.  
- **`words.json`** – Contains the words randomly selected for each game.  

### **Other Key Files**  
- **`model.py`** – Defines three key classes for improved communication between game components:  
  - `Model` – Manages global variables and facilitates interactions between game components.  
  - `ButtonHolder` – Handles button logic within the `ui_roundwindow.py` widget.  
  - `ScreensHolder` – Stores and manages UI widgets, allowing seamless transitions between screens.  
- **`test_classes.py`** – Contains unit tests for the `classes/` directory.  
- **`screens.py`** – Implements UI screens using PySide2 widgets:  
  - `EntranceScreen`  
  - `LogInScreen`  
  - `RoundScreen`  
  - `FinalRoundScreen`  
  - `FinalScreen`  
- **`gui.py`** – Defines the `MainWindow` class, which manages the application window and starts the program.  

## Requirements  
To run this project, you need **PySide2**. Install it using:  
```sh
pip install PySide2
