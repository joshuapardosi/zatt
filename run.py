#!/usr/bin/python2

from flask import Flask, render_template, request, send_file, redirect
from subprocess import check_output, call

from zatt_cluster import client_side
# from os import chdir as cd
# from re import match
import os

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/send", methods=['POST'])
def download():
    url = request.form.get('url', type=str)
    test_ke = request.form.get('test', type=str)
    port_ke = request.form.get('port', type=int)

    if (test_ke == "test_1"):
        test_1_append(port_ke)
    elif (test_ke == "test_2"):
        test_2_delete(port_ke)
    elif (test_ke == "test_3"):
        if(port_ke != 9102):
            test_3_read_from_different_client(port_ke)
    elif (test_ke == "test_4"):
            test_4_add_server(port_ke)
    elif (test_ke == "test_5"):
            test_5_remove_server(port_ke)
    elif (test_ke == "test_6"):
            test_6_input_file(port_ke)
    elif (test_ke == "test_7"):
            test_7_diagnostic(port_ke)
    elif (test_ke == "test_8"):
            test_8_export_file(port_ke)
    elif (test_ke == "test_9"):
        if(port_ke != 9102):
            test_9_compacted_log_replication(port_ke)
    else:
        return render_template("failed.html")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0")