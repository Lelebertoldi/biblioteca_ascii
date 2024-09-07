# Esse é um diretório da biblioteca ascii modificada por mim

## Quais foram as modificações feitas?

1 - Essa biblioteca possuía apenas um módulo: loadFromUrl, que recebia 3 argumentos - URL da imagem, colums (padrão 60) que era definido como colums * rows (altura * largura) e color (padrão True). Esse módulo convertia apenas imagens pelo seu link da internet, e os ajustes de altura e largura eram limitados.
  - Agora loadFromUrl recebe 4 argumentos:  URL da imagem, colums (padrão 60), row (padrão None) e color (padrão True).
      Com essa modificação é possível passar separadamente o valor de colums e rows (altura e largura) para ajustar a largura e altura da imagem separadamente. Se o valor de rows não for passado ela continua funcionando como o original, sendo colums definido como colums * rows (altura * largura).

2 - Foi adicionado um novo módulo: loadFromFile, que recebe 4 argumentos - caminho da imagem, colums (padrão 60), row (padrão None) e color (padrão True). Esse novo módulo recebe no primeiro argumento o caminho da imagem contida no computador, se a imagem estiver na mesma pasta do arquivo python que está sendo criado somente será necessário colocar o nome da imagem e sua extensão, exemplo: image.JPEG.

## Exemplos de uso dos módulos:

- Padrão: loadFromUrl(URL, columns=60, rows=None, color=True)

  ascii.loadFromUrl('https://raw.githubusercontent.com/Lelebertoldi/imagens_para_ascii/main/OIG3.66CdAQChAq.jpeg', 100, 40)

- Padrão: loadFromFile(image_file, columns=60, rows=None, color=True)

  ascii.loadFromFile("image.JPEG", 100, 40)


  ## Como instalar:

  1. Baixe a pasta dos arquivos desse diretório

  2. Vá até o local de instalação do seu python e viaje até a pasta Python\Lib\site-packages\
 
  3. Coloque a pasta dos arquivos desse diretório lá
 
  4. Dentro dessa pasta ascii abra seu VS Code 
 
  5. Execute o comando pip install -r requirements.txt
 
  6. Pronto, pode usufruir da sua nova bibioteca 



### Metadados originais:

Metadata-Version: 2.1
Name: ascii
Version: 3.6
Summary: Turns images into ascii art
Home-page: https://github.com/mkaminsky11/ascii
Author: Michael Kaminsky
Author-email: mkaminsky11@gmail.com
Keywords: ascii,image,asciiart,ascii art,art
Requires-Dist: Pillow
Requires-Dist: urllib3

