#!/bin/bash

# Hedef adres
TARGET=$1

# Maksimum zıplama sayısı
MAX_HOPS=30

# Kontrol: Hedef adres belirtilmiş mi?
if [ -z "$TARGET" ]; then
    echo "Kullanım: $0 [hedef_adres]"
    exit 1
fi

echo "Traceroute to $TARGET, max hops: $MAX_HOPS"

for ((i=1; i<=MAX_HOPS; i++)); do
    # TTL ayarı ile ping gönder
    RESPONSE=$(ping -c 1 -t $i $TARGET 2>/dev/null)

    # IP adresini ve hostname'i ayıkla
    IP=$(echo "$RESPONSE" | grep "from" | awk '{print $4}' | tr -d ':')
    HOST=$(echo "$RESPONSE" | grep "from" | awk '{print $5}' | tr -d '()')

    # Eğer yanıt yoksa
    if [ -z "$IP" ]; then
        echo "$i - * * *"
    else
        echo "$i - $IP ($HOST)"
    fi

    # Hedefe ulaştıysak döngüyü kır
    if echo "$RESPONSE" | grep -q "1 packets transmitted, 1 received"; then
        echo "Hedefe ulaşıldı!"
        break
    fi
done