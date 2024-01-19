from decimal import Decimal, getcontext
import time
import colorama

# Set the precision for calculations
getcontext().prec = 20000

# Define colors
colors = [
    colorama.Fore.RED,
    colorama.Fore.LIGHTYELLOW_EX,
    colorama.Fore.LIGHTGREEN_EX,
    colorama.Fore.LIGHTBLUE_EX,
    colorama.Fore.MAGENTA,
    colorama.Fore.LIGHTCYAN_EX,
]

def calculate_and_print_pi():
    pi = Decimal(0)
    color_index = 0  # Index to iterate through colors
    for k in range(20000):
        pi += (Decimal(1) / 16 ** k) * (
            Decimal(4) / (8 * k + 1) - Decimal(2) / (8 * k + 4) - Decimal(1) / (8 * k + 5) - Decimal(1) / (8 * k + 6)
        )

        temp_pi = str(pi * Decimal(10 ** 20000))
        digit = int(temp_pi.split('.')[1][k])

        color = colors[color_index]  # Use the current color
        print(color + str(digit), end='', flush=True)
        time.sleep(0.001)  # Adjust the delay to control the printing speed

        color_index = (color_index + 1) % len(colors)  # Move to the next color

    return pi

def main():
    colorama.init()

    print("Pi calculated so far: 3.", end="")
    pi = calculate_and_print_pi()

    print("\nFinal Pi generated up to 20,000 decimal places:")
    print(pi)

    colorama.deinit()

if __name__ == "__main__":
    main()
