from zatt.client import DistributedDict

def test_1_append(port):
    print('[Append Test]')
    d = DistributedDict('127.0.0.1', port)
    d['adams'] = 'the hitchhiker guide'
    print ("[1] d['adams'] =", d['adams'])
    del d
    d = DistributedDict('127.0.0.1', port)
    d['adams'] = 'the hitchhiker guide'
    print ("[2] d['adams'] =", d['adams'])

def test_2_delete(port):
    print('[Delete Test]')
    d = DistributedDict('127.0.0.1', port)
    d['adams'] = 'the hitchhiker guide'
    print ("[1] d =", d, "dengan d['adams'] =", d['adams'])
    del d['adams']
    print ("[2] Maka, d =", d)
        
def test_3_read_from_different_client(port):
    print('[Read from Different Client]')
    d = DistributedDict('127.0.0.1', port)
    d['adams'] = 'the hitchhiker guide'
    print ("[1] d['adams'] =", d['adams'], "pada port:", port)
    del d
    d = DistributedDict('127.0.0.1', 9102)
    d['adams'] = 'the hitchhiker guide'
    print ("[2] d['adams'] =", d['adams'], "pada port: 9102")

def test_4_add_server(port):
    print('[Add New Server]')
    d = DistributedDict('127.0.0.1', port)
    d['test'] = 0
    port_baru = int(input("[1] Pastikan server telah dijalankan." \
                          " Inputkan Port Server Baru = "))
    d.config_cluster('add', '127.0.0.1', port_baru)
    del d
    d = DistributedDict('127.0.0.1', port_baru)
    print ("[2] List baru Cluster=", d.diagnostic['volatile']['cluster']) 
    print ("[3] d[test] =", d['test'])

def test_5_remove_server(port):
    print('[Remove Server]')
    d = DistributedDict('127.0.0.1', port)
    port_del = int(input("[1] Inputkan port server yang mau dihapus = "))
    d.config_cluster('delete', '127.0.0.1', port_del)
    print ("[2] Port yang tersisa:", d.diagnostic['volatile']['cluster'])
    
def test_6_input_file(port):
    print('[Input File]')
    d = DistributedDict('127.0.0.1', port)
    path = input("[1] Open File. Path = ")
    opened = open(path,'r')
    d[path] = opened.read()
    print ("Isi File [", path, "] =", d[path], "\n[2] Sukses Disimpan.")
    print (d)
    opened.close()

def test_7_diagnostic(port):
    print('[Diagnostic Test]')
    d = DistributedDict('127.0.0.1', port)
    diagnostics = d.diagnostic
    print("\n[1] Server memberi vote untuk port:", diagnostics['persist']['votedFor'])
    print("[2] CurrentTerm:", diagnostics['persist']['currentTerm'])
    print("[3] Leader Saat ini:", diagnostics['volatile']['leaderId'])
    print("[4] List Cluster:", diagnostics['volatile']['cluster'])
    print ("\n[5] Full Diagnostic:", diagnostics)
    print ("\n[6] d:", d)

def test_8_export_file(port):
    print('[Export File]')
    d = DistributedDict('127.0.0.1', port)
    print ("[1] d =", d)
    path = input("[2] File yang ingin disave = ")
    opsi = input("[3] save || save_as = ")
    if (opsi == "save"):
        if ".txt" not in path:
            open(path + '.txt', 'w').write(str(d[path]))
            print ("[4] File =", path, "telah disimpan.")
    else:
        output = input("[4] Save Sebagai = ")
        if ".txt" not in output:
            open(output + ".txt",'w').write(str(d[path]))
        print ("[5] File =", path, ", disimpan sebagai =", output + ".txt")

def test_9_compacted_log_replication(port):
    print('[Compacted Log Replication]')
    d = DistributedDict('127.0.0.1', port)
    d['test'] = 0
    print("[1] d[test] =", d['test'])
    d['test'] = 1
    print("[2] d[test] =", d['test'])
    d['test'] = 2
    print("[3] d[test] =", d['test'])
    d['test'] = 3
    print("[4] d[test] =", d['test'])
    d['test'] = 4  # compaction kicks in
    print("[5] d[test] =", d['test'])
    del d
    d = DistributedDict('127.0.0.1', 9102)
    print("d[test] =", d['test'])
    
def coba():
    port = int(input("Port = "))
    print ("Menggunakan Port ", port)
    while True:
        uji = input("UJI COBA:\nTest_1 = Append\ntest_2 = Delete\ntest_3 = Read from different client\n" \
                    "test_4 = Add server\ntest_5 = Remove server\ntest_6 = Input file\ntest_7 = Diagnostic\n" \
                    "test_8 = Export_file\nend = Stop Loops\n\nTest ke Berapa? ")
        if (uji == "end"):
            break
        if (uji == "test_1"):
            test_1_append(port)
        elif (uji == "test_2"):
            test_2_delete(port)
        elif (uji == "test_3"):
            if(port != 9102):
                test_3_read_from_different_client(port)
        elif (uji == "test_4"):
            test_4_add_server(port)
        elif (uji == "test_5"):
            test_5_remove_server(port)
        elif (uji == "test_6"):
            test_6_input_file(port)
        elif (uji == "test_7"):
            test_7_diagnostic(port)
        elif (uji == "test_8"):
            test_8_export_file(port)
        elif (uji == "test_9"):
            if(port != 9102):
                test_9_compacted_log_replication(port)
                
if __name__ == '__main__':
    coba()

"""
    uji = input("UJI COBA:\ntest_1 = append\ntest_2 = delete\ntest_3 = read from different client\n" \
                "test_4 = add server\ntest_5 = remove server\ntest_6 = input file\ntest_7 = diagnostic\n" \
                "test_8 = export_file\n\nTest ke Berapa? ")
    if (uji == "test_1"):
        test_1_append(port)
    elif (uji == "test_2"):
        test_2_delete(port)
    elif (uji == "test_3"):
        if(port != 9102):
            test_3_read_from_different_client(port)
    elif (uji == "test_4"):
        test_4_add_server(port)
    elif (uji == "test_5"):
        test_5_remove_server(port)
    elif (uji == "test_6"):
        test_6_input_file(port)
    elif (uji == "test_7"):
        test_7_diagnostic(port)
    elif (uji == "test_8"):
        test_8_export_file(port)
    elif (uji == "test_9"):
        if(port != 9102):
            test_9_compacted_log_replication(port)
"""