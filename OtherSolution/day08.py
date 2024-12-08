# Python Code to Solve the Puzzle


def read_map(input_lines):
    antenna_positions = {}  # frequency: list of positions
    max_rows = len(input_lines)
    max_cols = len(input_lines[0]) if max_rows > 0 else 0

    for y, line in enumerate(input_lines):
        for x, ch in enumerate(line):
            if ch != ".":
                if ch not in antenna_positions:
                    antenna_positions[ch] = []
                antenna_positions[ch].append((x, y))

    return antenna_positions, max_cols, max_rows


def calculate_antinodes(antenna_positions, max_cols, max_rows):
    antinode_positions = set()

    for freq, positions in antenna_positions.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                A = positions[i]
                B = positions[j]

                # Calculate Antinode Positions
                P1 = (2 * A[0] - B[0], 2 * A[1] - B[1])
                P2 = (2 * B[0] - A[0], 2 * B[1] - A[1])

                # Check if P1 is within map bounds
                if 0 <= P1[0] < max_cols and 0 <= P1[1] < max_rows:
                    antinode_positions.add(P1)

                # Check if P2 is within map bounds
                if 0 <= P2[0] < max_cols and 0 <= P2[1] < max_rows:
                    antinode_positions.add(P2)

    return antinode_positions


def main():
    # Read the puzzle input
    input_lines = []
    try:
        while True:
            line = input()
            input_lines.append(line)
    except EOFError:
        pass  # No more input

    antenna_positions, max_cols, max_rows = read_map(input_lines)
    antinode_positions = calculate_antinodes(antenna_positions, max_cols, max_rows)
    total_antinodes = len(antinode_positions)

    print(f"Total unique antinode locations within bounds: {total_antinodes}")


if __name__ == "__main__":
    main()
