import numpy as np
from IPython.display import Markdown, display

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def visualise_code(filename):
    
    try:
        f=open(filename)
        # print(f.read())
        lines=f.readlines()

        print(color.YELLOW + "Visualising "+ color.END + color.UNDERLINE + str(filename) + color.END)

        for i in range(0,len(lines)):
            print(lines[i])
    except:
        # no file so it must be edited code
        print(color.YELLOW + "Visualising " + color.END + color.UNDERLINE + "edited_code" + color.END)
        print(filename)
    print(color.PURPLE + "End Visualisation " +color.END)
    print("\n")

def detect_indentation(line):
    return len(line) - len(line.lstrip())

def calc_nested_loops(indentation_array):
    indentation_array = np.array(indentation_array)
    max_indentation = 0
    different_indentation = []
    for i in range(len(indentation_array)):
        indentation = int(indentation_array[i,1])
        if indentation not in different_indentation: different_indentation += [indentation]

    nested_loop_count = len(different_indentation)
    return nested_loop_count

def detect_loops(filename, loop):
    edited_code = ""
    total_loop_count = 0  
    indentation_array = []
    counter = 0

    f = open(filename)
    lines=f.readlines()
    for i in range(len(lines)):
        edited_code += lines[i]
        if i > (len(lines) -2):
            break
        if lines[i].find(loop) != -1 and (lines[i].find("#") > lines[i].find(loop) or lines[i].find("#") == -1):  #this will add a line after while loop

            indentation = detect_indentation(lines[i+1])*" "
            edited_code += ("{indentation}counter{counter_number} +=1\n".format(indentation=indentation,counter_number=counter))


        if lines[i+1].find(loop) != -1 and (lines[i+1].find("#") > lines[i+1].find(loop) or lines[i+1].find("#") == -1):  #this will add a line before while loop

            total_loop_count += 1
            counter += 1
            indentation = detect_indentation(lines[i+1])*" "
            indentation_array += [[indentation, len(indentation)]]
            edited_code += ("{indentation}counter{counter_number} =0\n".format(indentation=indentation,counter_number=counter))
    
    # after added all lines
    if total_loop_count > 0:
        edited_code += ("\n")
        for j in range(1,counter+1):
            edited_code += ("print('whileloop{j} ran : ' + str(counter{j}) + ' times')\n".format(j=j))

    nested_loop_count = calc_nested_loops(indentation_array)
    edited_code += ("print('nested loop = ' + str(nested_loop_count) + ' times')\n")

    return edited_code, total_loop_count, nested_loop_count

def runcode(codelines):
    # need to join all the lines into 1 string for exec() to work
    long_string = ("")
    for line in codelines:
        long_string += line
    try:
        exec(long_string)
    except:
        printmd("**There is an error, codelines cannot be executed**")

### MAIN ###


if __name__ == "__main__":
    filelocation = "SCA/while_loop_nested.py"

    loop_name = "for"  #input while or for

    visualise_code(filelocation)
    edited_code, total_loop_count, nested_loop_count = detect_loops(filelocation, loop_name)

    visualise_code(edited_code)
    runcode(edited_code)

    print(color.RED + "\nSummary" + color.END)
    print("max nested loop = {count}".format(count=nested_loop_count))
    print("total {name} loop count = {count}".format(count=total_loop_count, name=loop_name))

