from os.path import exists
import pickle

# funções utilitárias para utilizar o Pickle
# caso o arquivo existir, retorna o objeto dentro dele
# caso contrário, cria o arquivo e retorna o valor padrão para esta variável
def load_pickle(default, filename):
   if exists(f'{filename}.pickle'):
       with open(f'{filename}.pickle', 'rb') as f:
           return pickle.load(f)
   else:
       with open(f'{filename}.pickle', 'wb') as f:
           pickle.dump(default, f)
           return default


def save_pickle(obj, filename):
    with open(f'./{filename}.pickle', 'wb') as f:
        pickle.dump(obj, f)
