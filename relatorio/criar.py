import jinja2
import os

class Relatorio:
    template_path = "templates"
    def __init__(self, titulo, autor, template = "cabecalho.tex"):
        env = jinja2.Environment(loader=jinja2.PackageLoader("relatorio"))
        self.template = env.get_template(template)
        self.titulo = titulo
        self.autor = autor
        self.sessoes = []
        self.variaveis = {
            "autor": self.autor,
            "titulo": self.titulo,
            "sessoes": self.sessoes
        }

    def _renderizar(self):
        return self.template.render(self.variaveis)

    def adicionar_sessao(self, sessao):
        self.sessoes.append(sessao)
