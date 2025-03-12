<h1 align="center">
  <img src="assets/icon/flask.png" width="80">  
  <img src="assets/icon/ollama.png" width="80">  
  <img src="dassets/icon/streamlit.png" width="80">  
  <br>
  🔥Local'de çalışan Chatbot🔥
</h1>


---

# 📷 API Test Görüntüsü
![DemoGorsel](assets/images/demo.png)


---

Bu proje, Flask tabanlı bir REST API ile Streamlit arayüzünü birleştirerek, Ollama üzerinden çalışan bir dil modeli (örneğin, DeepSeek R1) ile etkileşimli bir sohbet deneyimi sunar. Hem API üzerinden Postman gibi araçlarla mesaj gönderebilir hem de Streamlit arayüzü ile kullanıcı dostu bir şekilde sohbet edebilirsiniz.

## Özellikler

- **Flask REST API:** /api/chat endpoint’i üzerinden mesaj alır ve modeli çalıştırarak yanıt döndürür.
- **Streamlit Arayüzü:** Kullanıcı dostu bir web arayüzü ile sohbet etmenizi sağlar.
- **Ollama Desteği:** Lokal makinenizde DeepSeek R1 (veya başka bir model) çalıştırmak için Ollama CLI kullanılır.
- **JSON Formatı:** API istek ve yanıtları JSON formatındadır.
- **Modüler Yapı:** Flask backend flask_app klasöründe, Streamlit frontend streamlit_app klasöründe tutulur.

---

## Gereksinimler

1.	**Python 3.7+** (3.9 veya üstü önerilir)
2.	**Ollama CLI** (DeepSeek R1 modelini lokal olarak çalıştırmak için)
3.	**DeepSeek R1 (8B)** model dosyası (lokalde indirili olmalı)
4.	**Flask, Streamlit, Requests vb.** Python kütüphaneleri (details: requirements.txt)

> LLaMa 3.1 modeli, Ollama platformu üzerinden indirilebilir ve lokal makinede çalıştırılabilir. Aşağıdaki adımları takip ederek Ollama ve LLaMa 3.1 modelini yükleyip test edebilirsiniz.
> Ollama ve DeepSeek R1 (8B) model kurulum adımları için [ollama resmi dokümantasyonuna](https://ollama.com/library/deepseek-r1) göz atabilirsiniz.

---

# 🚀 Kurulum & Çalıştırma

## 1️⃣ Ollama ve DeepSeek R1 Modelini Kurun
LLaMa 3.1 modelini kullanabilmek için önce **Ollama CLI** aracını yüklemeniz gerekmektedir.

📌 macOS (Homebrew ile)
```bash
brew install ollama
```
📌 Linux (Debian / Ubuntu)
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
📌 Windows (Manuel Kurulum)
Windows kullanıcıları Ollama’yı aşağıdaki adımlarla yükleyebilir:

1. **Ollama’nın resmi yükleyicisini indirin:**  
   🔗 [Ollama Windows Yükleyicisi](https://ollama.com/download/windows)

2. **İndirilen `.exe` dosyasını çalıştırın ve yükleme adımlarını tamamlayın.**


Kurulum tamamlandıktan sonra terminali kapatıp yeniden açın ve aşağıdaki komut ile Ollama'nın başarıyla yüklendiğini doğrulayın:
```bash
ollama --version
```
Eğer şu şekilde bir çıktı alıyorsanız, Ollama başarıyla kurulmuştur:
```bash
ollama 0.1.20
```

## 2️⃣ LLaMa 3.1 Modelini İndirin
Ollama başarıyla kurulduktan sonra, LLaMa 3.1 (8B) modelini bilgisayarınıza indirmek için şu komutu çalıştırın:
```bash
ollama pull deepseek-r1:8b
```
Model başarıyla indirildiğinde, aşağıdaki komut ile yüklü modelleri listeleyebilirsiniz:
```bash
ollama list
```
Çıktı şu şekilde olmalıdır:
| NAME      | ID             | SIZE  | MODIFIED    |
|-----------|---------------|-------|------------|
| deepseek-r1:8b | 46e0c10c039e | 4.9 GB | .. minutes ago |

Bu, modelin başarıyla indirildiğini ve kullanılmaya hazır olduğunu gösterir.


## 3️⃣ Projeyi Klonlayın ve Çalıştırın
1. **Projeyi Klonlayın**
    ```bash
    git clone https://github.com/aliakkayamain/Akgun-Chatbox.git
    ```
    Şimdi projenin içine girin:
    ```bash
    cd Akgun-Chatbot
    ```

2. **Sanal Ortam Oluşturun ve Aktif Edin**
    ```bash
    python -m venv venv
    ```
    📌 Windows için
    ```bash
    venv\Scripts\activate
    ```
    📌 macOS/Linux için
    ```bash
    source venv/bin/activate
    ```

3. **Gerekli Kütüphaneleri Yükleyin**
    ```bash
    pip install -r requirements.txt
    ```

4. **Flask API’yi Başlatın**
    📌 Windows için
    ```bash
    set FLASK_APP=flask_app
    flask run
    ```
    📌 macOS/Linux için
    ```bash
    export FLASK_APP=flask_app
    flask run
    ```
Varsayılan olarak sunucu http://127.0.0.1:5000 adresinde çalışacaktır.

5. **Streamlit Arayüzünü Başlatın**
Flask API çalışmaya devam ederken, ayrı bir terminal penceresi açın ve yine proje kök dizininde şu komutu çalıştırın:
    ```bash
    streamlit run app.py
    ```
Bu komut, http://localhost:8501 adresinde Streamlit arayüzünü başlatacaktır. Tarayıcınız otomatik olarak açılmazsa, adresi elle girebilirsiniz.

Not: Hem Flask API hem de Streamlit uygulaması aynı anda çalışmalı; bu nedenle iki ayrı terminal veya süreç kullanmanız gerekir.
	•	Terminal 1: flask run
	•	Terminal 2: streamlit run app.py
---



---


---

# 📂 Proje Yapısı
```
AKGUN-CHATBOX/
│
├── __pycache__/         # Python tarafından derlenen bytecode dosyaları
│
├── docs/                # Dökümanlar ve ekran görüntüleri için ayrılmış klasör
│   └── images/          # Proje ile ilgili ekran görüntüleri
│
├── routes/              # API endpoint'lerini içeren klasör
│   ├── __pycache__/     # Python tarafından derlenen bytecode dosyaları
│   ├── chat.py          # "/chat" endpoint'ini tanımlayan kodlar
│   └── index.py         # "/" (root) endpoint'ini tanımlayan kodlar
│
├── .gitignore           # Git'e dahil edilmemesi gereken dosyaları belirleyen ayarlar
├── app.py               # Flask uygulamasının ana giriş noktası ve blueprint kayıtları
├── config.py            # Konfigürasyon ayarları (örn. DEBUG, PORT vb.)
├── README.md            # Proje dokümantasyonu
├── requirements.txt     # Proje bağımlılıklarının listesi (Flask vb.)
└── venv/                # Python sanal ortam (virtual environment) klasörü
```

---

# 📌 Geliştirme İpuçları

•	Flask ve Streamlit Ayrımı: Flask API flask_app içinde, Streamlit kodu streamlit_app içinde yer alır. Bu şekilde backend ve frontend mantığı ayrışır.
•	Ollama Model Seçimi: config.py içinde MODEL_NAME gibi bir değişken tanımlayarak farklı modelleri kolayca deneyebilirsiniz.
•	Hata Yönetimi: Hem API tarafında hem de Streamlit arayüzünde hata durumlarını yakalamak ve kullanıcıya anlamlı mesajlar döndürmek projenin kullanılabilirliğini artırır.


---

## 📬 İletişim  

•	Geliştirici: Ali Akkaya
•	E-posta: aliakkayamain@gmail.com
•	GitHub: aliakkayamain

Herhangi bir sorun veya katkıda bulunmak isterseniz lütfen iletişime geçmekten çekinmeyin!

Teşekkürler ve iyi çalışmalar!

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.