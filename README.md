## Описание:
Тестовое задание для https://codingteam.ru/
## Задание:

``` 
Стек Django\DRF
Даны модели "Категория Блюд" и "Блюдо" для ресторана.

Даны сериализаторы.

В выборку попадают только Блюда у которых is_publish=True.
Если в категории нет блюд (или все блюда данной категории 
имеют is_publish=False) - не включаем ее в выборку.

Запрос в БД сделать любым удобным способом:
Django ORM (предпочтительно), Raw SQL, Sqlalchemy... 

Написать View который вернет для API 127.0.0.1/api/v1/foods/ 
  ```

## Установка

```shell
git clone https://github.com/Eclipsium/codingTeam
cd codingTeam
pip intall -r requirements.txt
export ENV=DEV

./python manage.py runserver
```

## Админка
```
admin admin
```
## Тесты
```shell
./manage.py test
```

