## Homework_4: NumPy Exercise
Python project using **NumPy**, **Pandas**, and **Matplotlib** to:
- Build a simple **trading strategy**
- Solve an **energy maze** using dynamic programming

## Running_the_tests
python main.py


## Files_included
- `main_HW4.py` – main file  
- `aapl.csv` – input data (AAPL stock prices)  
- `Cumulative_P&L.png` – cumulative profit & loss plot  
- `Trading_Signals.png` – trading signals visualization  
- `Maze_Energy_Map.png` – energy maze visualization  
- `trading_results.csv` – output results  

## Installation_Libraries
- numpy  
- pandas  
- matplotlib  

## Tasks
### Task 1: Trading Strategy
- Execute rule-based buy/sell strategy  
- Unit test and replicate example from PDF  
- Plot cumulative P&L using AAPL data  

### Task 2: Energy Maze
- Solve maze with dynamic programming  
- Unit test example and arbitrary case  
- Compute minimum initial energy  

## Functions
- `trading_strategy(csv_file_name: str)` → signals, positions, account value  
- `min_initial_energy(maze: npt.NDArray[np.int_])` → minimum initial energy
