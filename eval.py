import subprocess

def run_job(cmd):
    ret = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return ret.stdout.decode(('UTF-8'))
    
if __name__ == '__main__':
    # Compile
    run_job("gcc main.c")

    # Run
    msg = run_job("./a.out").rstrip()
    if msg == "Hello World!":
        print("Ok!")
    else:
        print("Error. The correct answer is `Hello World!`, but your outupt is:")
        print("```")
        print(msg)
        print("```")
