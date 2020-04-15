import pdb

def get_input():
    re_input = []
    set_count = 0
    while True:
        temp_data = input()
        if temp_data!="":
            [m, n] = temp_data.split()
            m, n = int(m), int(n)
            temp_data = input()
            out = []
            for i in temp_data.split():
                out.append(int(i))
            temp_data= input()
            for i in temp_data.split():
                out.append(int(i))
            out = list(set(out))
            out = sorted(out)
            out = ' '.join([str(i) for i in out])
            print(out)
        else:
            break
    return re_input

def get_output(input):
    for temp in input:
        temp_data = list(temp)
        temp_data = sorted(temp_data)
        out = ' '.join(temp_data)
        print(out)
    return


if __name__=='__main__':
    code_input = get_input()
    # get_output(code_input)
