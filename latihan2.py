# ====== LATIHAN 2: String Formatting ======
print("=" * 50)
print("LATIHAN 2: String Formatting")
print("=" * 50)

umur = 18
txt = 'Hello, nama saya margaretha, dan umur saya adalah {} tahun'

print(txt.format(umur))

import re
import os


def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_nama(nama):
    """
    Validasi nama lengkap
    - Harus hanya berisi huruf
    - Tidak boleh kosong
    """
    if not nama.strip():
        return False, "Nama lengkap harus diisi"

    if not re.match(r'^[a-zA-Z\s]+$', nama):
        return False, "Nama lengkap harus hanya berisi huruf"

    return True, ""


def validate_no_telepon(no_telepon):
    """
    Validasi nomor telepon
    - Harus hanya berisi angka
    - Tidak boleh kosong
    """
    if not no_telepon.strip():
        return False, "Nomor telepon harus diisi"

    if not re.match(r'^\d+$', no_telepon):
        return False, "Nomor telepon harus hanya berisi angka"

    return True, ""


def validate_email(email):
    """
    Validasi email
    - Harus mengandung karakter @ dan .
    - Tidak boleh kosong
    """
    if not email.strip():
        return False, "Email harus diisi"

    if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
        return False, "Email harus mengandung karakter @ dan ."

    return True, ""


def validate_all(nama, no_telepon, email):
    """
    Validasi semua data form
    """
    errors = {}

    valid, msg = validate_nama(nama)
    if not valid:
        errors['nama'] = msg

    valid, msg = validate_no_telepon(no_telepon)
    if not valid:
        errors['no_telepon'] = msg

    valid, msg = validate_email(email)
    if not valid:
        errors['email'] = msg

    return len(errors) == 0, errors


def display_header():
    """Menampilkan header aplikasi"""
    print("=" * 50)
    print(" " * 10 + "VALIDASI FORM INPUT")
    print(" " * 8 + "Aplikasi Pendaftaran Online")
    print("=" * 50)
    print()


def display_menu():
    """Menampilkan menu utama"""
    print("Menu Utama:")
    print("1. Input Data Baru")
    print("2. Keluar")
    print()


def input_form():
    """Fungsi untuk input data form"""
    print("-" * 50)
    print("FORM PENDAFTARAN")
    print("-" * 50)

    nama = input("Nama Lengkap: ").strip()
    no_telepon = input("Nomor Telepon: ").strip()
    email = input("Email: ").strip()

    return nama, no_telepon, email


def display_validation_result(is_valid, errors, nama, no_telepon, email):
    """Menampilkan hasil validasi"""
    print("\n" + "=" * 50)

    if is_valid:
        print("✓ DATA PENDAFTARAN VALID")
        print("=" * 50)
        print("\nData Anda:")
        print(f"  Nama Lengkap   : {nama}")
        print(f"  Nomor Telepon  : {no_telepon}")
        print(f"  Email          : {email}")
        print("\n✓ Pendaftaran Anda berhasil diproses!")
        print("=" * 50)
    else:
        print("✗ DATA PENDAFTARAN TIDAK VALID")
        print("=" * 50)
        print("\nError yang ditemukan:\n")

        if 'nama' in errors:
            print(f"  ✗ Nama Lengkap: {errors['nama']}")

        if 'no_telepon' in errors:
            print(f"  ✗ Nomor Telepon: {errors['no_telepon']}")

        if 'email' in errors:
            print(f"  ✗ Email: {errors['email']}")

        print("\n" + "=" * 50)


def main():
    """Fungsi utama program"""
    while True:
        clear_screen()
        display_header()
        display_menu()

        pilihan = input("Pilih menu (1-2): ").strip()

        if pilihan == '1':
            clear_screen()
            display_header()

            nama, no_telepon, email = input_form()

            is_valid, errors = validate_all(nama, no_telepon, email)

            display_validation_result(is_valid, errors, nama, no_telepon, email)

            input("\nTekan Enter untuk melanjutkan...")

        elif pilihan == '2':
            clear_screen()
            print("Terima kasih telah menggunakan aplikasi ini!")
            print("Sampai jumpa lagi.")
            break

        else:
            print("\n✗ Pilihan tidak valid! Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()