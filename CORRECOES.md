# Revisão preservando seus códigos

Esta versão substitui a anterior. Os cinco notebooks foram recuperados diretamente dos arquivos enviados, preservando os nomes, a ordem das células, funções, variáveis, comentários, laços, estrutura dos gráficos e comandos de leitura e salvamento.

Foram corrigidas somente seis células, em quatro notebooks:

- Análise espectral: impedir que os laços ultrapassem os limites, corrigir o índice da frequência depois do incremento e tratar sinais de potência espectral zero.
- Filtragem: as mesmas correções espectrais, verificação dos dados informados e exclusão de frequências de corte inválidas para a aquisição.
- Suavização: corrigir a unidade exibida do span (fração, em vez de segundos) e o cabeçalho da coluna de tempo. O cálculo por diferenças, a frequência de aquisição e a varredura completa de spans foram mantidos.
- Ângulo do joelho: manter o laço por amostra, tratar segmentos de comprimento zero e valores do cosseno fora do intervalo numérico; tratar a ausência de vales; usar o argumento da função para calcular ciclos; salvar os resultados depois de calcular mínimos e máximos.

O notebook da tarefa de filtragem mantém todas as células de código originais. O arquivo `biomech.py` da versão anterior foi removido. Não houve consolidação de funções, vetorização nem troca de nomes para inglês.

O arquivo `biomechanics-signal-processing/docs/correcoes.diff` mostra cada linha de código modificada em comparação com os uploads.

Os módulos principais da aplicação de marcha, seu código visual e o script MATLAB `processaMarchaControle.m` são idênticos aos originais, byte por byte. Na aplicação, apenas os textos dos controles reais foram substituídos por descrições sintéticas; configurações públicas apontam para os exemplos. No importador MATLAB, foram removidos somente nomes e caminhos identificados, mantendo sua estrutura original. A logo fornecida foi restaurada.

Os dados sintéticos ficam em arquivos separados, com os nomes que seus notebooks já esperam. Dados de participantes continuam fora do pacote público. Os arquivos de entrada recebidos não foram sobrescritos. Saídas salvas dos notebooks foram limpas para publicação.

Verificação: quatro testes das correções passaram; as células de cálculo dos cinco notebooks foram executadas na ordem original em processos Python separados; a interface restaurada abriu sem erros. MATLAB e a interação do Jupyter no navegador ainda precisam ser conferidos no computador do usuário.
