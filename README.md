# maya-ctrl-combiner

This is a simple Python script for Autodesk Maya that allows you to **combine two NURBS curves** into a single controller shape. It's useful when creating custom rig controls built from multiple curve elements.

## What it does

- Takes two selected NURBS curve transform nodes.
- Duplicates both curves to preserve the originals.
- Moves the shape nodes of the second curve under the first.
- Deletes the leftover transform.
- Renames the new controller with a `_combined` suffix.

## How to use

1. Open Maya and select the two NURBS curves you want to combine.
2. Open the Script Editor and paste the script into the Python tab.
3. Run the script.
4. A new combined curve will be created and named like: `yourCurve_combined`.

## 🛠 Example use case

You're designing a control for a rig and need to combine a circle and a square to form a custom shape — this script merges them into one clean transform for easier rigging and control setup.

## File

- `combine_nurbs_curves.py`: the main script.

---

Let me know if you want to expand this into a proper Maya tool with UI or shelf button support!

