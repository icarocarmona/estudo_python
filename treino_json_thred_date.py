
import threading
import json
from datetime import datetime, timedelta
import time

class TR5:
    def __init__(self):
        print("Iniciado")

    def treino_threding(self):

        def check(log):
            print(log)
            for a in range(0,5):
                print('Pacote {val} de 5'.format(val=a))

        t = threading.Thread(target=check, args=('Executando assincrono',))
        t.start()
        while t.isAlive():
            print('Aguardando')
            time.sleep(2)

        return 'FIM PROCESSO'

    def treino_json(self):

        with open('C:/Users/tr_ialmeida/Downloads/python-workspace/elastic/treino.json') as fh:
            a = json.load(fh)
            for count, val in enumerate(a["objArray"]):
                # print(val)
                if (val["class"] == 'lower'):
                    print(val["class"],"=",val["age"])


    def treino_datetime(self):

        past = datetime.now()
        time.sleep(2)
        now = datetime.now()

        dif = now - past

        print(dif.total_seconds())
        print(datetime.strptime('2019/02/01', '%Y/%m/%d'))
        print(datetime.strftime(datetime.now(), '%Y/%m/%d'))
        outro = now - timedelta(days=2)

        print(outro)

if __name__ == '__main__':
    tmp  = TR5()
    # tmp.treino_threding()
    # tmp.treino_json()
    tmp.treino_datetime()
