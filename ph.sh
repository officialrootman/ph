#!/bin/bash

# theHarvester aracını kurmak için gerekli adımlar

echo "theHarvester kurulumuna başlanıyor..."

# Gerekli paketleri güncelleme ve yükleme
sudo apk update && sudo apk upgrade -y
sudo apk install -y apk add python3-pip git

# theHarvester'ı GitHub üzerinden klonlama
echo "theHarvester deposu klonlanıyor..."
git clone https://github.com/laramies/theHarvester.git
cd theHarvester || { echo "Klonlama başarısız oldu!"; exit 1; }

# Gerekli Python bağımlılıklarını yükleme
echo "Python bağımlılıkları yükleniyor..."
pip3 install -r requirements/base.txt

echo "Kurulum tamamlandı. theHarvester kullanıma hazır!"