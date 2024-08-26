def read_file(file_name):
    f = open('sampletext.txt')
    print(f.read())
    raise NotImplementedError()
    

def read_file_into_list(file_name):
    f = open('sampletext.txt', 'r')
    print(f.readlines())
    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    f = open('sampletext.txt')
    print(f.readline())
    raise NotImplementedError()


def read_even_numbered_lines(file_name):
    f = open('sampletext.txt', 'r')
    return list(f)[1:2]

    raise NotImplementedError()

def read_file_in_reverse(file_name):
    for line in reversed(list(open('sampletext.txt'))):
        print(line.rstrip())

    raise NotImplementedError()


def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()