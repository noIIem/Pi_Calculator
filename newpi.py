from decimal import Decimal, getcontext
import colorama
from colorama import Fore, Style

colorama.init()  # Initialize colorama for cross-platform colored output

# Define RGB values for custom colors
custom_colors = [
    (255, 0, 0),    # RED
    (255, 165, 0),  # ORANGE
    (255, 255, 0),  # YELLOW
    (0, 255, 0),    # LIME
    (0, 0, 255),    # BLUE
    (128, 0, 128),  # PURPLE
    (0, 128, 128),  # TEAL
    (255, 192, 203),# PINK
    (255, 99, 71),  # TOMATO
    (255, 69, 0),   # RED-ORANGE
    (0, 128, 0),    # GREEN
    (255, 0, 255),  # MAGENTA
    (173, 216, 230),# LIGHT BLUE
    (255, 255, 255),# WHITE
    (128, 128, 0),  # OLIVE
    (0, 128, 128),  # BLUE-GREEN
    (255, 69, 0),   # RED-ORANGE
    (255, 215, 0),  # GOLD
    (218, 112, 214),# ORCHID
    (0, 255, 255),  # CYAN
    (0, 255, 0)     # LIME
]

def rgb_to_ansi(r, g, b):
    # Convert RGB color values to ANSI escape sequences
    return f"\033[38;2;{r};{g};{b}m"

def calculate_pi():
    getcontext().prec = 20000  # Set precision for calculations

    pi = Decimal(0)
    for k in range(20000):
        pi += (Decimal(1) / 16 ** k) * (
            Decimal(4) / (8 * k + 1) - Decimal(2) / (8 * k + 4) - Decimal(1) / (8 * k + 5) - Decimal(1) / (8 * k + 6)
        )

        temp_pi = str(pi * Decimal(10 ** 20000))
        digit = int(temp_pi.split('.')[1][k])

        # Select color for the digit based on the index of the color list
        color_index = k % len(custom_colors)
        color = custom_colors[color_index]
        
        # Convert RGB color values to ANSI escape sequences for color display
        ansi_color = rgb_to_ansi(*color)
        print(f"{ansi_color}{digit}", end='', flush=True)
    
    print(Style.RESET_ALL)  # Reset color to default after printing all digits

    return pi

if __name__ == "__main__":
    print("Pi calculated so far: 3.", end="")
    pi = calculate_pi()

    print("\nFinal Pi generated up to 20,000 decimal places:")
    print(pi)
