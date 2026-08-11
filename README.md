# Sneak In Zombie

A lightweight 3D zombie-survival game prototype built with **Python** and **Panda3D**.

The core idea is a stealth-oriented open-field zombie survival game where the player must avoid being detected by zombies and can take down a zombie when approaching undetected.

---

## Current Project Status

The project is currently in the **prototype / learning stage**.

The focus so far has been on learning Panda3D and building the basic player, camera, movement, and animation systems.

### Initial State
![Sneak In Zombie Gameplay](game_assets\initial_stages\Character.gif)
### Implemented

- Panda3D project setup
- Python virtual environment
- Basic 3D scene
- Ground
- Third-person camera
- Camera follows the player
- Human 3D player character
- Rigged character loaded as a Panda3D `Actor`
- Directional-arrow keyboard controls
- Key-state dictionary for controls
- Smooth player movement using delta time
- Walking animation
- Run animation available in the character asset
- Basic animation state handling using `isWalking`
- Player orientation adjustment

### Current Character Animations

The current character asset contains:

```text
Run
Walk