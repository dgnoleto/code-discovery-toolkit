import hashlib
import sys
from pathlib import Path

# Adiciona o diretório raiz ao path para importar o script
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.analisar_repositorio import (
    calcular_hash,
    encontrar_duplicados_exatos,
    encontrar_duplicados_similares,
    encontrar_possiveis_nao_referenciados,
    listar_arquivos,
)


def test_calcular_hash(tmp_path):
    file_path = tmp_path / "test.txt"
    content = b"Ola Mundo, Code Discovery!"
    file_path.write_bytes(content)
    
    expected_hash = hashlib.sha256(content).hexdigest()
    assert calcular_hash(file_path) == expected_hash


def test_listar_arquivos(tmp_path):
    # Cria estrutura de teste
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "file1.py").write_text("print('1')")
    (tmp_path / "node_modules").mkdir()
    (tmp_path / "node_modules" / "ignored.js").write_text("print('ignored')")
    (tmp_path / "file2.js").write_text("console.log('2')")
    
    arquivos = listar_arquivos(tmp_path)
    relative_paths = {p.relative_to(tmp_path).as_posix() for p in arquivos}
    
    # node_modules deve ser ignorado
    assert "sub/file1.py" in relative_paths
    assert "file2.js" in relative_paths
    assert "node_modules/ignored.js" not in relative_paths


def test_encontrar_duplicados_exatos(tmp_path):
    f1 = tmp_path / "a.py"
    f2 = tmp_path / "b.py"
    f3 = tmp_path / "c.py"
    
    # f1 e f2 idênticos
    f1.write_text("print('igual')")
    f2.write_text("print('igual')")
    f3.write_text("print('diferente')")
    
    duplicados = encontrar_duplicados_exatos([f1, f2, f3])
    assert len(duplicados) == 1
    
    hash_key = list(duplicados.keys())[0]
    assert len(duplicados[hash_key]) == 2
    assert f1 in duplicados[hash_key]
    assert f2 in duplicados[hash_key]


def test_encontrar_duplicados_similares(tmp_path):
    f1 = tmp_path / "original.py"
    f2 = tmp_path / "similar.py"
    f3 = tmp_path / "diferente.py"
    
    content1 = "def calcular_soma(a, b):\n    resultado = a + b\n    return resultado\n"
    # Similaridade > 90% (apenas mudando nomes das variáveis)
    content2 = "def calcular_soma(x, y):\n    resultado = x + y\n    return resultado\n"
    content3 = "def subtracao(a, b):\n    return a - b\n"
    
    f1.write_text(content1)
    f2.write_text(content2)
    f3.write_text(content3)
    
    similares = encontrar_duplicados_similares([f1, f2, f3], threshold=0.9)
    assert len(similares) == 1
    
    file_a, file_b, ratio = similares[0]
    assert (file_a == f1 and file_b == f2) or (file_a == f2 and file_b == f1)
    assert ratio >= 0.9 and ratio < 1.0


def test_encontrar_possiveis_nao_referenciados_com_limites(tmp_path):
    f_lib = tmp_path / "config.py"
    f_app = tmp_path / "app.py"
    f_dead = tmp_path / "dead.py"
    
    # f_lib se chama "config", mas f_app contém "app_config_helper", não a palavra "config" isolada.
    # A regex com limite \b deve considerar f_lib como NÃO referenciado.
    f_lib.write_text("DB_HOST = 'localhost'")
    f_app.write_text("import app_config_helper\nprint('starting app')")
    f_dead.write_text("print('unused code')")
    
    suspeitos = encontrar_possiveis_nao_referenciados([f_lib, f_app, f_dead])
    relative_suspects = {p.relative_to(tmp_path).as_posix() for p in suspeitos}
    
    # config e dead devem ser listados como suspeitos não referenciados
    assert "config.py" in relative_suspects
    assert "dead.py" in relative_suspects


def test_encontrar_possiveis_nao_referenciados_com_referencia(tmp_path):
    f_lib = tmp_path / "auth.py"
    f_app = tmp_path / "app.py"
    
    # f_app contém a palavra inteira "auth"
    f_lib.write_text("def login(): pass")
    f_app.write_text("from auth import login\nlogin()")
    
    suspeitos = encontrar_possiveis_nao_referenciados([f_lib, f_app])
    relative_suspects = {p.relative_to(tmp_path).as_posix() for p in suspeitos}
    
    # auth.py NÃO deve ser listado como suspeito
    assert "auth.py" not in relative_suspects
