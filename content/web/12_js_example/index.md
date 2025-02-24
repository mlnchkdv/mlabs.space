---
weight: 1
title: Практика по JS
description: Добавляем интерактивность в CV с JavaScript
author: MLabs
authorLink: null
date: 2025-02-02T14:48:57.920Z
lastmod: null
slug: js_example
categories:
  - WEB
math: true
lightgallery: true
toc:
  auto: false
draft: false
---

{{< admonition abstract "Структура" false >}}

### **Структура практического задания: «Добавляем интерактивность в CV с JavaScript»**

#### 1. Введение (5-7 мин)
- **Цель**: Показать, как «оживить» статичное CV.
- **Пример Codepen**: Демо готового проекта (CV с темной темой, анимациями, динамическими секциями).
- **Исходные данные участников**: 
  - У всех есть CV на HTML/CSS (предложить универсальный шаблон для тех, у кого нет).
  - Фокус на модификацию существующего кода, а не создание с нуля.

#### 2. Базовое подключение JS (15 мин)
- **Задача**: Научиться связывать JS с HTML.
- **Codepen-демо**:
  ```html
  <!-- Добавляем в конец body -->
  <script>
    console.log("CV загружено!");
    document.body.style.border = "2px solid green"; // Визуальный маркер
  </script>
  ```
- **Практика**: 
  1. Добавить тег `<script>` в свой CV.
  2. Проверить работу через `console.log()`.
  3. Изменить цвет заголовка через JS.

#### 3. Переключатель тем (25 мин)
- **Логика**: 
  1. Создать кнопку в HTML.
  2. Написать функцию переключения классов.
  3. Добавить CSS-стили для темной темы.
- **Codepen-шаблон**:
  
  ```html
  <button id="theme-toggle">🌓</button>
  ```
  ```css
  .dark-theme {
    background: #333;
    color: white;
  }
  ```
  ```js
  const toggleBtn = document.getElementById('theme-toggle');
  toggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
    // Сохранение темы в localStorage (бонус для продвинутых)
  });
  ```
- **Задание**: 
  
  - Реализовать переключатель.
  - Добавить плавный переход через CSS `transition`.

#### 4. Динамическое отображение навыков (20 мин)
- **Идея**: Генерация списка навыков из массива.
- **Codepen-пример**:
  ```js
  const skills = ['HTML', 'CSS', 'Git', 'Адаптивная верстка'];
  const skillsList = document.getElementById('skills');
  
  skills.forEach(skill => {
    const li = document.createElement('li');
    li.textContent = skill;
    skillsList.appendChild(li);
  });
  ```
- **Задание**: 
  - Заменить статичный список в CV на динамический.
  - Добавить кнопку сортировки навыков.

#### 5. Интерактивная секция «Опыт работы» (30 мин)
- **Задача**: Показать/скрыть описание по клику.
- **Шаги**:
  1. Добавить класс `.collapsed` с `max-height: 0` в CSS.
  2. Написать функцию для переключения видимости.
- **Codepen-фрагмент**:
  ```js
  document.querySelectorAll('.experience-header').forEach(header => {
    header.addEventListener('click', () => {
      header.nextElementSibling.classList.toggle('collapsed');
    });
  });
  ```
- **Дополнительно**: Анимация через CSS `transition`.

#### 6. Валидация формы контактов (20 мин)
- **Цель**: Проверка email перед отправкой.
- **Codepen-демо**:
  ```html
  <form id="contact-form">
    <input type="email" id="email">
    <button type="submit">Отправить</button>
  </form>
  ```
  ```js
  document.getElementById('contact-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    if (!email.includes('@')) {
      alert('Некорректный email!');
      return;
    }
    // Отправка данных...
  });
  ```

#### 7. Дополнительные идеи (10 мин)
- **Для самостоятельной работы**:
  - Таймер обратного отсчета до следующего карьерного цели.
  - Drag-and-drop для перестановки секций.
  - Анимация прогресс-бара навыков.

#### 8. Итог и рефлексия (10 мин)
- **Проверка**: У всех должен быть рабочий Codepen с модифицированным CV.
- **Советы**:
  - Как дебажить код через DevTools.
  - Где искать ошибки (Console > Errors).

{{< /admonition >}}

### **Раздел 1. Введение**  

**Основная цель:**  
Научиться добавлять интерактивность в статичный сайт (CV) с помощью JavaScript, превратив его в динамичное портфолио.  

**Что узнают участники:**  

- Как связывать JavaScript с HTML/CSS.  
- Как создавать интерактивные элементы (переключатель темы, динамические списки, анимации).  
- Как работать с событиями (клики, отправка форм).  
- Как дебажить код и тестировать изменения в реальном времени.  

**Результат:**  
У каждого участника будет CV с рабочими JS-элементами, которые можно добавить в портфолио.  

#### Пример готового проекта  
**Codepen-демо:**  
[Ссылка на пример CV](https://codepen.io/mlnchkdv/pen/ByaLjzp)  

<iframe height="600" style="width: 100%;" scrolling="no" title="CV  basic" src="https://codepen.io/mlnchkdv/embed/ByaLjzp?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/mlnchkdv/pen/ByaLjzp">
  CV  basic</a> by mlnchkdv (<a href="https://codepen.io/mlnchkdv">@mlnchkdv</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

*Что включено в демо:*  

- Переключатель светлой/темной темы.  
- Динамически генерируемый список навыков.  
- Секции опыта работы с раскрывающимся описанием.  
- Валидация формы контактов.  

**Важно:**  
- Участники будут модифицировать **свой** проект, а не создавать его с нуля.  
- Если у кого-то нет готового CV, можно использовать универсальный шаблон (см. раздел 1.3).  

#### Исходные материалы  
**Для участников:**  
1. **Базовый CV на HTML/CSS.**  
   - Если своего нет, используйте шаблон: 
     
     ```html
     <header>
       <h1>Иван Иванов</h1>
       <p>Начинающий веб-разработчик</p>
     </header>
     
     <section id="skills">
       <h2>Навыки</h2>
       <ul class="skills-list">
         <!-- Список будет заполнен через JS -->
         <li>HTML</li>
         <li>CSS</li>
       </ul>
     </section>
     
     <section class="experience">
       <h2>Опыт работы</h2>
       <div class="experience-item">
         <h3 class="experience-header">Стажер в IT-компании</h3>
         <p class="experience-description">
           Участие в разработке фронтенда для внутренних проектов.
         </p>
       </div>
     </section>
     
     <section>
       <h2>Связаться со мной</h2>
       <form id="contact-form">
         <input type="email" id="email" placeholder="Ваш email">
         <button type="submit">Отправить</button>
       </form>
     </section>
     
     <!-- Кнопка переключателя темы (пока не работает) -->
     <button id="theme-toggle" style="position: fixed; top: 20px; right: 20px;">🌓</button>
     
     <!-- JS будет добавлен позже -->
     <script></script>
     ```
   
2. **Требования к проекту:**  
   - Все секции должны быть сверстаны (можно без сложного дизайна).  
   - Подключенные шрифты и стили (если есть).  

**Технические требования:**  
- Браузер с DevTools (Chrome, Firefox).  
- Аккаунт на [Codepen.io](https://codepen.io) для сохранения работы.  

#### Ключевые концепции JavaScript, которые будут использоваться  
1. **DOM-манипуляции:**  
   - Изменение классов, стилей и содержимого элементов.  
   - Пример: `document.querySelector()`, `classList.toggle()`.  

2. **Работа с событиями:**  
   - Обработка кликов, отправки форм.  
   - Пример: `addEventListener('click', callback)`.  

3. **Динамическое создание элементов:**  
   - Генерация HTML из массивов данных.  
   - Пример: `document.createElement()`, `appendChild()`.  

#### Почему это полезно?  
- **Для портфолио:** CV с интерактивными элементами выделит вас среди других начинающих разработчиков.  
- **Для практики:** Все примеры приближены к реальным задачам (например, темы оформления есть у большинства сайтов).  
- **Для развития:** Вы сможете добавить в CV больше фич (анимации, API, слайдеры).  

#### План  
Пошагово внедрим в CV:  
1. Подключение JavaScript.  
2. Переключатель темы.  
3. Динамический список навыков.  
4. Интерактивные секции опыта.  
5. Валидация формы.  

#### Перед началом работы  
**Проверьте, что у вас есть:**  
- [ ] Готовый CV на HTML/CSS или универсальный шаблон.  
- [ ] Открыт Codepen для редактирования.  
- [ ] Включена консоль браузера (F12 > Console).  

---

### **Раздел 2. Базовое подключение JavaScript**  
**Цель раздела:** Научить участников подключать JavaScript к HTML, работать с консолью браузера и выполнять простые манипуляции с DOM.

#### Теория: Как работает JS в браузере  
**Ключевые концепции:**  
1. **Тег `<script>`** — элемент для вставки JS-кода.  
   - Размещается в конце `<body>` (для быстрой загрузки контента).  
   - В Codepen можно использовать отдельную JS-панель.  
2. **DOM (Document Object Model)** — представление HTML-документа в виде дерева объектов.  
3. **Консоль разработчика** — инструмент для отладки (открыть: `F12` → Console).

#### Пошаговая инструкция  
**Шаг 1: Добавление тега `<script>`**  
```html
<!-- Вставьте перед закрывающим тегом </body> -->
<script>
  // Ваш код будет здесь
</script>
```

**Шаг 2: Проверка подключения**  
```js
console.log("🚀 JS подключен!"); 
// Сообщение появится в консоли при загрузке страницы
```

**Шаг 3: Простая манипуляция с DOM**  
```js
// Изменение стилей через свойство style
document.body.style.backgroundColor = "#f0f0f0"; 

// Поиск элемента по селектору
const header = document.querySelector("h1");
header.style.fontFamily = "Courier New";
```

#### Codepen-пример  
**[Шаблон для практики](https://codepen.io/mlnchkdv/pen/ByaLjzp)**  
**Исходный код:**  

```html
<!-- HTML -->
<h2 id="test-header">Проверка JS</h2>
<button id="demo-button">Нажми меня</button>
```
```js
// JS
const button = document.getElementById("demo-button");
button.addEventListener("click", () => {
  document.getElementById("test-header").textContent = "JS работает!";
});
```

#### Практическое задание  
**Задача:** Добавить интерактивность в своё CV.  

1. **Изменение цвета заголовка:**  
   ```js
   const nameTitle = document.querySelector("h1");
   nameTitle.style.color = "#3498db"; // Синий цвет
   ```

2. **Динамическое сообщение в консоль:**  
   ```js
   console.log("Текущая дата:", new Date().toLocaleDateString());
   ```

3. **Добавление границы секциям:**  
   ```js
   document.querySelectorAll("section").forEach(section => {
     section.style.border = "1px solid #eee";
   });
   ```

#### Частые ошибки  
| Ошибка                                               | Решение                                                      |
| ---------------------------------------------------- | ------------------------------------------------------------ |
| `Uncaught TypeError: Cannot read properties of null` | Убедитесь, что элемент существует в HTML.                    |
| Скрипт не работает                                   | Проверьте, что `<script>` расположен после элементов, которыми управляет. |
| Изменения не отображаются                            | Обновите страницу (Ctrl + F5).                               |

#### Советы по отладке  
1. Всегда проверяйте консоль на ошибки (`F12` → Console).  
2. Используйте `console.log()` для вывода промежуточных результатов.  
3. Тестируйте код по частям, а не весь сразу.  

#### Дополнительные задания  
**Для продвинутых:**  
- Добавьте анимацию при клике на кнопку:  
  ```js
  button.addEventListener("click", () => {
    button.style.transform = "scale(0.95)";
    setTimeout(() => { button.style.transform = "scale(1)"; }, 100);
  });
  ```

#### Что проверять после раздела  
- [ ] Сообщение в консоли без ошибок.  
- [ ] Визуальные изменения на странице (цвет заголовка, фон).  
- [ ] Рабочая кнопка в Codepen-примере.  

---

### **Раздел 3. Переключатель тем (Светлая/Темная)**  
**Цель раздела:** Реализовать динамическое переключение тем на сайте, сохраняя выбор пользователя.  

#### Теория: Как работает переключение тем  
**Ключевые концепции:**  
1. **CSS-классы** — переключаем стили через добавление/удаление классов.  
2. **localStorage** — сохраняем выбор темы между сессиями.  
3. **События** — обрабатываем клики на кнопке.  

**Почему именно так?**  
- Изменение классов эффективнее прямого изменения стилей через JS.  
- localStorage позволяет запоминать выбор пользователя.  

#### Пошаговая инструкция  
**Шаг 1: Добавить кнопку в HTML**  
```html
<!-- В любое место внутри body -->
<button id="theme-toggle" aria-label="Переключить тему">🌓</button>
```

**Шаг 2: Стили для темной темы**  
```css
/* Добавить в CSS */
.dark-theme {
  background: #2c3e50;
  color: white !important; /* Приоритет над вложенными стилями */
}

.dark-theme section {
  background: #34495e;
}

.dark-theme .skills-list li {
  background: #4a6b8b;
}

/* Плавные переходы */
body {
  transition: background 0.3s, color 0.3s;
}
```

**Шаг 3: JavaScript-логика**  
```js
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// Проверяем сохраненную тему
const savedTheme = localStorage.getItem('theme');
if (savedTheme) body.classList.add(savedTheme);

// Обработчик клика
themeToggle.addEventListener('click', () => {
  body.classList.toggle('dark-theme');
  
  // Сохраняем тему
  const currentTheme = body.classList.contains('dark-theme') ? 'dark-theme' : '';
  localStorage.setItem('theme', currentTheme);
});
```

#### Codepen-пример  
**Особенности реализации:**  

- Кнопка с иконкой луны/солнца (можно заменить на текст).  
- Сохранение темы при перезагрузке страницы.  
- Плавные переходы между темами.  

#### Практическое задание  
**Задача:** Интегрировать переключатель в своё CV.  

1. **Базовый вариант:**  
   - Реализовать переключение фона body.  
   - Добавить консоль-лог при клике:  
     ```js
     console.log('Текущая тема:', body.classList.contains('dark-theme') ? 'темная' : 'светлая');
     ```

2. **Продвинутый вариант:**  
   - Изменить иконку кнопки в зависимости от темы.  
     ```js
     themeToggle.textContent = body.classList.contains('dark-theme') ? '☀️' : '🌙';
     ```
   - Добавить кастомные свойства CSS (CSS Variables):  
     ```css
     :root {
       --primary-bg: #f9f9f9;
       --text-color: #333;
     }
     
     .dark-theme {
       --primary-bg: #2c3e50;
       --text-color: white;
     }
     
     body {
       background: var(--primary-bg);
       color: var(--text-color);
     }
     ```

#### Частые ошибки  
| Ошибка                                  | Решение                                                      |
| --------------------------------------- | ------------------------------------------------------------ |
| Класс добавляется, но стили не меняются | Проверьте !important в CSS или специфичность селекторов.     |
| Тема не сохраняется                     | Убедитесь, что localStorage работает (включите cookies в браузере). |
| Иконка не обновляется                   | Добавьте логику изменения иконки внутри обработчика клика.   |

#### Советы по отладке  
1. Проверяйте классы через **Инструменты разработчика** (F12 → Elements).  
2. Используйте `localStorage.clear()` для сброса темы.  
3. Тестируйте на реальных проектах — некоторые стили могут конфликтовать.  

#### Дополнительные идеи  
- **Системная тема по умолчанию:**  
  ```js
  // Автоопределение темы ОС
  const isDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
  if (isDarkMode) body.classList.add('dark-theme');
  ```
- **Градиентные переходы** — анимируйте изменение цвета фона.  

#### Что проверять после раздела  
- [ ] Кнопка меняет тему при клике.  
- [ ] Тема сохраняется после перезагрузки.  
- [ ] Нет конфликтов стилей в секциях CV.  

---

### **Раздел 4. Динамическое отображение навыков**  
**Цель раздела:** Научить генерировать HTML-элементы из массива данных, работать с методами массива и DOM.

#### Теория: Зачем это нужно?  
- **Динамический контент** — позволяет обновлять данные без правки HTML (например, список навыков из базы данных).  
- **Методы работы:**  
  - `document.createElement()` — создание элементов.  
  - `appendChild()` / `innerHTML` — добавление в DOM.  
  - `forEach()` — итерация по массиву.  

#### Пошаговая инструкция  
**Шаг 1: Подготовка HTML**  
```html
<!-- Замените статичный список на пустой контейнер -->
<section id="skills">
  <h2>Навыки</h2>
  <ul class="skills-list"></ul> <!-- Контейнер для динамического контента -->
</section>
```

**Шаг 2: Создание массива данных**  
```js
const skills = [
  'HTML5', 
  'CSS3', 
  'JavaScript', 
  'Git', 
  'Адаптивный дизайн',
  'Figma'
];
```

**Шаг 3: Генерация элементов**  
```js
const skillsList = document.querySelector('.skills-list');

skills.forEach(skill => {
  const li = document.createElement('li'); // 1. Создаем элемент
  li.textContent = skill;                  // 2. Добавляем текст
  li.classList.add('skill-item');          // 3. Добавляем класс (опционально)
  skillsList.appendChild(li);              // 4. Вставляем в DOM
});
```

#### Codepen-пример  
**Особенности:**  

- Кнопка «Добавить навык» для интерактивности.  
- Сортировка навыков по алфавиту.  
```js
// Добавьте этот код в пример:
document.getElementById('add-skill').addEventListener('click', () => {
  const newSkill = prompt('Введите новый навык:');
  if (newSkill) skills.push(newSkill);
  updateSkillsList(); // Перерисовываем список
});

function updateSkillsList() {
  skillsList.innerHTML = ''; // Очищаем контейнер
  skills.sort().forEach(skill => { // Сортируем
    const li = document.createElement('li');
    li.textContent = skill;
    skillsList.appendChild(li);
  });
}
```

#### Практическое задание  
**Задача:** Реализовать динамический список в своём CV.  

1. **Базовый вариант:**  
   - Заменить статичные навыки на массив.  
   - Добавить минимум 8 элементов.  

2. **Продвинутый вариант:**  
   - Реализовать фильтрацию навыков по ключевому слову:  
   ```js
   const filteredSkills = skills.filter(skill => skill.includes('CSS'));
   ```
   - Добавить кнопку «Сортировать А-Я»/«Сортировать Я-А»:  
   ```js
   let isSortedAsc = true;
   document.getElementById('sort-button').addEventListener('click', () => {
     skills.sort((a, b) => isSortedAsc ? b.localeCompare(a) : a.localeCompare(b));
     isSortedAsc = !isSortedAsc;
     updateSkillsList();
   });
   ```

#### Частые ошибки  
| Ошибка                                       | Решение                                                      |
| -------------------------------------------- | ------------------------------------------------------------ |
| `Cannot read property 'appendChild' of null` | Убедитесь, что элемент `.skills-list` существует в HTML.     |
| Дублирование элементов при обновлении        | Всегда очищайте контейнер (`innerHTML = ''`) перед перерисовкой. |
| Кириллица сортируется некорректно            | Используйте `localeCompare()`: `skills.sort((a, b) => a.localeCompare(b))`. |

#### Советы по отладке  
1. Проверяйте массив через `console.log(skills)` перед рендерингом.  
2. Используйте `debugger;` для остановки выполнения кода в нужном месте.  
3. Для сложных списков используйте библиотеки типа [Vue.js](https://vuejs.org/) (но это уже для продвинутых).  

#### Дополнительные идеи  
- **Прогресс-бар навыков** — визуализируйте уровень владения:  
  ```js
  const skillsWithLevel = [
    { name: 'HTML', level: 90 },
    { name: 'CSS', level: 85 }
  ];
  // Генерируем div с width = level + '%'
  ```
- **Drag-and-Drop** — разрешите менять порядок навыков (используйте [HTML5 Drag and Drop API](https://developer.mozilla.org/ru/docs/Web

---

### **Раздел 5. Интерактивная секция «Опыт работы»**  
**Цель раздела:** Научить создавать раскрывающиеся блоки с описанием опыта, используя события и CSS-анимации.

#### Теория: Как работает интерактивность  
**Ключевые концепции:**  
1. **Событие `click`** — отслеживание клика на элементе.  
2. **CSS-классы** — управление видимостью через `display`/`max-height`.  
3. **Плавные переходы** — анимация с помощью `transition`.  

**Почему именно так?**  
- Изменение классов через JS позволяет отделить логику от стилей.  
- CSS-анимации работают эффективнее JS-анимаций.  

#### Пошаговая инструкция  
**Шаг 1: Подготовка HTML**  
```html
<div class="experience-item">
  <h3 class="experience-header">Frontend Developer (2020-2023)</h3>
  <div class="experience-description">
    <p>Разработка интерфейсов для мобильных приложений.</p>
  </div>
</div>
```

**Шаг 2: Добавить CSS для анимации**  
```css
/* Стили по умолчанию */
.experience-description {
  max-height: 0;           /* Скрываем контент */
  overflow: hidden;        /* Скрываем выходящий за границы текст */
  transition: max-height 0.3s ease-out; /* Анимация раскрытия */
}

/* Класс для раскрытия */
.experience-description.open {
  max-height: 500px;       /* Максимальная высота (подбирается под контент) */
}
```

**Шаг 3: JavaScript-логика**  
```js
document.querySelectorAll('.experience-header').forEach(header => {
  header.addEventListener('click', () => {
    const description = header.nextElementSibling;
    description.classList.toggle('open'); // Добавляем/удаляем класс

    // Меняем иконку (опционально)
    header.textContent = description.classList.contains('open') 
      ? '▼ Frontend Developer (2020-2023)' 
      : '▶ Frontend Developer (2020-2023)';
  });
});
```

#### Codepen-пример  
**Особенности:**  

- Плавная анимация раскрытия.  
- Динамическое обновление иконки-индикатора.  
- Поддержка нескольких элементов.  

#### Практическое задание  
**Задача:** Добавить интерактивность в секцию опыта своего CV.  

1. **Базовый вариант:**  
   - Реализовать раскрытие/скрытие описания.  
   - Добавить консоль-лог при клике:  
     ```js
     console.log('Состояние блока:', description.classList.contains('open'));
     ```

2. **Продвинутый вариант:**  
   - Сохранять состояние блоков в `localStorage`.  
     ```js
     // После перезагрузки страницы
     document.querySelectorAll('.experience-header').forEach(header => {
       const description = header.nextElementSibling;
       const isOpen = localStorage.getItem(header.textContent) === 'true';
       if (isOpen) description.classList.add('open');
     });
     
     // При клике
     localStorage.setItem(header.textContent, description.classList.contains('open'));
     ```
   - Добавить анимацию вращения иконки:  
     ```css
     .experience-header::before {
       content: '▶';
       display: inline-block;
       transition: transform 0.3s;
     }
     
     .experience-description.open + .experience-header::before {
       transform: rotate(90deg);
     }
     ```

#### Частые ошибки  
| Ошибка                                    | Решение                                                      |
| ----------------------------------------- | ------------------------------------------------------------ |
| Анимация не работает                      | Убедитесь, что `max-height` задан в `px`, а не `%`.          |
| Контент выходит за границы                | Добавьте `overflow: hidden` к контейнеру.                    |
| Несколько блоков открываются одновременно | Используйте `event.target`, чтобы определить конкретный элемент. |

#### Советы по отладке
1. Проверяйте классы через **Инструменты разработчика** (F12 → Elements).  
2. Используйте `console.log(event.target)`, чтобы убедиться, что клик обрабатывается правильно.  
3. Тестируйте анимации на реальном контенте — высота `max-height` должна быть больше фактической высоты блока.  

#### Дополнительные идеи  
- **Аккордеон-меню** — закрывать предыдущий блок при открытии нового:  
  
  ```js
  header.addEventListener('click', () => {
    document.querySelectorAll('.experience-description').forEach(desc => {
      if (desc !== description) desc.classList.remove('open');
    });
  });
  ```
- **Анимация opacity** — комбинируйте `max-height` и `opacity` для эффекта "появления".  

#### Что проверять после раздела  
- [ ] Описание раскрывается/скрывается по клику.  
- [ ] Анимация плавная, без рывков.  
- [ ] Состояние блоков сохраняется (для продвинутой версии).  

---

### **Раздел 6. Валидация формы контактов**  
**Цель раздела:** Научить проверять данные формы на стороне клиента, отображать ошибки и предотвращать некорректные действия пользователя.

#### Теория: Зачем нужна валидация?  
- **Основная задача:**  
  - Обеспечить корректность данных (например, email содержит «@»).  
  - Улучшить UX через мгновенную обратную связь.  
- **Методы валидации:**  
  - Нативная HTML5-валидация (атрибуты `required`, `type="email"`).  
  - Кастомная валидация через JavaScript.  

#### Пошаговая инструкция  
**Шаг 1: Подготовка HTML-формы**  
```html
<form id="contact-form">
  <input type="text" id="name" placeholder="Имя" required>
  <input type="email" id="email" placeholder="Email" required>
  <button type="submit">Отправить</button>
  <p class="error-message" style="color: red; display: none;"></p>
</form>
```

**Шаг 2: JavaScript-обработчик отправки**  
```js
document.getElementById('contact-form').addEventListener('submit', (e) => {
  e.preventDefault(); // Отменяем перезагрузку страницы

  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const errorMessage = document.querySelector('.error-message');

  // Сбрасываем предыдущие ошибки
  errorMessage.style.display = 'none';

  // Проверка имени
  if (name.length < 2) {
    showError('Имя должно содержать минимум 2 символа');
    return;
  }

  // Проверка email
  if (!validateEmail(email)) {
    showError('Некорректный email');
    return;
  }

  // Если все проверки пройдены
  alert('Данные отправлены!');
  e.target.reset();
});

function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email); // Регулярное выражение
}

function showError(text) {
  const errorMessage = document.querySelector('.error-message');
  errorMessage.textContent = text;
  errorMessage.style.display = 'block';
}
```

#### Codepen-пример  
**[Рабочий пример](https://codepen.io/anon/pen/GRQjQjK)**  
**Особенности:**  
- Подсветка невалидных полей:  
  ```css
  .invalid {
    border: 2px solid #e74c3c !important;
  }
  ```
- Динамическое обновление ошибок.  

#### Практическое задание  
**Задача:** Реализовать валидацию для своей формы.  

1. **Базовый вариант:**  
   - Проверка пустых полей.  
   - Валидация email на наличие «@» и домена.  

2. **Продвинутый вариант:**  
   - Валидация номера телефона через регулярное выражение:  
     ```js
     function validatePhone(phone) {
       return /^\+?(\d{1,3})?[-. ]?(\(?\d{3}\)?[-. ]?)?[\d-. ]{7,10}$/.test(phone);
     }
     ```
   - AJAX-отправка данных на моковый API:  
     ```js
     fetch('https://jsonplaceholder.typicode.com/posts', {
       method: 'POST',
       body: JSON.stringify({ name, email })
     });
     ```

#### Частые ошибки  
| Ошибка                           | Решение                                                      |
| -------------------------------- | ------------------------------------------------------------ |
| Форма перезагружает страницу     | Добавьте `e.preventDefault()`.                               |
| Регулярное выражение не работает | Проверьте его на [RegExr](https://regexr.com/).              |
| Ошибки не сбрасываются           | Добавьте `errorMessage.style.display = 'none'` перед проверками. |

#### Советы по отладке  
1. Используйте `console.log(email)` для вывода введенных данных.  
2. Тестируйте регулярные выражения отдельно (например, в [RegExr](https://regexr.com/)).  
3. Проверьте, что `id` элементов совпадают в HTML и JS.  

#### Дополнительные идеи  
- **Валидация в реальном времени** — проверка при вводе:  
  ```js
  document.getElementById('email').addEventListener('input', () => {
    const email = document.getElementById('email').value;
    if (!validateEmail(email)) {
      showError('Некорректный email');
    }
  });
  ```
- **Кастомные подсказки** — всплывающие тултипы вместо `alert()`.  

#### Что проверять после раздела  
- [ ] Форма не отправляется при ошибках.  
- [ ] Сообщения об ошибках четкие и понятные.  
- [ ] Поля подсвечиваются при невалидных данных.  

---

### **Раздел 7. Дополнительные идеи для CV**  
**Цель раздела:** Вдохновить участников на самостоятельное развитие проекта, показав возможности расширения функционала с помощью JavaScript.

#### Теория: Куда двигаться дальше?  
**Ключевые направления:**  
1. **Анимации** — улучшение UX через визуальные эффекты.  
2. **Работа с API** — динамическая загрузка данных (погода, курсы валют).  
3. **Интерактивность** — drag-and-drop, кастомные виджеты.  

**Почему это важно?**  
- Дополнительные фичи делают CV уникальным.  
- Позволяют продемонстрировать навыки работы с разными технологиями.  

---

### **Идеи для реализации**  
#### Идея 1: Таймер до цели  
**Задача:** Показать, сколько дней осталось до достижения карьерной цели.  
```html
<!-- HTML -->
<div class="goal-timer">
  <p>До старта в новой компании: <span id="countdown"></span></p>
</div>
```

```js
// JS
const targetDate = new Date('2024-12-31');
const timerElement = document.getElementById('countdown');

function updateTimer() {
  const now = new Date();
  const diff = targetDate - now;
  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  timerElement.textContent = `${days} дней`;
}

updateTimer();
setInterval(updateTimer, 86400000); // Обновлять каждые 24 часа
```

#### Идея 2: Виджет погоды  
**Задача:** Отображать текущую погоду через API.  
```js
// Используем OpenWeatherMap API
fetch('https://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=ВАШ_API_КЛЮЧ&units=metric&lang=ru')
  .then(response => response.json())
  .then(data => {
    const temp = data.main.temp;
    document.getElementById('weather').textContent = `🌡️ ${temp}°C, ${data.weather[0].description}`;
  });
```

#### Идея 3: Drag-and-Drop для секций  
**Задача:** Позволить менять порядок секций CV.  
```html
<!-- HTML -->
<section class="draggable" draggable="true">
  <h2>Опыт работы</h2>
  ...
</section>
```

```js
// JS
document.querySelectorAll('.draggable').forEach(section => {
  section.addEventListener('dragstart', () => {
    section.classList.add('dragging');
  });

  section.addEventListener('dragend', () => {
    section.classList.remove('dragging');
  });
});

// Логика для определения позиции (можно использовать библиотеки)
```

#### Идея 4: Анимация прогресс-бара навыков  
**Задача:** Визуализировать уровень владения технологиями.  
```html
<!-- HTML -->
<div class="skill">
  <span>HTML</span>
  <div class="progress-bar">
    <div class="progress" data-level="85%"></div>
  </div>
</div>
```

```css
/* CSS */
.progress-bar {
  width: 200px;
  height: 10px;
  background: #eee;
}

.progress {
  height: 100%;
  background: #3498db;
  transition: width 0.5s;
}
```

```js
// JS
document.querySelectorAll('.progress').forEach(bar => {
  const level = bar.dataset.level;
  bar.style.width = level; // Анимируем через JS или CSS
});
```

---

### **Codepen-примеры**  
1. [Таймер обратного отсчета](https://codepen.io/...)
2. [Виджет погоды](https://codepen.io/...)
3. [Анимация прогресс-бара](https://codepen.io/...)

#### Практическое задание  
**Задача:** Выбрать 1-2 идеи и реализовать их в своем CV.  

**Базовый уровень:**  
- Добавить таймер до цели.  
- Реализовать анимацию при скролле (например, появление секций).  

**Продвинутый уровень:**  
- Интегрировать API (погода, GitHub-статистика).  
- Создать кастомный аудиоплеер для раздела «Хобби».  

#### Частые ошибки  
| Ошибка                    | Решение                                    |
| ------------------------- | ------------------------------------------ |
| API не возвращает данные  | Проверьте CORS-политику и API-ключи.       |
| Анимации тормозят         | Используйте `will-change` или `transform`. |
| Drag-and-Drop не работает | Добавьте атрибут `draggable="true"`.       |

#### Советы по реализации  
1. Для анимаций используйте [GSAP](https://greensock.com/gsap/) или [Animate.css](https://animate.style/).  
2. Для работы с API начните с моковых данных через `json-server`.  
3. Тестируйте интерактивность на мобильных устройствах.  

#### Полезные ресурсы  
1. [OpenWeatherMap API](https://openweathermap.org/api) — погода.  
2. [GitHub API](https://docs.github.com/en/rest) — статистика репозиториев.  
3. [CSS Tricks](https://css-tricks.com/) — готовые решения для анимаций.  

---

### Итог  
Участники получат готовое портфолио, которое можно:  
1. Разместить на GitHub Pages.  
2. Дополнять новыми разделами (блог, пет-проекты).  
3. Использовать как шаблон для других проектов.  

