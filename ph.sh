#!/bin/bash

usage() {
  echo "Kullanım: $0 [-m maksimum_adım] hedef_adres"
  exit 1
}

# Varsayılan değerler
MAX_HOPS=30

# Komut satırı seçeneklerini işle
while getopts "m:" opt; do
  case $opt in
    m) MAX_HOPS=$OPTARG;;
    *) usage;;
  esac
done
shift $((OPTIND-1))

if [ "$#" -ne 1 ]; then
  usage
fi

TARGET=$1

# DNS çözümleme
TARGET_IP=$(dig +short $TARGET)
if [ -z "$TARGET_IP" ]; then
  echo "Hedef alan adı çözümlenemedi."
  exit 1
fi

echo "Traceroute başlıyor: $TARGET ($TARGET_IP)"

for ((i=1; i<=MAX_HOPS; i++))
do
  # IPv4 ve IPv6 desteği ekle
  if [[ $TARGET_IP == *":"* ]]; then
    RESPONSE=$(ping6 -c 1 -t $i $TARGET | grep "time=")
  else
    RESPONSE=$(ping -c 1 -t $i $TARGET | grep "time=")
  fi

  if [[ -z $RESPONSE ]]; then
    echo "$i: * (Zaman aşımı)"
  else
    IP=$(echo $RESPONSE | awk -F'[()]' '{print $2}')
    RESPONSE_TIME=$(echo $RESPONSE | awk -F'time=' '{print $2}' | awk '{print $1}')
    echo "$i: $IP ($RESPONSE_TIME ms)"
    if [[ $IP == $TARGET ]]; then
      echo "Hedefe ulaşıldı!"
      break
    fi
  fi
done

echo "Traceroute tamamlandı!"