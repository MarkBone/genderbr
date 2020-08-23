PYTHONCMD=python

# Compila os arquivos python (apenas para verificação)
compile: deps
	${PYTHONCMD} -m compileall ./


# Executa todos os testes
tests: deps unit-tests integration-tests

# Executa os testes unitarios
unit-tests: deps delete-coverage-report
	${PYTHONCMD} -m pytest --cov=genderbr --cov-fail-under=0 --cov-report xml:coverage-reports/coverage-report.xml tests/unit

delete-coverage-report:
	rm -rf coverage-reports/

integration-tests: deps
	${PYTHONCMD} -m pytest tests/integration

deps:
	pip3 install -r requirements.txt

freeze:
	pip freeze > requirements.txt