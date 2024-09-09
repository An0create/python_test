def read_file(file_name):
    with open(file_name, 'r') as f:
        contents = f.read()
        print(contents)
        return contents
    
    raise NotImplementedError()


def read_file_into_list(file_name):
    with open(file_name, 'r') as f:
        content = f.readlines()
        return content

    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    with open(output_filename, 'w') as f:
        f.write(file_contents.split('\n')[0])


def read_even_numbered_lines(file_name):
    l = []
    with open(file_name, 'r') as file:
        s = file.readlines()
        c = 1
        for i in s:
            if(c%2 == 0):
                l.append(i)
            c += 1
    return l

    raise NotImplementedError()

def read_file_in_reverse(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        rev_lines = list(reversed(lines))
        print(rev_lines)
        return rev_lines

    raise NotImplementedError()


def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")

if __name__ == "__main__":
    main()