## Ferramenta e Modelo usados

* Gemni 3.6 Flash
* Copilot Student: (gpt-5.6-luna) --com acesso completo ao ambiente de desenvolvimento do projeto.

# o que foi feito por mim

• Tomada de decisão sobre como resolver os bugs encontrados: Avaliação das alternativas técnicas (como uso de allowlist no filtro de status e remoção da trava de 200 linhas) antes de aplicar cada correção.

• Investigação e leitura do código-fonte: Execução da suíte inicial de testes (pytest), navegação pelos módulos em src/onfly_report/ e cruzamento linha a linha com as regras de negócio descritas no README.md.

• Implementação manual das correções: Edição direta dos arquivos currency_converter.py, stay_calculator.py, filtro de status (is_billable), report_builder.py e csv_reservation_repository.py, e validação das correções implementadas em conjunto com a IA(Gemni).

• Blindagem e validação de entrada (row_parser.py): Criação de validações adicionais de integridade dos dados 
impedindo que checkout < checkin, rooms <= 0 e amount < 0.

• Execução de testes e auditoria final: Validação contínua via terminal com pytest, revisão manual dos arquivos restantes.

• Implementação de quatro novos testes unitários (implementei com base nos testes unitários já existentes, tentando manter a mesma estrutura de código, feito SEM AUXÍLIO de ferramentas de IA.), juntamente com o tratamento de erro feito no row_parser.py (no row_parser.py pedi auxílio a IA(Gemni) para entender melhor o funcionamento da sintaxe python neste caso).

• Revisão Final Completa após o recebimentodo do relatório feito pela IA(Copilot) e decisão de não considerar os pontos levantados pela IA(Copilot), visto que os pontos levantados se tratavam de casos que o README.md está informando que não ocorrerão.

# o que foi feito pela IA 
    
* Gemni 3.6 Flash - `sessao1.txt ou sessao1.pdf` (pdf é o formato padrão do gemni)

    • Auxílio com dúvidas de sintaxe e ecossistema Python: Explicação de conceitos da linguagem.

    • Apoio na investigação dos testes (pytest): Interpretação dos logs de falha para localizar as possíveis causas raízes dos defeitos nos módulos de: conversão de moeda, cálculo de noites, filtro de status faturáveis e ordenação do ranking de hotéis.

    • Orientação sobre boas práticas e regras de negócio: Revisão conceitual sobre precisão decimal, filtro por allowlist (status == "CONFIRMED"), tratamento de exceções no parser.

    • Revisão na auditoria do código-fonte: Apoio na análise dos repositórios de leitura de CSV, ajudando a entender o impacto do limite de 200 linhas em csv_reservation_repository.py.

* Copilot Student (gpt-5.6-luna) `sessao2.txt`

    • Relatório de revisão completa do código.
