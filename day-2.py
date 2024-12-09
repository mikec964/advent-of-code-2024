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
    found_problem: bool = False  # Any violation makes this True
    bad_levels:int = 0
    for idx, level in enumerate(report):
        if idx == 0:
            previous_level: int = level
            continue
        if idx == 1:
            is_increasing:bool = (level >= previous_level)
        if is_increasing and level <= previous_level:
            # print("Stopped increasing")
            found_problem = True
        if (not is_increasing) and level >= previous_level:
            # print("Stopped decreasing")
            found_problem = True
        # print(abs(level - previous_level), end=None)
        if abs(level - previous_level) > 3 or (abs(level - previous_level) < 1):
            # print("Change is <1 or >3")
            found_problem = True
        if found_problem:
            return False
        else:
            previous_level = level
    return True


def load_ints_from_rows(rows: list[str]) -> list[list[int]]:
    """Parse text lines with numbers, return lists of ints.
    
    Numbers in columns are separated by white space."""

    reports:list[list[int]] = []
    for line in rows:
        items:list[int] = [int(item) 
                            for item in line.split(" ")]
        reports.append(items)
    return reports


def calc_safe_with_dampener(report:list[int], dampener:int = 1) -> bool:
    # If a report fails, loop through removving a level to see if it passes
    is_safe: bool = calc_is_safe(report)
    if is_safe:
        return True
    for skip in range(0, len(report)):
        short_report: list[int] = report[:skip] + report[skip+1:]
        pp(short_report)
    return False


def calc_safe_reports(reports:list[list[int]]) -> int:
    safe_count:int = 0
    for report in reports:
        is_safe:bool = calc_safe_with_dampener(report, 1)
        print(report, is_safe)
        safe_count += 1 if is_safe else 0
    return safe_count


print("======= SAMPLE DATA ========")
report_lines:list[str] = dedent(report_text).splitlines()
reports: list[list[int]] = load_ints_from_rows(report_lines)
# pp(reports)
print(f"{calc_safe_reports(reports)} reports are safe.")
# print(calc_safe_with_dampener(reports[1]))
# print(calc_safe_with_dampener(reports[2]))
# print(calc_safe_with_dampener(reports[3]))
# print(calc_safe_with_dampener(reports[4]))
# print(calc_safe_with_dampener(reports[5]))

# print("======= REAL DEAL ========")
# with open("day-2-input.txt", "r") as f:
#     report_lines = f.readlines()
# reports: list[list[int]] = load_ints_from_rows(report_lines)
# # pp(reports)
# print(f"{calc_safe_reports(reports)} reports are safe.")
