import json, shlex, subprocess

if __name__=="__main__":
    webcam_command = "fswebcam -r 640x480 -S 20 --no-banner --quiet alpr.jpg"
    webcam_command_args = shlex.split(webcam_command)

    webcam_proc = subprocess.Popen(webcam_command_args, stdout=subprocess.PIPE)
    webcam_proc.communicate()

    alpr_command = "alpr -c eu -t hr -n 300 -j alpr.jpg"
    alpr_command_args = shlex.split(alpr_command)

    alpr_proc = subprocess.Popen(alpr_command_args, stdout=subprocess.PIPE)
    (alpr_out, alpr_err) = alpr_proc.communicate()

    print(alpr_out)

    alpr_json = json.loads(alpr_out)
    results = alpr_json["results"]

    print "Total results: %d" % len(results)

    order = 0
    for result in results:
        matches_template = result["matches_template"]
        if matches_template == 1:
            plate = result["plate"]
            order += 1
            print "Plate {0:d}: {1:s}".format(order, plate)

    print "------------"