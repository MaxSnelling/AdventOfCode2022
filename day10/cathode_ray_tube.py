
def register_check(cycle: int, register: int) -> int:
    """Check if cycle value is valid for adding to the signal
    sum.

    :param cycle: current cycle number
    :param register: current register value
    :return: value to add to signal strength sum
    """
    if cycle % 40 == 20:
        return register * cycle
    return 0


def sum_signal_strengths() -> int:
    """ Sum signal strength at valid cycle values.

    :return: signal strength sum
    """
    signal_sum = 0
    cycle = 1
    register = 1
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            cycle += 1

            if line.startswith("addx"):
                signal_sum += register_check(cycle, register)
                register += int(line.split(" ")[-1])
                cycle += 1

            signal_sum += register_check(cycle, register)
    return signal_sum


def crt_check(crt: list, cycle: int, register: int) -> None:
    """Add output to crt based on cycle and register.

    :param crt: current crt output
    :param cycle: current cycle value
    :param register: current register value
    :return:
    """
    if register <= (cycle % 40) <= register + 2:
        crt.append('#')
    else:
        crt.append('.')


def print_crt(crt: list) -> None:
    """Print crt output to console.

    :param crt: output of crt in a single list
    """
    i = 0
    while i + 40 <= len(crt):
        print(''.join(crt[i:i + 40]))
        i += 40


def generate_crt_output() -> list:
    """Calculate output of crt using cycle
    and register for sprite position.

    :return: output of crt in a single list"""
    crt = []
    cycle = 1
    register = 1
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            crt_check(crt, cycle, register)
            cycle += 1

            if line.startswith("addx"):
                crt_check(crt, cycle, register)
                register += int(line.split(" ")[-1])
                cycle += 1
    return crt


if __name__ == '__main__':
    #  Part 1
    signal_strengths_sum = sum_signal_strengths()
    print(f"Sum of signal strengths: {signal_strengths_sum}")

    #  Part 2
    crt_output = generate_crt_output()
    print_crt(crt_output)



