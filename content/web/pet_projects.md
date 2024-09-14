---
weight: 1
title: Проекты
description: Самостоятельные проекты для портфолио
author: MLabs
authorLink: null
date: 2024-09-11T14:48:57.920Z
lastmod: null
slug: projects
categories:
  - WEB
math: true
lightgallery: true
toc:
  auto: false
draft: false
---

## Pet projects

### Counter

![Counter](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fegsodt4dyfekiwp8ln4q.png "Counter")

**Описание:** Этот проект представляет собой простой счетчик, который позволяет пользователям увеличивать и уменьшать числовое значение, отображаемое на экране. Кроме того, проект включает кнопку для сброса счетчика на ноль.

**Концепции обучения:**

- Манипулирование DOM: Работа с элементами HTML с помощью JavaScript, включая получение доступа к ним и их изменение.
- Обработка событий: Перехват пользовательских действий (например, кликов мыши) и выполнение соответствующих действий с помощью JavaScript.
- Основные функции JavaScript: Создание функций для выполнения различных задач, таких как увеличение, уменьшение и сброс значения счетчика.

{{< admonition info "Пример реализации" false >}}

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>Counter | DOM Projects</title>
  </head>
  <body>
    <main>
      <h2>Counter</h2>
      <h1 id="counter-value" contenteditable="true">0</h1>
      <section class="btn-area">
        <button class="btn decrease">-</button>
        <button class="btn reset">&#x21bb;</button>
        <button class="btn increase">+</button>
      </section>
    </main>

    <script src="./script.js"></script>
  </body>
</html>
```

```css
@import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Raleway', Fallback, sans-serif;
  font-size: 16px;
}

body {
  display: flex;
  height: 100vh;
  margin: 0 20;
  justify-content: center;
  align-items: center;
  background-color: #f8f9fc;
}

main {
  text-align: center;
}

main h2 {
  font-size: 50px;
  font-weight: 500;
  margin-bottom: 5px;
}

main h1 {
  font-size: 48px;
  font-weight: 400;
  margin-bottom: 10px;
  display: inline-block;
  padding: 3px 10px;
  border-radius: 2px;
  background-color: rgba(162, 187, 241, 0.425);
}

.btn-area {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.btn-area .btn {
  font-size: 1.8em;
  height: 100%;
  width: 100%;
  padding: 5px 30px;
  margin: 0 10px;
  border: none;
  background: rgba(46, 59, 230, 0.781);
  color: white;
  border-radius: 3px;
  cursor: pointer;
}

button:active {
  transform: scale(0.98);
}
```

```js
const counterValue = document.getElementById("counter-value");
const allBtn = document.querySelectorAll(".btn");


allBtn.forEach((btn) => {
    btn.addEventListener("click", function (e) {
        btnClass = e.target.classList;

        let count = Number(counterValue.innerText);
        if (btnClass.contains("increase")) {
            count++;
        } else if (btnClass.contains("decrease")) {
            count--;
        } else if (btnClass.contains("reset")) {
            count = 0;
        }

        if (count > 0) {
            counterValue.style.color = "green";
        } else if (count < 0) {
            counterValue.style.color = "red";
        } else {
            counterValue.style.color = "black";
        }

        counterValue.innerText = count;
    });
});
```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

#### HTML

HTML-код создает основную структуру страницы:

1. **Основные элементы:**
   - `h2` — заголовок "Counter".
   - `h1` с `id="counter-value"` — элемент, отображающий текущее значение счетчика. Значение по умолчанию установлено в `0`, и этот элемент может быть редактируемым пользователем (`contenteditable="true"`).
   - `section` с классом `btn-area` содержит три кнопки:
     - Кнопка с классом `decrease` (`-`) — для уменьшения значения.
     - Кнопка с классом `reset` (↻) — для сброса значения.
     - Кнопка с классом `increase` (`+`) — для увеличения значения.

2. **Подключение JavaScript:**
   - `<script src="./script.js"></script>` подключает файл JavaScript, который будет управлять логикой счетчика и обработкой событий.

#### CSS

CSS стилизует элементы страницы и улучшает внешний вид интерфейса:

1. **Основные стили:**
   - Основные стили для страницы (`body`) задают фон, шрифт, и выравнивание элементов по центру.
   - Стили для контейнера `main` делают текст выровненным по центру и задают размер заголовка `h2` и значения счетчика `h1`.
   - Стили для кнопок (`.btn`) определяют размеры, цвет фона, цвет текста, закругленные углы и анимацию при нажатии.

#### JavaScript

JavaScript отвечает за обработку событий и изменение значения счетчика. Рассмотрим код подробнее:

1. **Получение элементов DOM:**
   - `const counterValue = document.getElementById("counter-value");` — получает элемент `h1`, отображающий текущее значение счетчика.
   - `const allBtn = document.querySelectorAll(".btn");` — получает все кнопки с классом `btn` (уменьшение, увеличение и сброс).

2. **Обработка событий:**
   - Используется метод `forEach` для перебора всех кнопок и добавления обработчика событий `click` для каждой кнопки:
     ```js
     allBtn.forEach((btn) => {
         btn.addEventListener("click", function (e) {
             ...
         });
     });
     ```
   - При нажатии на любую из кнопок вызывается функция, которая определяет, какая кнопка была нажата (используется `e.target.classList`).

3. **Логика изменения значения:**
   - В зависимости от класса нажатой кнопки (`increase`, `decrease`, `reset`), функция увеличивает, уменьшает или сбрасывает значение счетчика:
     ```js
     if (btnClass.contains("increase")) {
         count++;
     } else if (btnClass.contains("decrease")) {
         count--;
     } else if (btnClass.contains("reset")) {
         count = 0;
     }
     ```

4. **Изменение цвета в зависимости от значения счетчика:**
   - Если значение счетчика положительное, его цвет устанавливается в зеленый. Если отрицательное — в красный. Если счетчик равен нулю, цвет остается черным:
     ```js
     if (count > 0) {
         counterValue.style.color = "green";
     } else if (count < 0) {
         counterValue.style.color = "red";
     } else {
         counterValue.style.color = "black";
     }
     ```

5. **Обновление значения счетчика:**
   - После всех вычислений обновляется текст внутри элемента `h1` с новым значением счетчика:
     ```js
     counterValue.innerText = count;
     ```

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

#### 1. **Добавление инкремента и декремента по шагу**
- **Описание:** Введение возможности увеличения или уменьшения значения счетчика на заданное число (например, +5 или -5) вместо стандартного шага в 1.
- **Цель:** Практика работы с атрибутами HTML и их изменением с помощью JavaScript.
- **Реализация:** Добавить поле ввода, в котором пользователь сможет указать шаг изменения, и обновить логику обработки событий для использования этого значения.

#### 2. **Добавление функционала хранения данных в локальном хранилище (localStorage)**
- **Описание:** Сохранение текущего значения счетчика в `localStorage` браузера, чтобы оно сохранялось между сессиями.
- **Цель:** Изучение работы с локальным хранилищем браузера.
- **Реализация:** При изменении значения счетчика обновлять данные в `localStorage`, а при загрузке страницы проверять наличие сохраненного значения и восстанавливать его.

#### 3. **Реализация ограничения на минимальное и максимальное значения счетчика**
- **Описание:** Установить ограничения на минимальное и максимальное значения счетчика (например, от -10 до 10).
- **Цель:** Изучение использования условных операторов и логики для валидации ввода.
- **Реализация:** Добавить проверку в обработчик событий, чтобы не позволять пользователю превышать установленные пределы, и выводить предупреждающее сообщение.

#### 4. **Добавление анимаций при изменении значения**
- **Описание:** Введение анимаций при изменении значения счетчика, например, плавное увеличение или уменьшение числа.
- **Цель:** Изучение работы с CSS-анимациями и их активацией с помощью JavaScript.
- **Реализация:** Добавить CSS-анимации для изменения цвета, размера текста или других стилей и запускать их в обработчиках событий.

#### 5. **Создание визуальной диаграммы изменений**
- **Описание:** Добавление диаграммы или графика, который отображает изменения значений счетчика в реальном времени.
- **Цель:** Изучение работы с библиотеками для построения графиков, таких как Chart.js.
- **Реализация:** Использовать массив для хранения всех изменений значения счетчика и обновлять график при каждом изменении.

#### 6. **Добавление таймера для автоматического изменения значения счетчика**
- **Описание:** Создать таймер, который будет автоматически увеличивать или уменьшать значение счетчика через заданный интервал времени.
- **Цель:** Практика работы с функцией `setInterval` и `clearInterval`.
- **Реализация:** Добавить кнопку для запуска и остановки таймера, который будет автоматически изменять значение счетчика с определенной частотой.

#### 7. **Реализация звукового сопровождения**
- **Описание:** Добавить звуковые эффекты при нажатии кнопок (увеличение, уменьшение, сброс).
- **Цель:** Изучение работы с аудио в браузере.
- **Реализация:** Использовать API Audio для воспроизведения звуков при каждом действии пользователя.

#### 8. **Поддержка горячих клавиш для управления счетчиком**
- **Описание:** Реализовать управление счетчиком с помощью горячих клавиш (например, стрелки вверх/вниз для увеличения/уменьшения, клавиша `R` для сброса).
- **Цель:** Практика работы с обработчиками событий клавиатуры.
- **Реализация:** Добавить глобальный обработчик события `keydown` и проверить, какая клавиша была нажата, чтобы выполнить соответствующее действие.

#### 9. **Создание пользовательского интерфейса с помощью CSS Grid или Flexbox**
- **Описание:** Улучшение пользовательского интерфейса счетчика с использованием CSS Grid или Flexbox для лучшего расположения элементов.
- **Цель:** Закрепление навыков работы с современными методами создания макетов.
- **Реализация:** Переработать существующий макет, используя CSS Grid или Flexbox, чтобы сделать интерфейс более адаптивным и визуально приятным.

#### 10. **Добавление функции сброса по таймеру**

- **Описание:** Реализовать возможность сброса счетчика через определенный промежуток времени.
- **Цель:** Практика работы с функциями `setTimeout` и `clearTimeout`.
- **Реализация:** Добавить кнопку, которая запускает таймер для сброса значения через заданный промежуток времени.

{{< /admonition >}}

### DadJokes

![DadJokes](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fz09wwb70arrb5ccjhl87.png "DadJokes")

**Описание:** Проект использует внешний API для получения случайных шуток про отца с использованием асинхронных методов на JavaScript. После получения данные отображаются на веб-странице в виде шутки для развлечения пользователей.

**Концепции обучения:**

- Асинхронное программирование: Работа с операциями, требующими времени для завершения (например, получение данных из API), без блокировки основного потока выполнения в JavaScript.
- Fetch API: Использование встроенных функций браузера для выполнения HTTP-запросов к API и получения данных.
- Работа с API: Взаимодействие с внешними API для доступа к данным или функциональным возможностям, предоставляемым этими сервисами.

{{< admonition info "Пример реализации" false >}}

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>DadJokes | DOM Projects</title>
  </head>
  <body>
    <div class="container">
      <h3>Don't Laugh Challenge</h3>
      <div class="jokesDiv">Getting Jokes..</div>
      <button class="jokesGeneratorBtn">Get Another Joke</button>
    </div>

    <script src="./script.js"></script>
  </body>
</html>
```

```css
@import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Raleway', Fallback, sans-serif;
  font-size: 16px;
}

body {
  background-color: #f8f9fc;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 20px;
}

.container {
  text-align: center;
  background-color: #fff;
  padding: 50px;
  border-radius: 14px;
  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.1);
  min-width: 200px;
  border: 1px solid lightgray;
}

.container h3 {
  font-weight: 400;
  font-size: 22px;
  color: rgb(136, 136, 138);
  margin-bottom: 35px;
}

.jokesDiv {
  font-size: 30px;
  letter-spacing: 1px;
  line-height: 40px;
  margin: 50px auto;
  max-width: 800px;
}

.jokesGeneratorBtn {
  border: none;
  outline: none;
  border-radius: 10px;
  font-size: 1rem;
  padding: 13px 45px;
  color: #f8f8f8f6;
  background-color: rgb(95, 95, 255);

  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.jokesGeneratorBtn:active {
  transform: scale(0.98);
}

.jokesGeneratorBtn:focus {
  outline: 0;
}

.jokesGeneratorBtn:disabled {
  opacity: 0.5;
  cursor: wait;
}
```

```js
const jokesDiv = document.querySelector(".jokesDiv");
const generatorBtn = document.querySelector(".jokesGeneratorBtn");

const url = "https://icanhazdadjoke.com/";
let timer_on = 10000;
let interval;

function startInterval(){
  interval = setInterval(generateJokes, timer_on);
}

async function generateJokes() {
  generatorBtn.setAttribute("disabled", "disabled");

  try {
    const response = await fetch(url, {
      headers: {
        Accept: "application/json",
      },
    });
    const joke = await response.json();

    jokesDiv.innerHTML = joke.joke;
  } catch {
    jokesDiv.innerHTML = "Error getting jokes";
  } finally {
    generatorBtn.removeAttribute("disabled");
  }
}

generateJokes();
startInterval()



generatorBtn.addEventListener("click", function () {
  generateJokes();
  clearInterval(interval)
  startInterval()

});
```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

#### HTML

HTML-код создает базовую структуру страницы:

1. **Основные элементы:**
   - `h3` — заголовок "Don't Laugh Challenge".
   - `div` с классом `jokesDiv` — элемент, в котором отображается текст шутки. Изначально в нем отображается "Getting Jokes...".
   - `button` с классом `jokesGeneratorBtn` — кнопка для получения новой шутки.

2. **Подключение JavaScript:**
   - `<script src="./script.js"></script>` подключает файл JavaScript, который будет отвечать за получение и отображение шуток.

#### CSS

CSS оформляет элементы страницы для улучшения внешнего вида:

1. **Основные стили:**
   - Стили для всего тела (`body`), чтобы разместить элементы по центру страницы и задать им фон.
   - Оформление контейнера `.container`, где находятся заголовок, шутка и кнопка, с использованием тени, закругленных углов и внутреннего отступа.
   - Стили для `.jokesDiv` делают текст шутки крупным и хорошо читаемым.
   - Кнопка `.jokesGeneratorBtn` имеет стили для изменения цвета, формы и анимации при нажатии.

#### JavaScript

JavaScript отвечает за взаимодействие с API и обработку событий. Рассмотрим код подробнее:

1. **Получение элементов DOM:**
   - `const jokesDiv = document.querySelector(".jokesDiv");` — получает элемент `div`, в котором будет отображаться шутка.
   - `const generatorBtn = document.querySelector(".jokesGeneratorBtn");` — получает кнопку для генерации новой шутки.

2. **Установка URL API и таймера:**
   - `const url = "https://icanhazdadjoke.com/";` — URL API, который возвращает случайную шутку.
   - `let timer_on = 10000;` — интервал в миллисекундах (10 секунд), через который будет автоматически генерироваться новая шутка.
   - `let interval;` — переменная для хранения интервала таймера.

3. **Функция для запуска интервала:**
   - `function startInterval() { interval = setInterval(generateJokes, timer_on); }` — функция для запуска интервала, который вызывает `generateJokes` каждые 10 секунд.

4. **Асинхронная функция для получения шуток:**
   - `async function generateJokes()` — асинхронная функция для получения данных шутки из API.
   - В начале функция отключает кнопку, чтобы предотвратить повторные нажатия во время выполнения запроса:
     ```js
     generatorBtn.setAttribute("disabled", "disabled");
     ```
   - Функция выполняет HTTP-запрос с использованием `fetch` и передает заголовок, чтобы получить данные в формате JSON:
     ```js
     const response = await fetch(url, {
       headers: {
         Accept: "application/json",
       },
     });
     const joke = await response.json();
     ```
   - Если запрос проходит успешно, текст шутки отображается в `jokesDiv`. Если произошла ошибка, выводится сообщение об ошибке:
     ```js
     jokesDiv.innerHTML = joke.joke;
     // или, в случае ошибки:
     jokesDiv.innerHTML = "Error getting jokes";
     ```
   - В блоке `finally` кнопка снова активируется для пользователя:
     ```js
     generatorBtn.removeAttribute("disabled");
     ```

5. **Запуск первой шутки и интервала:**
   - `generateJokes();` — вызывается для получения первой шутки при загрузке страницы.
   - `startInterval();` — запускает интервал, чтобы автоматически получать новые шутки каждые 10 секунд.

6. **Обработчик события для кнопки:**
   - `generatorBtn.addEventListener("click", function () { ... });` — добавляет обработчик события для кнопки. При нажатии на кнопку:
     - Снова вызывается функция `generateJokes()`.
     - Сбрасывается текущий интервал таймера и запускается новый, чтобы отсчет начинался заново после каждого нажатия.

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

#### 1. **Добавление функции поиска шуток по ключевому слову**

- **Описание:** Позволить пользователям искать шутки, используя ключевые слова.
- **Цель:** Практика работы с параметрами запросов в API и обработка пользовательского ввода.
- **Реализация:** Добавить поле ввода для ключевых слов и кнопку поиска. При нажатии кнопки отправлять запрос к API с ключевым словом и отображать результаты.

#### 2. **Добавление кнопки для сохранения избранных шуток**
- **Описание:** Возможность сохранять любимые шутки в избранное.
- **Цель:** Закрепление навыков работы с `localStorage` или `sessionStorage` для хранения данных на стороне клиента.
- **Реализация:** Добавить кнопку "Добавить в избранное" рядом с каждой шуткой. При нажатии на кнопку шутка сохраняется в `localStorage`, и пользователь может просмотреть все избранные шутки в отдельном разделе.

#### 3. **Реализация функции "Поделиться шуткой"**
- **Описание:** Возможность поделиться шуткой через социальные сети или скопировать её в буфер обмена.
- **Цель:** Изучение работы с API социальных сетей и API буфера обмена.
- **Реализация:** Добавить кнопки "Поделиться" для каждой шутки с опциями для Twitter, Facebook и копирования текста в буфер обмена.

#### 4. **Добавление анимаций и визуальных эффектов**
- **Описание:** Использование анимаций для отображения новой шутки или избранных шуток.
- **Цель:** Изучение CSS-анимаций и их динамического включения с помощью JavaScript.
- **Реализация:** Добавить анимацию при появлении новой шутки, используя CSS и JavaScript для управления классами и стилями.

#### 5. **Добавление таймера для автоматического обновления шуток**
- **Описание:** Возможность включить таймер, который будет автоматически запрашивать новую шутку через заданный интервал времени.
- **Цель:** Практика работы с функциями `setInterval` и `clearInterval`.
- **Реализация:** Добавить кнопку для включения/выключения таймера. При нажатии на кнопку шутки будут автоматически обновляться каждые несколько секунд или минут.

#### 6. **Реализация офлайн-режима**
- **Описание:** Кэширование шуток для их отображения в офлайн-режиме.
- **Цель:** Изучение использования Service Workers и кэширования данных в браузере.
- **Реализация:** Настроить Service Worker для кэширования данных API, чтобы шутки были доступны, даже если пользователь потеряет подключение к интернету.

#### 7. **Добавление рейтинговой системы для шуток**
- **Описание:** Возможность оценивать шутки (например, лайки или звезды).
- **Цель:** Изучение работы с элементами интерфейса и взаимодействие с сервером или локальным хранилищем для сохранения рейтингов.
- **Реализация:** Добавить кнопки для оценки каждой шутки и отобразить общий рейтинг рядом с каждой шуткой.

#### 8. **Добавление режима "Тёмная тема"**
- **Описание:** Добавление переключателя между светлой и тёмной темами интерфейса.
- **Цель:** Практика работы с темами и изменением CSS-переменных или классов.
- **Реализация:** Добавить переключатель на странице, который изменяет тему с помощью CSS-переменных или добавления/удаления классов.

#### 9. **Поддержка мультиязычности**
- **Описание:** Возможность выбирать язык интерфейса и шуток.
- **Цель:** Изучение работы с API, поддерживающими мультиязычность, и навыки интернационализации интерфейсов.
- **Реализация:** Добавить переключатель языка, который будет изменять язык интерфейса и отправлять запросы к API с параметром языка.

#### 10. **Добавление прогрессивного загрузчика**
- **Описание:** Показать прогресс загрузки при получении новой шутки.
- **Цель:** Изучение управления асинхронными запросами и визуальной обратной связи.
- **Реализация:** Добавить индикатор загрузки (например, спиннер) для отображения прогресса загрузки данных из API.

#### 11. **Добавление голосового вывода шуток**

- **Описание:** Возможность воспроизведения шуток голосом.
- **Цель:** Изучение работы с Web Speech API для текстового синтеза речи.
- **Реализация:** Использовать Web Speech API для чтения шутки вслух по нажатию кнопки.

{{< /admonition >}}

### Random Dog

**Описание:** Проект предназначен для получения случайных изображений собак из внешнего API с использованием асинхронных методов на JavaScript. Полученные изображения отображаются на веб-странице в качестве развлечения для пользователей.

**Концепции обучения:**

- Асинхронное программирование: Обработка операций, требующих времени для завершения (например, получение данных из API), без блокировки основного потока выполнения в JavaScript.
- Fetch API: Использование встроенных функций браузера для выполнения HTTP-запросов к API и получения данных.
- Работа с API: Взаимодействие с внешними API для доступа к данным или функциональным возможностям, предоставляемым этими сервисами.

{{< admonition info "Пример реализации" false >}}

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>Random Dog Image | DOM Projects</title>
  </head>
  <body>
    <div class="container">
      <h3>Random Dog Image Generator</h3>
      <div class="imageDiv"><img id="dogImage" src="" alt="Random Dog" /></div>
      <button class="imageGeneratorBtn">Get Another Image</button>
    </div>

    <script src="./script.js"></script>
  </body>
</html>
```

```css
@import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Raleway', Fallback, sans-serif;
  font-size: 16px;
}

body {
  background-color: #f8f9fc;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 20px;
}

.container {
  text-align: center;
  background-color: #fff;
  padding: 50px;
  border-radius: 14px;
  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.1);
  min-width: 200px;
  border: 1px solid lightgray;
}

.container h3 {
  font-weight: 400;
  font-size: 22px;
  color: rgb(136, 136, 138);
  margin-bottom: 35px;
}

.imageDiv {
  margin: 50px auto;
  max-width: 400px;
  max-height: 400px;
  overflow: hidden;
}

.imageDiv img {
  width: 100%;
  height: auto;
  display: block;
}

.imageGeneratorBtn {
  border: none;
  outline: none;
  border-radius: 10px;
  font-size: 1rem;
  padding: 13px 45px;
  color: #f8f8f8f6;
  background-color: rgb(95, 95, 255);

  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.imageGeneratorBtn:active {
  transform: scale(0.98);
}

.imageGeneratorBtn:focus {
  outline: 0;
}

.imageGeneratorBtn:disabled {
  opacity: 0.5;
  cursor: wait;
}
```

```js
const imageDiv = document.querySelector(".imageDiv");
const generatorBtn = document.querySelector(".imageGeneratorBtn");
const dogImage = document.getElementById("dogImage");

const url = "https://dog.ceo/api/breeds/image/random";
let timer_on = 10000;
let interval;

function startInterval() {
  interval = setInterval(generateImage, timer_on);
}

async function generateImage() {
  generatorBtn.setAttribute("disabled", "disabled");

  try {
    const response = await fetch(url);
    const data = await response.json();

    dogImage.src = data.message; // Устанавливаем источник изображения на URL, полученный из API
  } catch {
    imageDiv.innerHTML = "Error getting image";
  } finally {
    generatorBtn.removeAttribute("disabled");
  }
}

generateImage();
startInterval();

generatorBtn.addEventListener("click", function () {
  generateImage();
  clearInterval(interval);
  startInterval();
});
```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

#### HTML

1. **Основные элементы:**
   - `h3` — заголовок "Random Dog Image Generator".
   - `div` с классом `imageDiv` — элемент, содержащий изображение случайной собаки. Изначально в элементе `img` установлено пустое значение `src`.
   - `button` с классом `imageGeneratorBtn` — кнопка для получения нового изображения.

2. **Подключение JavaScript:**
   - `<script src="./script.js"></script>` подключает файл JavaScript, который будет отвечать за получение и отображение изображения.

#### CSS

1. **Основные стили:**
   - Стили для всего тела (`body`), чтобы разместить элементы по центру страницы и задать им фон.
   - Оформление контейнера `.container`, где находятся заголовок, изображение и кнопка, с использованием тени, закругленных углов и внутреннего отступа.
   - Стили для `.imageDiv` делают изображение адаптивным и ограничивают его размер.
   - Кнопка `.imageGeneratorBtn` имеет стили для изменения цвета, формы и анимации при нажатии.

#### JavaScript

1. **Получение элементов DOM:**
   
   - `const imageDiv = document.querySelector(".imageDiv");` — получает контейнер для изображения.
   - `const generatorBtn = document.querySelector(".imageGeneratorBtn");` — получает кнопку для генерации нового изображения.
   - `const dogImage = document.getElementById("dogImage");` — получает элемент `img` для отображения изображения.
   
2. **Установка URL API и таймера:**
   - `const url = "https://dog.ceo/api/breeds/image/random";` — URL API, который возвращает случайное изображение собаки.
   - `let timer_on = 10000;` — интервал в миллисекундах (10 секунд), через который будет автоматически генерироваться новое изображение.
   - `let interval;` — переменная для хранения интервала таймера.

3. **Функция для запуска интервала:**
   - `function startInterval() { interval = setInterval(generateImage, timer_on); }` — функция для запуска интервала, который вызывает `generateImage` каждые 10 секунд.

4. **Асинхронная функция для получения изображения:**
   - `async function generateImage()` — асинхронная функция для получения данных изображения из API.
   - В начале функция отключает кнопку, чтобы предотвратить повторные нажатия во время выполнения запроса:
     ```js
     generatorBtn.setAttribute("disabled", "disabled");
     ```
   - Функция выполняет HTTP-запрос с использованием `fetch` и получает данные в формате JSON:
     ```js
     const response = await fetch(url);
     const data = await response.json();
     ```
   - Если запрос проходит успешно, URL изображения устанавливается в качестве значения `src` для элемента `img`. Если произошла ошибка, выводится сообщение об ошибке:
     ```js
     dogImage.src = data.message;
     // или, в случае ошибки:
     imageDiv.innerHTML = "Error getting image";
     ```
   - В блоке `finally` кнопка снова активируется для пользователя:
     ```js
     generatorBtn.removeAttribute("disabled");
     ```

5. **Запуск первого изображения и интервала:**
   - `generateImage();` — вызывается для получения первого изображения при загрузке страницы.
   - `startInterval();` — запускает интервал, чтобы автоматически получать новые изображения каждые 10 секунд.

6. **Обработчик события для кнопки:**
   - `generatorBtn.addEventListener("click", function () { ... });` — добавляет обработчик события для кнопки. При нажатии на кнопку:
     - Снова вызывается функция `generateImage()`.
     - Сбрасывается текущий интервал таймера и запускается новый, чтобы отсчет начинался заново после каждого нажатия.

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

#### 1. **Создание галереи изображений собак**

- **Описание:** Добавить возможность просматривать и сохранять несколько изображений собак в виде галереи.
- **Цель:** Закрепление навыков работы с массивами, циклами и манипуляцией DOM.
- **Реализация:** Создать галерею с миниатюрами изображений и кнопкой "Показать больше", которая добавляет новые изображения по запросу к API.

#### 2. **Добавление функции сохранения изображений в избранное**
- **Описание:** Позволить пользователям сохранять понравившиеся изображения в избранное.
- **Цель:** Практика работы с `localStorage` или `sessionStorage` для хранения данных на стороне клиента.
- **Реализация:** Добавить кнопку "Добавить в избранное" рядом с каждым изображением. При нажатии на кнопку изображение сохраняется в `localStorage`, и пользователь может просмотреть все избранные изображения в отдельном разделе.

#### 3. **Реализация функции загрузки изображений**
- **Описание:** Возможность загрузки понравившихся изображений собак на устройство пользователя.
- **Цель:** Изучение работы с атрибутами HTML и ссылками для загрузки файлов.
- **Реализация:** Добавить кнопку "Скачать", которая создает ссылку на изображение и инициирует его загрузку на устройство пользователя.

#### 4. **Добавление автоматической смены изображений (слайд-шоу)**
- **Описание:** Введение функции автоматической смены изображений собак через определенные промежутки времени.
- **Цель:** Практика работы с функциями `setInterval` и `clearInterval` и взаимодействие с DOM.
- **Реализация:** Добавить кнопку для включения/выключения слайд-шоу. При включении слайд-шоу изображения будут автоматически обновляться каждые несколько секунд.

#### 5. **Реализация адаптивного дизайна**
- **Описание:** Сделать интерфейс приложения адаптивным для разных устройств, включая мобильные телефоны и планшеты.
- **Цель:** Закрепление навыков использования Flexbox, Grid и медиа-запросов в CSS.
- **Реализация:** Оптимизировать макет для разных размеров экранов, чтобы интерфейс оставался удобным и привлекательным на любом устройстве.

#### 6. **Добавление голосового управления**
- **Описание:** Позволить пользователям запрашивать изображения собак голосовыми командами.
- **Цель:** Изучение использования Web Speech API для обработки голосовых команд.
- **Реализация:** Добавить кнопку для активации голосового ввода, использовать Web Speech API для распознавания команд, таких как "покажи другую собаку" или "покажи лабрадора".

#### 7. **Добавление функции загрузки пользовательских изображений**
- **Описание:** Возможность пользователям загружать свои фотографии собак и добавлять их в галерею.
- **Цель:** Практика работы с формами и загрузкой файлов в JavaScript.
- **Реализация:** Добавить элемент формы для загрузки изображения, а также превью и кнопки для сохранения и добавления в галерею.

#### 8. **Добавление темной и светлой темы**
- **Описание:** Реализовать поддержку светлой и темной тем для пользовательского интерфейса.
- **Цель:** Закрепление навыков работы с темами и изменением CSS-переменных или классов.
- **Реализация:** Добавить переключатель темы на странице, который будет изменять тему с помощью CSS-переменных или добавления/удаления классов.

#### 9. **Поддержка мультиязычности**
- **Описание:** Возможность переключения языка интерфейса.
- **Цель:** Изучение принципов интернационализации (i18n) и работы с различными языковыми наборами.
- **Реализация:** Добавить переключатель языка, который будет изменять текст интерфейса в зависимости от выбранного языка.

#### 10. **Интеграция с социальными сетями**
- **Описание:** Возможность делиться изображениями собак через социальные сети.
- **Цель:** Изучение взаимодействия с API социальных сетей и создания ссылок для публикации контента.
- **Реализация:** Добавить кнопки для публикации изображений в социальных сетях.

#### 11. **Реализация офлайн-режима**

- **Описание:** Кэшировать изображения собак для их отображения в офлайн-режиме.
- **Цель:** Изучение использования Service Workers и кэширования данных в браузере.
- **Реализация:** Настроить Service Worker для кэширования изображений и основных данных, чтобы они были доступны, даже если пользователь потеряет подключение к интернету.

{{< /admonition >}}

### Form Validation

![Form Validation](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7b7mbyvuwxdwkzv2eidr.png "Form Validation")

**Описание:** Проект демонстрирует проверку формы на стороне клиента с использованием JavaScript. В процессе выполнения проверяются данные, введенные пользователем в форму, перед отправкой. При успешной проверке отображается сообщение об успехе, а введенные данные становятся доступными для просмотра в режиме только для чтения.

**Концепции обучения:**

- Валидация формы: Использование JavaScript для проверки данных, вводимых пользователем в форму, перед их отправкой. Это позволяет обеспечить целостность данных и предотвратить обработку недействительных значений.
- Манипулирование DOM: Получение доступа к элементам формы и их изменение (например, вывод сообщений об ошибках или отключение полей ввода) на основе результатов проверки.
- Обработка событий: Перехват события отправки формы и выполнение логики проверки с помощью JavaScript.

{{< admonition info "Пример реализации" false >}}

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css"
      integrity="sha512-PgQMlq+nqFLV4ylk1gwUOgm6CtIIXkKwaIHp/PAIWHzig/lKZSEGKEysh0TCVbHJXCLN7WetD8TFecIky75ZfQ=="
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="style.css" />
    <title>Form Validation | DOM Projects</title>
  </head>
  <body>
    <div class="container" id="main-page">
      <div class="header">
        <h2>REGISTRATION FORM</h2>
      </div>

      <form class="form" id="form">
        <div class="form-group">
          <label for="">Username</label>
          <input
            type="text"
            id="username"
            placeholder="Enter your name"
            autocomplete="off"
          />
          <i class="fas fa-check-circle"></i>
          <i class="fas fa-exclamation-circle"></i>
          <small>Error Msg</small>
        </div>

        <div class="form-group">
          <label for="">Email</label>
          <input type="email" id="email" placeholder="Enter your email" />
          <i class="fas fa-check-circle"></i>
          <i class="fas fa-exclamation-circle"></i>
          <small>Error Msg</small>
        </div>

        <!-- <div class="form-group">
				<label for="">Phone Number</label>
				<input type="number" id="phone" placeholder="Enter phone number">
				<i class="fas fa-check-circle"></i>
				<i class="fas fa-exclamation-circle"></i>
				<small>Error Msg</small>
			</div> -->

        <div class="form-group">
          <label for="">Password</label>
          <input
            type="password"
            id="password"
            placeholder="Enter your password"
          />
          <i class="fas fa-check-circle"></i>
          <i class="fas fa-exclamation-circle"></i>
          <small>Error Msg</small>
        </div>

        <div class="form-group">
          <label for="">Retype Password</label>
          <input
            type="password"
            id="retypepass"
            placeholder="Enter password again"
          />
          <i class="fas fa-check-circle"></i>
          <i class="fas fa-exclamation-circle"></i>
          <small>Error Msg</small>
        </div>

        <input id="submit-btn" type="submit" value="Submit" class="btn" />
      </form>
    </div>

    <!-- message after submitted -->
    <div class="container" id="submitted-msg">
      <div class="submit-msg-inner">
        <h1>Thanks <span id="msg-name"></span> for Your Registration.</h1>
        <button onclick="previewForm()" class="preview-btn">
          Preview Form
        </button>
      </div>
    </div>

    <script src="script.js"></script>
  </body>
</html>
```

```css
@import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Raleway', Fallback, sans-serif;
  font-size: 16px;
}

:root {
  --lg-lightcolor: linear-gradient(to left,
      rgba(116, 235, 0.6),
      rgba(159, 172, 23, 0));
}

body {
  background-color: #f8f9fc;

  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.container {
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 40px 8px rgba(0, 0, 0, 0.091);
  overflow: hidden;
  width: 500px;
  max-width: 100%;
}

#main-page {
  display: block;
}

.header {
  background-image: linear-gradient(62deg, #4e54c8 0%, #8f94fb 100%);
  padding: 25px 0;
}

.header h2 {
  color: white;
  font-size: 24px;
  text-transform: uppercase;
  text-align: center;
}

.form {
  padding: 30px;
}

.form-group {
  margin-bottom: 25px;
  position: relative;
}

.form-group label {
  display: inline-block;
  margin-bottom: 5px;
}

.form-group input {
  width: 100%;
  border: 2px solid #f0f0f0;
  border-radius: 5px;
  display: block;
  font-size: 14px;
  padding: 10px;
}

.form-group input:focus {
  outline: 0;
  border-color: #777;
}

.form-group.success input {
  border-color: #2ecc71;
}

.form-group.error input {
  border-color: #e74c3c;
}

.form-group i {
  position: absolute;
  right: 12px;
  top: 38px;
  visibility: hidden;
}

.form-group.success i.fa-check-circle {
  color: #2ecc71;
  visibility: visible;
}

.form-group.error i.fa-exclamation-circle {
  color: #e74c3c;
  visibility: visible;
}

.form-group small {
  color: #e74c3c;
  position: absolute;
  left: 0;
  bottom: -20px;
  visibility: hidden;
}

.form-group.error small {
  visibility: visible;
}

.form .btn {
  /*background-color: #8EC5FC;*/
  background-image: linear-gradient(62deg, #4e54c8 0%, #8f94fb 100%);

  border-radius: 6px;
  border: none;
  outline: none;
  color: #fff;
  display: block;
  font-size: 16px;
  padding: 11px 0;
  margin-top: 30px;
  width: 100%;
  font-weight: 800;
  text-transform: uppercase;
  transition: all 1s ease;
  cursor: pointer;
}

.form .btn:hover {
  background-image: linear-gradient(62deg, #8f94fb 0%, #4e54c8 100%);
}

#submitted-msg {
  display: none;
  background-color: aliceblue;
}

.submit-msg-inner {
  text-align: center;
  padding: 65px;
}

#msg-name {
  color: green;
}

.preview-btn {
  border: none;
  outline: none;
  border-radius: 5px;
  padding: 5px 15px;
  background-color: orange;
  font-size: 16px;
  cursor: pointer;
  margin-top: 18px;
}

.disabled-btn {
  background: #8f94fb;
  border-radius: 6px;
  border: none;
  outline: none;
  color: #fff;
  display: block;
  font-size: 16px;
  padding: 11px 0;
  margin-top: 20px;
  width: 100%;
  font-weight: 800;
  text-transform: uppercase;
  transition: all 1s ease;
}

@media (max-width: 768px) {
  #main-page {
    margin-top: 50px;
    margin-bottom: 15px;
  }
}

@media (max-width: 525px) {
  #main-page {
    margin-top: 15px;
    margin-bottom: 15px;
  }

  .container {
    width: 400px;
  }

  .header {
    padding: 20px 0;
  }

  .header h2 {
    font-size: 18px;
  }

  .form {
    padding: 19px;
  }

  .form-group {
    margin-bottom: 19px;
  }

  .form-group input {
    font-size: 14px;
    padding: 7px;
  }

  .form-group i {
    right: 10px;
    top: 33px;
  }
}

@media (max-width: 375px) {
  #main-page {
    margin-top: 10px;
    margin-bottom: 10px;
  }

  .container {
    width: 330px;
  }

  .header h2 {
    font-size: 18px;
  }

  .form {
    padding: 17px;
  }

  .form-group {
    margin-bottom: 22px;
  }

  .form-group input {
    padding: 5px;
  }

  .form-group i {
    right: 10px;
    top: 32px;
  }
}

@media (max-width: 325px) {
  .container {
    width: 300px;
  }

  .header h2 {
    font-size: 16px;
  }

  .form {
    padding: 15px;
  }

  .form-group {
    margin-bottom: 22px;
  }

  .form-group input {
    padding: 5px;
  }

  .form-group i {
    right: 10px;
    top: 32px;
  }
}
```

```js
const form = document.getElementById("form");
const userName = document.getElementById("username");
const email = document.getElementById("email");
// const phone = document.getElementById('phone');
const password = document.getElementById("password");
const cpassword = document.getElementById("retypepass");

//add event
form.addEventListener("submit", (event) => {
  console.log("form submit");
  event.preventDefault();

  validate();
});

//is email(check the email)
const isEmail = (emailVal) => {
  let atSymbol = emailVal.indexOf("@");
  if (atSymbol < 1) return false;

  let dot = emailVal.lastIndexOf(".");
  if (dot <= atSymbol + 3) return false;

  if (dot === emailVal.length - 1) return false;

  return true;
};

const validate = () => {
  const userNameVal = username.value.trim();
  const emailVal = email.value.trim();
  // const phoneVal = phone.value.trim();
  const passwordVal = password.value.trim();
  const cpasswordVal = cpassword.value.trim();

  // validate userName
  if (userNameVal === "") {
    setErrorMsg(username, "Username cannot be blank");
  } else if (userNameVal.length <= 2) {
    setErrorMsg(username, "Enter min 3 char");
  } else {
    setSuccessmsg(username);
  }

  // validate email
  if (emailVal === "") {
    setErrorMsg(email, "Email cannot be blank");
  } else if (!isEmail(emailVal)) {
    setErrorMsg(email, "Not valid email");
  } else {
    setSuccessmsg(email);
  }

  //validate phone
  /*if(phoneVal === ""){
		setErrorMsg(phone, 'phone num cannot be blank');
	} else if (phoneVal.length != 11 ) {
		setErrorMsg(phone, 'not valid phone num');
	} else{
		setSuccessmsg(phone);
	}*/

  //validate password
  if (passwordVal === "") {
    setErrorMsg(password, "Password cannot be blank");
  } else if (passwordVal.length < 8) {
    setErrorMsg(password, "Enter min 8 char");
  } else {
    setSuccessmsg(password);
  }

  //validate confirm password
  if (cpasswordVal === "") {
    setErrorMsg(cpassword, "Field cannot be blank");
  } else if (cpasswordVal.length < 8) {
    setErrorMsg(cpassword, "Enter min 8 char");
  } else if (cpasswordVal != passwordVal) {
    setErrorMsg(cpassword, "Password didn't matched ");
  } else {
    setSuccessmsg(cpassword);
  }

  setTimeout(() => {
    let successCls = document.querySelectorAll(".success");
    if (successCls.length == 4) {
      showSubmittedMsg();
    }
  }, 1000);
};

function showSubmittedMsg() {
  let mainPage = document.getElementById("main-page");
  mainPage.style.display = "none";
  let successMsgPage = document.getElementById("submitted-msg");
  successMsgPage.style.display = "block";

  document.getElementById("msg-name").innerText = userName.value;
}

function setErrorMsg(input, errormsg) {
  const formGroup = input.parentNode;
  const small = formGroup.querySelector("small");
  formGroup.className = "form-group error";
  small.innerText = errormsg;
}

function setSuccessmsg(input) {
  const fromGroup = input.parentNode;
  fromGroup.className = "form-group success";
}

function previewForm() {
  document.getElementById("main-page").style.display = "block";
  document.getElementById("submitted-msg").style.display = "none";

  let submitBtn = document.getElementById("submit-btn");
  submitBtn.classList.remove("btn");
  submitBtn.classList.add("disabled-btn");
  submitBtn.disabled = true;
}
```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

#### HTML

HTML-код создает структуру страницы и форму для ввода данных:

1. **Основные элементы:**
   - `div` с классом `container` и `id="main-page"` содержит форму регистрации.
   - `form` с классом `form` и `id="form"` — сама форма с несколькими полями ввода: "Имя пользователя", "Email", "Пароль", "Повторите пароль".
   - В каждом `div` с классом `form-group` содержатся элементы ввода (`input`), иконки для индикации статуса (успех или ошибка), и `small` для отображения сообщений об ошибках.

2. **Сообщение об успехе:**
   - `div` с `id="submitted-msg"` содержит сообщение об успешной регистрации и кнопку для предварительного просмотра введенных данных.

3. **Подключение JavaScript:**
   - `<script src="script.js"></script>` подключает файл JavaScript для обработки проверки формы и отображения сообщений.

#### CSS

CSS стилизует элементы страницы, обеспечивая удобство использования и привлекательный внешний вид:

1. **Основные стили:**
   - Основные стили для страницы, включая фон, шрифт и размещение контейнера формы по центру.
   - Стили для контейнера `.container`, формы, заголовков, иконок и сообщений об ошибках.
   - Стили для кнопок с различными эффектами при наведении курсора и нажатии.

2. **Респонсивность:**
   - Использование медиа-запросов для адаптации формы под разные размеры экранов.

#### JavaScript

JavaScript отвечает за логику проверки данных, обработку событий и отображение сообщений. Рассмотрим код подробнее:

1. **Получение элементов формы:**
   - `const form = document.getElementById("form");` — получает форму по `id`.
   - `const userName`, `email`, `password`, `cpassword` — получают поля ввода формы по `id`.

2. **Обработка события отправки формы:**
   - `form.addEventListener("submit", (event) => { ... });` — добавляет обработчик события `submit` для формы. При попытке отправки формы выполняется логика проверки:
     - `event.preventDefault();` предотвращает стандартное поведение отправки формы.
     - Вызывается функция `validate()` для проверки введенных данных.

3. **Проверка правильности данных:**
   - **Функция `isEmail(emailVal)`** — проверяет, является ли введенное значение корректным email-адресом.
   - **Функция `validate()`** — выполняет проверку данных для каждого поля формы:
     - Проверяет, не пустое ли поле, соответствует ли длина минимальным требованиям, и совпадают ли пароли.
     - В случае ошибки вызывает `setErrorMsg(input, message)`, чтобы указать на ошибку.
     - В случае успеха вызывает `setSuccessmsg(input)` для отображения статуса "успех".

4. **Отображение сообщений:**
   - **Функция `setErrorMsg(input, errormsg)`** — добавляет класс `error` к `form-group` и выводит сообщение об ошибке.
   - **Функция `setSuccessmsg(input)`** — добавляет класс `success` к `form-group`, чтобы показать успешное прохождение проверки.
   - **Функция `showSubmittedMsg()`** — скрывает форму и отображает сообщение об успешной регистрации.

5. **Предпросмотр данных:**
   - **Функция `previewForm()`** — отображает введенные данные в форме в режиме только для чтения. Кнопка "Отправить" блокируется и стилизуется как неактивная.

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

#### 1. **Добавление асинхронной валидации через API**

- **Описание:** Проверка введенных данных, таких как имя пользователя или email, в реальном времени через запросы к серверу или API.
- **Цель:** Изучение асинхронного программирования и работы с Fetch API для выполнения запросов.
- **Реализация:** Добавить обработчик событий для ввода в поле email или имя пользователя, который будет отправлять запрос к API для проверки доступности и корректности введенных данных.

#### 2. **Реализация динамического отображения ошибок**
- **Описание:** Динамическое отображение сообщений об ошибках, которые появляются или исчезают в зависимости от правильности ввода данных.
- **Цель:** Практика работы с DOM и управлением элементами интерфейса.
- **Реализация:** Создать функции, которые динамически добавляют или удаляют сообщения об ошибках и применяют стили к полям формы при вводе данных.

#### 3. **Создание пользовательского интерфейса с использованием CSS-анимаций**
- **Описание:** Использование анимаций для плавного появления и исчезновения сообщений об ошибках или успешной валидации.
- **Цель:** Закрепление навыков работы с CSS-анимациями и переходами.
- **Реализация:** Добавить CSS-анимации для элементов формы, таких как сообщения об ошибках или всплывающие подсказки, чтобы сделать интерфейс более интерактивным и дружелюбным.

#### 4. **Добавление проверки на стороне клиента с регулярными выражениями (RegEx)**
- **Описание:** Использование регулярных выражений для проверки вводимых данных (например, формата email, номера телефона или пароля).
- **Цель:** Изучение работы с регулярными выражениями в JavaScript.
- **Реализация:** Создать функции для проверки различных полей формы с использованием регулярных выражений и выводить сообщения об ошибках при некорректном вводе.

#### 5. **Реализация функции "Показать/Скрыть пароль"**
- **Описание:** Добавить возможность отображать или скрывать введенный пароль.
- **Цель:** Практика работы с элементами интерфейса и обработкой событий.
- **Реализация:** Добавить иконку "глаза" рядом с полем ввода пароля. При клике на иконку переключать атрибут `type` поля ввода между `password` и `text`.

#### 6. **Добавление индикатора надежности пароля**
- **Описание:** Показать уровень надежности пароля с использованием графического индикатора.
- **Цель:** Закрепление навыков работы с CSS и JavaScript для динамического обновления интерфейса.
- **Реализация:** Реализовать индикатор, который будет изменять цвет и длину в зависимости от сложности пароля (например, длины, наличия специальных символов, цифр и заглавных букв).

#### 7. **Добавление сохранения состояния формы**
- **Описание:** Автоматическое сохранение данных формы в `localStorage`, чтобы пользователи не потеряли введенные данные при случайной перезагрузке страницы.
- **Цель:** Изучение работы с `localStorage` для хранения данных на стороне клиента.
- **Реализация:** При каждом вводе данных сохранять текущее состояние формы в `localStorage`, а при загрузке страницы восстанавливать данные из `localStorage`.

#### 8. **Добавление валидации на стороне сервера**
- **Описание:** Реализовать валидацию на стороне сервера с использованием API.
- **Цель:** Закрепление навыков асинхронного взаимодействия с сервером и работы с JSON.
- **Реализация:** Отправлять данные формы на сервер для дополнительной проверки через Fetch API и отображать результаты валидации на клиентской стороне.

#### 9. **Добавление многошаговой формы (Wizard Form)**
- **Описание:** Разделение формы на несколько шагов с динамическим управлением переходами между шагами.
- **Цель:** Практика работы с динамическими элементами интерфейса и управлением состоянием формы.
- **Реализация:** Создать несколько шагов формы с кнопками "Далее" и "Назад", чтобы пользователь мог последовательно вводить данные. Добавить индикатор прогресса для визуализации этапов.

#### 10. **Реализация мультиязычности**
- **Описание:** Возможность переключения языка интерфейса.
- **Цель:** Закрепление навыков работы с интернационализацией (i18n).
- **Реализация:** Добавить переключатель языка, который будет изменять текст всех сообщений и подсказок в форме.

#### 11. **Создание адаптивного дизайна формы**
- **Описание:** Обеспечить корректное отображение формы на устройствах с различными размерами экрана.
- **Цель:** Закрепление навыков работы с CSS Grid, Flexbox и медиа-запросами.
- **Реализация:** Оптимизировать макет формы для мобильных устройств, планшетов и настольных компьютеров.

#### 12. **Добавление проверки по капче или reCAPTCHA**
- **Описание:** Добавить защиту формы от спама с помощью CAPTCHA или reCAPTCHA.
- **Цель:** Изучение работы с внешними сервисами и интеграция API в проект.
- **Реализация:** Внедрить Google reCAPTCHA или другую проверку CAPTCHA перед отправкой формы.

#### 13. **Создание пользовательских всплывающих сообщений об ошибках**
- **Описание:** Использовать модальные окна или всплывающие уведомления для отображения сообщений об ошибках.
- **Цель:** Практика работы с модальными окнами, их открытием и закрытием.
- **Реализация:** Создать кастомные уведомления об ошибках, которые будут появляться в центре экрана и исчезать автоматически через несколько секунд.

#### 14. **Добавление анимации переходов между шагами**
- **Описание:** Создать плавные анимации при переходе между шагами многошаговой формы.
- **Цель:** Закрепление навыков работы с CSS-анимациями и управлением состоянием элементов с помощью JavaScript.
- **Реализация:** Добавить CSS-анимации, которые будут активироваться при переходе между шагами.

#### 15. **Внедрение валидации на основе правил для различных типов полей**
- **Описание:** Использование заранее заданных правил для валидации полей разных типов (например, текст, email, телефон).
- **Цель:** Закрепление знаний о валидации данных и оптимизация кода.
- **Реализация:** Создать функции для валидации различных типов полей и применить их ко всем соответствующим полям формы.

{{< /admonition >}}

### Random User

![Random User](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjlfog2j2okpgtx01eyso.png "Random User")

**Описание:** Проект использует API для генерации случайной информации о пользователе. В процессе работы с API получаются данные, такие как имя, электронная почта, аватар и другие, которые отображаются на веб-странице в виде профиля случайного пользователя.

**Концепции обучения:**

- Асинхронное программирование: Закрепление навыков выполнения асинхронных операций в JavaScript.
- Fetch API: Практика использования встроенных функций для выполнения HTTP-запросов к API и получения данных.
- Работа с API: Изучение взаимодействия с внешними API для доступа к различным функциям или данным.

{{< admonition info "Пример реализации" false >}}

<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
    <!-- Иконка с подписью -->
    <div style="display: flex; flex-direction: column; align-items: center;">
        <svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="envelope" class="svg-inline--fa fa-envelope fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" style="width: 30px; height: 30px;"><path fill="currentColor" d="M464 64H48C21.49 64 0 85.49 0 112v288c0 26.51 21.49 48 48 48h416c26.51 0 48-21.49 48-48V112c0-26.51-21.49-48-48-48zm0 48v40.805c-22.422 18.259-58.168 46.651-134.587 106.49-16.841 13.247-50.201 45.072-73.413 44.701-23.208.375-56.579-31.459-73.413-44.701C106.18 199.465 70.425 171.067 48 152.805V112h416zM48 400V214.398c22.914 18.251 55.409 43.862 104.938 82.646 21.857 17.205 60.134 55.186 103.062 54.955 42.717.231 80.509-37.199 103.053-54.947 49.528-38.783 82.032-64.401 104.947-82.653V400H48z"></path></svg>
        <span>email.svg</span>
    </div>
    <!-- Иконка с подписью -->
    <div style="display: flex; flex-direction: column; align-items: center;">
        <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="map-marked-alt" class="svg-inline--fa fa-map-marked-alt fa-w-18" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" style="width: 30px; height: 30px;"><path fill="currentColor" d="M288 0c-69.59 0-126 56.41-126 126 0 56.26 82.35 158.8 113.9 196.02 6.39 7.54 17.82 7.54 24.2 0C331.65 284.8 414 182.26 414 126 414 56.41 357.59 0 288 0zm0 168c-23.2 0-42-18.8-42-42s18.8-42 42-42 42 18.8 42 42-18.8 42-42 42zM20.12 215.95A32.006 32.006 0 0 0 0 245.66v250.32c0 11.32 11.43 19.06 21.94 14.86L160 448V214.92c-8.84-15.98-16.07-31.54-21.25-46.42L20.12 215.95zM288 359.67c-14.07 0-27.38-6.18-36.51-16.96-19.66-23.2-40.57-49.62-59.49-76.72v182l192 64V266c-18.92 27.09-39.82 53.52-59.49 76.72-9.13 10.77-22.44 16.95-36.51 16.95zm266.06-198.51L416 224v288l139.88-55.95A31.996 31.996 0 0 0 576 426.34V176.02c0-11.32-11.43-19.06-21.94-14.86z"></path></svg>
        <span>map.svg</span>
    </div>
    <!-- Иконка с подписью -->
    <div style="display: flex; flex-direction: column; align-items: center;">
        <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="phone" class="svg-inline--fa fa-phone fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" style="width: 30px; height: 30px;"><path fill="currentColor" d="M493.4 24.6l-104-24c-11.3-2.6-22.9 3.3-27.5 13.9l-48 112c-4.2 9.8-1.4 21.3 6.9 28l60.6 49.6c-36 76.7-98.9 140.5-177.2 177.2l-49.6-60.6c-6.8-8.3-18.2-11.1-28-6.9l-112 48C3.9 366.5-2 378.1.6 389.4l24 104C27.1 504.2 36.7 512 48 512c256.1 0 464-207.5 464-464 0-11.2-7.7-20.9-18.6-23.4z"></path></svg>
        <span>phone.svg</span>
    </div>
    <!-- Иконка с подписью -->
    <div style="display: flex; flex-direction: column; align-items: center;">
        <svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="user" class="svg-inline--fa fa-user fa-w-14" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" style="width: 30px; height: 30px;"><path fill="currentColor" d="M313.6 304c-28.7 0-42.5 16-89.6 16-47.1 0-60.8-16-89.6-16C60.2 304 0 364.2 0 438.4V464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48v-25.6c0-74.2-60.2-134.4-134.4-134.4zM400 464H48v-25.6c0-47.6 38.8-86.4 86.4-86.4 14.6 0 38.3 16 89.6 16 51.7 0 74.9-16 89.6-16 47.6 0 86.4 38.8 86.4 86.4V464zM224 288c79.5 0 144-64.5 144-144S303.5 0 224 0 80 64.5 80 144s64.5 144 144 144zm0-240c52.9 0 96 43.1 96 96s-43.1 96-96 96-96-43.1-96-96 43.1-96 96-96z"></path></svg>
        <span>user.svg</span>
    </div>
</div>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>Random User | DOM Projects</title>
  </head>
  <body>
    <main class="main-section">
      <!-- watermark -->
      <p id="watermark" class="watermark">RANDOM USER GENERATOR</p>
      <section class="section-1"></section>
      <section class="section-2"></section>

      <!-- Random user card -->
      <div class="card">
        <!-- card top-section -->
        <div class="top-section">
          <div id="user-image" class="img-circle-box">
            <!-- <img src="images/jisan.jpg" alt="" /> -->
          </div>
          <p onclick="genrateNewUser()" class="new">Generate New user</p>
        </div>
        <!-- card bottom-section -->

        <div class="bottom-section">
          <div class="user-info">
            <div id="user-name-div" class="user-info-inner user-name">
              <h5>Hi, my name is</h5>
              <h3 id="user-name"></h3>
            </div>

            <div id="user-email-div" class="user-info-inner user-email">
              <h5>My Email address is</h5>
              <h3 id="user-email"></h3>
            </div>

            <div id="user-phone-div" class="user-info-inner user-phone">
              <h5>My phone number is</h5>
              <h3 id="user-phone"></h3>
            </div>

            <div id="user-address-div" class="user-info-inner user-address">
              <h5>My address is</h5>
              <h3 id="user-address"></h3>
            </div>
          </div>

          <div class="icon-area">
            <div class="icon-inner">
              <img onclick="showUserName()" src="./img/user.svg" alt="" />
            </div>

            <div class="icon-inner">
              <img onclick="showUserEmail()" src="./img/email.svg" alt="" />
            </div>

            <div class="icon-inner">
              <img onclick="showUserPhone()" src="./img/phone.svg" alt="" />
            </div>

            <div class="icon-inner">
              <img onclick="showUserLocation()" src="./img/map.svg" alt="" />
            </div>
          </div>
        </div>
      </div>
    </main>

    <script src="script.js"></script>
  </body>
</html>
```

```css
@import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Raleway', Fallback, sans-serif;
  font-size: 16px;
}

.section-1 {
  width: 100%;
  background-color: #2c2e31;
  height: 270px;
}

.section-2 {
  width: 100%;
  height: 393px;
  background-color: #f9f9f9;
  color: black;
}

.main-section {
  position: relative;
}

.card {
  position: absolute;
  left: 0;
  top: 12%;
  bottom: 0;
  right: 0;
  margin: 0 auto;
  width: 675px;
  height: 396px;
  box-shadow: 0 0 4px 2px rgba(0, 0, 0, 0.1);
  background-color: white;
  border-radius: 5px;
}

.card .top-section {
  position: relative;
  width: 100%;
  height: 150px;
  background-color: #f9f9f9;
  border-bottom: 1px solid #d4d4d4;
}

.card .img-circle-box {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: 150px;
  height: 150px;
  margin: 0 auto;
  margin-top: 50px;
  border: 1px solid #d7d7d7;
  border-radius: 50%;
  background-color: white;
}

.card .img-circle-box img {
  width: 100%;
  border-radius: 50%;
  padding: 5px;
  cursor: pointer;
}

.card .new {
  position: absolute;
  left: 0%;
  top: 0%;
  right: 0;
  bottom: 0;
  cursor: pointer;
  transition: all 0.3s ease;
  display: inline-block;
  height: 30px;
  text-align: center;
  color: white;
  background-color: #686a6df1;
  padding-top: 5px;
}

.user-info {
  font-family: "Raleway", sans-serif;
}

.user-info .user-info-inner {
  width: 100%;
  margin: 0 auto;
  margin-top: 70px;
  text-align: center;
}

.user-info .user-info-inner h5 {
  font-size: 16px;
  color: gray;
  font-weight: 500;
}

.user-info .user-info-inner h3 {
  font-size: 2.4em;
  font-weight: 600;
}

.icon-area {
  display: flex;
  justify-content: space-around;
  width: 75%;
  margin: 0 auto;
  margin-top: 45px;
}

.icon-area .icon-inner {
  width: 25px;
}

.icon-area .icon-inner img {
  width: 100%;
  cursor: pointer;
}

.watermark {
  position: absolute;
  width: 100%;
  text-align: center;
  background-color: rgba(0, 255, 0, 0.658);
  color: white;
  padding: 5px 0;
}

.user-email,
.user-phone,
.user-address {
  display: none;
}

footer {
  position: absolute;
  left: 0;
  right: 0;
  top: 83%;
  bottom: 0;
}

footer p {
  text-align: center;
  color: gray;
  font-size: 14px;
}

footer .copywriteName {
  color: orange;
  cursor: pointer;
}

@media (max-width: 644px) {
  .card {
    width: 500px;
  }

  .user-info .user-info-inner h3 {
    font-size: 2em;
    font-weight: 600;
  }
}

@media (max-width: 425px) {
  .card {
    width: 390px;
  }

  .user-info .user-info-inner h3 {
    font-size: 1.5em;
  }
}

@media (max-width: 375px) {
  .card {
    width: 360px;
  }

  .user-info .user-info-inner h3 {
    font-size: 1.3em;
  }
}

@media (max-width: 320px) {
  .card {
    width: 290px;
  }

  .user-info .user-info-inner h5 {
    font-size: 14px;
    line-height: 30px;
  }

  .user-info .user-info-inner h3 {
    font-size: 1.2em;
  }

  .user-info .user-info-inner {
    margin-top: 80px;
  }

  .section-1 {
    height: 230px;
  }
}
```

```js
const url = "https://randomuser.me/api/";
function apiFetch() {
  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      showDataOnUi(data);
    });
}

function showDataOnUi(data) {
  const userName = `${
    data.results[0].name.first + " " + data.results[0].name.last
  }`;

  const userEmail = `${data.results[0].email}`;

  const userPhone = `${data.results[0].phone}`;

  const location = `${
    data.results[0].location.city + ", " + data.results[0].location.country
  }`;

  const image = `<img src="${data.results[0].picture.large}" alt=""/>`;

  document.getElementById("user-name").innerText = userName;
  document.getElementById("user-email").innerText = userEmail;
  document.getElementById("user-phone").innerText = userPhone;
  document.getElementById("user-address").innerText = location;
  document.getElementById("user-image").innerHTML = image;

  document.getElementById("");
}

function displayCurrentInfo(id1, id2, id3, id4) {
  document.getElementById(id1).style.display = "block";
  document.getElementById(id2).style.display = "none";
  document.getElementById(id3).style.display = "none";
  document.getElementById(id4).style.display = "none";
  document.getElementById(id4).style.display = "none";
}

function showUserName() {
  displayCurrentInfo(
    "user-name-div",
    "user-email-div",
    "user-phone-div",
    "user-address-div"
  );
}
function showUserEmail() {
  displayCurrentInfo(
    "user-email-div",
    "user-phone-div",
    "user-address-div",
    "user-name-div"
  );
}
function showUserPhone() {
  displayCurrentInfo(
    "user-phone-div",
    "user-email-div",
    "user-address-div",
    "user-name-div"
  );
}
function showUserLocation() {
  displayCurrentInfo(
    "user-address-div",
    "user-phone-div",
    "user-email-div",
    "user-name-div"
  );
}

setTimeout(() => {
  document.getElementById("watermark").style.display = "none";
}, 2500);

apiFetch();

function genrateNewUser() {
  apiFetch();
}
```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

#### HTML

HTML-код создает основную структуру страницы:

1. **Основные элементы:**
   - `main` с классом `main-section` — основной контейнер для элементов.
   - `div` с классом `card` — карточка для отображения данных о случайном пользователе.
   - Внутри карточки находятся:
     - `div` с `id="user-image"` — контейнер для изображения пользователя.
     - Несколько `div` с классом `user-info-inner` и соответствующими `id` (например, `user-name-div`, `user-email-div`), которые содержат информацию о пользователе (имя, email, телефон и адрес).
     - `div` с классом `icon-area` — блок с иконками, которые при клике отображают определенную информацию о пользователе (имя, email, телефон, адрес).

2. **Подключение JavaScript:**
   - `<script src="script.js"></script>` подключает файл JavaScript, который отвечает за получение и отображение данных о пользователе.

#### CSS

CSS стилизует элементы страницы, делая интерфейс привлекательным и удобным для пользователя:

1. **Основные стили:**
   - Основные стили для страницы (`body`), включая шрифт, фон и размещение контейнера по центру.
   - Стили для карточки (`.card`), которая содержит данные о пользователе. Карточка имеет закругленные углы, тени и делится на верхнюю (`top-section`) и нижнюю (`bottom-section`) части.
   - Стили для иконок (`.icon-area`), которые позволяют пользователю выбирать, какую информацию отображать на карточке.

2. **Адаптивный дизайн:**
   - Использование медиа-запросов для адаптации карточки под разные размеры экранов, обеспечивая корректное отображение на мобильных устройствах.

#### JavaScript

JavaScript отвечает за взаимодействие с API, обработку данных и отображение их на странице. Рассмотрим код подробнее:

1. **Определение URL API и функция `apiFetch()`:**
   - `const url = "https://randomuser.me/api/";` — URL для получения случайной информации о пользователе с помощью API.
   - `function apiFetch()` — функция для выполнения запроса к API и получения данных о пользователе:
     - Используется метод `fetch` для отправки запроса к API.
     - Полученный ответ преобразуется в формат JSON, и данные передаются в функцию `showDataOnUi(data)` для отображения на странице.

2. **Функция `showDataOnUi(data)`:**
   - Получает данные о пользователе и отображает их на странице:
   - Извлекает имя, email, телефон, местоположение и изображение пользователя из полученных данных:
     ```js
     const userName = `${data.results[0].name.first + " " + data.results[0].name.last}`;
     const userEmail = `${data.results[0].email}`;
     const userPhone = `${data.results[0].phone}`;
     const location = `${data.results[0].location.city + ", " + data.results[0].location.country}`;
     const image = `<img src="${data.results[0].picture.large}" alt=""/>`;
     ```
   - Устанавливает соответствующие значения в элементы DOM:
     ```js
     document.getElementById("user-name").innerText = userName;
     document.getElementById("user-email").innerText = userEmail;
     document.getElementById("user-phone").innerText = userPhone;
     document.getElementById("user-address").innerText = location;
     document.getElementById("user-image").innerHTML = image;
     ```

3. **Функции для отображения выбранной информации:**
   - **Функция `displayCurrentInfo(id1, id2, id3, id4)`** — отображает выбранную информацию и скрывает остальные:
     ```js
     function displayCurrentInfo(id1, id2, id3, id4) {
       document.getElementById(id1).style.display = "block";
       document.getElementById(id2).style.display = "none";
       document.getElementById(id3).style.display = "none";
       document.getElementById(id4).style.display = "none";
     }
     ```
   - **Функции `showUserName()`, `showUserEmail()`, `showUserPhone()`, `showUserLocation()`** — используют `displayCurrentInfo` для отображения конкретной информации (например, имени, email и т.д.) при клике на соответствующую иконку.

4. **Инициализация и обновление данных:**
   - `apiFetch()` — вызывается при загрузке страницы, чтобы сразу отобразить данные о случайном пользователе.
   - `function genrateNewUser()` — вызывается при клике на кнопку "Generate New User" для получения новых данных о пользователе.

5. **Дополнительные функции:**
   - **Функция `setTimeout()`** используется для скрытия водяного знака через 2.5 секунды после загрузки страницы:
     ```js
     setTimeout(() => {
       document.getElementById("watermark").style.display = "none";
     }, 2500);
     ```

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

#### 1. **Добавление функции поиска и фильтрации пользователей**

- **Описание:** Возможность фильтровать пользователей по определенным критериям (например, по полу, возрасту, стране и т.д.).
- **Цель:** Практика работы с параметрами запросов API и фильтрацией данных.
- **Реализация:** Добавить поля выбора или фильтры, которые будут отправлять соответствующие параметры в запрос к API и отображать результаты на основе выбранных критериев.

#### 2. **Реализация функции сохранения избранных пользователей**
- **Описание:** Позволить пользователям сохранять информацию о понравившихся пользователях в избранное.
- **Цель:** Закрепление навыков работы с `localStorage` или `sessionStorage` для хранения данных на стороне клиента.
- **Реализация:** Добавить кнопку "Добавить в избранное" рядом с каждым пользователем. При нажатии на кнопку информация о пользователе сохраняется в `localStorage`, и пользователь может просмотреть всех избранных пользователей в отдельном разделе.

#### 3. **Создание карточек с пользователями в виде сетки или списка**
- **Описание:** Отображение информации о пользователях в виде карточек, размещенных в сетке или списке.
- **Цель:** Закрепление навыков работы с CSS Grid или Flexbox для создания адаптивных макетов.
- **Реализация:** Разместить информацию о каждом пользователе в карточке с использованием CSS Grid или Flexbox для создания привлекательного и адаптивного дизайна.

#### 4. **Реализация функции поиска по имени пользователя**
- **Описание:** Возможность поиска пользователей по имени.
- **Цель:** Практика работы с фильтрацией данных и обработкой пользовательского ввода.
- **Реализация:** Добавить поле поиска, которое будет фильтровать отображаемых пользователей в реальном времени по введенному имени.

#### 5. **Добавление анимации при загрузке данных**
- **Описание:** Показать индикатор загрузки или анимацию во время запроса к API.
- **Цель:** Изучение управления асинхронными запросами и визуальная обратная связь пользователю.
- **Реализация:** Добавить индикатор загрузки (например, спиннер) и скрывать его при получении данных из API.

#### 6. **Добавление функции сортировки пользователей**
- **Описание:** Возможность сортировки пользователей по различным критериям, таким как имя, возраст, страна и т.д.
- **Цель:** Закрепление навыков работы с массивами и методами сортировки.
- **Реализация:** Добавить элементы управления для выбора сортировки и реализовать соответствующую логику сортировки при нажатии на элементы управления.

#### 7. **Добавление возможности редактирования и сохранения информации о пользователях**
- **Описание:** Возможность редактировать информацию о пользователях и сохранять изменения в `localStorage`.
- **Цель:** Практика работы с формами, обработкой событий и `localStorage`.
- **Реализация:** Добавить кнопку "Редактировать" на карточках пользователей, при нажатии на которую отображаются поля ввода для редактирования информации.

#### 8. **Реализация темной и светлой темы интерфейса**
- **Описание:** Возможность переключения между светлой и темной темами интерфейса.
- **Цель:** Закрепление навыков работы с темами и изменением CSS-переменных или классов.
- **Реализация:** Добавить переключатель темы на странице, который будет изменять тему с помощью CSS-переменных или добавления/удаления классов.

#### 9. **Добавление функции экспорта данных в различные форматы**
- **Описание:** Возможность экспорта данных пользователей в файлы разных форматов (например, CSV, JSON).
- **Цель:** Изучение работы с данными в различных форматах и API для скачивания файлов.
- **Реализация:** Добавить кнопку "Экспорт", которая будет генерировать файл с данными о пользователях и предоставлять возможность скачать его.

#### 10. **Реализация многоязычной поддержки интерфейса**
- **Описание:** Возможность переключения языка интерфейса.
- **Цель:** Закрепление навыков интернационализации (i18n).
- **Реализация:** Добавить переключатель языка, который будет изменять текст всех элементов интерфейса в зависимости от выбранного языка.

#### 11. **Создание функции автоматического обновления списка пользователей**
- **Описание:** Введение таймера, который автоматически обновляет список пользователей через заданные интервалы времени.
- **Цель:** Практика работы с функциями `setInterval` и `clearInterval`.
- **Реализация:** Добавить кнопку для включения/выключения автоматического обновления и реализацию соответствующего таймера.

#### 12. **Добавление поддержки загрузки пользовательских аватаров**
- **Описание:** Возможность пользователям загружать свои собственные изображения для профиля.
- **Цель:** Закрепление навыков работы с формами и загрузкой файлов в JavaScript.
- **Реализация:** Добавить элемент формы для загрузки изображения и реализовать предварительный просмотр перед сохранением.

#### 13. **Интеграция с картами для отображения местоположения пользователя**
- **Описание:** Отображение местоположения пользователя на карте (например, с использованием Google Maps API).
- **Цель:** Изучение работы с внешними API и отображением географических данных.
- **Реализация:** Добавить кнопку "Показать на карте" рядом с адресом пользователя, которая открывает карту с указанием местоположения.

#### 14. **Реализация функции уведомлений**
- **Описание:** Отправка уведомлений пользователю, когда появляется новый пользователь или информация обновляется.
- **Цель:** Изучение работы с уведомлениями браузера.
- **Реализация:** Использовать Web Notifications API для отображения уведомлений на рабочем столе при обновлении данных.

#### 15. **Добавление функции "Сравнение пользователей"**
- **Описание:** Возможность выбрать нескольких пользователей для сравнения их данных.
- **Цель:** Закрепление навыков работы с массивами и объектами, а также манипуляций с DOM.
- **Реализация:** Добавить флажки для выбора пользователей и кнопку "Сравнить", которая будет отображать таблицу или модальное окно с сравнением выбранных пользователей.

{{< /admonition >}}

### Morse Code Translator

![Morse Code Translator](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fil6si3v62r76udcis9lq.png "Morse Code Translator")

**Описание:** Проект позволяет пользователям переводить текст в азбуку Морзе и обратно. Пользователь может ввести текст и получить соответствующий перевод в азбуку Морзе или ввести код Морзе и получить его перевод в текст.

**Концепции обучения:**

- Манипулирование строками: Работа с строками в JavaScript, включая функции для разбиения, объединения и обработки символов, которые необходимы для перевода азбуки Морзе.
- Условные операторы: Использование условных операторов (if/else) в JavaScript для реализации логики перевода в зависимости от пользовательского ввода (текста или кода Морзе).

{{< admonition info "Пример реализации" false >}}

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
      integrity="sha512-iBBXm8fW90+nuLcSKlbmrPcLa0OT92xO1BIsZ+ywDWZCvqsWgccV3gFoRBv0z+8dLJgyAHIhR35VZc2oM/gI1w=="
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="style.css" />
    <title>Morse Code Translator | DOM Projects</title>
  </head>
  <body>
    <!-- navigation section -->
    <nav>
      <div class="container nav-wrapper">
        <a href="#" class="brand">
          <img src="./img/logo.png" alt="logo" />
          <span>Morse Decoder</span>
        </a>

        <a
          target="_blank"
          href="https://github.com/Jisan-mia/dom-projects/tree/main/projects/5-morse-translator"
          class="brand"
        >
          <img src="./img/github_PNG58.png" alt="github-logo" />
          <span>Github</span>
        </a>
      </div>
    </nav>

    <!-- header section -->
    <section class="header">
      <header class="container">
        <h2>Morse Code Translator</h2>
        <p>
          It's easy to use Morse Code Translator, translate Morse code to text
          and text to Morse code.
        </p>
      </header>
    </section>

    <!-- both input area  -->
    <section class="main container">
      <div class="text-area">
        <div class="top">
          <i id="textClipboard" class="far fa-clipboard"></i>
          <strong>Text</strong>
        </div>
        <textarea
          oninput="onTextInput(this)"
          name="text"
          id="textAreaInput"
          rows="5"
        ></textarea>
      </div>
      <div class="morse-area">
        <div class="top">
          <i id="morseClipboard" class="far fa-clipboard"></i>
          <strong>Morse Code</strong>
        </div>
        <textarea
          oninput="onMorseInput(this)"
          name="morse"
          id="morseAreaInput"
          rows="5"
        ></textarea>
      </div>
    </section>

    <!-- morse faq accordion -->
    <section class="container morse-accordion">
      <h1 style="text-align: center; margin: 20px 0 40px 0" class="faq-heading">
        Morse Code Related FAQ
      </h1>
      <article class="contentBox">
        <h3 class="accordion-label">What is Morse Code?</h3>
        <p class="accordion-content">
          Morse Code is a character encoding scheme that allows operators to
          send messages using a series of electrical pulses represented as short
          or long pulses, dots, and dashes in other words.
        </p>
      </article>

      <article class="contentBox">
        <h3 class="accordion-label">Who Invented Morse Code and When?</h3>
        <p class="accordion-content">
          Samuel F. B. Morse and his assistant Alfred Vail are known as the
          inventors of the Morse code. And Morse code developed in the 1830s
          then advanced in the 1840s.
        </p>
      </article>

      <article class="contentBox">
        <h3 class="accordion-label">What is Morse Code Used For?</h3>
        <p class="accordion-content">
          In the past, Morse code had extensive usage, especially in the
          military. Although Morse code has a limited usage area today, it is
          still being used in aviation, amateur radio activities, and assistive
          technology (AT).
        </p>
      </article>

      <article class="contentBox">
        <h3 class="accordion-label">Who Invented Morse Code and When?</h3>
        <p class="accordion-content">
          Samuel F. B. Morse and his assistant Alfred Vail are known as the
          inventors of the Morse code. And Morse code developed in the 1830s
          then advanced in the 1840s.
        </p>
      </article>

      <article class="contentBox">
        <h3 class="accordion-label">How to Use Morse Code?</h3>
        <p class="accordion-content">
          Morse code can be used in various ways, such as with pen and paper or
          with the aid of light and sound. Even, it can be used with the parts
          of the body like eyes or fingers.
        </p>
      </article>

      <article class="contentBox">
        <h3 class="accordion-label">When Was Morse Code Patented?</h3>
        <p class="accordion-content">
          Samuel Morse received a U.S. patent, US1647A, for dot-dash telegraphy
          signals on June 20, 1840. On the other hand, some sources claim that
          Samuel Morse received a patent issued by an Ottoman Sultan, Abdulmejid
          I, for Morse Code. However, according to Cyrus Hamlin’s memoirs and
          The New York Times obituary published on April 3, 1872, Samuel Morse
          received not a patent, but an order of the Ottoman Empire, Order of
          Glory, instead.
        </p>
      </article>

      <article class="contentBox">
        <h3 class="accordion-label">
          What Was the First Message Sent by Morse Code?
        </h3>
        <p class="accordion-content">
          “What hath God wrought” is the first official message sent by Samuel
          F.B. Morse on May 24, 1844, to open the Baltimore - Washington
          telegraph line.
        </p>
      </article>

      <article class="contentBox">
        <h3 class="accordion-label">What is Morse Code Used For?</h3>
        <p class="accordion-content">
          In the past, Morse code had extensive usage, especially in the
          military. Although Morse code has a limited usage area today, it is
          still being used in aviation, amateur radio activities, and assistive
          technology (AT).
        </p>
      </article>

      <article class="contentBox">
        <h3 class="accordion-label">How to Use Morse Code?</h3>
        <p class="accordion-content">
          “What hath God wrought” is the first official message sent by Samuel
          F.B. Morse on May 24, 1844, to open the Baltimore - Washington
          telegraph line.
        </p>
      </article>

      <article class="contentBox">
        <h3 class="accordion-label">How to Read Morse Code?</h3>
        <p class="accordion-content">
          If you are not proficient enough in reading Morse code, you can look
          up for the corresponding Morse representation of each character from
          the Morse alphabet table, or you can use Morse code translator.
        </p>
      </article>
      <article class="contentBox">
        <h3 class="accordion-label">How to Translate Morse Code?</h3>
        <p class="accordion-content">
          If you’d like to translate or decipher Morse code and if you do not
          know how to read Morse code, you can use Morse Code Translator online.
          With the Morse Decoder, you can decode Morse code and read English
          text easily. Therefore, you can and end your search for the question
          of how do you translate Morse code.
        </p>
      </article>

      <article class="contentBox">
        <h3 class="accordion-label">What is Morse Code Translator?</h3>
        <p class="accordion-content">
          Morse Code Translator is a translator that lets anyone translate text
          to Morse code and decode Morse code to text easily. With the online
          Morse code translator, anyone can convert any plain text in English or
          whatever language to Morse code and vice versa.
        </p>
      </article>

      <article class="contentBox">
        <h3 class="accordion-label">How to Use Morse Code Translator?</h3>
        <p class="accordion-content">
          Just type in the Morse code or text to the corresponding input fields
          to use the Morse code converter. For instance, do you remember the
          Nokia SMS Tone? Try decoding “... -- ...” then playing the audio of
          it. How about decoding a secret message in Morse or the easter egg you
          found in a game you played? Well, Morse Code Translator can help you
          as long as you have an internet connection and the ambition to learn
          Morse code.
        </p>
      </article>

      <article class="contentBox">
        <h3 class="accordion-label">What Does SOS Mean?</h3>
        <p class="accordion-content">
          SOS is a distress signal in Morse code, which is internationally
          recognized worldwide for obtaining help. It was first adopted by the
          German government in 1905. Although some people think that SOS stands
          for “Save Our Souls” or “Save Our Ship”, its letters do not stand for
          anything.
        </p>
      </article>

      <article class="contentBox">
        <h3 class="accordion-label">What is SOS in Morse Code?</h3>
        <p class="accordion-content">SOS in Morse code is “... --- ...”</p>
      </article>

      <article class="contentBox">
        <h3 class="accordion-label">How to Say Hello in Morse Code?</h3>
        <p class="accordion-content">
          “Hello” in Morse code is “.... . .-.. .-.. ---”
        </p>
      </article>

      <article class="contentBox">
        <h3 class="accordion-label">What Does 3 Dots Mean in Morse Code?</h3>
        <p class="accordion-content">
          Letter S is three dots in Morse code: “...”
        </p>
      </article>
      <article class="contentBox">
        <h3 class="accordion-label">International Morse Code Rule</h3>

        <ol class="accordion-content" style="padding-left: 25px">
          <li>The length of a .(dot) is one unit.</li>
          <li>A -(dash) is three unit.</li>
          <li>The space between parts of the same letter is one unit.</li>
          <li>The space beteween letters is three unit.</li>
          <li>The space between words is seven unit.</li>
        </ol>
      </article>
    </section>

    <!-- morse code chart -->
    <section class="morse-chart container">
      <h1>Morse Code Chart</h1>
      <div id="morseMainChart"></div>
    </section>

    <footer class="container">
      <p>
        &copy; Created by
        <a target="_blank" href="https://www.linkedin.com/in/jisan-mia/"
          >Jisan Mia</a
        >
      </p>
    </footer>

    <script src="./script.js"></script>
  </body>
</html>
```

```css
@import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Raleway', Fallback, sans-serif;
  font-size: 16px;
}

.container {
  max-width: 1152px;
  margin: 0 auto;
  width: 90%;
}

/* nav */
nav {
  width: 100%;
  background-color: #f5f5f5;
}

.nav-wrapper {
  width: 90%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
}

.brand img {
  width: 30px;
  margin-right: 8px;
}

.git-link {
  display: flex;
  align-items: center;
}

nav a {
  text-decoration: none;
  color: #48487b;
  padding: 15px 8px;
  font-size: 1rem;
}

nav a:hover {
  background-color: #e8e8e8;
}

/* header */
.header {
  background-image: linear-gradient(90deg, #27276b, #534c98, #27276b);
  color: #fff;
  line-height: 1.5;
}

.header h2 {
  font-size: 2rem;
}

.header .container {
  padding: 20px 0;
}

/* main */

.main {
  margin-top: 20px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  grid-gap: 20px;
}

.main textarea {
  min-width: 100%;
  resize: vertical;
  max-width: 100%;
  border: 0.6px solid lightgray;
  border-radius: 2px;
  margin-top: 10px;
  padding: 10px;
  font-size: 1.1rem;
  color: rgb(58, 55, 55);
  min-height: 160px;
}

.main textarea:focus {
  outline: none !important;
  border-color: #3273dc;
  box-shadow: 0 0 0 0.125rem rgb(50 115 220 / 25%);
}

.main .top i {
  font-size: 1.5rem;
  color: rgb(75, 75, 75);
  margin-right: 8px;
  cursor: pointer;
}

.main .top {
  display: flex;
  align-items: center;
}

/* morsecode chart img */
.morse-chart {
  margin: 60px auto;
  border: 0.5px solid #e0e0e0;
  text-align: center;
}

.morse-chart h1 {
  padding: 12px;
  font-size: 2rem;
}

#morseMainChart {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  /* grid-row-gap: 20px; */
}

.chart-item {
  border-top: 0.1px solid lightgray;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 12px 0;
}

.chart-item strong {
  /* display: block; */
  font-size: 1.2rem;
  font-weight: 800;
}

.chart-item .symbol {
  font-weight: 400;
  font-size: 1.4;
  color: #3d3d3d;
  letter-spacing: 5px;
}

/* accordion design */
/* morse-accordion
contentBox
accordion-label
accordion-content */

.morse-accordion {
  margin: 80px auto;
  font-family: "Roboto", sans-serif;
}

.morse-accordion .contentBox {
  margin: 18px auto;
}

.accordion-label {
  font-weight: 500;
  font-size: 1.1rem;
  background: #eff3f0;
  padding: 15px 20px;
  cursor: pointer;
  transition: all 0.2s linear;
  margin-bottom: 10px;
}

.accordion-label::after {
  content: "+";
  float: right;
  font-size: 1.2rem;
}

.accordion-label.is-open::after {
  content: "-";
}

.accordion-label:hover,
.accordion-label.is-open {
  background: #dbdbdbd0;
}

.accordion-content {
  line-height: 2;
  letter-spacing: 0.9px;
  font-size: 1rem;
  font-weight: 400;
  color: #555454;
  padding: 0px 20px;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease-in-out;
}

/* footer design */
footer {
  text-align: center;
  margin: 40px auto !important;
}

footer p {
  font-family: "Roboto", sans-serif;
  color: #5a5858da;
}

footer a {
  text-decoration: none;
  color: #4714fff5;
}

@media (max-width: 768px) {
  .header h2 {
    font-size: 1.2rem;
  }

  .header p {
    font-size: 0.8rem;
  }

  nav a {
    padding: 15px 0;
  }

  .main textarea {
    min-height: 120px;
  }

  .main .top i {
    font-size: 1rem;
    margin-right: 5px;
  }

  nav a {
    padding: 10px 5px;
    font-size: 0.8rem;
  }

  .brand img {
    width: 20px;
    margin-right: 5px;
  }

  .accordion-content {
    line-height: 1.3;
    letter-spacing: 0.8px;
    font-size: 0.85rem;
    font-weight: 400;
    padding: 0px 12px;
  }

  .morse-accordion .contentBox {
    margin: 10px auto;
  }

  .accordion-label {
    font-weight: 500;
    font-size: 0.9rem;
    padding: 8px 12px;
    margin-bottom: 7px;
  }

  .morse-chart h1 {
    padding: 12px;
    font-size: 1.5rem;
  }
}

@media (max-width: 425px) {
  .main {
    margin-top: 15px;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    grid-gap: 15px;
  }
}
```

```js
const textAreaInput = document.querySelector("#textAreaInput");
const morseAreaInput = document.querySelector("#morseAreaInput");
const textClipboard = document.querySelector("#textClipboard");
const morseClipboard = document.querySelector("#morseClipboard");
const morseMainChart = document.getElementById("morseMainChart");
const accordions = document.querySelectorAll(".accordion-label");
// morse code key vales
const MORSE_CODE = {
  ".-": "A",
  "-...": "B",
  "-.-.": "C",
  "-..": "D",
  ".": "E",
  "..-.": "F",
  "--.": "G",
  "....": "H",
  "..": "I",
  ".---": "J",
  "-.-": "K",
  ".-..": "L",
  "--": "M",
  "-.": "N",
  "---": "O",
  ".--.": "P",
  "--.-": "Q",
  ".-.": "R",
  "...": "S",
  "-": "T",
  "..-": "U",
  "...-": "V",
  ".--": "W",
  "-..-": "X",
  "-.--": "Y",
  "--..": "Z",
  "-----": "0",
  ".----": "1",
  "..---": "2",
  "...--": "3",
  "....-": "4",
  ".....": "5",
  "-....": "6",
  "--...": "7",
  "---..": "8",
  "----.": "9",
};

// MORSE_CODE obj keys to values and values to keys odolbodl
const odolBodolFunc = (keys, values) => {
  let obj = {};
  for (let i = 0; i < keys.length; i++) {
    obj[values[i]] = keys[i];
  }
  return obj;
};
const morseKeys = Object.keys(MORSE_CODE);
const morseValues = Object.values(MORSE_CODE);
const odolBodolMorse = odolBodolFunc(morseKeys, morseValues);

//individual validations
/*
//text input validate
const checkTextInputValidation = (input) => {
	textAreaInput.value = textAreaInput.value.replace(input, "");
	textAreaInput.style.borderColor = "red";
	setTimeout(() => {
		textAreaInput.style.borderColor = "#3273dc";
	}, 400);
};
//morse code validate
const checkMorseValidation = (input) => {
	morseAreaInput.value = morseAreaInput.value.replace(input, "");
	morseAreaInput.style.borderColor = "red";
	setTimeout(() => {
		morseAreaInput.style.borderColor = "#3273dc";
	}, 400);
};
*/

//check validation for both textInputArea and MorseInputArea
const checkInputValidation = (input, inputArea) => {
  inputArea.value = inputArea.value.replace(input, "");

  if (inputArea.value == morseAreaInput.value) {
    if (input === "") {
      // console.log("it's space");
    } else {
      inputArea.style.borderColor = "red";
      setTimeout(() => {
        inputArea.style.borderColor = "#3273dc";
      }, 400);
    }
  } else {
    inputArea.style.borderColor = "red";
    setTimeout(() => {
      inputArea.style.borderColor = "#3273dc";
    }, 400);
  }
};

//show output on screen function
const showOutput = (input, areaInput, tTMMTT) => {
  if (input) {
    areaInput.value = tTMMTT;
  } else {
    areaInput.value = "";
  }
};

// translator for both textToMorse and MorseToText
// tTMMTT = textToMorseOrMorseToText
const textToMorseOrMorseToText = (letters, morseCode, inputArea) => {
  let tTMMTT = [];

  for (let x = 0; x < letters.length; x++) {
    tTMMTT[x] = [];
    for (let y = 0; y < letters[x].length; y++) {
      if (morseCode[letters[x][y]]) {
        tTMMTT[x].push(morseCode[letters[x][y]]);
      } else {
        checkInputValidation(letters[x][y], inputArea);
      }
    }
  }
  return tTMMTT;
};

// text to morse code
const onTextInput = (e) => {
  // JISAN MIA
  const textInput = e.value.toUpperCase();
  const word = textInput.split(" ");
  const letters = word.map((char) => char.split(""));

  /*
	let morse = [];
	for (let x = 0; x < letters.length; x++) {
		morse[x] = [];
		for (let y = 0; y < letters[x].length; y++) {
			if (odolBodolMorse[letters[x][y]]) {
				morse[x].push(odolBodolMorse[letters[x][y]]);
			} else {
				checkInputValidation(letters[x][y], textAreaInput);
			}
		}
	}
*/
  const textToMorse = textToMorseOrMorseToText(
    letters,
    odolBodolMorse,
    textAreaInput
  );
  const textToMorseMain = textToMorse.map((word) => word.join(" ")).join("   ");
  showOutput(textInput, morseAreaInput, textToMorseMain);
};

// morse code to text
const onMorseInput = (e) => {
  // .--- .. ... .- -.   -- .. .-
  /*
	# Another solution
	const morseToTextV2 = morseInput
		.split("   ")
		.map((word) =>
			word
				.split(" ")
				.map((char) => MORSE_CODE[char])
				.join("")
		)
		.join(" ")
		.trim();
*/

  const morseInput = e.value;
  const word = morseInput.split("   ");
  const letters = word.map((char) => char.split(" "));

  /*
	let morseToText2 = [];
	for (let x = 0; x < letters.length; x++) {
		morseToText[x] = [];
		for (let y = 0; y < letters[x].length; y++) {
			if (MORSE_CODE[letters[x][y]]) {
				morseToText[x].push(MORSE_CODE[letters[x][y]]);
			} else {
				checkInputValidation(letters[x][y], morseAreaInput);
			}
		}
	}
	*/

  const morseToText = textToMorseOrMorseToText(
    letters,
    MORSE_CODE,
    morseAreaInput
  );

  const morseToTextMain = morseToText.map((word) => word.join("")).join(" ");

  showOutput(morseInput, textAreaInput, morseToTextMain);
};

// copy clipboard
textClipboard.addEventListener("click", function () {
  copyClipboard(textAreaInput);
});
morseClipboard.addEventListener("click", function () {
  copyClipboard(morseAreaInput);
});

//function for copying clipboard for both morseinput and textinput
function copyClipboard(areaInput) {
  if (textAreaInput.value || morseAreaInput.value) {
    areaInput.select();
    areaInput.setSelectionRange(0, 99999);

    /* Copy the text inside the text field */
    document.execCommand("copy");

    /* Alert the copied text */
    alert("Copied the text: " + areaInput.value);
  } else {
    alert("Type something to copy");
  }
}

// show morse code of English alphabet and numbers in the ui
Object.entries(MORSE_CODE).forEach(([key, value]) => {
  const colros = [
    "#FAFAFA",
    "#fcfcfc",
    "#f7f5f6",
    "#e3e4e5",
    "#d9dfe0",
    "#fdfff5",
    "#e5e9e1",
    "#dde4e3",
    "#d2d2df", //8
    "#d6d7d2",
    "#dee1e9",
    "#dcdcdc",
    "#fafafa", //12
    "#dae4ee",
    "#e5edf1",
    "#e2e3eb", //15
    "#f7f7f7",
    "#f4f5f0",
    "#eff3f0",
    "#f8f8ff",
  ];

  const randomInd = Math.floor(Math.random() * colros.length + 1);
  const randomCol = colros[randomInd];

  morseMainChart.innerHTML += `<div style="background-color: ${randomCol}" class="chart-item">
							 		<strong> ${value}</strong> 
									<strong class="symbol"> ${key} </strong> 	
								<div>`;
});

// accordion
Array.from(accordions).forEach((accordion) => {
  accordion.addEventListener("click", function () {
    // toggle accordions + and -
    this.classList.toggle("is-open");
    const content = this.nextElementSibling;
    if (content.style.maxHeight) {
      //content is open, need to close
      content.style.maxHeight = null;
    } else {
      // content is close, need to open
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
});
```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

#### HTML

HTML-код создает структуру страницы с элементами управления и информационными разделами:

1. **Навигация:**
   - `<nav>` содержит ссылки на главную страницу и репозиторий проекта на GitHub.

2. **Основные элементы:**
   - Раздел с заголовком и описанием переводчика азбуки Морзе.
   - Два текстовых поля для ввода текста и кода Морзе. При вводе текста или кода срабатывают функции `onTextInput(this)` и `onMorseInput(this)` соответственно.
   - Секция с часто задаваемыми вопросами (FAQ) об азбуке Морзе, представленная в виде аккордеона.
   - Таблица с кодами Морзе для различных символов (букв и цифр).
   - Подвал страницы с указанием автора проекта.

#### CSS

CSS стилизует элементы страницы, улучшая их внешний вид и делая интерфейс удобным для пользователя:

1. **Основные стили:**
   - Установка шрифта, базовых отступов и размера текста.
   - Стилизация навигации, заголовка и текстовых полей.
   - Стилизация аккордеона для секции FAQ, таблицы кодов Морзе и других элементов.
   
2. **Медиа-запросы:**
   - Используются для обеспечения адаптивного дизайна на различных устройствах, таких как мобильные телефоны и планшеты.

#### JavaScript

JavaScript реализует логику перевода текста в азбуку Морзе и наоборот, а также добавляет дополнительные функции для взаимодействия пользователя с приложением. Рассмотрим основные части кода:

1. **Определение элементов DOM:**
   - `const textAreaInput` и `const morseAreaInput` — получают доступ к полям ввода текста и кода Морзе.
   - `const MORSE_CODE` — объект, содержащий соответствие между символами и их представлением в азбуке Морзе.

2. **Функции перевода:**
   - **`textToMorseOrMorseToText`** — универсальная функция, которая обрабатывает перевод текста в код Морзе и обратно, используя соответствия символов и кода Морзе из объекта `MORSE_CODE`.
   - **`onTextInput`** — функция, которая вызывается при вводе текста. Преобразует введенный текст в код Морзе и отображает результат.
   - **`onMorseInput`** — функция, вызываемая при вводе кода Морзе. Преобразует введенный код в текст и отображает результат.

3. **Функции проверки ввода:**
   - **`checkInputValidation`** — проверяет правильность ввода данных в текстовые поля и визуально выделяет ошибки красным цветом.
   - **`showOutput`** — отображает результат перевода в соответствующем поле.

4. **Копирование текста в буфер обмена:**
   - **`copyClipboard`** — функция для копирования текста или кода Морзе в буфер обмена при нажатии на соответствующую кнопку.

5. **Отображение таблицы с символами Морзе:**
   - `Object.entries(MORSE_CODE).forEach()` — заполняет таблицу кодов Морзе в HTML, используя данные из объекта `MORSE_CODE`.

6. **Реализация аккордеона:**
   - Обработчики событий для каждого аккордеона (`accordion`) добавляют или убирают класс `is-open` и изменяют максимальную высоту контента для анимации раскрытия/скрытия FAQ.

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

### 1. **Реализация поддержки различных языков**

- **Описание:** Добавить возможность перевода текста на разных языках в азбуку Морзе и обратно.
- **Цель:** Изучение работы с различными языковыми наборами и их соответствием азбуке Морзе.
- **Реализация:** Добавить переключатель языка и расширить логику преобразования, чтобы поддерживать различные алфавиты (например, кириллицу, латиницу).

### 2. **Добавление функции аудиовоспроизведения кода Морзе**
- **Описание:** Возможность воспроизведения кода Морзе с помощью звуковых сигналов (точек и тире).
- **Цель:** Изучение работы с Web Audio API для создания и управления аудиосигналами.
- **Реализация:** Создать функцию, которая преобразует текст в звуковые сигналы, используя `OscillatorNode` для воспроизведения коротких и длинных сигналов.

### 3. **Поддержка визуального воспроизведения кода Морзе (световой сигнал)**
- **Описание:** Реализовать функцию, которая использует визуальные индикаторы (например, мигающий свет) для отображения кода Морзе.
- **Цель:** Закрепление навыков работы с CSS-анимациями и JavaScript для управления анимацией.
- **Реализация:** Создать элемент (например, кружок), который будет менять цвет или яркость в зависимости от длины сигнала.

### 4. **Добавление функции обучения азбуке Морзе**
- **Описание:** Реализовать режим обучения, который помогает пользователю запомнить символы азбуки Морзе.
- **Цель:** Изучение работы с динамическим созданием элементов и обработкой событий.
- **Реализация:** Добавить режим, где пользователю показывается случайный символ в Морзе, и он должен ввести соответствующую букву или символ.

### 5. **Создание клавиатуры для ввода кода Морзе**
- **Описание:** Создать виртуальную клавиатуру для ввода кода Морзе с помощью точек и тире.
- **Цель:** Закрепление навыков работы с событиями мыши и клавиатуры, а также взаимодействием с DOM.
- **Реализация:** Добавить виртуальную клавиатуру с кнопками для ввода точек и тире, а также кнопкой для удаления символов и разделителей.

### 6. **Добавление функции перевода текстовых файлов в азбуку Морзе и обратно**
- **Описание:** Возможность загружать текстовые файлы и преобразовывать их содержимое в азбуку Морзе или наоборот.
- **Цель:** Изучение работы с файловыми API, чтением файлов и их содержимого в JavaScript.
- **Реализация:** Добавить элемент `<input type="file">` для загрузки файлов и функцию для их чтения с использованием `FileReader`.

### 7. **Интеграция с браузерными уведомлениями**
- **Описание:** Использовать уведомления для отправки переведенного текста или напоминаний пользователю.
- **Цель:** Изучение работы с Web Notifications API.
- **Реализация:** Отправлять уведомление с результатом перевода, например, когда пользователь завершает ввод.

### 8. **Добавление кнопки "Скопировать/Очистить" для удобства пользователя**
- **Описание:** Добавить кнопки для копирования переведенного текста в буфер обмена и очистки всех полей ввода.
- **Цель:** Закрепление навыков работы с буфером обмена и манипуляцией DOM.
- **Реализация:** Создать кнопки "Скопировать" и "Очистить" с соответствующими обработчиками событий для выполнения этих действий.

### 9. **Реализация функции сохранения истории переводов**
- **Описание:** Хранить историю всех переводов, чтобы пользователь мог вернуться к предыдущим переводам.
- **Цель:** Практика работы с `localStorage` или `sessionStorage` для сохранения данных на стороне клиента.
- **Реализация:** Сохранять каждый перевод в `localStorage` и предоставлять пользователю интерфейс для просмотра или удаления истории переводов.

### 10. **Реализация поддержки темной и светлой темы интерфейса**
- **Описание:** Возможность переключения между светлой и темной темами интерфейса.
- **Цель:** Закрепление навыков работы с темами и изменением CSS-переменных или классов.
- **Реализация:** Добавить переключатель темы на странице, который будет изменять тему с помощью CSS-переменных или добавления/удаления классов.

### 11. **Добавление функции "Перевод из аудиовхода"**
- **Описание:** Возможность записи аудиосигналов с микрофона и их расшифровки в текст.
- **Цель:** Изучение работы с Web Audio API и распознаванием звуковых сигналов.
- **Реализация:** Использовать API для записи аудио и алгоритмы для распознавания частоты звуковых сигналов (точек и тире).

### 12. **Поддержка морзе-чатов**
- **Описание:** Создание функции обмена сообщениями в реальном времени, где текст автоматически переводится в код Морзе.
- **Цель:** Практика работы с WebSockets или Firebase для создания реального чата.
- **Реализация:** Реализовать интерфейс чата, где пользователи могут отправлять сообщения, которые будут автоматически переводиться в Морзе.

### 13. **Добавление режима тестирования на скорость перевода**
- **Описание:** Добавить режим тестирования, где пользователи могут соревноваться, кто быстрее переведет текст в код Морзе или наоборот.
- **Цель:** Практика работы с таймерами, управлением состоянием игры и манипуляцией DOM.
- **Реализация:** Создать режим игры, где пользователь видит таймер и случайный текст или код Морзе для перевода.

### 14. **Добавление функции преобразования текста в изображения для визуального кода Морзе**
- **Описание:** Возможность преобразования текста в изображения кода Морзе для сохранения или отправки.
- **Цель:** Закрепление навыков работы с HTML5 Canvas API.
- **Реализация:** Создать изображение кода Морзе, используя Canvas API, и позволить пользователю скачать его.

### 15. **Реализация адаптивного дизайна**
- **Описание:** Сделать интерфейс приложения адаптивным для разных устройств, включая мобильные телефоны и планшеты.
- **Цель:** Закрепление навыков работы с Flexbox, Grid и медиа-запросами в CSS.
- **Реализация:** Оптимизировать макет для разных размеров экранов, чтобы интерфейс оставался удобным и функциональным на любом устройстве.

{{< /admonition >}}

<!--

### Calculator

![Normal Calculator](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqpgq9hnt59vlcaz8r0zx.png "Calculator")

**Description**: This project builds upon the basic calculator by offering a more comprehensive user experience for standard mathematical calculations. It caters to users familiar with basic calculator functionalities.

**Learning Concepts:**

-   Building upon existing projects: Demonstrates expanding on the basic calculator concept to create a more user-friendly and feature-rich calculator.
-   Enhanced user interaction: Introduces techniques for improving user interaction with the calculator, such as handling decimal inputs or incorporating memory functions.

{{< admonition info "Пример реализации" false >}}

```html
```

```css
```

```js

```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

{{< /admonition >}}

### Scientific Calculator

![Scientific Calculator](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4taeew6vv1ublamhbyod.png "Scientific Calculator")

**Description**: This project takes calculator functionality to the next level by offering scientific functions like trigonometry (sine, cosine, tangent), logarithms, and exponents. It caters to users who require advanced mathematical calculations.

**Learning Concepts:**

-   Building complex applications: Demonstrates creating a more intricate application with advanced scientific functionalities.
-   Mathematical functions in JavaScript: Introduces using JavaScript's built-in math functions for advanced calculations

{{< admonition info "Пример реализации" false >}}

```html
```

```css
```

```js

```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

{{< /admonition >}}

### Simple Todo App

![Simple Todo App](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F55d842o20i8j528q2maz.png "Simple Todo App")

**Description**: This project is a basic to-do list application. Users can add new tasks, mark them as completed, and delete them from the list. It demonstrates managing and keeping track of tasks.

**Learning Concepts:**

-   DOM manipulation: This project reinforces practices of adding, removing, and modifying list items in the HTML dynamically using JavaScript.
-   Arrays: It demonstrates storing and managing task data using arrays in JavaScript.
-   User interface updates: Explores how to update the visual representation of the to-do list (adding, completing, deleting tasks) based on user interactions.

{{< admonition info "Пример реализации" false >}}

```html
```

```css
```

```js

```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

{{< /admonition >}}

### Profile Form & Card

![Profile Form & Card](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F13yidfqfe156556rky87.png "Profile Form & Card")

**Description**: This project allows users to create dynamic profile cards with a form. Users can enter their information, and upon submission, a new profile card is created and displayed on the page. It also includes functionality to delete existing profile cards.

**Learning Concepts:**

-   Form handling: This project builds upon concepts from form validation (project 3) by focusing on capturing form data and utilizing it for further actions.
-   DOM creation and manipulation: It goes beyond basic DOM manipulation by dynamically creating new HTML elements (profile cards) based on user input.
-   Event handling: Continues practicing capturing user interactions with the form and delete buttons and triggering appropriate actions.

{{< admonition info "Пример реализации" false >}}

```html
```

```css
```

```js

```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

{{< /admonition >}}

### PC Component Filtering

![PC Component Filtering](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ftxtgpqu4t0zbi2mcovbo.png "PC Component Filtering")

**Description**: This project allows users to filter computer parts based on their selections. Users can choose from various options like CPU brand, RAM size, graphics card type, etc., and the displayed list of components will update dynamically to reflect the chosen filters.

**Learning Concepts:**

-   DOM manipulation: Similar to previous projects, this project practices updating the displayed component list dynamically based on user selections.
-   Arrays and data filtering: Explores using arrays to store computer part data and implements filtering logic in JavaScript to match user selections.
-   User interface updates: Focuses on updating the visual representation of the component list based on the applied filters.

{{< admonition info "Пример реализации" false >}}

```html
```

```css
```

```js

```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

{{< /admonition >}}

### Weather App

![Weather App](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fl4tjhdmz5xlpxia218lp.png "Weather App")

**Description**: This project is a weather application that allows users to search for current weather information by city name. It utilizes an external weather API to fetch data and displays details like temperature, humidity, and weather conditions on the screen.

**Learning Concepts:**

-   Asynchronous programming: Similar to projects like DadJokes, this project reinforces concepts of handling asynchronous operations for fetching weather data.
-   Fetch API: Continues practicing using tools for making HTTP requests to APIs and retrieving weather data.
-   Working with APIs: Further explores interacting with external APIs to access weather information.

{{< admonition info "Пример реализации" false >}}

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

{{< /admonition >}}

### Testimonial Slider

![Testimonial Slider](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsroguxb8914j1dv65fpw.png "Testimonial Slider")

**Description**: This project creates a testimonial section with a slider functionality. It displays quotes or testimonials from users, and users can navigate through them using a slider control.

**Learning Concepts:**

-   DOM manipulation: Demonstrates manipulating the visibility of testimonial elements based on the slider position.
-   Event handling: Captures user interactions with the slider control and triggers the sliding animation.

{{< admonition info "Пример реализации" false >}}

```html
```

```css
```

```js

```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

{{< /admonition >}}

### Animation on Scroll

![Animation on Scroll](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3o5psut9f3d5cmns3ld3.png "Animation on Scroll") 
**Description**: This project incorporates animations that are triggered as you scroll down the page. As the user scrolls, different elements on the web page become animated, adding visual interest and interactivity.

**Learning Concepts:**

-   CSS animations: Explores using CSS animations to create visual effects that activate based on scroll position.
-   JavaScript for scroll events: Introduces using JavaScript to detect scroll events and trigger animations accordingly.

{{< admonition info "Пример реализации" false >}}

```html
```

```css
```

```js

```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

{{< /admonition >}}

### Search Field Reveal

![Search Field Reveal](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fawycht9282x9n35gyy5j.png "Search Field Reveal")

**Description**: This project utilizes animations to enhance the user experience. It creates a search field that reveals itself with an animation upon user interaction (e.g., clicking a button).

**Learning Concepts:**

-   CSS animations: Introduces using CSS animations to create dynamic visual effects for the search field reveal.
-   Event handling: Covers capturing user interactions (eg. button clicks) and using JavaScript to trigger the animations.

{{< admonition info "Пример реализации" false >}}

```html
```

```css
```

```js

```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

{{< /admonition >}}

### Question List & Progress

![Question List & Progress](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1p6unngf1az0084i3tnb.png "Question List & Progress")

**Description**: This project demonstrates common DOM manipulation techniques in JavaScript. It features a list of questions and a progress indicator that updates as the user answers the questions.

**Learning Concepts:**

-   DOM manipulation: This project emphasizes manipulating elements like the progress indicator based on user interaction with the questions.
-   Event handling: Captures user interactions with the question elements and triggers actions like updating the progress indicator.

{{< admonition info "Пример реализации" false >}}

```html
```

```css
```

```js

```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

{{< /admonition >}}

### Modal

![Modal](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fq0b06e0fi84z7wqsjev4.png "Modal") 
**Description**: This project creates a modal window, which is a popup element that overlays the main content of the page. It's commonly used for things like login forms, signup prompts, or alert messages.

**Learning Concepts:**

-   DOM manipulation: Focuses on showing and hiding the modal window element based on user interaction.
-   Event handling: Captures clicks on the trigger element and the modal's close button to control its visibility.

{{< admonition info "Пример реализации" false >}}

```html
```

```css
```

```js

```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

{{< /admonition >}}

### Advanced Todo

![Advanced Todo](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8baq9a3n6qdwlookd338.png "Advanced Todo")

**Description**: This project builds upon the simple to-do app (project 8) by offering advanced functionalities like filtering, editing, and deleting tasks. Users can categorize tasks, edit existing ones, and delete unwanted tasks from the list.

**Learning Concepts:**

-   Building upon existing projects: Similar to the scientific calculator (project 7), this project demonstrates expanding on a basic concept (to-do list) to create a more advanced application.
-   User interface updates: Extends the concept of updating the to-do list to include functionalities like filtering, editing task content, and removing tasks.

{{< admonition info "Пример реализации" false >}}

```html
```

```css
```

```js

```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

{{< /admonition >}}

### Retro Calculator

![Retro Calculator](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fthdpc8rzcppjfhlw8aru.png "Retro Calculator")

**Description**: This project implements a classic calculator design with a physical keyboard support for input. It allows users to enter numbers and perform calculations using a layout resembling a traditional calculator.

**Learning Concepts:**

-   Event handling: Similar to other projects, this project focuses on capturing user interactions, but in this case, it includes handling both clicks on calculator buttons and key presses from the keyboard.
-   DOM manipulation: Updates the calculator display based on user input and calculation results.
-   Object-oriented programming: This project introduces concepts of object-oriented programming (OOP) in JavaScript for creating a more modular and reusable calculator functionality.

{{< admonition info "Пример реализации" false >}}

```html
```

```css
```

```js

```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

{{< /admonition >}}

### Simple Quiz App

![Simple Quiz App](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkhvz1xnzfvusxb8hvwrh.png "Simple Quiz App")
**Description**: This project creates a simple quiz application where users can answer questions and see their results. It includes a timer for each question to add a time pressure element.

**Learning Concepts:**

-   DOM manipulation: Updates the quiz interface to display questions, handle answer selections, and show the final

{{< admonition info "Пример реализации" false >}}

```html
```

```css
```

```js

```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

{{< /admonition >}}

### Advanced Quiz App

![Advanced Quiz App](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F98kzkz9jyfl6vjkau9z1.png "Advanced Quiz App")

**Description**: This project builds upon the simple quiz app by offering more customization options. Users can set the number of questions, choose the topic, and define the difficulty level before starting the quiz.

**Learning Concepts:**

-   Building upon existing projects: Similar to other projects (scientific calculator, advanced to-do list), this project demonstrates extending a basic concept with additional features.
-   User input validation: It introduces concepts of validating user input for the customization options (e.g., ensuring a valid number of questions is chosen).
-   Conditional statements: Plays a more prominent role in this project as JavaScript logic needs to adapt the quiz based on user-defined parameters.

{{< admonition info "Пример реализации" false >}}

```html
```

```css
```

```js

```

{{< /admonition >}}

{{< admonition info "Пояснение к коду реализации" false >}}

{{< /admonition >}}

{{< admonition info "Идеи для улучшения" false >}}

{{< /admonition >}}

### Take the Next Step:

Ready to embark on your front-end development journey? Here's how to get started with DOM Projects:

1.  Visit the DOM Projects repository on GitHub: [https://github.com/Jisan-mia/dom-projects](https://github.com/Jisan-mia/dom-projects)
2.  Browse the project list and choose one that aligns with your skill level and interests.
3.  Follow the setup [instructions](https://github.com/Jisan-mia/dom-projects?tab=readme-ov-file#how-to-set-up-dom-projects-for-development) and open the project in your browser.
4.  Dive into the code, experiment, and learn!

Each project in DOM Projects allows you to practice your coding skills and helps you understand key concepts in front-end development. Whether you’re a beginner just starting or an experienced developer looking to brush up your skills, DOM Projects has something for everyone.

Remember, the best way to learn is by doing. So, roll up your sleeves, pick a project, and start coding! Happy learning!

-->