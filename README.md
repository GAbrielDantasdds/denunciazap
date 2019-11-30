# Scripts para denúncia com o WhatsApp
Projeto WhatsApp Dice

*<h4> Arquivos que devem estar no celular: </h4>*

<ol>
<li> atual.py</li>
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
<ol>
