from zatt.client import DistributedDict
from flask import Flask, render_template, request, send_file, redirect
from subprocess import check_output, call

# from os import chdir as cd
# from re import match

import os
import webbrowser

def row_major(alist, sublen):      
  return [alist[i:i+sublen] for i in range(0, len(alist), sublen)]

def test_1_append(port):
    html_file = open('test_1.html','w')
    message_up = """
<html>
<head>
    <title>Converter</title>
    <link rel=stylesheet type=text/css href="{{ url_for('static', filename='bootstrap.min.css') }}">
    <script src="/static/js/jquery.min.js"></script>
    <script src="/static/js/ytdl.js"></script>
</head>
<body>
    """
    message_down = """
</body>
</html>
    """
    html_file.write(message_up)
    html_file.write('[Append Test]')
    d = DistributedDict('127.0.0.1', port)
    d['adams'] = 'the hitchhiker guide'
    html_file.write("<p>[1] d['adams'] =" + str(d['adams']) + "</p>")
    del d
    d = DistributedDict('127.0.0.1', port)
    d['adams'] = 'the hitchhiker guide'
    html_file.write("<p>[2] d['adams'] =" + str(d['adams']) + "</p>")
    html_file.write(message_down)
    webbrowser.open_new_tab('test_1.html')

def test_2_delete(port):
    html_file = open('test_2.html','w')
    message_up = """
<html>
<head>
    <title>Converter</title>
    <link rel=stylesheet type=text/css href="{{ url_for('static', filename='bootstrap.min.css') }}">
    <script src="/static/js/jquery.min.js"></script>
    <script src="/static/js/ytdl.js"></script>
</head>
<body>
    """
    message_down = """
</body>
</html>
    """
    html_file.write(message_up)
    html_file.write('[Delete Test]')
    d = DistributedDict('127.0.0.1', port)
    d['adams'] = 'the hitchhiker guide'
    html_file.write("<p>[1] d =" + str(d) + "dengan d['adams'] =" + str(d['adams']) + "</p>")
    del d['adams']
    html_file.write("<p>[2] Maka, d =" + str(d) + "</p>")
    html_file.write(message_down)
    webbrowser.open_new_tab('test_2.html')
        
def test_3_read_from_different_client(port):
    html_file = open('test_3.html','w')
    message_up = """
<html>
<head>
    <title>Converter</title>
    <link rel=stylesheet type=text/css href="{{ url_for('static', filename='bootstrap.min.css') }}">
    <script src="/static/js/jquery.min.js"></script>
    <script src="/static/js/ytdl.js"></script>
</head>
<body>
    """
    message_down = """
</body>
</html>
    """
    html_file.write(message_up)
    html_file.write('[Read from Different Client]')
    d = DistributedDict('127.0.0.1', port)
    d['adams'] = 'the hitchhiker guide'
    html_file.write("<p>[1] d['adams'] =" + str(d['adams']) + "pada port: " + str(port) + "</p>")
    del d
    d = DistributedDict('127.0.0.1', 9102)
    d['adams'] = 'the hitchhiker guide'
    html_file.write("<p>[2] d['adams'] =" + str(d['adams']) + "pada port: 9102" + "</p>")
    html_file.write(message_down)
    webbrowser.open_new_tab('test_3.html')

def test_5_diagnostic(port):
    html_file = open('test_7.html','w')
    message_up = """
<html>
<head>
    <title>Converter</title>
    <link rel=stylesheet type=text/css href="{{ url_for('static', filename='bootstrap.min.css') }}">
    <script src="/static/js/jquery.min.js"></script>
    <script src="/static/js/ytdl.js"></script>
</head>
<body>
    """
    message_down = """
</body>
</html>
    """
    html_file.write(message_up)
    html_file.write('[Diagnostic Test]')
    d = DistributedDict('127.0.0.1', port)
    diagnostics = d.diagnostic
    html_file.write("\n<p>[1] Server memberi vote untuk port: " + str(diagnostics['persist']['votedFor']) + "</p>")
    html_file.write("<p>[2] CurrentTerm: " + str(diagnostics['persist']['currentTerm']) + "</p>")
    html_file.write("<p>[3] Leader Saat ini: " + str(diagnostics['volatile']['leaderId']) + "</p>")
    html_file.write("<p>[4] List Cluster: " + str(diagnostics['volatile']['cluster']) + "</p>")
    html_file.write("\n<p>[5] Full Diagnostic: " + str(diagnostics) + "</p>")
    html_file.write("\n<p>[6] d: " + str(d) + "</p>")
    html_file.write(message_down)
    webbrowser.open_new_tab('test_7.html')

def test_6_export_file(port):
    html_file = open('D:/Desktop/zatt/zatt_cluster/templates/test_6.html','w')
    message_up = """
<html>
<head>
    <title>Zatt</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" \
    integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <script src="/static/js/jquery.min.js"></script>
    <script src="/static/js/ytdl.js"></script>
</head>
<body>
    <div class="container">
    <div class="title">
        <h1><strong>Export File</strong></h1>
    </div>
    """
    message_down = """
            <button id="submit" class="btn btn-primary" type="submit" form="dlform" value="test8">Send</button>
            </div>
        </form>
    </div>
</body>
</html>
    """
    input = """
        <form id="dlform" name="dlform" action="/test6" method="post">
            <div class="form-group">
    """
    html_file.write(message_up)
    d = DistributedDict('127.0.0.1', port)
    html_file.write(input)
    html_file.write("<label>[1] d = " + str(d) + "</label><br>")
    html_file.write("<label>[2] File yang ingin disave</label>\
                     <input class='form-control' id='files' name='files' type='text'>\
                 </div>\
                 <div class='form-group'>\
                     <label>Port </label>\
                     <input class='form-control' type='number' id='port' name='port' value='"+ str(port) +"'><br>")
    html_file.write(message_down)
    webbrowser.open_new_tab('/test_6')

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/test_4")
def test_4():
    return render_template("test_4.html")

@app.route("/test4", methods=['POST'])
def test_4_export_file():
    url = request.form.get('url', type=str)
    file_ke = request.form.get('files', type=str)
    port_ke = request.form.get('port', type=int)
    html_file = open('D:/Desktop/zatt/zatt_cluster/templates/result.html','w')
    message_up = """
<html>
<head>
    <title>Zatt</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" \
    integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <script src="/static/js/jquery.min.js"></script>
    <script src="/static/js/ytdl.js"></script>
</head>
<body>
    <div class="container">
    <div class="title">
        <h1><strong>Penyimpanan Sukses</strong></h1>
    </div>
    """
    message_down = """
            </div>
        </form>
    </div>
</body>
</html>
    """
    input = """
        <form id="dlform" name="dlform" action="/test8" method="post">
            <div class="form-group">
                <label for="files">File:</label>
    """
    d = DistributedDict('127.0.0.1', port_ke)
    opened = open(file_ke,'r')
    d[file_ke] = opened.read()
    html_file.write(message_up)
    html_file.write(input)
    html_file.write("<p>Isi File [" + file_ke + "] = " + d[file_ke] + "</p><p>Sukses Disimpan.</p>")
    html_file.write("<p>d = " + str(d) + ".")
    opened.close()
    webbrowser.open_new_tab('D:/Desktop/zatt/zatt_cluster/templates/result.html')
    return render_template("index.html")

@app.route("/test6", methods=['POST'])
def test_8_input_file():
    url = request.form.get('url', type=str)
    file_ke = request.form.get('files', type=str)
    port_ke = request.form.get('port', type=int)

    d = DistributedDict('127.0.0.1', port_ke)
    if ".txt" not in file_ke:
        open('D:/Desktop/zatt/zatt_cluster/export/'+ file_ke + '.txt', 'w').write(str(d[file_ke]))
    webbrowser.open_new_tab('D:/Desktop/zatt/zatt_cluster/export/'+ file_ke + '.txt')
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
        return render_template("test_4.html")
        #test_4_input_file(port_ke)
    elif (test_ke == "test_5"):
            test_5_diagnostic(port_ke)
    elif (test_ke == "test_6"):
            test_6_export_file(port_ke)
            return render_template("test_6.html")
    else:
        return render_template("failed.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0")