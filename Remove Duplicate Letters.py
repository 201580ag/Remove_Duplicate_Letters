input_txt = input("파일 경로를 입력해 주세요.: ")

with open('input.txt', 'r') as f:
    lines = f.readlines()

unique_lines = list(set([line.strip() for line in lines]))

with open('output.txt', 'w') as f:
    for line in unique_lines:
        f.write(line + '\n')
