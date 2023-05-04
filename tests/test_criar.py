from relatorio.criar import Relatorio

def test_autor_e_titulo():
    relat = Relatorio("Finanças", "Pedro Tokar")
    resultado = relat._renderizar()
    assert r'\author{ Pedro Tokar }' in resultado
    assert r'\title{ Finanças }' in resultado

def test_adicionar_sessao():
    relat = Relatorio("Finanças", "Pedro Tokar")
    relat.adicionar_sessao(r'\section{Sessão 1}')
    resultado = relat._renderizar()
    assert r'\section{Sessão 1}' in resultado
