import os, sys, fnmatch
"""
formato do comando
ffmpeg -i 'ENTRADA' -i 'LEGENDA' -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt -map:v0 -map a -map 1:0 -ss 00:00:00 -to 00:00:10 "SAIDA"
"""
base_path = "/home/jp/Imagens/logos_ifpi"

# checa se a plataforma
if sys.platform == 'linux':
    cmd = 'ffmpeg'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'

caminho_origem = '/home/jp/Vídeos'
caminho_destino = '/home/jp/Vídeos/convertidos'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mkv'):
            continue
        caminho_completo = os.path.join(raiz, arquivo)
        nome, extensao = os.path.splitext(caminho_completo)
        caminho_legenda = nome + '.srt'

        if os.path.isfile(caminho_legenda):
            print('Achei a legenda')
            legenda = f'-i {caminho_legenda}'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            legenda = ''
            map_legenda = ''

        nome, extensao = os.path.splitext(arquivo)
        saida = f"{caminho_destino}/{nome}_novo.{extensao}"
        print(nome)
        print(arquivo)

        comando = (f"{cmd} -i '{caminho_completo}' {legenda}"
                   f"{codec_video} {crf} {preset} {codec_audio} {bitrate}"
                   f"{debug} {map_legenda} {saida}")
        print(comando)
