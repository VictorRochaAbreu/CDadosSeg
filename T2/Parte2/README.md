Obtenha alguns binários de Windows (você pode pegá-los do seu próprio computador, se tiver o sistema operacional instalado, ou de sites de download de programas, como sourceforge e outros). Exemplos de binários: calc.exe, ping.exe, paint.exe, netstat.exe...
Escreva um script em Python (ou .ipynb) que receba como entrada um arquivo ou diretório e enumere a seções executáveis do(s) binário(s), imprimindo na saída padrão um dicionário de listas, onde a chave é o nome do binário e o valor é uma lista de seções executáveis. Dica: https://github.com/erocarrera/pefile
Escreva outro script em Python (ou .ipynb) que receba como entrada dois arquivos .exe e os compare, imprimindo na saída padrão quais seções são comuns a ambos os binários, quais somente estão presentes no binário 1 e quais somente estão presentes no binário 2. Siga as regras de formato/apresentação já estabelecidas nesta tarefa.

A Parte 2 é divida em dois scripts ao qual o primeiro retorna somente as sessões executaveis do programa abaixo temos um exemplo de entrada e a saida, o argumento de entrada pode ser um diretorio que no caso do exemplo se chama Exe ou pode ser um unico arquivo .exe:

C:\Users\Victor\Desktop\CIENCIA DE DADOS SEGURANÇA>python T2p2.py Exe

As seções executaveis do programa calc1.exe são:
        .text
        
o segundo retorna as sessões comuns e tambem separadamente as unicas de 2 executaveis, temos um exemplo de entrada e a saida:

C:\Users\Victor\Desktop\CIENCIA DE DADOS SEGURANÇA>python T2p2b.py calc.exe mspaint.exe

--                  --
--  SESSÕES COMUNS  --
--     DOS  EXE     --
--                  --

         - .rdata
         - .pdata
         - .rsrc
         - .data
         - .reloc
         - .text

--                  --
--  SESSÕES UNICAS  --
--     DOS  EXE     --
--                  --

mspaint.exe
         - .didat        
