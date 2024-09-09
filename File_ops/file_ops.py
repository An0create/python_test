def read_file(file_name):
    with open(file_name, 'r') as f:
        contents = f.read()
        print(contents)
        return contents

def read_file_into_list(file_name):
    with open(file_name, 'r') as f:
        contents = f.readlines()
        return contents

def write_first_line_to_file(file_contents, output_filename):
    with open(output_filename, 'w') as f:
        f.write(file_contents.split('\n')[0])
        

def read_even_numbered_lines(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return [line.strip() for idx, line in enumerate(lines) if idx % 2 == 1]

def read_file_in_reverse(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        rev_lines = list(reversed(lines))
        print(rev_lines)
        return rev_lines

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")