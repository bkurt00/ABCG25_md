# ABCG25_md

This repository contains input files and utility scripts used in molecular docking and MM/PBSA analyses of StABCG25 models.

## 📦 prepare_box.py — Vina Grid Box Generator

The `prepare_box.py` script is used to automatically generate the grid box center and size for each receptor file to be used in AutoDock Vina docking runs.

### 🔧 Functionality

- Scans all `.pdbqt` files in a specified directory
- Extracts atomic coordinates (x, y, z) of each receptor
- Calculates:
  - `center_x`, `center_y`, `center_z` = geometric center
  - `size_x`, `size_y`, `size_z` = box dimensions
- Writes AutoDock Vina command lines for each receptor into a `.txt` file

### 🚀 Example Output

