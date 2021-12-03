import subprocess
from pathlib import Path


def run_job(cmd):
    ret = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return ret.stdout.decode(('UTF-8'))

def print_codeblock(s):
    print("```")
    print(s)
    print("```")

if __name__ == '__main__':
    print("## Run `gcc main.c`")

    msg = run_job("gcc main.c")
    if Path("a.out").exists():
        print("Compiled successfully.")
    else:
        print_codeblock(msg)
        print("Error: Failed to compile")

    print(f"## Run `./a.out`")
    msg = run_job('./a.out').rstrip()
    print_codeblock(msg)
    
    print("## Judge")
    if msg == 'Hello World!':
        print("Ok!")
    else:
        print(f"Error: `{msg}` is not `Hello World!`.")
    
