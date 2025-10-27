import os

FILE_NAME = "todo.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return f.read().splitlines()

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("Belum ada tugas.")
    else:
        print("Daftar tugas:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== TO-DO LIST ===")
        print("1. Lihat daftar tugas")
        print("2. Tambah tugas")
        print("3. Hapus tugas")
        print("4. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            new_task = input("Tugas baru: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("-> Tugas ditambah!")
        elif choice == "3":
            show_tasks(tasks)
            index = int(input("Nomor tugas yang mau dihapus: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f"-> Tugas '{removed}' dihapus!")
            else:
                print("Nomor tidak valid.")
        elif choice == "4":
            print("Keluar...")
            break
        else:
            print("Pilihan salah!")

if __name__ == "__main__":
    main()
