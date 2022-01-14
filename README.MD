# Скрипты для работы с Evernote Cloud API 

## Что необходимо
1) Python2 должен быть уже установлен. Затем используйте pip для установки зависимостей:
```python
pip install -r requirements.txt
```
2) Получить токен на https://dev.evernote.com/.
3) Создать в папке проекта файл `.env`, прописать в нем переменные окружения:
- `EVERNOTE_PERSONAL_TOKEN` - токен Evernote Cloud API;
- `SANDBOX` - тип токена (`true` - для "песочницы", `false` - для реального использования)
- `INBOX_NOTEBOOK_GUID` - глобальный уникальный идентификатор (GUID) блокнота;
- `JOURNAL_TEMPLATE_NOTE_GUID` - GUID заметки, которая будет использована в качестве шаблона;
- `JOURNAL_NOTEBOOK_GUID` - GUID блокнота в который будет добавлена новая заметка.

## list_notebooks.py
Запустите скрипт командой:
```python
python2 list_notebooks.py
 ```
В консоль выведутся ваши блокноты (GUID и название).
## dump_inbox.py
Запустите скрипт командой:
```python
python2 dump_inbox.py {количество заметок}
```
В консоль выведутся заметки из блокнота указанного в переменной окружения `INBOX_NOTEBOOK_GUID`.
Передавать количество заметок необязательно, по умолчанию выведится 10 шт.
## add_note2journal.py
Запустите скрипт командой:
```python
python2 add_note2journal.py {дата в формате YYYY-MM-DD}
```
В блокноте, указанном в `JOURNAL_NOTEBOOK_GUID` будет создана заметка по шаблону, указанном в `JOURNAL_TEMPLATE_NOTE_GUID`.
Передавать дату необязательно, по умолчанию используется текущая дата.


