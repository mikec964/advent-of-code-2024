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


def load_ints_from_rows(rows: list[str]) -> list[list[int]]:
    """Parse strings with white space separated ints, return lists of ints."""
    reports:list[list[int]] = []
    for line in rows:
        items:list[int] = [int(item) 
                            for item in line.split(" ")]
        reports.append(items)
    return reports


def calc_is_safe(report:list[int]) -> bool:
    """Return true if numbers in list follow rules.
    
    All numbers must be increasing or decreasing.
    """
    is_increasing: bool = False
    previous_level: int = report[0]
    for idx, level in enumerate(report):
        if idx == 0:
            continue
        if level == previous_level or abs(level - previous_level) > 3:
            return False
        if idx == 1:
            is_increasing = (level > previous_level)
        if is_increasing and level < previous_level:
            return False
        if (not is_increasing) and level > previous_level:
            return False
        previous_level = level
    return True


def calc_safe_with_dampener(report:list[int], dampener:int = 1) -> tuple[bool, list[int]]:
    # If a report fails, loop through removing a level to see if it passes
    is_safe: bool = calc_is_safe(report)
    if is_safe:
        return (True, report)
    # We start the loop with is_safe == False
    for skip in range(0, len(report)):
        short_report: list[int] = report[:skip] + report[skip+dampener:]
        # pp(short_report)
        if calc_is_safe(short_report):
            return (True, short_report)
    return (False, [])


def calc_safe_report_count(reports:list[list[int]]) -> int:
    safe_count:int = 0
    for report in reports:
        is_safe, solution = calc_safe_with_dampener(report)
        safe_count += 1 if is_safe else 0
        print(report, solution, is_safe, safe_count)
    return safe_count


print("======= SAMPLE DATA ========")
report_lines:list[str] = dedent(report_text).splitlines()
reports: list[list[int]] = load_ints_from_rows(report_lines)
# pp(reports)
print(f"{calc_safe_report_count(reports)} reports are safe.")

print("======= REAL DEAL ========")
with open("day-2-input.txt", "r") as f:
    report_lines = f.readlines()
reports: list[list[int]] = load_ints_from_rows(report_lines)
# pp(reports)
print(f"{calc_safe_report_count(reports)} reports are safe.")
