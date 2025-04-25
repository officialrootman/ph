<?php
// Kullanıcıdan web sitesi URL'si ve tarama türünü al
echo "Tarama yapmak istediğiniz web sitesini girin: ";
$website = trim(fgets(STDIN));
echo "Tarama türünü seçin (1 - Açıklık Taraması, 2 - Domain Bilgisi Toplama): ";
$scanType = trim(fgets(STDIN));

// cURL oturumunu başlat
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $website);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Web sitesinden veri al
$response = curl_exec($ch);
curl_close($ch);

if ($scanType == "1") {
    // Açıklık taraması (örnek olarak XSS kontrolü)
    echo "Açıklık taraması başlatılıyor...\n";
    if (strpos($response, "<script>") !== false) {
        echo "Potansiyel XSS açıklığı tespit edildi!\n";
    } else {
        echo "XSS açıklığı bulunamadı.\n";
    }
} elseif ($scanType == "2") {
    // Domain bilgisi toplama (WHOIS sorgusu)
    echo "Domain bilgileri toplanıyor...\n";
    $whoisData = shell_exec("whois " . parse_url($website, PHP_URL_HOST));
    echo $whoisData;
} else {
    echo "Geçersiz seçim. Lütfen 1 veya 2 girin.\n";
}
?>