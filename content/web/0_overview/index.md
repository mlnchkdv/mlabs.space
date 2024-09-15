---
weight: 1
title: Обзор курса
description: Основы современной вёрстки
author: MLabs
authorLink: null
date: 2023-09-11T14:48:57.920Z
lastmod: null
slug: overview
categories:
  - WEB
math: true
lightgallery: true
toc:
  auto: false
draft: false
---

# <div style="text-align: center;">Современный Web-дизайн в профессиональной деятельности</div>

<!--
{{< admonition info "Достижения 311:" false >}}

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSg9l6StvWEoEvnau9VjoMp2dlqn8PPyhJxHwLXZxQR-SXixlbW_BmPIE1XjM8GxrO0YtriqOlaZ39X/pubhtml?gid=1746296934&amp;range=B1:M30&single=true&widget=false&chrome=false&headers=false" width="100%" height="514px" frameborder="0" scrolling="no"></iframe>

{{< /admonition >}}

{{< admonition info "Достижения 312:" false >}}

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSg9l6StvWEoEvnau9VjoMp2dlqn8PPyhJxHwLXZxQR-SXixlbW_BmPIE1XjM8GxrO0YtriqOlaZ39X/pubhtml?gid=657377415&amp;range=B1:M30&single=true&widget=false&chrome=false&headers=false" width="100%" height="514px" frameborder="0" scrolling="no"></iframe>

{{< /admonition >}}

{{< admonition info "Достижения 321:" false >}}

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSg9l6StvWEoEvnau9VjoMp2dlqn8PPyhJxHwLXZxQR-SXixlbW_BmPIE1XjM8GxrO0YtriqOlaZ39X/pubhtml?gid=0&amp;range=B1:M30&single=true&widget=false&chrome=false&headers=false" width="100%" height="514px" frameborder="0" scrolling="no"></iframe>

{{< /admonition >}}

{{< admonition info "Достижения 323:" false >}}

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSg9l6StvWEoEvnau9VjoMp2dlqn8PPyhJxHwLXZxQR-SXixlbW_BmPIE1XjM8GxrO0YtriqOlaZ39X/pubhtml?gid=2000913631&amp;range=B1:M30&single=true&widget=false&chrome=false&headers=false" width="100%" height="514px" frameborder="0" scrolling="no"></iframe>

{{< /admonition >}}

{{< admonition info "Достижения 331:" false >}}

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSg9l6StvWEoEvnau9VjoMp2dlqn8PPyhJxHwLXZxQR-SXixlbW_BmPIE1XjM8GxrO0YtriqOlaZ39X/pubhtml?gid=584294338&amp;range=B1:M31&single=true&widget=false&chrome=false&headers=false" width="100%" height="514px" frameborder="0" scrolling="no"></iframe>

{{< /admonition >}}

{{< admonition info "Достижения 332:" false >}}

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSg9l6StvWEoEvnau9VjoMp2dlqn8PPyhJxHwLXZxQR-SXixlbW_BmPIE1XjM8GxrO0YtriqOlaZ39X/pubhtml?gid=1852629622&amp;range=B1:M30&single=true&widget=false&chrome=false&headers=false" width="100%" height="514px" frameborder="0" scrolling="no"></iframe>

{{< /admonition >}}

{{< admonition info "Список команд и проектов 2023-2024" false >}}

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRsl8LdmmLkenLGnmBlbU9fEJZrBnvWMvzNXE2da45Bx02sz5SAn63A9BCvlGdkGT9zBhFE4fZlT2_j/pubhtml?gid=0&amp;range=A1:L121&single=true&widget=false&chrome=false&headers=false" width="100%" height="600px" frameborder="0" scrolling="no"></iframe>

{{< /admonition >}}

-->



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
        min-height: 80vh;
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
    .semester-label {
        font-size: 1.4em;
        color: #333;
        margin: 10px 0 5px;
    }
    .progress-bar-container {
        width: 85%;
        background-color: #ddd;
        border-radius: 8px;
        margin-top: 10px;
        position: relative;
        height: 40px;
        overflow: visible;
    }
    @media (max-width: 500px) {
        .counter {
            padding: 7px;
            min-height: 90vh;
        }
        #countdown {
            font-size: 1.2em;
        }
        .progress-bar-container {
            width: 100%;
        }
    }
    .progress-bar {
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
        width: 70px;
        transform: translateX(-50%);
        line-height: 1.1;
    }
    .milestone br {
        margin: 1px;
    }
</style>
<div class="counter">
    <div class="title">До защиты проектов:</div>
    <div id="countdown">Загрузка...</div>
    <!-- Первая полоса загрузки -->
    <div class="semester-label">Семестр 1</div>
    <div class="progress-bar-container">
        <div class="progress-bar" id="progress-bar-semester1">0%</div>
        <div class="tick" style="left: 50%;"></div>
        <div class="tick" style="left: 70%;"></div>
        <div class="tick" style="left: 90%;"></div>
        <div class="milestone" style="left: 50%;"><b><i>Initial Assessment</i></b></div>
        <div class="milestone" style="left: 70%;"><i>Submission</i></div>
        <div class="milestone" style="left: 90%;"><i>Pitching 1</i></div>
    </div>
    <!-- Вторая полоса загрузки -->
    <br><br>
    <div class="semester-label">Семестр 2</div>
    <div class="progress-bar-container">
        <div class="progress-bar" id="progress-bar-semester2">0%</div>
        <div class="tick" style="left: 10%;"></div>
        <div class="tick" style="left: 30%;"></div>
        <div class="tick" style="left: 55%;"></div>
        <div class="tick" style="left: 75%;"></div>
        <div class="tick" style="left: 95%;"></div>
        <div class="milestone" style="left: 10%;"><b><i>Interim Assessment</i></b></div>
        <div class="milestone" style="left: 30%;"><i>Pitching 2</i></div>
        <div class="milestone" style="left: 55%;"><i>Pitching 3</i></div>
        <div class="milestone" style="left: 75%;"><b><i style="color: red;">Final Assessment</i></b></div>
        <div class="milestone" style="left: 95%;"><i>Project Defense</i></div>
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
        const endDate = new Date("2025-05-22T12:00:00");
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
        const startDate1 = new Date("2024-09-16T00:00:00");
        const endDate1 = new Date("2024-12-01T00:00:00");
        const startDate2 = new Date("2025-02-01T00:00:00");
        const endDate2 = new Date("2025-05-01T00:00:00");
        const now = new Date();
        // Обновление первой полосы загрузки
        if (now < startDate1) {
            document.getElementById("progress-bar-semester1").style.width = "0%";
            document.getElementById("progress-bar-semester1").innerHTML = "0%";
        } else {
            const totalDuration1 = endDate1 - startDate1;
            const elapsed1 = now - startDate1;
            const progressPercentage1 = Math.min((elapsed1 / totalDuration1) * 100, 100);
            document.getElementById("progress-bar-semester1").style.width = progressPercentage1 + "%";
            document.getElementById("progress-bar-semester1").innerHTML = Math.floor(progressPercentage1) + "%";
        }
        // Обновление второй полосы загрузки
        if (now < startDate2) {
            document.getElementById("progress-bar-semester2").style.width = "0%";
            document.getElementById("progress-bar-semester2").innerHTML = "0%";
        } else {
            const totalDuration2 = endDate2 - startDate2;
            const elapsed2 = now - startDate2;
            const progressPercentage2 = Math.min((elapsed2 / totalDuration2) * 100, 100);
            document.getElementById("progress-bar-semester2").style.width = progressPercentage2 + "%";
            document.getElementById("progress-bar-semester2").innerHTML = Math.floor(progressPercentage2) + "%";
        }
    }
    setInterval(function () {
        updateCountdown();
        updateProgressBar();
    }, 1000);
</script>





## Семестр 1 (HTML&CSS)

- [:(fa-solid fa-code): HTML и структура Web-документа](../html)
- [:(fa-solid fa-ellipsis): Глобальные атрибуты HTML](../attributes/)
- [:(fa-solid fa-palette): Основы CSS](../css/)
- [:(fa-solid fa-border-top-left): Отображения элементов, Единицы измерения, Работа с цветом](../units/), [:(fa-brands fa-codepen): Блочные-элементы](https://codepen.io/mlnchkdv/full/rNbyQNa), [:(fa-brands fa-codepen): Flex-элементы](https://codepen.io/mlnchkdv/full/KKYWrPY), [:(fa-brands fa-codepen): Список всех именнованных цветов](https://codepen.io/mlnchkdv/full/LYvWgJZ),[:(fa-brands fa-codepen): Отсортированные цвета в CSS](https://codepen.io/mlnchkdv/full/abxJRQO)
- [:(fa-solid fa-text-height): Оформление текста](../text_style), [:(fa-brands fa-codepen): Базовые CSS-свойства для фона](https://codepen.io/mlnchkdv/full/eYovPyo)
- [:(fa-solid fa-table-columns): Позиционирование](../position), [:(fa-brands fa-codepen): Позиционирование блоков](https://codepen.io/mlnchkdv/full/gOymByv), [:(fa-brands fa-codepen): CSS-свойства position](https://codepen.io/mlnchkdv/full/poBexMm)
- [:(fa-solid fa-display): Адаптивность](../adaptive)
- [:(fa-solid fa-clapperboard): Анимации](../animation), [:(fa-brands fa-codepen): CSS-свойства Transform](https://codepen.io/mlnchkdv/full/XWQMxVL), [:(fa-brands fa-codepen): 1 Пример анимаций в интерфейсе](https://codepen.io/mlnchkdv/pen/zYXZMxr), [:(fa-brands fa-codepen): 2 Пример анимаций в интерфейсе](https://codepen.io/mlnchkdv/pen/MWRpzag)
- [:(fa-solid fa-images): Форматы изображений](../image_formats)

## Семестр 2 (Цифровой дизайн)

- [:(fa-solid fa-book-open): Обзор курса](../design_overview)

## Семестр 2 (JS)

- [:(fa-brands fa-js): Введение в JavaScript](../intro_js)
- [:(fa-solid fa-folder-tree): DOM JavaScript](../dom_nodes)

## Дополнительные материалы

- [:(fa-solid fa-circle-exclamation): Инструкция по выполнению ВКР](../readme)
- [:(fa-solid fa-file-word): Шаблон выпускной работы](../files/Шаблон-ИФиЖ.docx) и [:(fa-solid fa-quote-left): пример ВКР](../files/Пример_ВКР_(ycadm.ru).docx)
- [:(fa-brands fa-codepen): Примеры лэндингов](../examples)
- [:(fa-brands fa-readme): Глоссарий](../glossary)
- [:(fa-solid fa-briefcase): Проекты для портфолио](../projects)

## Источники

[[1](../files/Чекмарев-Управление_ИТ-проектами_и_процессами.pdf)] *Чекмарев А.В. – Управление ИТ-проектами и процессами: учебник для вузов, Москва: Издательство Юрайт, 2022.*

[[2](../files/HTML5+CSS3_Основы_современного_дизайна_Кириченко_А_В,_Хрусталев.pdf)] *Кириченко А.В., Хрусталев А.А. – HTML5+CSS3. Основы современного Web-дизайна, СПб: Наука и Техника, 2018.*

[[3](../files/jаvascript_Рецепты_для_разработчиков_Скотт_Адам_Д_2023.pdf)] *Скотт Адам Д., Макдоналд Мэтью, Пауэрс Шелли – JavaScript. Рецепты для разработчиков, 3-е изд., СПб: Серия «Бестселлеры OReilly», 2023.*



<!-- ## Критерии оценки проектов

Оценка web-проекта по следующим критериям:

1. **Техническая реализация** (<u>5 баллов</u>): насколько хорошо веб-сайт работает технически. Это может включать в себя проверку на наличие ошибок, проверку, работает ли веб-сайт на различных устройствах и браузерах, а также оценку качества кода и его документации (комментарии).

2. **Дизайн, юзабилити и UI/UX** (<u>2 балла</u>): визуальный дизайн и удобство использования веб-сайта. Это может включать в себя оценку цветовой схемы, выбора шрифтов, расположения элементов на странице, а также насколько легко пользователям найти информацию и выполнить задачи на веб-сайте.

3. **Содержание** (<u>1 балл</u>): качество и полезность содержания на веб-сайте. Это может включать в себя оценку точности и актуальности информации, а также оценку, насколько хорошо содержание отвечает на потребности целевой аудитории.

4. **Инновационность** (<u>2 балла</u>): насколько веб-сайт представляет собой что-то новое или уникальное. Это может включать в себя оценку уникальных функций или подходов, использованных на веб-сайте, или оценку, насколько веб-сайт отличается от других веб-сайтов в той же области.

   -->
