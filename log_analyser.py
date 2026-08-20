def read_log(filename):
    # Open the file and return a list of lines (stripped of whitespace)
    lines = []
    try:
        with open (filename, "r") as file:
            for line in file:
                lines.append(line.rstrip())
            return lines
    except FileNotFoundError:
        print("File not found")
        return []

    # Handle FileNotFoundError — print a message and return an empty list

def analyse_log(lines):
    total_lines = 0
    error_count = 0
    warning_count = 0
    info_count = 0
    error_lines = []
    # Loop through every line
    for line in lines:
        total_lines += 1
        if "ERROR" in line:
            error_count += 1
            error_lines.append(line)
        elif "WARNING" in line:
            warning_count += 1
        elif "INFO" in line:
            info_count += 1
    return total_lines, error_count, warning_count,info_count, error_lines
    # Count: total_lines, error_count, warning_count, info_count
    # Build a list of error lines.
    # Return all five values

def write_report(filename, total, errors, warnings, infos, error_lines):
    # Write a summary report to a text file
    with open (filename, "w") as file:
        file.write("Log Summary Report \n")
        file.write(f"Total lines: {total} \n")
        file.write(f"Errors: {errors} \n")
        file.write(f"Warnings: {warnings} \n")
        file.write(f"info: {infos} \n")

        file.write("Error lines: \n")
        for line in error_lines:
            file.write(f"Error: {line} \n")
    # Include all counts and list every error line

def main():
    # Call read_log to get the lines
    lines = read_log("system.log")

    # Call analyse_log to get the counts
    total_lines, error_count, warning_count, info_count, error_lines = analyse_log(lines)

    # Print a summary to the console
    print(f"Total lines:{total_lines}")
    print(f"Error_count:{error_count}")
    print(f"warning_count:{warning_count}")
    print(f"info count:{info_count}")


    # Call write_report to save it
    write_report("app_log.txt",total=total_lines, errors= error_count, warnings=warning_count, infos=info_count, error_lines=error_lines)



if __name__ == "__main__":
    main()