# Merhabalar

## Öncelikle inventory içerisinde settings.py girip DATABASES alanını güncelleyin.

## Sonrasında ise sırayla aşağıdaki kodları terminale yazın
python manage.py makemigrations
python manage.py migrate
## Bu kodlar ile veritabanına tabloları açabilmekteyiz. Aşağıdaki kodla ise bir adet superuser oluşturmaktayız
python manage.py createsuperuser
## Superuser oluşturduktan sonra ise aşağıdaki kod ile projeyi derleyiniz
python manage.py runserver
## Derleme yapıldıktan sonra admin paneline gitmemiz gerekmektedir.
http://127.0.0.1:8000/admin veya http://localhost:8000/admin bu siteler portlara göre değişebilir.
Önemli olan /admin eklemektir. Ekleme yaptıktan sonra kullanıc ile girip inventory alanından envantere ürün ekleyebiliriz.
