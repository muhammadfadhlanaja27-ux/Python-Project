users = {
  "user1" : {"role" : "user"},
  "admin1" : {"admin" : "admin"}
}

def can_access(username, needed_role):
  return users[username]["role"] == needed_role

def view_user_data(username):
  return "Data user biasa"

def view_admin_data(username):
  if not can_access(username, "admin"):
    return "Access denied"
  return "Data rahasia admin"

def update_config(username):
  if not can_access(username, "admin"):
    return "Access denied"
  return "Konfigurasi berhasil diubah"

def main():
  print(view_admin_data("user1"))
  print(view_admin_data("admin1"))
  print(update_config("user1"))
  print(update_config("admin1"))

if __name__ == "__main__":
  main()