from python_aternos import Client

def starter():
    atclient = Client()
    atclient.login_with_session('zChnUq9QmiTCP7ahytUIoWARbfDvgUcorAEFDtqLF7zlrFiPJfWbpuYX5V3xoQAlpnmsEMqPyGpvH2cdcPGhfTxQBCiCBb9KvHXK')
    aternos = atclient.account
    servs = aternos.list_servers()
    myserv = servs[0]
    myserv.start()