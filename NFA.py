class NFA:
    estadoAtual = None;
    def __init__(self, estados, transicao, inicial, final):
        self.estados = estados;
        self.transicao = transicao;
        self.inicial = inicial;
        self.final = final;
        self.estadoAtual = inicial;
        return;
    
    def transicaoEstado(self, valor):
        if ((self.estadoAtual, valor) not in self.transicao.keys()):
            self.estadoAtual = None;
            return;
        self.estadoAtual = self.transicao[(self.estadoAtual, valor)];
        return;
    
    def isEstadoFinal(self):
        return self.estadoAtual in final;
    
    def vaiEstadoInicial(self):
        self.estadoAtual = self.inicial;
        return;
    
    def testa(self, palavra):
        self.vaiEstadoInicial();
        for p in palavra:
            self.transicaoEstado(p);
            continue;
        return self.isEstadoFinal();
    pass;



estados = {'q0','q1','q2'};

tf = dict();
tf[('q0','a')] = 'q1'

tf[('q1','b')] = 'q2'


inicial = 'q0';
final = {'q2'};

FA = NFA(estados, tf, inicial, final);

entrada = list('ab');

print (FA.testa(entrada));
