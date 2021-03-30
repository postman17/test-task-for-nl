# test-task-for-nl
## Установка
- copy .env.example to .env
- docker-compose up
##Условия
######	Дана модель предметной области с сущностями:
- Страница(Page) 
- Контент типа видео (Video)
-	специфичные атрибуты: ссылка на видеофайл, ссылка на Файл субтитров о Контент типа эудио(Audio)
-	специфичные атрибуты: битрейт в количестве бит в секунду о Контент типа текст (Text)
-	специфичные атрибуты: поле для хранение текста произвольной длинны
######	Нужно учитывать, что специфичные атрибуты разных видов контента существенно различаются.
######	У всех видов контента присутствует атрибут "счетчик просмотров" (counter).
######	У всех видов контента и страниц есть атрибут "заголовок" (title).
######	Со страницей может быть связан любой вид контента в любом количестве. Семантика такая: “на страницу можно выложить любой вид контента в любом количестве". Например: на странице может быть 5 видео, 3 аудио и 7 текстов в любом порядке и в перемешку.
- Следует учитывать, что в будущем виды контента могу добавляться и функционал должен легко расширяться.
##Функциональные требования
######	Сделать API для получения списка всех страниц.
- Должна поддерживаться пагинация (постраничная выдача результатов) 
- В ответе должен содержаться URL на API с детальной информацией о странице (пункт №2).
######	Сделать API для получения детальной информации о странице
- Помимо атрибутов страницы в ответе должны содержаться все привязанные к странице объекты контента в виде вложенной структуры - упорядоченного списка привязанных к странице объектов контента со всеми атрибутами, включая специфичные.
######	При обращении к API с деталями о странице счетчик просмотров каждого объекта контента, привязанного к странице должен увеличиваться на единицу.
- Нагрузка на данное API предполагается существенная, поэтому желательно непосредственно изменение данных в БД реализовать в фоновой задаче, 
- Важно обратить внимание, что увеличение счетчика должно происходить строго атомарно. То есть, если две задачи параллельно обновляют счетчик одного объекта, то на выходе всегда должно получаться "+2".
######	Заведение страниц и привязка к ним контента должна выполняться через админку.
- Должен поддерживаться поиск по заголовку (title) страниц и контента (по частичному совпадению от начала).
- Желательно для удобства реализовать привязку и управление контентом на странице в виде inline-блоков в разделе управления страницей (Раде) в админке, 
- Желательно, чтобы была возможность задавать порядок выдачи в API объектов, привязанных к странице.
