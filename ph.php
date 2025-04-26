<?php
echo "Sisteme Giriş Başarılı!\n";
echo "Not: Sistem 7 saniye içinde açılacak.\n";
sleep(1);

exec("python3 ph.py");
?>
