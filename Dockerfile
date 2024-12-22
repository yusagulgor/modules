# Python 3.12 imajını kullanarak temel imajı oluşturun
FROM python:3.12

# Çalışma dizinini oluşturun ve ayarlayın
WORKDIR /app

# Python gereksinimlerini yükleyin
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Node.js ve npm yükleme
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# package.json dosyasını kopyalayın ve npm paketlerini yükleyin
COPY package.json ./
RUN npm install

# Proje dosyalarını kopyalayın
COPY . .

# Uygulamanın dinleyeceği portu açın
EXPOSE 3000

# Varsayılan komutu çalıştırın
CMD ["python", "src/main.py"]
