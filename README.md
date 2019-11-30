# Scripts para denúncia com o WhatsApp
Projeto WhatsApp Dice

*<h4> Arquivos que devem estar no celular: </h4>*

<ol>
<li> atualizar_banco.py</li>
<li> banco.py</li>
<li> cliente.py</li>
<li> main.py</li>
<li> verificador.py</li>
</ol>
  
*<h4>Arquivos que devem estar no computador:</h4>*

<ol>
<li> atualizar_mapa.py</li>
<li> marcarMapa.py</li>
<li> servidor.py</li>
<li>locations.csv</li>
</ol>

*<h4>Configurações:</h4>*

_Todas as bibliotecas são nativas do Python3._

Obs.: *No arquivo *cliente.py* a variável ip deve ser atualizada conforme
endereço de ip da sua máquina.*

Trecho do código a ser alterado:
```
def enviar(dado):
    ip = 'endereço de ip da sua máquina' 
    [...]
```

<h1>Tutorial para realizar denúncias</h1>
<ol>
  <li>Primeiramente, rode o script *banco.py* para criar o banco de imagens (imagens.bd)</li>
  <li>Após, rode o script *atualizar_mapa.py* na sua máquina</li>
  <li>Agora é só rodar o script *main.py* no celular e voalá</li>
</ol>

<h1>Explicando os arquivos e principais funções e procedimentos </h1>
banco.py: tem a função criar() que gera o banco de dados, não retorna nada e não tem parâmetros.<br>
atualizar_banco.py: tem a função atualizar() que recebe o nome de uma imagem como parâmetro e retorna True <br>
cliente.py: tem a função enviar() que recebe uma string(valores de lat e long no caso) como parâmetro.<br>
main.py: tem duas funções e um procedimento:
<ol>
  <li>dms_para_dd(dms, ref) que recebe as coordenadas em Graus Minutos e Seg (dms) e a Referência (ref) e retorna
  uma coordenada em Graus decimais (dd).</li>
  <li>coordenadas(nome_imagem) que recebe o nome de uma imagem (ou o caminho dela) e extrai as coordenadas dela (porém em dms).</li>
  <li>conexao() que chama as demais funções.
</ol><br>
servidor.py: tem a função receber(). Quando ela é chamada, fica esperando receber algo via rede com o tamanho máximo
de 1024 bytes.<br>
verificador.py: tem a função verificar(nome) que recebe como parâmetro o nome de uma imagem. retorna: True, se a imagem estiver no banco imagens.bd. False caso contrário.


