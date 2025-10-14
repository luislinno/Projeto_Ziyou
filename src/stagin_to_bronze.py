# Import de funções criadas
from package.funcoes import downloadDataset, FileMove


# Função que realiza o download dos arquivos na origem
downloadDataset("olistbr/brazilian-ecommerce")


# Atribuição de caminhos de origem e destino dos dados
path = ("C:\\Users\\Nando\\.cache\\kagglehub\\datasets\\olistbr\\brazilian-ecommerce\\versions\\2\\", "C:\\Users\\Nando\\Desktop\\Projeto_Ziyou\\Projeto_Ziyou\\data\\bronze\\")

# Move os arquivos da pasta stagin para pasta bronze
FileMove(*path)


