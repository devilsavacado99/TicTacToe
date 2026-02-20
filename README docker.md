# Tic Tac Toe Game - Docker Compose

## Explanations

### How to build the image
İmage, Dockerfile.tictactoe dosyasından oluşturulur. Direkt dockerfile dosyasından docker build command'i ile oluşturulabilir. Ancak docker-compose.yml dosyasında sahip olduğumuz için bu projede image'ı compose dosyasından docker compose run command'i ile oluşturabiliriz.

### How to run the game

Dockerfile'da oyunumuz için bize gereken her şeyi (dosyalar,kütüphane,yazılım dili vb.) ayarlamıştık zaten. Oyun kullanıcıdan input aldığı için compose'da stdin_open ve terminale ihtiyaç duyduğumuz için tty kullandık. Compose.yml dosyasında docker compose --profile dev run --rm tic-tac-toe-game-service_1 command'i ile oyunu oynayabiliriz.

### How to run tests

Testlerde kullanıcıdan input almadığımız ve terminale de ihtiyaç duymadığımız için compose dosyasındaki test service'ında stdin_open ve tty kullanmadık. Testleri "docker compose --profile dev run --rm tic-tac-toe-test-service_2" command'i ile çalıştırabiliriz.


### How to start development mode

Dockerfile'da Multi-stage kullandık, dev ve prod olmak üzere. Bu nedenle development modunu kullanabilmek için compose dosyasında target: dev olarak ayarlanmıştır. Bu modda oyunu oynamak için docker compose --profile dev up --build veya "docker compose --profile dev run --rm tic-tac-toe-game-service_1" command'i kullanılabilir. Compose up ve compose run arasındaki fark ise "up" compose.yml'de yer alan bütün servisleri default komutları ile kaldırmak için kullanılır; run ise compose.yml'deki hepsini değil sadece bazılarını kaldırmak için veya compose.yml'de yer alan default command'leri override etmek için kullanılır.

Testleri development kullanarak çalıştırmak için "docker compose --profile dev run --rm tic-tac-toe-test-service_2" kullanılabilir.

-rm kullanılmasının nedeni ise işi biten container'ın silinmesi amacını taşımaktadır. Her run edilişinde  yeni container kaldırıldığı için silinmeyen container'lar diskte yer kaplamaya devam edecektir.


### Why each volume exists

Dockerfile'da iki stage ayarladık: dev ve prod. Dev için ayarladığım stage'de host'ta olan dosyaları kopyalamadık. Peki dosyalar kopyalanmadıysa docker bunu nasıl görecek? Burada devreye compose.yml dosyasındaki volume giriyor. bind mount yaparak hosttaki kodun yer aldığı dizini container'a bağlarız, böylece Host’taki dosyalar birebir container’da görünür. Volume'de bize bu dosya dizinindeki verileri kalıcı hale getirmemize yarar. Bu nedenle dev stage'i için "- ./app:/tic_tac_toe_app/app:rw"
      "- ./tests:/tic_tac_toe_app/tests:rw" volumlerini kullandık.


### Difference between:Dockerfile CMD vs Compose command

Dockerfile'da CMD ile container ayağa kalktığında yapmasını istediğimiz komutu veririz. CMD, docker run veya compose command ile override edilebilir, ancak override edilmezse default olarak cmd çalışır.

### Environment Variables

Environment Variables, uygulama yaparken anahtar-değer çiftleri olarak yardımcı olurlar. Bir dosya dizini,URL veya parola verilmesini elle yapmak yerine env var olarak tanımlarız ve bu bize otomasyon sağlar. Ayrıca bazen bunların compose.yml'de görünmesini gizlilik nedeniyle de istemeyiz. Bu nedenle env var kullanırız. Ben, bu projede bu çiftlerden nasıl yararlanacağımı tam olarak bilemediğim için kullanmadığım bir variable tanımladım.