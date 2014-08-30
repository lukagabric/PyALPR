import os, shlex, subprocess

if __name__=="__main__":
    webcam_command = "fswebcam -r 640x480 -S 20 --no-banner --quiet alpr.jpg"
    webcam_command_args = shlex.split(webcam_command)

    webcam_proc = subprocess.Popen(webcam_command_args, stdout=subprocess.PIPE)
    (webcam_out, webcam_err) = webcam_proc.communicate()

    print "webcam output:", webcam_out

    alpr_command = "alpr -c eu -t hr -n 300 -j alpr.jpg"
    alpr_command_args = shlex.split(alpr_command)

    alpr_proc = subprocess.Popen(alpr_command_args, stdout=subprocess.PIPE)
    (alpr_out, alpr_err) = alpr_proc.communicate()
    print "alpr output:", alpr_out
