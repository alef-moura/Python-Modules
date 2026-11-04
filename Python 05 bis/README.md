# 05 · The Codex — Ambientes, dependências e imports

Rode tudo a partir desta pasta.

```bash
python3 ex0/construct.py                    # fora de um venv
python3 -m venv lab_env && source lab_env/bin/activate
python3 ex0/construct.py                    # dentro do venv
pip install -r ex0/requirements.txt && python3 ex0/loading.py
pip install -r ex1/requirements.txt
cp ex1/.env.example ex1/.env && python3 ex1/oracle.py
MATRIX_MODE=production API_KEY=secret123 python3 ex1/oracle.py

python3 ft_alembic_0.py
python3 ft_alembic_1.py        # falha de propósito (AttributeError)
python3 ft_distillation_0.py
python3 ft_transmutation_0.py
python3 ft_kaboom_0.py
python3 ft_kaboom_1.py         # falha de propósito (import circular)
```
