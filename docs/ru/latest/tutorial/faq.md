# Несколько ответов на часто задаваемые вопросы

## asyncio

В этом разделе будет очень краткое и простое описание работы с модулем **asyncio** и простые рекомендации по решению проблем с блокировкой.

## Что такое coroutine?

Coroutine — это функция (сопрограмма), которую необходимо вызывать через **await**.

Когда выполнение кода в Python достигает **await**, он прекращает выполнение этой функции и возвращается к ней до тех пор, пока не выполнит другие сопрограммы и не выйдет из этой функции.

Благодаря такому подходу программа может выполнять несколько задач одновременно без использования потоков.
а следовательно, будет экономия ресурсов железа и высокая производительность.

### Не забудьте написать `await` перед функцией `async`, иначе она не запустится

```python
import asyncio

async def get_cat() -> str: return "cat"

async def main():
    print(get_cat())  # <coroutine object get_cat at 0x...>
    print(await get_cat())  # cat

asyncio.run(main())
```

## Где писать await?

Вам нужно писать **await** только внутри **async** функций и нигде больше.

```python
# bad
async def bar() -> str: return "bar"

def main():
    print(await bar()) 
    # Syntax ^ Error: 'await' outside async function

main()
```

```python
# bad
async def main():
    print("main")

await main()  # SyntaxError: 'await' outside function
```

```python
# good
import asyncio

async def bar() -> str: return "bar"

async def main():
    print(await bar())

asyncio.run(main())
```

## Как получить клиентский cookie

Самый простой способ — использовать расширение [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg) (нужный файл cookie — `_fox_session`), или вы можете использовать наш метод `get_cookie(browser)`.

## Как отправить запрос, которого нет в нашем фреймворке

Чтобы отправить какой-нибудь необычный запрос, используйте `Client` метод, который называется `custom_request()`, вот пример его использования:

```python
from foxford import get_cookie
from foxford import Client
import asyncio

client = Client("token")

async def main():
    objectives = await client.custom_request(
        "GET", 
        "https://foxford.ru/api/user/objectives"
    )
    # писать каждую задачу в переменной objectives
    for objective in objectives:
        print(f"Задача №{objectives.index(objective)+1}") # +1 cuz python lmao
        print("=================================")
        print(objective["title"])
        print(objective["subtitle"])
        print("=================================")

asyncio.run(main())
```
## Примеры из этой части туториала

* [custom_request.py](https://github.com/FrostX-Official/foxford/blob/main/examples/custom_request.py)