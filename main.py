import argparse
import itertools

from typing import List


def main(args: argparse.Namespace):
    """
    Main method.

    Parameters
    ----------
    args : argparse.Namespace
        Command line arguments.
    """
    # convert arguments.
    target: List[str] = list(args.value)
    abbreviation: int = args.abbreviation if args.abbreviation else -1
    output_path: str = args.output if args.output else ''

    ret: List[str] = []

    # anagram iteration.
    if (abbreviation > 0):
        for pattern in itertools.permutations(target):
            pattern = ''.join(pattern)[:abbreviation]
            if not pattern in ret:
                ret.append(pattern)
    else:
        for pattern in itertools.permutations(target):
            ret.append(''.join(pattern))

    # output file or stdout.
    if output_path:
        with open(output_path, 'w') as f:
            f.write('\n'.join(ret))
    else:
        for s in ret:
            print(s)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Output all patterns of anagram.')
    parser.add_argument('value', type=str, help='Input string')
    parser.add_argument('--abbreviation', '-a', type=int, help='Output string length from begin (optional)')
    parser.add_argument('--output', '-o', type=str, help='Output file path (optional)')
    args = parser.parse_args()
    main(args)
