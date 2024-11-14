# Miles to Kilometer Converter

This is a simple graphical user interface (GUI) application built with Python's `tkinter` library. It allows users to input a distance in miles and convert it to kilometers.

## Project Overview

The program opens a window with an input field for miles, a "Calculate" button, and a label displaying the equivalent distance in kilometers. The conversion is based on the formula:

\[
\text{kilometers} = \text{miles} \times 1.60934
\]

### Features

- Input field for entering miles.
- A button to trigger the conversion.
- Display of the conversion result in kilometers.

## Code Structure

The code is structured as follows:

1. **Window Setup**: Initializes the `tkinter` window with padding and dimensions.
2. **Input Field**: An entry box for the user to input the distance in miles.
3. **Labels**: Labels to display text for "Miles", "is equal to", and the result in kilometers.
4. **Conversion Function**: A function, `miles_to_km`, that retrieves the input value, performs the conversion, and updates the result label.
5. **Calculate Button**: A button that triggers the conversion function.
