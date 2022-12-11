"""Day 6 of AoC."""

def find_marker(chars, char_length):
    """Find the first start-of-packet/message marker

    In other words: when do we have a list of unique chars of length ```char_length```?

    Parameters
    ----------
    chars : str
        A message
    char_length : int
        Length of the makrer

    Returns
    -------
    markers: str
        Detected chars that form the first marker
    idx: int
        Nb chars processed before the first makrer is detected
    """
    marker = ''
    idx = -1

    for i, char in enumerate(list(chars)):
        # Stop if our marker is complete
        if len(marker) == char_length:
            idx = i
            break
        # If char is already in marker, remove this char and the chars before
        elif char in marker:
            marker = marker[marker.index(char)+1:]
        # Add the new char
        marker += char

    return marker, idx

def main(file_path):
    """Main script for day 6.

    Parameters
    ----------
    file_path : str
        Path to input file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        chars = file.read()[:-1]

    # Part 1
    packet_marker, packet_idx = find_marker(chars, 4)
    print(f'Part 1: {packet_marker} after character {packet_idx}')

    # Part 2
    msg_marker, msg_idx = find_marker(chars, 14)
    print(f'Part 2: {msg_marker} after character {msg_idx}')

if __name__ == '__main__':
    main('input/day6.txt')
