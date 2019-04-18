class NFA:    
    estadoAtual = None;
    alf = list('abcdefghijklmnopqrstuvwxyz')
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

#L é linguagem
#P é a palavra
#TF são as funções de transição
#FA é nosso Automato Finito

L = 'a*b'
P = 'aAAAb'

n = len(L)

estados = set();
estadosV = set();

for i in range(0, n+1):
    estados.add('q'+str(i))


tf = dict();

for i in range(0, n):  
   if L[i] == '*' or L[i] == '?':
       tf[('q'+str(i), '')] = 'q'+str(i+1)
   else:
       tf[('q'+str(i), L[i])] = 'q'+str(i+1)
       
   if L[i] == '*':
       tf[('q'+str(i), 'A')] = 'q'+str(i)

#tf[('q1','b')] = 'q2'
       
       
print(tf)

inicial = 'q0';
final = {'q'+str(n)};

FA = NFA(estados, tf, inicial, final);

entrada = list(P);

print (FA.testa(entrada));
