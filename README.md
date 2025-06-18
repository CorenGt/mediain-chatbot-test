# Mediain Chatbot Test

Bu proje, tıbbi metinler ve genel sohbet için geliştirilmiş bir Flask tabanlı chatbot uygulamasıdır. Kullanıcılar hem selamlaşma ve genel sohbet edebilir, hem de tıbbi içerikli mesajlar yazarak olası hastalık tahminleri ve tıbbi terim tanımlamaları alabilirler.

## Özellikler
- **Genel Sohbet:** Microsoft DialoGPT-small modeli ile doğal dilde sohbet edebilirsiniz.
- **Tıbbi Analiz:**
  - [MASK] veya <mask> içeren cümlelerde Bio_ClinicalBERT ile olası hastalık/koşul tahmini.
  - d4data/biomedical-ner-all modeli ile tıbbi terimlerin tanımlanması.
- **Web Arayüzü:** Basit ve kullanıcı dostu bir arayüz ile mesajlaşma imkanı.

## Kullanılan Teknolojiler
- Python 3
- Flask
- Hugging Face Transformers
  - microsoft/DialoGPT-small
  - emilyalsentzer/Bio_ClinicalBERT
  - d4data/biomedical-ner-all
- HTML/CSS (Basit arayüz için)

## Kurulum
1. **Depoyu klonlayın:**
   ```bash
   git clone <repo-link>
   cd mediain-chatbot-test
   ```
2. **Gerekli paketleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```
   veya manuel olarak:
   ```bash
   pip install flask transformers
   ```
3. **Uygulamayı başlatın:**
   ```bash
   python app.py
   ```
4. **Tarayıcıdan erişin:**
   
   `http://127.0.0.1:5000/`

## Kullanım
- Ana sayfada mesajınızı yazıp gönderin.
- Selamlaşma veya genel sohbet için klasik ifadeler kullanabilirsiniz ("hello", "hi", "how are you" gibi).
- Tıbbi analiz için sağlıkla ilgili bir cümle yazabilirsiniz. Örneğin:
  - "I have a headache and fever."
  - "Shortness of breath could be a sign of [MASK]."

## Notlar
- Bu uygulama tıbbi teşhis koymaz, sadece bilgilendirme amaçlıdır. Lütfen sağlık sorunlarınız için bir doktora danışın.
- Modellerin ilk yüklenmesi internet bağlantısı gerektirir ve birkaç dakika sürebilir.

## Katkı
Katkıda bulunmak isterseniz, lütfen bir pull request açın veya issue oluşturun.

## Lisans
MIT Lisansı 
