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

[![Counter](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fegsodt4dyfekiwp8ln4q.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fegsodt4dyfekiwp8ln4q.png)  
**Описание:** Простой проект счетчика, который позволяет пользователям увеличивать и уменьшать число, отображаемое на экране. Он также включает кнопку для сброса счетчика на ноль.

**Концепции обучения:**

- Манипулирование DOM: Узнайте, как получить доступ к элементам HTML и изменять их с помощью JavaScript.
- Обработка событий: Поймите, как перехватывать действия пользователя (в данном случае щелчки) и вызывать определенные действия с помощью JavaScript.
- Основные функции JavaScript: Изучите, как писать функции для выполнения таких задач, как увеличение, уменьшение и сброс значения счетчика.

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

В HTML-коде проекта создается базовая структура страницы:

1. **Основные элементы:**
   - `h2` используется для заголовка "Counter".
   - `h1` с `id="counter-value"` — это элемент, который отображает текущее значение счетчика и может быть редактируемым (`contenteditable="true"`). Изначально значение установлено в `0`.
   - Блок `section` с классом `btn-area` содержит три кнопки: "уменьшить" (`-`), "сбросить" (↻), и "увеличить" (`+`).

2. **Подключение JavaScript:**
   - `<script src="./script.js"></script>` подключает файл JavaScript, который будет обрабатывать события кнопок.

#### CSS

CSS для этого проекта отсутствует в данном тексте, но предполагается, что он будет использоваться для оформления элементов на странице. Например, можно использовать CSS для расположения кнопок, изменения цветов и улучшения визуального восприятия.

#### JavaScript

JavaScript отвечает за управление логикой счетчика. Рассмотрим код подробнее:

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
   - Наконец, после всех вычислений, обновляется текст внутри элемента `h1` с новым значением счетчика:
     ```js
     counterValue.innerText = count;
     ```

{{< /admonition >}}

### DadJokes

[![DadJokes](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fz09wwb70arrb5ccjhl87.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fz09wwb70arrb5ccjhl87.png)  
**Описание:** Этот проект получает случайные шутки про отца из внешнего API, используя асинхронные методы на JavaScript. После получения анекдот отображается на веб-странице для вашего развлечения.

**Концепции обучения:**

- Асинхронное программирование: Поймите, как обрабатывать операции, требующие времени для завершения (например, получение данных из API), не блокируя основной поток выполнения в JavaScript.
- Fetch API: Узнайте, как использовать встроенные функции браузера для выполнения HTTP-запросов к API и получения данных.
- Работа с API: Изучите, как взаимодействовать с внешними API для получения доступа к данным или функциональным возможностям, предоставляемым этими сервисами.

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

### Form Validation

[![Form Validation](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7b7mbyvuwxdwkzv2eidr.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7b7mbyvuwxdwkzv2eidr.png)  
**Описание**: Этот проект демонстрирует проверку формы на стороне клиента с помощью JavaScript. Он проверяет вводимые пользователем данные в форме перед отправкой. Кроме того, при успешной проверке выводится сообщение об успехе, а пользователи могут просматривать введенные данные в формате, доступном только для чтения.

**Концепции обучения:**

- Валидация формы: Поймите, как использовать JavaScript для проверки вводимых пользователем данных в формах перед отправкой. Это помогает обеспечить целостность данных и предотвратить обработку недействительных данных.
- Манипулирование DOM: Узнайте, как получать доступ к элементам формы и изменять их (например, выводить сообщения об ошибках или отключать поля ввода) на основе результатов проверки.
- Обработка событий: Перехватывайте событие отправки формы и запускайте логику проверки с помощью JavaScript.

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

<!--

### Random User

[![Random User](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjlfog2j2okpgtx01eyso.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjlfog2j2okpgtx01eyso.png)  
**Description**: This project utilizes an API to generate random user information. It fetches data like name, email, avatar, and more, and displays it on the web page, simulating a random user profile.

**Learning Concepts:**

-   Asynchronous programming: Similar to project 2 (DadJokes), this project reinforces asynchronous operations in JavaScript.
-   Fetch API: Continues practicing using tools for making HTTP requests to APIs and retrieving data.
-   Working with APIs: Further explores interacting with external APIs to access specific functionalities or data.

### Morse Code Translator

[![Morse Code Translator](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fil6si3v62r76udcis9lq.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fil6si3v62r76udcis9lq.png)  
**Description**: This project allows users to translate between Morse code and text. Users can either type text and see the corresponding Morse code or enter Morse code and view the translated text.

**Learning Concepts**:

-   String manipulation: Understand how to work with strings in JavaScript, including functions for splitting, joining, and character manipulation, which are crucial for Morse code translation.
-   Conditional statements: Learn how to use conditional statements (if/else) in JavaScript to implement the translation logic based on user input (text or Morse code).

### Basic Calculator

[![Basic Calculator](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Friz357iso4aux1an08sx.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Friz357iso4aux1an08sx.png)  
**Description**: This project uses JavaScript to build a bare minimum basic calculator application. It allows users to perform fundamental arithmetic operations like addition, subtraction, multiplication, and division. Users can enter numbers and choose the desired operation using buttons on the screen. The calculator displays the calculated result.

**Learning Concepts**:

-   Event handling: Similar to previous projects, this project practices capturing user clicks on calculator buttons and triggering actions (updating the calculation and result).
-   DOM manipulation: Demonstrates how to update the displayed numbers and result within the calculator interface using JavaScript.
-   Basic math operations in JavaScript: Explores using JavaScript's built-in math operators and functions for performing calculations like addition, subtraction, multiplication, and division.

### Normal Calculator

[![Normal Calculator](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqpgq9hnt59vlcaz8r0zx.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqpgq9hnt59vlcaz8r0zx.png)  
**Description**: This project builds upon the basic calculator by offering a more comprehensive user experience for standard mathematical calculations. It caters to users familiar with basic calculator functionalities.

**Learning Concepts:**

-   Building upon existing projects: Demonstrates expanding on the basic calculator concept to create a more user-friendly and feature-rich calculator.
-   Enhanced user interaction: Introduces techniques for improving user interaction with the calculator, such as handling decimal inputs or incorporating memory functions.

### Scientific Calculator

[![Scientific Calculator](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4taeew6vv1ublamhbyod.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4taeew6vv1ublamhbyod.png)  
**Description**: This project takes calculator functionality to the next level by offering scientific functions like trigonometry (sine, cosine, tangent), logarithms, and exponents. It caters to users who require advanced mathematical calculations.

**Learning Concepts:**

-   Building complex applications: Demonstrates creating a more intricate application with advanced scientific functionalities.
-   Mathematical functions in JavaScript: Introduces using JavaScript's built-in math functions for advanced calculations

### Simple Todo App

[![Simple Todo App](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F55d842o20i8j528q2maz.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F55d842o20i8j528q2maz.png)  
**Description**: This project is a basic to-do list application. Users can add new tasks, mark them as completed, and delete them from the list. It demonstrates managing and keeping track of tasks.

**Learning Concepts:**

-   DOM manipulation: This project reinforces practices of adding, removing, and modifying list items in the HTML dynamically using JavaScript.
-   Arrays: It demonstrates storing and managing task data using arrays in JavaScript.
-   User interface updates: Explores how to update the visual representation of the to-do list (adding, completing, deleting tasks) based on user interactions.

### Profile Form & Card

[![Profile Form & Card](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F13yidfqfe156556rky87.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F13yidfqfe156556rky87.png)  
**Description**: This project allows users to create dynamic profile cards with a form. Users can enter their information, and upon submission, a new profile card is created and displayed on the page. It also includes functionality to delete existing profile cards.

**Learning Concepts:**

-   Form handling: This project builds upon concepts from form validation (project 3) by focusing on capturing form data and utilizing it for further actions.
-   DOM creation and manipulation: It goes beyond basic DOM manipulation by dynamically creating new HTML elements (profile cards) based on user input.
-   Event handling: Continues practicing capturing user interactions with the form and delete buttons and triggering appropriate actions.

### PC Component Filtering

[![PC Component Filtering](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ftxtgpqu4t0zbi2mcovbo.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ftxtgpqu4t0zbi2mcovbo.png)  
**Description**: This project allows users to filter computer parts based on their selections. Users can choose from various options like CPU brand, RAM size, graphics card type, etc., and the displayed list of components will update dynamically to reflect the chosen filters.

**Learning Concepts:**

-   DOM manipulation: Similar to previous projects, this project practices updating the displayed component list dynamically based on user selections.
-   Arrays and data filtering: Explores using arrays to store computer part data and implements filtering logic in JavaScript to match user selections.
-   User interface updates: Focuses on updating the visual representation of the component list based on the applied filters.

### Weather App

[![Weather App](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fl4tjhdmz5xlpxia218lp.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fl4tjhdmz5xlpxia218lp.png)  
**Description**: This project is a weather application that allows users to search for current weather information by city name. It utilizes an external weather API to fetch data and displays details like temperature, humidity, and weather conditions on the screen.

**Learning Concepts:**

-   Asynchronous programming: Similar to projects like DadJokes (project 2), this project reinforces concepts of handling asynchronous operations for fetching weather data.
-   Fetch API: Continues practicing using tools for making HTTP requests to APIs and retrieving weather data.
-   Working with APIs: Further explores interacting with external APIs to access weather information.

### Testimonial Slider

[![Testimonial Slider](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsroguxb8914j1dv65fpw.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsroguxb8914j1dv65fpw.png)  
**Description**: This project creates a testimonial section with a slider functionality. It displays quotes or testimonials from users, and users can navigate through them using a slider control.

**Learning Concepts:**

-   DOM manipulation: Demonstrates manipulating the visibility of testimonial elements based on the slider position.
-   Event handling: Captures user interactions with the slider control and triggers the sliding animation.

### Animation on Scroll

[![Animation on Scroll](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3o5psut9f3d5cmns3ld3.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3o5psut9f3d5cmns3ld3.png)  
**Description**: This project incorporates animations that are triggered as you scroll down the page. As the user scrolls, different elements on the web page become animated, adding visual interest and interactivity.

**Learning Concepts:**

-   CSS animations: Explores using CSS animations to create visual effects that activate based on scroll position.
-   JavaScript for scroll events: Introduces using JavaScript to detect scroll events and trigger animations accordingly.

### Search Field Reveal

[![Search Field Reveal](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fawycht9282x9n35gyy5j.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fawycht9282x9n35gyy5j.png)  
**Description**: This project utilizes animations to enhance the user experience. It creates a search field that reveals itself with an animation upon user interaction (e.g., clicking a button).

**Learning Concepts:**

-   CSS animations: Introduces using CSS animations to create dynamic visual effects for the search field reveal.
-   Event handling: Covers capturing user interactions (eg. button clicks) and using JavaScript to trigger the animations.

### Question List & Progress

[![Question List & Progress](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1p6unngf1az0084i3tnb.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1p6unngf1az0084i3tnb.png)  
**Description**: This project demonstrates common DOM manipulation techniques in JavaScript. It features a list of questions and a progress indicator that updates as the user answers the questions.

**Learning Concepts:**

-   DOM manipulation: This project emphasizes manipulating elements like the progress indicator based on user interaction with the questions.
-   Event handling: Captures user interactions with the question elements and triggers actions like updating the progress indicator.

### Modal

[![Modal](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fq0b06e0fi84z7wqsjev4.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fq0b06e0fi84z7wqsjev4.png)  
**Description**: This project creates a modal window, which is a popup element that overlays the main content of the page. It's commonly used for things like login forms, signup prompts, or alert messages.

**Learning Concepts:**

-   DOM manipulation: Focuses on showing and hiding the modal window element based on user interaction.
-   Event handling: Captures clicks on the trigger element and the modal's close button to control its visibility.

### Advanced Todo

[![Advanced Todo](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8baq9a3n6qdwlookd338.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8baq9a3n6qdwlookd338.png)  
**Description**: This project builds upon the simple to-do app (project 8) by offering advanced functionalities like filtering, editing, and deleting tasks. Users can categorize tasks, edit existing ones, and delete unwanted tasks from the list.

**Learning Concepts:**

-   Building upon existing projects: Similar to the scientific calculator (project 7), this project demonstrates expanding on a basic concept (to-do list) to create a more advanced application.
-   User interface updates: Extends the concept of updating the to-do list to include functionalities like filtering, editing task content, and removing tasks.

### Retro Calculator

[![Retro Calculator](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fthdpc8rzcppjfhlw8aru.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fthdpc8rzcppjfhlw8aru.png)  
**Description**: This project implements a classic calculator design with a physical keyboard support for input. It allows users to enter numbers and perform calculations using a layout resembling a traditional calculator.

**Learning Concepts:**

-   Event handling: Similar to other projects, this project focuses on capturing user interactions, but in this case, it includes handling both clicks on calculator buttons and key presses from the keyboard.
-   DOM manipulation: Updates the calculator display based on user input and calculation results.
-   Object-oriented programming: This project introduces concepts of object-oriented programming (OOP) in JavaScript for creating a more modular and reusable calculator functionality.

### Simple Quiz App

[![Simple Quiz App](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkhvz1xnzfvusxb8hvwrh.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkhvz1xnzfvusxb8hvwrh.png)  
**Description**: This project creates a simple quiz application where users can answer questions and see their results. It includes a timer for each question to add a time pressure element.

**Learning Concepts:**

-   DOM manipulation: Updates the quiz interface to display questions, handle answer selections, and show the final

### Advanced Quiz App

[![Advanced Quiz App](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F98kzkz9jyfl6vjkau9z1.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F98kzkz9jyfl6vjkau9z1.png)  
**Description**: This project builds upon the simple quiz app by offering more customization options. Users can set the number of questions, choose the topic, and define the difficulty level before starting the quiz.

**Learning Concepts:**

-   Building upon existing projects: Similar to other projects (scientific calculator, advanced to-do list), this project demonstrates extending a basic concept with additional features.
-   User input validation: It introduces concepts of validating user input for the customization options (e.g., ensuring a valid number of questions is chosen).
-   Conditional statements: Plays a more prominent role in this project as JavaScript logic needs to adapt the quiz based on user-defined parameters.

### Take the Next Step:

Ready to embark on your front-end development journey? Here's how to get started with DOM Projects:

1.  Visit the DOM Projects repository on GitHub: [https://github.com/Jisan-mia/dom-projects](https://github.com/Jisan-mia/dom-projects)
2.  Browse the project list and choose one that aligns with your skill level and interests.
3.  Follow the setup [instructions](https://github.com/Jisan-mia/dom-projects?tab=readme-ov-file#how-to-set-up-dom-projects-for-development) and open the project in your browser.
4.  Dive into the code, experiment, and learn!

Each project in DOM Projects allows you to practice your coding skills and helps you understand key concepts in front-end development. Whether you’re a beginner just starting or an experienced developer looking to brush up your skills, DOM Projects has something for everyone.

Remember, the best way to learn is by doing. So, roll up your sleeves, pick a project, and start coding! Happy learning!

-->