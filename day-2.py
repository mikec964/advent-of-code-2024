from pprint import pp
from textwrap import dedent


report_text:str = """\
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    """

def calc_is_safe(report:list[int]) -> bool:
    is_safe: bool = True  # Any violation makes this False
    for idx, level in enumerate(report):
        if idx == 0:
            previous_level: int = level
            continue
        if idx == 1:
            is_increasing:bool = (level >= previous_level)
        # if idx >= 1:
        #     print(previous_level, level)
        if is_increasing and level <= previous_level:
            # print("Stopped increasing")
            is_safe = False
            break
        if (not is_increasing) and level >= previous_level:
            # print("Stopped decreasing")
            is_safe = False
            break
        # print(abs(level - previous_level), end=None)
        if abs(level - previous_level) > 3 or (abs(level - previous_level) < 1):
            # print("Change is <1 or >3")
            is_safe = False
            break
        previous_level = level
    return is_safe


def load_int_by_row(filename = "day-2-input.txt") -> list[list[int]]:
    """Read a file with n numbers per row, return a list per row.
    
    Columns are separated by white space."""

    reports:list[list[int]] = []
    with open(filename, "r") as f:
        for line in f:
            items:list[int] = [int(item) 
                                for item in line.split(" ")]
            reports.append(items)
    return reports


reports: list[list[int]] = load_int_by_row()
pp(reports)
safe_count:int = 0
for report in reports:
    is_safe:bool = calc_is_safe(report)
    print(report, is_safe)
    safe_count += 1 if is_safe else 0
print(f"{safe_count} reports are safe.")
