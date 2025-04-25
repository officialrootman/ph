<?php
// Kullanıcının girdiği URL'yi analiz eder
function analyzeLink($url) {
    // Kara liste kontrolü
    $blacklist = [
        'http://example-malicious.com',
        'http://phishing-site.com'
    ];

    if (in_array($url, $blacklist)) {
        return "Bu URL kara listede. Dikkatli olun!";
    }

    // HTTP Başlık analizi
    $headers = @get_headers($url);
    if (!$headers) {
        return "URL erişilemez veya zararlı olabilir.";
    }

    foreach ($headers as $header) {
        if (strpos($header, 'Content-Type: text/html') !== false) {
            return "Link güvenli gibi görünüyor.";
        } elseif (strpos($header, 'application/') !== false) {
            return "Potansiyel olarak tehlikeli bir dosya içeriyor.";
        }
    }

    return "Daha fazla analiz gerekli.";
}

// HTML formu ile kullanıcıdan URL alınır
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $url = $_POST['url'];
    $result = analyzeLink($url);
}
?>

<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zararlı Link Analiz Aracı</title>
</head>
<body>
    <h1>Zararlı Link Analiz Aracı</h1>
    <form method="post" action="">
        <label for="url">URL Girin:</label>
        <input type="text" id="url" name="url" required>
        <button type="submit">Analiz Et</button>
    </form>

    <?php if (isset($result)): ?>
        <p>Sonuç: <?php echo htmlspecialchars($result); ?></p>
    <?php endif; ?>
</body>
</html>