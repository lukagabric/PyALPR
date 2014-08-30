import os, shlex, subprocess

if __name__=="__main__":
    webcam_command = "fswebcam -r 640x480 --no-banner alpr.jpg"
    os.system(webcam_command)

    alpr_command = "alpr -c eu -t hr -n 300 -j alpr.jpg"
    alpr_command_args = shlex.split(alpr_command)

    alpr_proc = subprocess.Popen(alpr_command_args, stdout=subprocess.PIPE, shell=True)
    (out, err) = alpr_proc.communicate()
    print "program output:", out
