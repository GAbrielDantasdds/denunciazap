from PIL import Image as Img
from cliente import enviar
from time import sleep
from PIL.ExifTags import GPSTAGS
import glob as g
from verificador import verificar
from atualizar_banco import atualizar

#############################################
# FUNÇÃO dms_para_dd:                       |
# PARÂMETROS: coordenada em (DMS) e A Refe- |
# rência da coordenada (REF).               |
# PROCESSO: Converte as coordenadas de DMS  |
# para DD.                                  |
# RETORNO: Coodenadas em DD.                |
#############################################


def dms_para_dd(dms, ref):
    graus =   dms[0][0] / dms[0][1]
    minutos = dms[1][0] / dms[1][1] / 60
    segs =    dms[2][0] / dms[2][1] / 3600

    if ref in ['S', 'W']:
        graus = -graus
        minutos = -minutos
        segs = -segs
    return (graus + minutos + segs)


def coordenadas(nome_imagem):
    im = Img.open(nome_imagem)
    exif = im._getexif()
    dic = {}
    try:
        for ele, v in exif[34853].items():
            dic[GPSTAGS[ele]]= v
        return (dic['GPSLatitude'], dic['GPSLatitudeRef']), (dic['GPSLongitude'], dic['GPSLongitudeRef'])
    except:
        return f'Não foi possível extrair os metadados da imagem: {nome_imagem}'

def conexao():
    imagens = g.glob('*jpeg')
    if imagens != None:
        for elemento in imagens:
            if verificar(elemento) == False:
                try:
                    lat, lon = coordenadas(elemento)
                except:
                    print(f'Não foi possível extrair os dados da imagem {elemento}')
                enviar(f'{dms_para_dd(lat[0], lat[1])}, {dms_para_dd(lon[0], lon[1])}\n')
                atualizar(elemento)
                print('informações extraídas de {elemento}')
            else:
                print(f'{elemento} já consta no banco de dados!')



while True:
    conexao()
    print('Rodando')
    sleep(5)

