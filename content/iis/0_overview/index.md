---
weight: 1
title: Описание курса
description: Интеллектуальные Информационные Системы
author: MLabs
authorLink: null
date: 2023-08-05T14:48:57.920Z
lastmod: null
slug: overview
categories:
  - IIS
math: true
lightgallery: true
toc:
  auto: false
draft: false
---

# <div style="text-align: center;">Проектирование и разработка интеллектуальных информационных систем</div>

<!--

{{< admonition info "Рейтинги 2023" false >}}

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQzrzoTnnXC7iszTCoCmujs903jVUV1tZc8FTPioC8kA6_EVCooT8cwGhnvV-rjLHFbp0Vi2TNGCM5e/pubhtml?gid=0&amp;range=B1:I47&single=true&widget=false&chrome=false&headers=false" width="100%" height="514px" frameborder="0" scrolling="no"></iframe>

{{< /admonition >}}

-->

{{< admonition info "Рейтинги 2024" false >}}

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vS7A26ptPjkjJXg-2-u0Q3xEmi-MdDwh097U6oVyVCGXRbPrr1DgoLKczym0TxhokTlD_3aI9H_sEKi/pubhtml?gid=0&amp;range=B1:F73&single=true&widget=false&chrome=false&headers=false" width="100%" height="514px" frameborder="0" scrolling="no"></iframe>

{{< /admonition >}}

<style>
    .counter {
        font-family: 'Arial', sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 15px;
        margin: 0;
        background-color: #e8f4f8;
        box-sizing: border-box;
        min-height: 60vh;
    }
    .title {
        font-size: 2.1em;
        line-height: 1.1;
        font-weight: bold;
        color: #333;
        margin-bottom: 20px;
        text-align: center;
    }
    #countdown {
        font-size: 1.6em;
        color: #444;
        margin-bottom: 30px;
    }
    #progress-bar-container {
        width: 85%;
        background-color: #ddd;
        border-radius: 8px;
        margin-top: 20px;
        position: relative;
        height: 40px;
        overflow: visible;
    }
    @media (max-width: 500px) {
        .counter {
            padding: 7px;
            min-height: 62vh;
        }
        #countdown {
            font-size: 1.2em;
            /* margin-bottom: 30px; */
        }
        #progress-bar-container {
            width: 100%;
        }
    }
    #progress-bar {
        width: 0;
        height: 100%;
        background-color: #4caf50;
        border-radius: 8px;
        text-align: center;
        line-height: 40px;
        color: white;
        position: relative;
        transition: width 0.5s ease;
    }
    .tick {
        position: absolute;
        width: 2px;
        height: 50px;
        background-color: #333;
        bottom: -10px;
    }
    .milestone {
        position: absolute;
        top: 50px;
        font-size: 0.7em;
        color: #555;
        text-align: center;
        width: 100px;
        transform: translateX(-50%);
    }
    .milestone br {
        margin: 1px;
    }
</style>
<div class="counter">
    <div class="title">До защиты проектов:</div>
    <div id="countdown">Загрузка...</div>
    <div id="progress-bar-container">
        <div id="progress-bar">0%</div>
        <div class="tick" style="left: 50%;"></div>
        <div class="tick" style="left: 70%;"></div>
        <div class="tick" style="left: 90%;"></div>
        <div class="milestone" style="left: 50%;"><i>Submission</i></div>
        <div class="milestone" style="left: 70%;"><i>Pitching 1</i><br style="margin: 5px;">23.11.24</div>
        <div class="milestone" style="left: 90%;"><i>Pitching 2</i><br style="margin: 5px;">14.12.24</div>
    </div>
</div>
<script>
    function declension(number, one, two, five) {
        number = Math.abs(number) % 100;
        const n1 = number % 10;
        if (number > 10 && number < 20) return five;
        if (n1 > 1 && n1 < 5) return two;
        if (n1 === 1) return one;
        return five;
    }
    function updateCountdown() {
        const endDate = new Date("2024-12-23T12:00:00");
        const now = new Date();
        const timeDifference = endDate - now;
        if (timeDifference <= 0) {
            document.getElementById("countdown").innerHTML = "Срок достигнут!";
            return;
        }
        const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);
        const daysText = declension(days, 'день', 'дня', 'дней');
        const hoursText = declension(hours, 'час', 'часа', 'часов');
        const minutesText = declension(minutes, 'минута', 'минуты', 'минут');
        const secondsText = declension(seconds, 'секунда', 'секунды', 'секунд');
        document.getElementById("countdown").innerHTML = days + " " + daysText + " " + hours + " " + hoursText + " " +
            minutes + " " + minutesText;
    }
    function updateProgressBar() {
        const startDate = new Date("2024-09-01T00:00:00");
        const endDate = new Date("2024-12-23T00:00:00");
        const now = new Date();
        if (now < startDate) {
            document.getElementById("progress-bar").style.width = "0%";
            document.getElementById("progress-bar").innerHTML = "0%";
            return;
        }
        const totalDuration = endDate - startDate;
        const elapsed = now - startDate;
        const progressPercentage = Math.min((elapsed / totalDuration) * 100, 100);
        document.getElementById("progress-bar").style.width = progressPercentage + "%";
        document.getElementById("progress-bar").innerHTML = Math.floor(progressPercentage) + "%";
    }
    setInterval(function () {
        updateCountdown();
        updateProgressBar();
    }, 1000);
</script>





**Целью курса** является изучение базовых парадигм разработки интеллектуальных информационных систем (ИИС), т.е. систем обладающих способностью собирать, обрабатывать и анализировать большое количество данных, на основе которых она может автоматически принимать решения и выполнять задачи. Такие системы могут быть использованы для широкого круга задач в различных отраслях, включая финансы, здравоохранение, транспорт, производство и множество других областей.

Интеллектуальные системы могут автоматизировать процессы и улучшать качество принимаемых решений. Они могут анализировать данные и выдавать рекомендации или предсказания, учитывая сложные факторы и зависимости, вычисляемые на основе статистических данных.

## Разделы

![](plan.png "Course roadmap")

[**Intro**] Введение в ИИС и выравнивание знаний.

> Определение, основные принципы, характеристики; анализ существующих примеров ИИС и их роли в различных областях; этические и социальные аспекты разработки и использования ИИС. Оформление кода, разработка проектов на языке Python, а также хранение и извлечение данных.

{{< admonition abstract "Вопросы" false >}}

- Отличающие характеристики интеллектуальных системы от информационных;
- Основные этапы жизненного цикла разработки интеллектуальных информационных систем;
- Требования к данным, обучающим выборкам и инфраструктуре, при разработке интеллектуальных систем;
- Структура кода (PEP8) и проекта на *Python*;
- Модульное тестирование (автотесты);
- Типы лицензий;
- Документирование и журналирование;
- Роль обучающей, валидационной и тестовой выборок данных при разработке интеллектуальных систем;
- Несбалансированные данные для обучения моделей;
- Извлечение данных;
- Безопасность и конфиденциальность данных;
- Реляционные и нереляционные базы данных;
- Графовые базы данных;
- Векторная базы данных.

{{< /admonition >}}

- [:(fa-solid fa-flag-checkered): Введение](../intro/)
- [:(fa-brands fa-python): Пишем отличный код](../codestyle/)
<!-- - [:(fa-solid fa-database): Работа с данными]() -->

[**Algo**] Алгоритмизация стратегий и решений для разработки ИИС.

> Базовые возможности ИИС на примерах задач оптимизации и анализа данных, сравнение эффективности реализаций и основы теории алгоритмов.

{{< admonition abstract "Вопросы" false >}}

- Концепции разработки алгоритмов;
- Линейное, вероятностное и функциональное программирование в решении практических задач;
- Алгоритмы на графах и сетях;
- Генетические алгоритмы;
- Алгоритмы решения задач большой размерности;
- Подходы для ускорения работы алгоритмов.

{{< /admonition >}}

- [:(fa-solid fa-route): Разработка алгоритмов](../algo/)
- [:(fa-solid fa-circle-nodes): Алгоритмы на графах и сетях](../graph/)
<!-- - [:(fa-solid fa-code-branch):]()
- [:(fa-solid fa-code):]()
- [:(fa-solid fa-chart-line):]()
- [:(fa-solid fa-chart-pie):]()
- [:(fa-solid fa-circle-nodes):]()
- [:(fa-solid fa-network-wired):]() -->

[**ML**] Классификация и описание моделей и их метрик в машинном обучении.

> Обзор на классические задачи машинного обучения и разбор ключевых алгоритмов, с точки зрения их принципа работы и сравнения при помощи базовых метрик оценки.

{{< admonition abstract "Вопросы" false >}}

- Модели и метрики, общий подход
- Обучение с учителем
- Обучение без учителя
    - Модели кластеризации и её метрики
    - Ансамблевые модели и метрики
    - Снижение размерности
- Рекомендательные системы 

{{< /admonition >}}

<!-- - [:(fa-solid fa-robot):]() -->

- [:(fa-solid fa-robot): Модели и метрики в ML](../models/)
- [:(fa-solid fa-diagram-project): Классификация, деревья решений и k-ближайших соседей](../classification/)
- [:(fa-solid fa-magnifying-glass-chart): Рекомендательные системы](../)

[**NLP**] Техники и Модели обработки естественного языка (NLP).

> Формирование понятийного аппарата и обзор открытых инструментов в области анализа естественного языка, навыки поиска и использования готовых NLP-моделей, и создание исследовательского цикла от исходных текстовых данных до отчета с артефактами.

{{< admonition abstract "Вопросы" false >}}

- Терминология, базовые возможности и инструменты в NLP
- Векторизация и группировка (embedding) слов 
- Рекуррентная нейросеть (RNN) в NLP
- Тональность и эмоциональная классификация текста
- NER

{{< /admonition >}}

- <a href="../8_word_embeddings/Word Embeddings.pptx" download>:(fa-solid fa-paragraph): Word Embeddings</a>
- [:(fa-solid fa-list-ol): Text Classification](../9_text_classification/text_classification.pdf)

[**LLM**] Большие языковые модели (LLM) для ИИС.

> На основе OpenAI API и комбинации запросов, создание приложений для генеративной текстовой модели (>GPT-3.5).

{{< admonition abstract "Вопросы" false >}}

- Работа с OpenAI API 
- Базовые понятия в Prompt Engineering

{{< /admonition >}}

<!-- - [:(fa-solid fa-brain):]() -->

## Задания

[**Intro**] Введение в ИИС и выравнивание знаний.

1. Python, Numpy, Pandas: <a href="../tasks/1_python_numpy_pandas_manual.ipynb" download>:(fa-solid fa-book): Manual</a>, <a href="../tasks/1_python_numpy_pandas.ipynb" download>:(fa-solid fa-file-code): Notebook</a>, [:(fa-solid fa-database): Titanic data](../data/titanic.csv), [:(fa-solid fa-database): Iris data](../data/iris.csv)
2. Работа с данными: <a href="../tasks/2_data _sql.ipynb" download>:(fa-solid fa-file-code): Notebook</a>
3. Визуализация данными: <a href="../tasks/3_visualize_data.ipynb" download>:(fa-solid fa-file-code): Notebook</a>

[**Algo**] Алгоритмизация стратегий и решений для разработки ИИС.

<!-- 3. Линейное программирование: -->

4. Алгоритмы на графах: <a href="../tasks/4_graph.ipynb" download>:(fa-solid fa-file-code): Notebook</a>

[**ML**] Классификация и описание моделей и их метрик в машинном обучении.

5. Основы машинного обучения: <a href="../tasks/6_ml_classic.ipynb" download>:(fa-solid fa-file-code): Notebook</a>

6. Деревья решений (Decision Tree): <a href="../tasks/7_decision_tree-2.ipynb" download>:(fa-solid fa-file-code): Notebook</a>, [:(fa-solid fa-database): ans data](../data/ans.csv), [:(fa-solid fa-database): train data](../data/train.csv), [:(fa-solid fa-database): test data](../data/test.csv)

    <!--5. Рекомендательные системы: -->

[**NLP**] Техники и Модели обработки естественного языка (NLP).

7. Word Embeddings: <a href="../tasks/8_torch_intro.ipynb" download>:(fa-solid fa-file-code): Notebook</a>

8. Streamlit: <a href="../tasks/9_streamlit_example.py" download>:(fa-solid fa-file-code): Notebook</a>
9. Латентное размещение Дирихле (LDA): <a href="../tasks/LDA_topic_models.ipynb" download>:(fa-solid fa-file-code): Notebook</a>, [:(fa-solid fa-database): Elon Musk data](../data/data_elonmusk.csv)
10. Анализ текста: <a href="../tasks/10_text_analysis_part1.ipynb" download>:(fa-solid fa-file-code): Notebook 1</a>, <a href="../tasks/10_text_analysis_part2.ipynb" download>:(fa-solid fa-file-code): Notebook 2</a>, [:(fa-solid fa-database): Text data](../data/texts.zip)

## Проекты

<style>
    .role-button {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 5px 10px;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
        margin: 2px 0;
        display: inline-block;
    }
    .tech-button {
        background-color: #28a745;
        color: white;
        border: none;
        padding: 5px 10px;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
        margin: 2px 0;
        display: inline-block;
    }
    .project-card {
        border: 1px solid #b2a6a6;
        border-radius: 10px;
        padding: 15px;
        margin: 15px 0;
        background-color: #f9f9f907;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
</style>


{{< admonition success "👶 Простые:" false >}}

<div class="project-card">

#### **Проект: Визуализация данных о заболеваемости COVID-19**
- **Описание**: Разработка интерактивного веб-приложения для визуализации статистики заболеваемости COVID-19 по регионам, странам и времени. Приложение позволяет пользователям выбирать регионы и периоды времени для анализа графиков и тенденций.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">Streamlit</button>, <button class="tech-button">Plotly</button>
- **Источник данных**: [Our World in Data](https://ourworldindata.org/coronavirus), [Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)
- **Источник модели**: Не требуется
- **Системные характеристики**: CPU с 2 ядрами, 4 ГБ ОЗУ, 10 ГБ свободного места на диске
- **Роли в команде**: 
  - <button class="role-button">🖥️ Разработчик бэкенда</button> – отвечает за сбор, очистку и обработку данных из внешних источников, интеграцию данных в приложение, настройку сервера и API.
  - <button class="role-button">🎨 Разработчик фронтенда</button> – создает пользовательский интерфейс, настраивает визуализацию данных с помощью Plotly и Streamlit, следит за отзывчивостью интерфейса.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует данные, выявляет тренды и паттерны, предоставляет рекомендации по улучшению визуализаций.
  - <button class="role-button">✅ Тестировщик/менеджер проекта</button> – проверяет функциональность и корректность приложения, управляет задачами и сроками команды.

</div>

<div class="project-card">

#### **Проект: Приложение для отслеживания личных финансов**
- **Описание**: Веб-приложение для управления личными финансами с возможностью учета доходов и расходов, анализа и генерации отчетов.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">Flask</button> или <button class="tech-button">Django</button>, <button class="tech-button">SQLite</button>, <button class="tech-button">Bootstrap</button>
- **Источник данных**: Открытые API банков ([Plaid API](https://plaid.com/))
- **Источник модели**: Не требуется
- **Системные характеристики**: CPU с 2 ядрами, 4 ГБ ОЗУ, 10 ГБ свободного места на диске
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик бэкенда</button> – создает серверную часть приложения, интегрирует API для получения данных банков, обрабатывает данные и настраивает их хранение в базе данных.
  - <button class="role-button">🎨 Разработчик фронтенда</button> – отвечает за визуальное представление данных, создает формы ввода и таблицы, разрабатывает адаптивный интерфейс с использованием Bootstrap.
  - <button class="role-button">📊 Аналитик данных</button> – создает алгоритмы для анализа финансовых данных, разрабатывает отчеты и инструменты визуализации для пользователя.
  - <button class="role-button">🎨 UX/UI дизайнер</button> – проектирует пользовательский интерфейс, разрабатывает макеты и взаимодействия, оптимизирует приложение для удобства использования.

</div>

<div class="project-card">

#### **Проект: Telegram-бот для рекомендаций фильмов**
- **Описание**: Создание Telegram-бота, который предоставляет рекомендации фильмов на основе жанра, года выпуска или рейтинга.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">Telegram Bot API</button>, <button class="tech-button">OMDb API</button>
- **Источник данных**: [OMDb API](https://www.omdbapi.com/)
- **Источник модели**: Не требуется
- **Системные характеристики**: CPU с 2 ядрами, 4 ГБ ОЗУ, 5 ГБ свободного места на диске
- **Роли в команде**:
  - <button class="role-button">🤖 Разработчик бота</button> – реализует функциональность бота, создает логику обработки команд и ответов, интегрирует бот с Telegram API.
  - <button class="role-button">🌐 Разработчик API-интеграции</button> – отвечает за подключение к OMDb API, получение данных о фильмах и их обработку.
  - <button class="role-button">✅ Тестировщик/контент-менеджер</button> – проверяет работу бота, управляет контентом (данные фильмов), создает тестовые сценарии.
  - <button class="role-button">🎨 UX/UI дизайнер</button> – разрабатывает текстовые и визуальные элементы взаимодействия с ботом, улучшает пользовательский опыт.

</div>

<div class="project-card">

#### **Проект: Приложение для учёта спортивных достижений**
- **Описание**: Веб-приложение для спортсменов, позволяющее отслеживать спортивные достижения и прогресс (например, бег, велосипед, плавание).
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">Flask</button>, <button class="tech-button">Chart.js</button>, <button class="tech-button">HTML/CSS</button>
- **Источник данных**: [Strava API](https://developers.strava.com/)
- **Источник модели**: Не требуется
- **Системные характеристики**: CPU с 2 ядрами, 4 ГБ ОЗУ, 10 ГБ свободного места на диске
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик бэкенда</button> – создает API для работы с данными пользователей, интегрирует Strava API для получения данных о спортивных достижениях.
  - <button class="role-button">🎨 Разработчик фронтенда</button> – разрабатывает интерфейс приложения, настраивает визуализацию данных с использованием Chart.js.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует спортивные данные, создает отчеты и графики прогресса.
  - <button class="role-button">✅ Менеджер проекта/тестировщик</button> – организует процессы разработки, тестирует функциональность и координирует команду.

</div>

<div class="project-card">

#### **Проект: Приложение для планирования задач с использованием Kanban-доски**
- **Описание**: Приложение для планирования задач, основанное на методологии Kanban, с функциями добавления, изменения и удаления задач.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">Django</button>, <button class="tech-button">React.js</button>
- **Источник данных**: Нет (приложение использует внутренние данные пользователя)
- **Источник модели**: Не требуется
- **Системные характеристики**: CPU с 2 ядрами, 4 ГБ ОЗУ, 10 ГБ свободного места на диске
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик бэкенда</button> – разрабатывает серверную часть приложения, отвечает за управление данными задач, их хранение и обработку.
  - <button class="role-button">🎨 Разработчик фронтенда</button> – создает пользовательский интерфейс Kanban-доски, настраивает взаимодействие с сервером.
  - <button class="role-button">✅ Тестировщик</button> – проводит тестирование функциональности приложения, выявляет и исправляет ошибки.
  - <button class="role-button">🎨 UX/UI дизайнер</button> – проектирует макеты Kanban-доски, улучшает пользовательский опыт и удобство использования.

</div>

<div class="project-card">

#### **Проект: Приложение для рекомендаций книг по жанрам**
- **Описание**: Веб-приложение, которое предлагает пользователю книги для чтения на основе выбранных жанров.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">Flask</button>, <button class="tech-button">Goodreads API</button>, <button class="tech-button">Bootstrap</button>
- **Источник данных**: [Goodreads API](https://www.goodreads.com/api)
- **Источник модели**: Не требуется
- **Системные характеристики**: CPU с 2 ядрами, 4 ГБ ОЗУ, 10 ГБ свободного места на диске
- **Роли в команде**:
  - <button class="role-button">🌐 Разработчик API</button> – реализует взаимодействие с Goodreads API, получает и обрабатывает данные о книгах.
  - <button class="role-button">🎨 Разработчик фронтенда</button> – создает интерфейс для выбора и просмотра книг, разрабатывает страницы с использованием Bootstrap.
  - <button class="role-button">📚 Менеджер контента</button> – управляет базой данных книг, следит за актуальностью и качеством данных.
  - <button class="role-button">🎨 UX/UI дизайнер</button> – проектирует и улучшает внешний вид приложения, разрабатывает макеты интерфейсов.

</div>

<div class="project-card">

#### **Проект: Приложение для управления списками покупок**
- **Описание**: Веб-приложение для создания и управления списками покупок с возможностью делиться ими с другими пользователями.
- **Стек**: <button class="tech-button">JavaScript</button>, <button class="tech-button">Node.js</button>, <button class="tech-button">MongoDB</button>, <button class="tech-button">React</button>
- **Источник данных**: Нет (локальные данные пользователя)
- **Источник модели**: Не требуется
- **Системные характеристики**: CPU с 2 ядрами, 4 ГБ ОЗУ, 10 ГБ свободного места на диске
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик бэкенда</button> – разрабатывает серверную логику для управления списками покупок, настраивает базы данных.
  - <button class="role-button">🎨 Разработчик фронтенда</button> – создает интерфейс приложения, реализует взаимодействие с сервером и базой данных.
  - <button class="role-button">✅ Тестировщик</button> – проверяет функциональность приложения, устраняет ошибки и улучшает производительность.
  - <button class="role-button">🎨 UX/UI дизайнер</button> – проектирует пользовательский интерфейс, оптимизирует приложение для лучшего опыта.

</div>

<div class="project-card">

#### **Проект: Веб-приложение для изучения иностранных языков**
- **Описание**: Приложение, которое помогает учить новые слова и фразы, используя флэш-карты и мини-тесты.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">Django</button>, <button class="tech-button">Vue.js</button>, <button class="tech-button">SQLite</button>
- **Источник данных**: [Open Multilingual Wordnet](http://compling.hss.ntu.edu.sg/omw/)
- **Источник модели**: Не требуется
- **Системные характеристики**: CPU с 2 ядрами, 4 ГБ ОЗУ, 10 ГБ свободного места на диске
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик бэкенда</button> – создает серверную часть приложения, отвечает за хранение и обработку данных о словах и тестах.
  - <button class="role-button">🎨 Разработчик фронтенда</button> – создает интерфейс приложения, разрабатывает компоненты для флэш-карт и тестов.
  - <button class="role-button">📚 Контент-менеджер</button> – управляет базой данных слов и выражений, следит за их актуальностью и полнотой.
  - <button class="role-button">✅ Тестировщик</button> – проверяет корректность работы приложения, выявляет и устраняет баги.

</div>

<div class="project-card">

#### **Проект: Интерактивное приложение для расчета калорийности блюд**
- **Описание**: Веб-приложение, которое позволяет пользователям вводить ингредиенты и рассчитывать калорийность блюда.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">Flask</button>, <button class="tech-button">Chart.js</button>, <button class="tech-button">HTML/CSS</button>
- **Источник данных**: [USDA Food Data Central](https://fdc.nal.usda.gov/)
- **Источник модели**: Не требуется
- **Системные характеристики**: CPU с 2 ядрами, 4 ГБ ОЗУ, 10 ГБ свободного места на диске
- **Роли в команде**:
  - <button class="role-button">🌐 Разработчик API</button> – интегрирует приложение с базой данных продуктов, реализует API для обработки пользовательских запросов.
  - <button class="role-button">🎨 Разработчик фронтенда</button> – разрабатывает интерфейс приложения, настраивает визуализацию данных с использованием Chart.js.
  - <button class="role-button">✅ Тестировщик</button> – тестирует приложение, выявляет и исправляет ошибки.
  - <button class="role-button">🎨 UX/UI дизайнер</button> – разрабатывает макеты интерфейса, оптимизирует приложение для удобства использования.

</div>

<div class="project-card">

#### **Проект: Приложение для мониторинга уровня шума в городах**
- **Описание**: Приложение для сбора и отображения данных о уровне шума в разных частях города. Использует данные, полученные с мобильных устройств пользователей.
- **Стек**: <button class="tech-button">JavaScript</button>, <button class="tech-button">Node.js</button>, <button class="tech-button">Google Maps API</button>, <button class="tech-button">MongoDB</button>
- **Источник данных**: [London Datastore](https://data.london.gov.uk/), данные пользователей
- **Источник модели**: Не требуется
- **Системные характеристики**: CPU с 2 ядрами, 4 ГБ ОЗУ, 10 ГБ свободного места на диске
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик бэкенда</button> – разрабатывает серверную часть приложения, настраивает базы данных для хранения и обработки данных о шуме.
  - <button class="role-button">🎨 Разработчик фронтенда</button> – создает интерфейс для отображения данных о шуме, интегрирует карты и визуализации.
  - <button class="role-button">✅ Тестировщик</button> – проверяет корректность работы приложения, находит и исправляет баги.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует данные о шуме, выявляет паттерны и тренды, предлагает улучшения.

</div>

{{< /admonition >}}

{{< admonition warning "👨‍💻 Средние:" false >}}

<div class="project-card">

#### **Проект: Прогнозирование цен акций российских компаний с использованием LSTM**
- **Описание**: Разработка системы прогнозирования цен акций российских компаний, таких как "Сбербанк", "Газпром", "Яндекс", с использованием методов глубокого обучения (Long Short-Term Memory — LSTM). Система анализирует исторические данные с Московской Биржи (MOEX) и предсказывает цены на основе временных рядов.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">TensorFlow</button>, <button class="tech-button">Keras</button>, <button class="tech-button">Plotly</button>, <button class="tech-button">Dash</button>
- **Источник данных**: [Московская Биржа (MOEX)](https://www.moex.com/), [Alpha Vantage API](https://www.alphavantage.co/)
- **Источник модели**: Предобученная LSTM модель с [TensorFlow Hub](https://tfhub.dev/google/collections/financial-timeseries/1)
- **Системные характеристики**: GPU (например, NVIDIA с поддержкой CUDA), 8 ГБ ОЗУ, 50 ГБ свободного места на диске
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик моделей</button> – обучает модели LSTM для прогнозирования цен акций, настраивает гиперпараметры и проводит экспериментирование.
  - <button class="role-button">🌐 Разработчик API</button> – интегрирует данные с Московской Биржи и Alpha Vantage API, настраивает API для получения данных в реальном времени.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует финансовые данные, готовит датасеты для обучения моделей, проводит визуализацию результатов.
  - <button class="role-button">✅ Тестировщик/менеджер проекта</button> – тестирует производительность и точность модели, отвечает за координацию команды и управление сроками.
  

</div>

<div class="project-card">

#### **Проект: Система рекомендаций для российских интернет-магазинов**
- **Описание**: Разработка системы рекомендаций для российских интернет-магазинов, которая анализирует поведение пользователей и предлагает персонализированные товары и услуги в реальном времени.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">Apache Kafka</button>, <button class="tech-button">TensorFlow</button>, <button class="tech-button">Scikit-Learn</button>, <button class="tech-button">React.js</button>
- **Источник данных**: [Открытые данные маркетплейсов (Ozon, Wildberries)](https://data.ozon.ru/), [Kaggle (E-commerce Data)](https://www.kaggle.com/)
- **Источник модели**: Модель рекомендаций BERT4Rec с [HuggingFace](https://huggingface.co/transformers/model_doc/bert4rec.html)
- **Системные характеристики**: CPU с 8 ядрами, 16 ГБ ОЗУ, 200 ГБ свободного места на диске
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик моделей</button> – обучает рекомендательные модели, настраивает их параметры и тестирует на реальных данных.
  - <button class="role-button">🌐 Разработчик API</button> – настраивает API для обработки данных в реальном времени, интегрирует систему с данными от Ozon и Wildberries.
  - <button class="role-button">🎨 Разработчик фронтенда</button> – создает интерфейс для отображения рекомендаций пользователям, улучшает визуальное восприятие.
  - <button class="role-button">✅ Тестировщик/аналитик данных</button> – проводит тестирование системы, оценивает качество рекомендаций и предлагает улучшения.
  

</div>

<div class="project-card">

#### **Проект: Платформа анализа потребностей в туристических услугах**
- **Описание**: Платформа для анализа данных о туристических поездках по России, включая интеграцию с социальными сетями и автоматизацию маркетинговых стратегий для туристических агентств.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">Django</button>, <button class="tech-button">Vue.js</button>, <button class="tech-button">TensorFlow</button>, <button class="tech-button">PostgreSQL</button>
- **Источник данных**: [Открытые данные Ростуризма](https://tourism.gov.ru/contents/statistika/), [Twitter API](https://developer.twitter.com/en/docs/twitter-api)
- **Источник модели**: Модель анализа тональности (Russian Sentiment Analysis) с [HuggingFace](https://huggingface.co/blanchefort/rubert-base-cased-sentiment)
- **Системные характеристики**: CPU с 8 ядрами, 16 ГБ ОЗУ, 250 ГБ свободного места на диске
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик бэкенда</button> – интегрирует платформу с данными Ростуризма и Twitter API, обрабатывает данные и управляет базой данных.
  - <button class="role-button">🎨 Разработчик фронтенда</button> – создает интерфейс для визуализации анализа и отчетов по потребностям туристов.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует данные из социальных сетей и источников по туризму, использует модели анализа тональности.
  - <button class="role-button">✅ Тестировщик/менеджер проекта</button> – проводит тестирование системы, управляет процессами разработки и сроками.
  

</div>

<div class="project-card">

#### **Проект: Интеллектуальная система для управления городским транспортом**
- **Описание**: Платформа для анализа и прогнозирования пассажиропотока в городском транспорте на основе данных о движении автобусов, метро, трамваев и троллейбусов в Москве.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">Pandas</button>, <button class="tech-button">Django</button>, <button class="tech-button">Power BI</button>, <button class="tech-button">PostgreSQL</button>
- **Источник данных**: [Открытые данные Московского транспорта](https://data.mos.ru/opendata/), [Яндекс API](https://yandex.ru/dev/maps/)
- **Источник модели**: Модели временных рядов для анализа пассажиропотока с [HuggingFace](https://huggingface.co/)
- **Системные характеристики**: CPU с 4 ядрами, 8 ГБ ОЗУ, 100 ГБ свободного места на диске
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик моделей</button> – обучает модели для прогнозирования пассажиропотока, анализирует результаты и оптимизирует алгоритмы.
  - <button class="role-button">🌐 Разработчик API</button> – создает API для интеграции данных о движении транспорта и пассажиропотока, настраивает связи с Яндекс API.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует данные о движении транспорта, разрабатывает стратегии для оптимизации пассажиропотока.
  - <button class="role-button">✅ Тестировщик/UX/UI дизайнер</button> – тестирует интерфейс, улучшает пользовательский опыт и разрабатывает макеты.
  

</div>

<div class="project-card">

#### **Проект: Система предсказания отказов оборудования для российских заводов**
- **Описание**: Использование методов машинного обучения для анализа данных с датчиков российских заводов и предсказания вероятности отказа оборудования, что позволяет предотвратить поломки и снизить затраты на ремонт.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">Scikit-Learn</button>, <button class="tech-button">Flask</button>, <button class="tech-button">Grafana</button>
- **Источник данных**: [Открытые данные Российского промышленного сектора](https://data.gov.ru/opendata), [Kaggle (Machine Failure Data)](https://www.kaggle.com/)
- **Источник модели**: Модель классификации отказов оборудования с [TensorFlow Hub](https://tfhub.dev/google/ft_transformer/1)
- **Системные характеристики**: CPU с 4 ядрами, 8 ГБ ОЗУ, 50 ГБ свободного места на диске
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик моделей</button> – обучает модели для предсказания отказов оборудования, проводит оптимизацию и анализирует результаты.
  - <button class="role-button">🌐 Разработчик API</button> – интегрирует приложение с датчиками и внешними системами заводов, создает API для обмена данными.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует данные с датчиков, готовит их для обучения моделей.
  - <button class="role-button">✅ Тестировщик/менеджер проекта</button> – проверяет производительность системы, управляет задачами и сроками выполнения.

</div>

{{< /admonition >}}

{{< admonition danger "👨‍🎓 Сложные:" false >}}


<div class="project-card">

#### **Проект: Интеллектуальная система управления энергопотреблением в умных домах**
- **Описание**: Разработка системы для управления энергопотреблением в умных домах, использующей данные с IoT-датчиков для оптимизации использования электроэнергии и снижения затрат.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">TensorFlow</button>, <button class="tech-button">Keras</button>, <button class="tech-button">Apache Kafka</button>, <button class="tech-button">Docker</button>, <button class="tech-button">Grafana</button>
- **Источник данных**: [Открытые данные энергетики России](https://data.gov.ru/), [Open Power System Data](https://open-power-system-data.org/)
- **Источник модели**: Модель прогнозирования энергопотребления с [TensorFlow Hub](https://tfhub.dev/google/timeseries/ar_model/1)
- **Системные характеристики**: GPU (NVIDIA RTX 3090), 32 ГБ ОЗУ, 1 ТБ SSD
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик моделей</button> – обучает и оптимизирует модели для прогнозирования энергопотребления, анализирует результаты и улучшает точность.
  - <button class="role-button">🌐 Инженер DevOps</button> – создает инфраструктуру для развертывания и масштабирования системы, интегрирует Docker и Apache Kafka.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует данные с датчиков, выявляет паттерны и проводит исследование для улучшения точности моделей.
  - <button class="role-button">✅ Тестировщик/менеджер проекта</button> – тестирует работоспособность системы, управляет задачами и сроками.

</div>

<div class="project-card">

#### **Проект: Автоматизация обнаружения мошенничества в банковских операциях**
- **Описание**: Разработка системы для автоматизированного обнаружения мошенничества в банковских операциях, использующей машинное обучение и анализ поведения пользователей.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">PyTorch</button>, <button class="tech-button">Scikit-Learn</button>, <button class="tech-button">SQL</button>, <button class="tech-button">Kafka</button>
- **Источник данных**: [Открытые банковские данные России](https://data.gov.ru/), [Kaggle (Fraud Detection Datasets)](https://www.kaggle.com/)
- **Источник модели**: Модель для обнаружения аномалий с [HuggingFace](https://huggingface.co/models)
- **Системные характеристики**: GPU (NVIDIA A100), 64 ГБ ОЗУ, 2 ТБ SSD
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик моделей</button> – разрабатывает и обучает модели для обнаружения мошенничества, проводит тестирование и оптимизацию.
  - <button class="role-button">🌐 Инженер данных</button> – отвечает за обработку и подготовку данных, разработку потоков данных и интеграцию с банковскими системами.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует результаты моделей, выявляет аномалии и улучшает алгоритмы.
  - <button class="role-button">✅ Инженер по безопасности</button> – проверяет безопасность системы, устраняет уязвимости и управляет рисками.

</div>

<div class="project-card">

#### **Проект: Система прогнозирования запасов для ритейла**
- **Описание**: Создание системы прогнозирования запасов для крупной сети розничных магазинов, использующей временные ряды и данные о продажах для оптимизации логистики и снижения издержек.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">TensorFlow</button>, <button class="tech-button">Keras</button>, <button class="tech-button">Apache Spark</button>, <button class="tech-button">Tableau</button>
- **Источник данных**: [Открытые данные ритейла](https://data.gov.ru/), [Kaggle (Retail Sales Datasets)](https://www.kaggle.com/)
- **Источник модели**: Модель прогнозирования продаж с [Facebook Prophet](https://facebook.github.io/prophet/)
- **Системные характеристики**: GPU (NVIDIA RTX 3080), 32 ГБ ОЗУ, 1 ТБ SSD
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик моделей</button> – обучает модели прогнозирования, настраивает гиперпараметры и проводит тестирование.
  - <button class="role-button">🌐 Инженер данных</button> – отвечает за сбор, очистку и подготовку данных для моделей.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует результаты прогноза, предоставляет рекомендации по улучшению моделей и стратегии закупок.
  - <button class="role-button">✅ Тестировщик/менеджер проекта</button> – тестирует систему, управляет проектом и координирует задачи команды.

</div>

<div class="project-card">

#### **Проект: Система автоматического распознавания лиц для безопасности на предприятиях**
- **Описание**: Разработка системы автоматического распознавания лиц для контроля доступа на предприятии, использующей нейросети и компьютерное зрение.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">OpenCV</button>, <button class="tech-button">TensorFlow</button>, <button class="tech-button">Docker</button>, <button class="tech-button">Kubernetes</button>
- **Источник данных**: [Открытые данные изображений лиц](https://data.gov.ru/), [Kaggle (Face Recognition Datasets)](https://www.kaggle.com/)
- **Источник модели**: Модель для распознавания лиц с [FaceNet](https://github.com/davidsandberg/facenet)
- **Системные характеристики**: GPU (NVIDIA RTX 3090), 64 ГБ ОЗУ, 1 ТБ SSD
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик моделей</button> – разрабатывает и обучает модели для распознавания лиц, оптимизирует их производительность.
  - <button class="role-button">🌐 Инженер DevOps</button> – разворачивает и масштабирует систему с использованием Docker и Kubernetes.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует точность моделей и улучшает алгоритмы.
  - <button class="role-button">✅ Инженер по безопасности</button> – управляет рисками и проверяет уязвимости системы.

</div>

<div class="project-card">

#### **Проект: Автоматизированная система прогнозирования урожайности в сельском хозяйстве**
- **Описание**: Разработка системы для прогнозирования урожайности сельскохозяйственных культур на основе данных о погоде, почве и состоянии растений.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">Scikit-Learn</button>, <button class="tech-button">TensorFlow</button>, <button class="tech-button">Apache Hadoop</button>, <button class="tech-button">GeoPandas</button>
- **Источник данных**: [Открытые данные сельского хозяйства России](https://data.gov.ru/), [NASA Earth Data](https://earthdata.nasa.gov/)
- **Источник модели**: Модель прогнозирования урожайности с [DeepMind’s Alpha Fold](https://github.com/deepmind/alphafold)

- **Системные характеристики**: GPU (NVIDIA A100), 128 ГБ ОЗУ, 4 ТБ SSD
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик моделей</button> – обучает модели на данных о погоде и состоянии растений, оптимизирует их для различных культур.
  - <button class="role-button">🌐 Инженер данных</button> – собирает и обрабатывает данные из различных источников, интегрирует их в систему.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует данные о почве и погоде, улучшает модели прогноза.
  - <button class="role-button">✅ Тестировщик/менеджер проекта</button> – проверяет точность системы, управляет проектом и координирует работу команды.

</div>

<div class="project-card">

#### **Проект: Система предсказания дорожных заторов и аварий в реальном времени**
- **Описание**: Разработка системы предсказания заторов и аварий на дорогах крупных городов, используя данные с камер наблюдения, GPS и социальные сети.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">OpenCV</button>, <button class="tech-button">TensorFlow</button>, <button class="tech-button">Flask</button>, <button class="tech-button">Kafka</button>
- **Источник данных**: [Открытые данные транспорта России](https://data.gov.ru/), [API Яндекс.Пробки](https://yandex.ru/dev/maps/)
- **Источник модели**: Модель обнаружения объектов и прогнозирования трафика с [YOLO (You Only Look Once)](https://github.com/AlexeyAB/darknet)
- **Системные характеристики**: GPU (NVIDIA RTX 4090), 64 ГБ ОЗУ, 2 ТБ SSD
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик моделей</button> – обучает модели для анализа трафика и предсказания аварий, оптимизирует их для реального времени.
  - <button class="role-button">🌐 Инженер DevOps</button> – разворачивает систему на сервере, масштабирует и обеспечивает бесперебойную работу.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует данные о движении, улучшает точность прогнозов.
  - <button class="role-button">✅ Инженер по безопасности</button> – следит за защитой данных, проверяет систему на уязвимости.

</div>

<div class="project-card">

#### **Проект: Платформа для автоматизации анализа медицинских изображений**
- **Описание**: Создание системы для автоматического анализа медицинских изображений (например, рентгеновских снимков, КТ) с целью диагностики заболеваний.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">PyTorch</button>, <button class="tech-button">OpenCV</button>, <button class="tech-button">Docker</button>, <button class="tech-button">Kubernetes</button>
- **Источник данных**: [Открытые медицинские данные России](https://data.gov.ru/), [Kaggle (Medical Image Datasets)](https://www.kaggle.com/)
- **Источник модели**: Модель глубокого обучения для анализа изображений с [CheXNet](https://stanfordmlgroup.github.io/projects/chexnet/)
- **Системные характеристики**: GPU (NVIDIA RTX 4090), 128 ГБ ОЗУ, 2 ТБ SSD
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик моделей</button> – разрабатывает и обучает модели для анализа медицинских изображений, оптимизирует их точность.
  - <button class="role-button">🌐 Инженер DevOps</button> – отвечает за развертывание и масштабирование системы на сервере с помощью Docker и Kubernetes.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует результаты диагностики, улучшает алгоритмы анализа изображений.
  - <button class="role-button">✅ Тестировщик/инженер по безопасности</button> – тестирует систему на корректность и безопасность, устраняет уязвимости.

</div>

<div class="project-card">

#### **Проект: Платформа анализа настроений и отзывов клиентов для крупного бизнеса**
- **Описание**: Разработка системы для анализа настроений и отзывов клиентов по социальным сетям и отзывам на сайтах, использующей технологии NLP и машинное обучение.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">HuggingFace Transformers</button>, <button class="tech-button">PyTorch</button>, <button class="tech-button">Apache Kafka</button>, <button class="tech-button">React.js</button>
- **Источник данных**: [Открытые данные социальных сетей](https://data.gov.ru/), [API VK](https://vk.com/dev), [Twitter API](https://developer.twitter.com/en/docs/twitter-api)
- **Источник модели**: Модель для анализа тональности текстов с [RuBERT](https://huggingface.co/DeepPavlov/rubert-base-cased)
- **Системные характеристики**: GPU (NVIDIA RTX 3090), 64 ГБ ОЗУ, 2 ТБ SSD
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик моделей</button> – обучает модели анализа тональности, оптимизирует их для конкретных доменов.
  - <button class="role-button">🌐 Инженер данных</button> – собирает данные из социальных сетей и отзывов, готовит их для обучения моделей.
  - <button class="role-button">🎨 Разработчик фронтенда</button> – создает интерфейс для визуализации анализа отзывов и настроений.
  - <button class="role-button">✅ Тестировщик/менеджер проекта</button> – тестирует систему, управляет проектом и контролирует выполнение задач.

</div>

<div class="project-card">

#### **Проект: Система автоматического анализа юридических документов**
- **Описание**: Разработка системы для автоматизированного анализа и обработки юридических документов, включая определение ключевых рисков и возможностей.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">HuggingFace Transformers</button>, <button class="tech-button">PyTorch</button>, <button class="tech-button">Flask</button>, <button class="tech-button">SQL</button>
- **Источник данных**: [Открытые юридические данные России](https://data.gov.ru/), [Kaggle (Legal Text Datasets)](https://www.kaggle.com/)
- **Источник модели**: Модель NLP для анализа юридических текстов с [BERT for Legal](https://github.com/huggingface/transformers)
- **Системные характеристики**: GPU (NVIDIA RTX 3090), 64 ГБ ОЗУ, 1 ТБ SSD
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик моделей</button> – обучает модели для анализа юридических текстов, оптимизирует их для конкретных задач.
  - <button class="role-button">🌐 Инженер данных</button> – отвечает за сбор и подготовку юридических документов для анализа.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует результаты моделей, находит паттерны и риски в юридических документах.
  - <button class="role-button">✅ Тестировщик/инженер по безопасности</button> – тестирует систему, проверяет на уязвимости и улучшает безопасность.

</div>

<div class="project-card">

#### **Проект: Платформа для мониторинга и управления климатом в сельском хозяйстве**
- **Описание**: Разработка системы мониторинга и управления климатическими условиями для фермеров, включающей прогнозирование погоды и управление поливом.
- **Стек**: <button class="tech-button">Python</button>, <button class="tech-button">TensorFlow</button>, <button class="tech-button">Django</button>, <button class="tech-button">Grafana</button>, <button class="tech-button">IoT</button>
- **Источник данных**: [Открытые данные метеорологии России](https://meteo.ru/), [NASA Earth Data](https://earthdata.nasa.gov/)
- **Источник модели**: Модель прогнозирования погоды с [WeatherBench](https://github.com/pangeo-data/WeatherBench)
- **Системные характеристики**: GPU (NVIDIA RTX 4090), 128 ГБ ОЗУ, 2 ТБ SSD
- **Роли в команде**:
  - <button class="role-button">🖥️ Разработчик моделей</button> – обучает модели для прогнозирования климатических условий, улучшает их точность.
  - <button class="role-button">🌐 Инженер IoT</button> – интегрирует систему с IoT-устройствами для сбора данных с полей.
  - <button class="role-button">📊 Аналитик данных</button> – анализирует климатические данные, предлагает стратегии управления.
  - <button class="role-button">✅ Тестировщик/менеджер проекта</button> – тестирует работоспособность системы, управляет задачами и сроками.

</div>

{{< /admonition >}}

<!--

{{< admonition success "👶 Простые:" false >}}

1. **Трекер финансовых расходов**. Разработайте приложение с использованием `Streamlit`, которое позволит пользователям вводить свои ежедневные финансовые расходы. Приложение должно агрегировать данные и предоставлять пользователю статистику о том, сколько он потратил по категориям за месяц. Рекомендуемый стэк: `Python`, `Streamlit`, `Pandas`.
2. **Анализ данных о фильмах**. Используя библиотеку `Pandas`, разработайте скрипт для анализа данных о фильмах. Вам нужно будет загрузить данные, выполнить базовый анализ жанров, годов выпуска и рейтингов, а затем визуализировать результаты с помощью графиков. Рекомендуемый стэк: `Python`, `Pandas`.
3. **Текстовый анализатор тональности**. Создайте приложение с использованием `Streamlit`, которое позволит пользователям вводить текст и определять его тональность (положительная, нейтральная или отрицательная). Для анализа тональности используйте библиотеки для обработки текста и машинного обучения. Рекомендуемый стэк: `Python`,  `Streamlit`, `Pandas`, `NLTK`, `spaCy`, `pymorphy2` .
4. **Генератор случайных фактов**. Разработайте приложение с использованием `Streamlit`, которое будет предоставлять пользователю случайные факты из разных областей знаний. Используйте библиотеки для генерации случайных чисел и создания интерактивных интерфейсов. Рекомендуемый стэк: `Python`,  `Streamlit`, `Pandas`, `random`, `wikipediaapi`, `NLTK`.
5. **Анализ данных о продажах**. Воспользуйтесь библиотекой `Pandas` для анализа данных о продажах определенного продукта за несколько месяцев. Создайте отчет с общей статистикой, графиками продаж по дням и анализом популярных товаров. Визуализируйте результаты с помощью библиотеки `Matplotlib` или `Seaborn`. Рекомендуемый стэк: `Python`, `Pandas`.

{{< /admonition >}}

{{< admonition warning "👨‍💻 Средние:" false >}}

1. **Калькулятор с автозаполнением**. Разработайте простой калькулятор, который предоставляет автозаполнение для операторов и чисел при вводе математических выражений. Например, при вводе «2+» калькулятор должен предложить автозаполнение с операторами «+», «-», «*», «/», а также предыдущими результатами вычислений. Рекомендуемый стэк: `Python`, `Streamlit`, `Pandas`.
2. **Система рекомендаций для книжного магазина**. Создайте систему, которая предоставляет рекомендации пользователям книг на основе их предыдущих покупок. Используйте простые алгоритмы, такие как рекомендации на основе наиболее популярных книг или схожих интересов. Рекомендуемый стэк: `Python`, `Pandas`.
3. **Конвертер валют с анализом трендов**. Реализуйте инструмент для конвертации валют с возможностью отображения графика изменения курса валюты за определенный период времени. Возможно, используйте сторонние API для получения данных о курсах валют. Рекомендуемый стэк: `Python`, `Streamlit`, `Pandas`, `yfinance`.
4. **Простой чат-бот для путешествий**. Разработайте чат-бота, который может отвечать на вопросы пользователей о популярных туристических направлениях, предоставлять информацию о погоде, достопримечательностях и ценах на билеты. Рекомендуемый стэк: `Python`, `Streamlit`, `Pandas`, `telebot`.
5. **Определение тональности текстовых отзывов**. Создайте интеллектуальную информационную систему, которая может автоматически анализировать тональность текстовых отзывов (положительная, нейтральная или отрицательная). Используйте простые алгоритмы анализа сентиментов, например, на основе ключевых слов или частоты использования позитивных и негативных слов. Рекомендуемый стэк: `Python`,  `Streamlit`, `Pandas`, `NLTK`, `spaCy`, `pymorphy2` .

{{< /admonition >}}

{{< admonition danger "👨‍🎓 Сложные:" false >}}

1. **Генератор автоматических резюме**. Разработайте инструмент на `Streamlit`, который принимает на вход текст статьи или блога и создает автоматическое резюме этого текста. Воспользуйтесь методами анализа текста и выделения ключевых предложений.
2. **Анализ новостных статей**. Создайте приложение на `Streamlit`, которое позволит пользователю вводить ключевое слово или фразу, после чего приложение будет анализировать новостные статьи и выводить сводку основных событий и информации по данной теме.
3. **Система вопрос-ответ для FAQ**. Разработайте чат-бота, который будет отвечать на часто задаваемые вопросы (FAQ) по определенной теме. Используйте методы обработки текста и анализа интентов, чтобы чат-бот понимал вопросы и предоставлял соответствующие ответы.
4. **Анализ новостных трендов**. Создайте интерактивную дашборд-панель на `Streamlit`, которая будет отображать актуальные новости и анализировать тренды по ключевым словам. Используйте API новостных источников, библиотеки для обработки текста и визуализации данных.
5. **Детекция аномалий в временных рядах**. Разработайте систему, которая автоматически обнаруживает аномалии в временных рядах данных, например, в метриках производительности серверов или финансовых показателях. Используйте методы машинного обучения, такие как `Isolation Forest`, `One-Class SVM`, для обнаружения аномалий.

{{< /admonition >}}

-->

## Критерии оценки

{{< admonition quote "" >}}

Вы должны уметь правильно формулировать свою мысль вне зависимости от ее наличия!

{{< /admonition >}}

<!--

##### Оценка за курс

Конечная оценка за весь курс, суммируется по следующей формуле:

- [*Project*] Сумма всех баллов за проектные задания (<u>минимум 2 проекта</u>);
- [*Test*] Сумма баллов за тестовые задания;
- [*Other*] Индивидуальные достижения – при защите, разработке и т.д. (до 50 баллов)
- [*Exam*] Экзамен (до 50 баллов);
- [*Rate*] Коэффициент посещаемости (от 1 до 1,51 из расчета 1 посещение = 0,015).

$$
\bf{\text{Grade}} = \frac{\left [ \text{Project} + \text{Test} + \text{Exam} + \text{Other} \right ] \cdot \text{Rate}}{453} \cdot 100
$$
{{< admonition info "Знаменатель" false >}}

Значение под знаменателем бралось из расчета:

- 2 проекта по <u>50 баллов</u>, 
- выполнение всех тестовых заданий на 100% = <u>100 баллов</u>, 
- экзамен на <u>50 баллов</u>,
- личные достижения на <u>50 баллов</u>,
- полная посещаемость 34 занятий даёт $1+34\cdot 0.015$ <u>коэффициент 1,51</u>.

$$
\left [100 + 100 + 50 + 50\right ] \cdot 1.51 = 453
$$

{{< /admonition >}}

В результате, конечная оценка, будет соответствовать:

- 0-39 – **Неудовлетворительно**
- 40-59 – **Удовлетворительно** 🥉
- 60-79 – **Хорошо** 🥈
- 80-100 – **Отлично** 🥇

-->

<!--
##### Оценка проектного задания

Для оценки проектного задания используются следующие критерии, от 1 до 10 баллов за каждый пункт:

- **Техническая реализация (Код)** – оценивается качество кода, архитектурные решения, соответствие требованиям, а также новизна и актуальность с точки зрения использованных технологий.

- **Качество результата (Результат)** – оценка точности, эффективности и достигнутых результатов, их соответствие целям проекта, при необходимости сравнение эффективни решения задачи по метрикам.

- **Функциональность и алгоритмы (Функциональность)** – оценивается разработанная функциональность интеллектуальной системы (удобство в использовании) и адекватность использованных подходов, моделей, алгоритмов, т.е. реализация моделей машинного обучения, обработка данных, генерация выводов и рекомендаций и т.д.

- **Интеграция, документация и тестирование (Интеграция)** – оценивается способность интеграции различных компонент разработанной системы в другие проекты. Тестирование должно быть документировано и обосновано.

- **Презентация проекта (Презентация)** – оценивается представление проекта, понятность и суть.

| Баллы | Код                                                          | Результат                                                    | Функциональность                                             | Интеграция                                                   | Презентация                                                  |
| :---: | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
|  1-3  | Отсутствие реализации или неполная реализация основных компонентов системы. | Результат не соответствует требованиям задания, неудовлетворительный уровень выполнения. | Отсутствие или неправильная реализация основных алгоритмов и функциональностей. | Отсутствие интеграции, недостаточная документация и неполное тестирование. | Неудовлетворительное представление проекта, неясное изложение информации. |
|  4-6  | Реализованы основные компоненты системы, но присутствуют существенные недоработки или ошибки. | Результат частично соответствует требованиям, но присутствуют значительные недоработки. | Алгоритмы и функциональности частично реализованы, но работоспособность сомнительна. | Некоторая интеграция, базовая документация и неполное тестирование. | Базовое представление проекта, но присутствуют недоработки в организации и структуре презентации. |
|  7-9  | Основные компоненты системы реализованы, большинство функциональностей работает корректно. | Результат соответствует большей части требований, но есть небольшие недочеты. | Большая часть функциональностей и алгоритмов реализована и работает корректно. | Хорошая интеграция, достаточная документация и системное тестирование. | Хорошо организованная презентация, четкое и логичное изложение информации. |
|  10   | Качественная техническая реализация всех компонентов системы, минимальное количество ошибок. | Качественный результат, полностью соответствующий требованиям задания. | Качественная реализация всех алгоритмов и функциональностей, точность и эффективность доказаны. | Качественная интеграция, полная и структурированная документация, широкий спектр тестов. | Профессиональное и убедительное представление проекта, умение ответить на вопросы. |

{{< echarts >}}

title:
  text: Пример оценки
tooltip:
  trigger: axis
legend:
  data:
    - Project 1
    - Project 2
radar:
  indicator:
    - name: Код
      max: 10
    - name: Результат
      max: 10
    - name: Функциональность
      max: 10
    - name: Интеграция
      max: 10
    - name: Презентация
      max: 10
series:
  - name: Budget vs spending
    type: radar
    tooltip:
      trigger: item
    areaStyle: {}
    data:
      - value:
          - 9
          - 7
          - 6
          - 3
          - 5
        name: Project 1
      - value:
          - 5
          - 4
          - 8
          - 7
          - 10
        name: Project 2

{{< /echarts >}}

-->

1. **Реализация и полнота проекта** (20%)
   - **Соответствие требованиям**: проект должен соответствовать первоначально заявленным требованиям и задачам. Оценивается полнота и качество выполнения поставленных задач.
   - **Функциональность**: система должна корректно выполнять заявленные функции. Проверяется наличие всех ключевых функций, их работоспособность и правильность выполнения.
   - **Завершенность**: оценивается, завершен ли проект полностью или остались незакрытые задачи или ошибки.

2. **Качество кода и архитектуры** (15%)
   - **Чистота и читаемость кода**: код должен быть структурированным, хорошо документированным и читаемым. Следование лучшим практикам программирования, включая использование комментариев, ясных имен переменных и функций.
   - **Архитектура проекта**: оценивается выбор архитектурных решений, их соответствие задачам проекта, гибкость и масштабируемость. Наличие логической структуры, модульности и разделения ответственности.
   - **Эффективность и оптимизация**: оценка эффективности работы системы, включая использование ресурсов (памяти, процессора), быстродействие и оптимизация запросов к базе данных.

3. **Использование технологий и моделей** (20%)
   - **Правильность выбора технологий и моделей**: соответствие выбранных технологий и моделей задачам проекта. Оценивается уместность и целесообразность их использования.
   - **Интеграция и использование внешних библиотек и API**: умение эффективно использовать внешние библиотеки и API, их правильная интеграция в проект.
   - **Актуальность моделей и методов**: оценка актуальности и новизны использованных методов и моделей машинного обучения, наличие инновационных подходов.

4. **Анализ данных и обучение моделей** (15%)
   - **Качество данных и подготовка**: оценивается качество исходных данных, их очистка, обработка и подготовка для анализа и обучения моделей.
   - **Точность и адекватность моделей**: оценка точности обученных моделей, их адекватности решаемой задаче. Использование метрик оценки качества, таких как точность (accuracy), полнота (recall), F1-мера и другие.
   - **Обоснование выбора моделей и методов**: насколько обоснован выбор использованных моделей и методов, их преимуществ и ограничений для конкретного проекта.

5. **Интерфейс и пользовательский опыт (UX/UI)** (10%)
   - **Дизайн и удобство использования**: оценивается удобство и интуитивность интерфейса, соответствие современным стандартам UX/UI-дизайна.
   - **Эргономика и адаптивность**: проверка на эргономичность и адаптивность интерфейса под различные устройства и платформы.
   - **Качество визуализации данных**: оценивается качество и информативность визуализаций, используемых в проекте (графики, диаграммы, интерактивные панели).

6. **Документация и презентация проекта** (5%)
   - **Качество документации**: наличие и качество документации к проекту, включая техническую документацию, инструкции для пользователей, установочные руководства и комментарии в коде.
   - **Презентация проекта**: оценивается качество презентации, включающей демонстрацию функционала, основных особенностей и преимуществ проекта.
   - **Обоснование решений**: способность команды обосновать выбранные решения, подходы и методы.

7. **Инновационность и оригинальность решения** (10%)
   - **Инновационность подходов**: использование инновационных технологий, методов и подходов. Оценка новизны идеи и оригинальности проекта.
   - **Решение новых или сложных задач**: способность проекта решать новые или особенно сложные задачи, которые до этого не имели эффективных решений.

8. **Командная работа и организация процесса** (5%)
   - **Эффективность командной работы**: оценивается взаимодействие в команде, распределение ролей и задач, соблюдение сроков.
   - **Управление проектом**: оценка качества управления проектом, использования методов Agile/Scrum, управления задачами и отслеживания прогресса.


{{< echarts >}}

title:
  text: Критерии оценки проекта
tooltip:
  trigger: item
series:
  - name: Критерии
    type: pie
    radius: '50%'
    data:
      - value: 20
        name: Реализация и полнота проекта
      - value: 15
        name: Качество кода и архитектуры
      - value: 20
        name: Использование технологий и моделей
      - value: 15
        name: Анализ данных и обучение моделей
      - value: 10
        name: Интерфейс (UX/UI)
      - value: 5
        name: Документация и презентация проекта
      - value: 10
        name: Инновационность и оригинальность решения
      - value: 5
        name: Командная работа и организация процесса
        emphasis:
        itemStyle:
        shadowBlur: 10
        shadowOffsetX: 0
        shadowColor: rgba(0, 0, 0, 0.5)

{{< /echarts >}}

#### Важность баланса в проекте

На визуализации представлены два проекта — **Проект A** и **Проект B**, демонстрирующие, насколько важно соблюдать баланс в работе над проектом.

**Проект A: Сильная реализация, слабое оформление**
Проект A получил высокие оценки за:
- **Техническую реализацию**: сильные стороны в разработке, качестве кода, использовании технологий и анализе данных.
- Однако слаб в **оформлении**: низкие оценки за UX/UI и презентацию. Проект может быть труден в использовании и плохо воспринимается пользователями.

**Проект B: Хорошее оформление, слабая реализация**
Проект B показывает:
- **Высокое качество UX/UI и презентации**: проект удобен и понятен пользователям.
- Но **слабую техническую реализацию**: средние и низкие оценки за реализацию, код и анализ данных, что снижает его эффективность.

{{< echarts >}}

title:
  text: Дисбаланс в оценке проекта
tooltip:
  trigger: axis
legend:
  data:
    - Проект A
    - Проект B
radar:
  indicator:
    - name: Реализация проекта
      max: 20
    - name: Код и архитектура
      max: 15
    - name: Технологии и модели
      max: 20
    - name: Данные и обучение модели
      max: 15
    - name: Интерфейс (UX/UI)
      max: 10
    - name: Презентация проекта
      max: 5
    - name: Оригинальность решения
      max: 10
    - name: Организация процесса
      max: 5
series:
  - name: Оценка проекта
    type: radar
    data:
      - value:
          - 18  # Проект A: высокая оценка за реализацию
          - 14  # Проект A: высокий уровень кода и архитектуры
          - 17  # Проект A: хорошее использование технологий и моделей
          - 13  # Проект A: высокий уровень анализа данных и обучения моделей
          - 3   # Проект A: низкий UX/UI
          - 2   # Проект A: плохая презентация проекта
          - 8   # Проект A: достаточно оригинальное решение
          - 4   # Проект A: средняя организация процесса
        name: Проект A
      - value:
          - 10  # Проект B: средняя реализация проекта
          - 7   # Проект B: средний уровень кода и архитектуры
          - 9   # Проект B: использование технологий на среднем уровне
          - 5   # Проект B: базовый анализ данных и обучение моделей
          - 9   # Проект B: высокий уровень UX/UI
          - 4   # Проект B: отличная презентация проекта
          - 7   # Проект B: высокая оригинальность решения
          - 3   # Проект B: удовлетворительная организация процесса
        name: Проект B
    areaStyle: {}

{{< /echarts >}}

Успешный проект требует сочетания **сильной технической реализации** и **качественного оформления**. Хорошо разработанный продукт должен быть не только функциональным, но и удобным в использовании. Помните: **баланс** — ключ к успеху любого проекта!

<!-- ##### Тестирование

Тестирование по теоретическим основам курса:

[<div style="text-align: center;">:(fa-solid fa-robot fa-bounce): Telegram-bot для тестирования</div>]() -->

## Рекомендации

{{< admonition info "Про IDE" false >}}

[JupyterLab](https://github.com/jupyterlab/jupyterlab/releases) – гибкая, интегрируемая и легко расширяемая среда, поддерживающая одновременную работу с несколькими блокнотами Jupyter (`*.ipynb`), текстовыми файлами, датасетами и терминалами (поддерживает  также изображения, CSV, JSON, Markdown, PDF [и другие форматы](http://jupyterlab.readthedocs.io/en/latest/user/file_formats.html#file-and-output-formats)).

[Spyder](https://www.spyder-ide.org/) – бесплатная среда разработки предназначенная для ученых, инженеров и аналитиков данных, интерфейс очень похож на RStudio.

{{< /admonition >}}

{{< admonition info "Про online IDE" false >}}

- [Deepnote](https://deepnote.com/) – удобная платформа для командной работы, имеет множество возможностей для интеграции, имеется [educatiaon plan](https://deepnote.com/docs/edu-verification) (`Python`, `R`, `SQL`).
- [HEX](https://hex.tech/) – мощная онлайн платформа делающая упор на работу с данными, интегрированные инструменты позволяют не только подключить данные из множества источников, но и увидеть множество вариантов визуализации (`Python`, `R`, `SQL`).
- [GoogleColab](https://colab.research.google.com/) – относительно хорошая производительность бесплатно предоставляемых мощностей (`Python`).

{{< /admonition >}}

{{< admonition info "Про табличный формат" false >}}

- [EmEditor](https://en.wikipedia.org/wiki/EmEditor) –  [коммерческий](./soft/Emurasoft_EmEditor_Professional_v18.6.8_Final_2019_x86_x64_RUS_rutracke.torrent) текстовый редактор для Windows, способный работать с очень большими объемами табличных данных  (до 248 ГБ или 2,1 миллиарда строк).

{{< /admonition >}}

{{< admonition info "Про хостинг" false >}}

<!-- ![](bot_hosting.png "Возможный вариант архитектуры") -->

- [Streamlit Share](https://share.streamlit.io/)
- [Netlify](https://netlify.com/)

{{< /admonition >}}

## Источники

[**Intro**] Введение в ИИС и выравнивание знаний.

![](cover_intro.png " ")

{{< admonition example "📚 Библиография:" false >}}

[[1](./books/Андрейчиков-Интеллектуальные_информационные_системы_и_методы_искусственного_интеллекта.pdf)] *Андрейчиков Александр – Интеллектуальные информационные системы и методы искусственного интеллекта, 2023.*

[[2](./books/Остроух-Интеллектуальные_информационные_системы_и_технологии.pdf)] *Остроух Андрей, Николаев Андрей – Интеллектуальные информационные системы и технологии : монография, 2021.*

[[3](./books/LeanDS_Managing_ML_products.pdf)] *Асхат Уразбаев – Управление DS проектами и продуктами при помощи Lean Data Science, 2020.*

[[4](./books/Agile.pdf)] *Коул Роб, Скотчер Эдвард – Блистательный Agile. Гибкое управление проектами с помощью Agile, Scrum и Kanban, 2019.*

[[5](./books/Дизайн_мышление.pdf)] *Леврик Михаэль, Линк Патрик, Лейфер Ларри – Дизайн-мышление. От инсайта к новым продуктам и рынкам, 2020.*

[[6](./books/Автостопом_по_Python_-_Кеннет_Рейтц,_Таня_Шлюссер.pdf)] *Кеннет Рейтц, Таня Шлюссер – Автостопом по Python, 2017.*

[[7](./books/Python_Лучшие_практики_и_инструменты_4_е_изд.pdf)] *Яворски Михал, Зиаде Тарек – Pythoп. Лучшие практики и инструменты. 4-е изд., 2024.*

[[8](./books/Кэти_Танимура_SQL_для_анализа_данных_2024.pdf)] *Танимура Кэти – SQL для анализа данных, 2024.*

[[9](./books/ChatGPT_ваш_наставник_по_Python.pdf)] *Серхио Рохас-Галеано – ChatGPT: ваш наставник по Python, 2023.*

{{< /admonition >}}

<div style="text-align: center;">***</div>

[**Algo**] Алгоритмизация стратегий и решений для разработки ИИС.

![](cover_algo.png " ")

{{< admonition example "📚 Библиография:" false >}}

[[1](./books/40_alghoritmov_Python.pdf)] *Ахмад Имран – 40 алгоритмов, которые должен знать каждый программист на Python, 2023.*

[[2](./books/Alghoritmy_priniatiia_rieshieni.pdf)] *Кохендерфер Микель, Уилер Тим, Рэй Кайл – Алгоритмы принятия решений, 2023.*

[[3](./books/Алгоритмы_для_начинающих.pdf)] *Луридас Панос – Алгоритмы для начинающих: теория и практика для разработчика, 2018.*

[4] *LeetCode: Online Programming Learning Platform – https://leetcode.com*

[5] *LeetCode & Coding Interview Guide – https://doocs.github.io/leetcode/#/README_EN*

[[6](./books/Lectures_on_Intelligent_Systems.pdf)] *Leonardo Vanneschi, Sara Silva – Lectures on Intelligent Systems, 2023.*

{{< /admonition >}}

<div style="text-align: center;">***</div>

[**ML**] Классификация и описание моделей и их метрик в машинном обучении.

{{< admonition example "📚 Библиография:" false >}}

[[1](./books/Alghoritmy_DataScience.pdf)] *Протодьяконов А.В. – Алгоритмы DataScience и их практическая реализация на Python, 2022.* 

[2] *labml.ai: Annotated PyTorch Paper Implementations – https://nn.labml.ai*

{{< /admonition >}}

<div style="text-align: center;">***</div>

[**NLP**] Техники и Модели обработки естественного языка (NLP).

<!-- ![](cover_nlp.png " ") -->

{{< admonition example "📚 Библиография:" false >}}

[1] *NLP Course | For You – https://lena-voita.github.io/nlp_course.html*

[[2](./books/Обработка_естественного_языка_в_действии.pdf)] *Хобсон Лейн, Ханнес Хапке, Коул Ховард – Обработка естественного языка в действии, 2020.*

{{< /admonition >}}

<div style="text-align: center;">***</div>

[**LLM**] Большие языковые модели (LLM) для ИИС.

{{< admonition example "📚 Библиография:" false >}}

[[1](./books/GPT-3_programmirovanie_na_Python.pdf)] *Aймен Эль Амри – GPT-3: программирование на Python в примерах, 2023.*

[2] 

[3] *Brex's Prompt Engineering Guide – https://github.com/brexhq/prompt-engineering*

{{< /admonition >}}