# Versão pública para portfólio

Instale com `python -m pip install -r requirements.txt`.
Execute `python marcha.py` para o exemplo por configuração, ou `python -m streamlit run app.py` para a interface.

Na interface, carregue os dois arquivos `synthetic_evaluation` da pasta `examples`: QJT e PP. São 2 ciclos direitos e 3 esquerdos. A referência incluída também é sintética. As figuras e médias servem apenas para demonstrar o programa.

Para usar seus próprios dados localmente, adapte `config.json`. Guarde dados privados em `private_data/` e não os inclua no GitHub. As convenções de colunas, eixos e sinais precisam corresponder ao seu processamento. Consulte o README em inglês para os métodos e as limitações.
