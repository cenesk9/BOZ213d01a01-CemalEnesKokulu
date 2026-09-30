# Tek ve Çift Sayı Bulucu
## Problem
Sisteme girilen sayının tek sayı mı, çift sayı mı olduğunu belirlemektir.
## Nasıl Kurulur ve Çalıştırılır?

1. Python'ı Yükleyin: Bilgisayarınızda Python yüklü değilse, [python.org](https://www.python.org) adresine giderek son sürümü indirip kurun. (Kurulum ekranında alt kısımdaki "Add Python to PATH" kutucuğunu işaretlemeyi unutmayın).
2. Kodu İndirin: Bu sayfanın sağ üst köşesindeki yeşil Code butonuna tıklayın ve Download ZIP seçeneğini seçerek dosyayı bilgisayarınıza indirin. İnen ZIP dosyasını klasöre çıkartın.
3. Programı Açın: Klasörün içindeki Python (.py uzantılı) dosyasına sağ tıklayın ve Edit with IDLE seçeneğini seçin.
4. Çalıştırın: Açılan pencerede üst menüden Run > Run Module yolunu izleyerek (veya doğrudan klavyeden F5 tuşuna basarak) programı başlatabilirsiniz. 
Artık sayı girmeye başlayabilirsin.

## Kod Nasıl Çalışır?
1. Kod ilk olarak kullanıcıdan bir sayı girmesini ister (input). Bu sayıyı tam sayıya çevirir (int).
2. Girilen sayının 2'ye tam bölünüp bölünmediğini kontrol eder.
3. Sayı 2'ye tam bölünüyorsa, yani kalan 0 ise (if), sistem girilen sayıyı çift sayı olarak belirler ve ekrana çift sayı olduğunu yazar (print).
4. Sayı 2'ye tam bölünmüyorsa, yani kalan 0'dan farklı ise (else), girilen sayıyı tek sayı olarak belirler ve ekrana tek sayı olduğunu yazar (print).
5. Kod bir döngüde çalışıyor (while True). Girilen sayının tek mi çift mi olduğunu belirledikten sonra tekrar bir sayı girmenizi istiyor ve kod çalışmaya devam ediyor.
6. Kodu bitirmek için kullanıcının 0 yazmasını ister ve döngüyü bozarak (break) programı bitirir.
