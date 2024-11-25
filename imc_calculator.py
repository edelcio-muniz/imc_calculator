import sqlite3
from datetime import date

def create_db():
    conn = sqlite3.connect('imc.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS imc_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        peso REAL NOT NULL,
        altura REAL NOT NULL,
        imc REAL NOT NULL,
        data_extracao DATE NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def save_record(nome, peso, altura, imc):
    conn = sqlite3.connect('imc.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO imc_records (nome, peso, altura, imc, data_extracao)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, peso, altura, imc, date.today()))
    conn.commit()
    conn.close()

def main():
    nome = input("Digite seu nome: ")
    try:
        peso = float(input("Digite o peso em kg: "))
        altura = float(input("Digite a altura em metros: "))

        if peso <= 0 or altura <= 0:
            raise ValueError("Peso e altura devem ser maiores que zero.")
        
        imc = peso / (altura ** 2)
        print(f"O índice de massa corpórea (IMC) é: {imc:.2f}")

        save_record(nome, peso, altura, imc)

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    create_db()
    main()
