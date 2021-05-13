import os


def write_file():
    file = open("test.php", "r")
    line_list = file.readlines()
    note = open("demo2.php", "a")

    for line in line_list:
        note.write(line)
    print(note.line_buffering)
    file.close()
    note.close()
    os.remove("demo2.php")


if __name__ == '__main__':
    test = write_file()
