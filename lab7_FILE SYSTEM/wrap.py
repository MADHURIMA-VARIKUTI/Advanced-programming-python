import sys

def wrap_lines(filename, width):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        wrapped_lines = []
        for line in lines:
            words = line.split()
            wrapped_line = ""
            line_length = 0

            for word in words:
                if line_length + len(word) <= width:
                    wrapped_line += word + " "
                    line_length += len(word) + 1
                else:
                    wrapped_lines.append(wrapped_line.strip())
                    wrapped_line = word + " "
                    line_length = len(word) + 1

            if wrapped_line:
                wrapped_lines.append(wrapped_line.strip())

        with open(filename, "w") as file:
            file.writelines("\n".join(wrapped_lines))

        print(f"Lines in '{filename}' wrapped to a maximum width of {width}.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wrap.py <filename> <width>")
    else:
        filename = sys.argv[1]
        width = int(sys.argv[2])
        wrap_lines(filename, width)

# PS D:\210953314\lab7> python "D:\\210953314\\lab7\\wrap.py" "D:\\210953314\\lab7\\wrap.txt" 30
# Lines in 'D:\\210953314\\lab7\\wrap.txt' wrapped to a maximum width of 30.
