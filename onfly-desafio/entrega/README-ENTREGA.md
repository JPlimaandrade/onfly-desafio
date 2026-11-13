# Defeitos Corrigidos

## Cálculo de Conversão para BRL

Causa raíz: 
amount estava sendo dividido por rate, além de que amount e rate estavam sendo tratados como float.

Abordagem: De acordo com as instruções do desafio, não deve existir valores sendo tratados como float, e de acordo com as regras de negocio do desafio, o retorno da função deveria ser (amount * rate) e não (amount / rate), dito isso, 
modifiquei o retorno da função convert_to_brl para apenas retornar (amount * rate) em Decimal.

Validação: Execute `pytest tests/test_currency.py` na raiz do projeto. Verifique se o teste é concluído com sucesso e confirma que a conversão de BRL e USD é calculada pela multiplicação do valor pela taxa de câmbio, sem inversão da operação.

## Cálculo de dias de Estadia

Causa raíz: 
As datas estavam sendo tratadas como apenas DIA (dd)-(dd), quando 
na verdade deveriam ser tratadas como (yyyy/mm/dd)-(yyyy/mm/dd).

Abordagem: Como as 2 variáveis são do tipo date, e o Python calcula a diferença exata das variáveis de tipo date e retorna um timedelta, usei a propriedade .days do timedelta para, com precisão pegar a diferença de datas corretamente, independente de mês ou ano.

Validação: Execute `pytest tests/test_nights.py` na raiz do projeto. Verifique se o teste é concluído com sucesso e confirma que uma reserva de 30/01/2025 a 02/02/2025 resulta em 3 noites, considerando corretamente a virada do mês.

## Retorno de Status

Causa raíz: 
O filtro de status estava deixando passar o "NO_SHOW" 
no return quando só deveria deixar passar o "CONFIRMED".

Abordagem: Alterei o filtro de retorno da função para retornar APENAS os status que fossem CONFIRMED.

Validação: Execute `pytest tests/test_status_rules.py` na raiz do projeto. Verifique se o teste é concluído com sucesso e confirma que somente reservas com status `CONFIRMED` entram nos totais financeiros, enquanto reservas `CANCELLED` e `NO_SHOW` são excluídas desses cálculos.

## Ordenação no Ranking de Hotéis

Causa raíz: 
A ordenação de preço dos hotéis estava em ordem crescente, 
quando na verdade deveria ser decrescente.

Abordagem: Procurei onde fica a ordenação dos top Hotéis, analisando o código achei ranked_hotels e ali alterei os valores da etiqueta para que os valores de dinheiro ficassem negativos (somente na etiqueta) assim invertendo a ordenação de crescente para decrescente.

Validação: Execute `pytest tests/test_top_hotels.py` na raiz do projeto. Verifique se o teste é concluído com sucesso e confirma que os hotéis são retornados em ordem decrescente de valor, com H01, H02 e H03 nas três primeiras posições.

## Gerar Relatório completo

Causa raíz: 
Causado pelos erros de Cálculo de conversão para BRL e Erro de retorno de status.

Abordagem: Corrigi os problemas de cálculo de conversão e o Filtro de status retornando "NO_SHOW" e os testes para esta funcionalidade passaram sem mais problemas.

Validação: Execute `pytest tests/test_regression_report.py` na raiz do projeto. Verifique se o teste é concluído com sucesso e confirma a geração correta do relatório completo, incluindo reservas, noites, conversão para BRL e média da diária.

# Possíveis defeitos não listados

## Limite de 200 Linhas no Repository

Causa raíz: Limite no código do arquivo csv_reservation_repository.py de 200 linhas no máximo, impedindo que as outras 100 linhas de dados fossem computadas no CLI. 

Abordagem: Removi o trecho de código que barrava as linhas até 200, assim 
permitindo que o conteúdo completo do arquivo reservas_hoteis.csv fosse computado pelo CLI.

Validação: Execute o CLI utilizando o arquivo completo `data/reservas_hoteis.csv` e confirme que todas as linhas do arquivo são processadas. Em seguida, execute `pytest` na raiz do projeto e verifique se toda a suíte de testes é concluída com sucesso.

## Tratamento de dados

Causa raíz: Falta de verificação do conteúdo dos arquivos em /dados permitindo dados inválidos

Abordagem: Implementei em row_parser.py 4 validações de conteúdo dos arquivos, sendo elas: 
 checkout não pode ser feito antes de checkin,
 quartos não podem ser iguais a 0 em uma reserva,
 quartos não podem assumir valores negativos,
 valores de reservas não podem ser negativos.


Validação: Execute `pytest tests/test_input_validation.py` na raiz do projeto. Verifique se os quatro testes são concluídos com sucesso:

- `test_checkin_after_checkout_is_ignored`: confirma que registros com data de check-in posterior à data de check-out são ignorados.
- `test_rooms_equal_to_zero_is_ignored`: confirma que registros com quantidade de quartos igual a zero são ignorados.
- `test_rooms_less_than_zero_is_ignored`: confirma que registros com quantidade de quartos negativa são ignorados.
- `test_amount_is_negative_is_ignored`: confirma que registros com valor negativo são ignorados.
