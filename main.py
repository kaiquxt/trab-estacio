import sqlite3
import sys

def connect_db():
    return sqlite3.connect('ngo_system.db')

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS food_donations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            donor_name TEXT NOT NULL,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def add_volunteer(name, email):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO volunteers (name, email) VALUES (?, ?)
        ''', (name, email))
        conn.commit()
        print(f"Voluntário '{name}' adicionado com sucesso!")
    except sqlite3.IntegrityError:
        print(f"Erro: O e-mail '{email}' já está registrado.")

    conn.close()

def add_food_donation(donor_name, item_name, quantity):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO food_donations (donor_name, item_name, quantity) VALUES (?, ?, ?)
    ''', (donor_name, item_name, quantity))
    conn.commit()
    print(f"Doação de '{item_name}' de {donor_name} registrada com sucesso!")

    conn.close()

def list_volunteers():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM volunteers')
    volunteers = cursor.fetchall()

    print("\nLista de Voluntários:")
    for volunteer in volunteers:
        print(f"ID: {volunteer[0]}, Nome: {volunteer[1]}, E-mail: {volunteer[2]}")

    conn.close()

def list_food_donations():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM food_donations')
    donations = cursor.fetchall()

    print("\nDoações de Alimentos:")
    for donation in donations:
        print(f"ID: {donation[0]}, Doador: {donation[1]}, Item: {donation[2]}, Quantidade: {donation[3]}")

    conn.close()

def main():
    create_tables()
    print("Sistema iniciado!")  # Mensagem de debug para confirmar o início do sistema

    while True:
        print("\nMenu:")
        print("1. Adicionar Voluntário")
        print("2. Adicionar Doação de Alimentos")
        print("3. Listar Voluntários")
        print("4. Listar Doações de Alimentos")
        print("5. Sair")

        choice = input("Escolha uma opção: ")
        print(f"Opção escolhida: {choice}")  # Mensagem de debug para verificar a escolha

        if choice == '1':
            name = input("Nome do voluntário: ")
            email = input("E-mail do voluntário: ")
            add_volunteer(name, email)
        elif choice == '2':
            donor_name = input("Nome do doador: ")
            item_name = input("Nome do item: ")
            quantity = int(input("Quantidade: "))
            add_food_donation(donor_name, item_name, quantity)
        elif choice == '3':
            list_volunteers()
        elif choice == '4':
            list_food_donations()
        elif choice == '5':
            print("Saindo do sistema...")
            sys.exit()
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
