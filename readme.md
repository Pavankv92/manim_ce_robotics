# ManimCE Robotics

This repository is based on [Manim Community Edition (ManimCE)](https://www.manim.community/), and is primarily used for creating animations for robotics applications. It provides example scenes and utilities to help visualize concepts in robotics using Manim.

---

## How to Use Manim Sideview in VS Code

### 1. Check if Manim is in your PATH

1. Open the integrated terminal in VS Code (press <kbd>Ctrl</kbd> + <kbd>`</kbd>).
2. Type:
   ```
   manim --version
   ```
   If you see the version, Manim is in your PATH.

### 2. Find the Correct Manim Path

1. In your terminal, run:
   ```
   which manim
   ```
   This will output the correct path to your Manim executable (e.g., `/path/to/your/venv/bin/manim`).

### 3. Update the Manim Sideview Settings

1. Open VS Code settings (<kbd>⌘</kbd> + <kbd>,</kbd> on Mac).
2. Search for `manim-sideview`.
3. Find the setting for **"manim-sideview: Default manim Path"** (or similar).
4. Paste the path you got from the `which manim` command.
5. Restart VS Code (or reload the window) to ensure the extension picks up the new path.



### 4. Useful Manim Sideview Commands

- **Run the current scene:**  
  Press <kbd>Ctrl</kbd> + <kbd>`</kbd> first, then press <kbd>r</kbd>.

- **Change the scene:**  
  Press <kbd>Ctrl</kbd> + <kbd>`</kbd> first, then press <kbd>c</kbd>.

---
