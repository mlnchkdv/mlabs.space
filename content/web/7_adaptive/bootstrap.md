---
weight: 1
title: Введение в Bootstrap
description: Bootstrap - CSS-фреймворк для создания адаптивных сайтов
author: MLabs
authorLink: null
date: 2023-08-03T14:48:57.920Z
lastmod: null
slug: bootstrap
categories:
  - WEB
math: true
lightgallery: true
toc:
  auto: false
draft: false
---

### Введение в Bootstrap для новичков

**[Bootstrap](https://bootstrap-4.ru/docs/5.3/getting-started/introduction/)** — это популярный CSS-фреймворк для создания адаптивных и удобных интерфейсов веб-сайтов. Он предоставляет готовые стили и компоненты, такие как сетка, карточки, формы, навбары, модальные окна и многое другое, что упрощает и ускоряет процесс разработки.

**Преимущества Bootstrap**:
1. **Адаптивность**: Bootstrap автоматически подстраивает элементы для различных устройств и экранов.
2. **Скорость разработки**: с помощью готовых компонентов можно легко и быстро создать привлекательный интерфейс.
3. **Широкий функционал**: Bootstrap предлагает множество готовых компонентов, которые можно настроить под свои нужды.

### Быстрый старт с Bootstrap

Чтобы быстро начать работу с Bootstrap, можно подключить его через **CDN**. Это позволяет сразу использовать стили и скрипты Bootstrap в вашем проекте без необходимости загружать их на компьютер.

**Шаги**:
1. Добавьте ссылки на стили и скрипты Bootstrap в `<head>` вашего HTML-документа.
    ```html
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    ```
2. Используйте готовые классы и компоненты для создания элементов интерфейса.

### Пример кода

Ниже приведен пример веб-страницы, которая включает разнообразные компоненты Bootstrap, такие как навбар, карточки, кнопки, модальное окно и форма. Этот пример оптимизирован для максимальной адаптивности и будет хорошо смотреться на различных устройствах.

<iframe height="600" style="width: 100%;" scrolling="no" title="Bootstrap Advanced Example" src="https://codepen.io/mlnchkdv/embed/MWNXqEE?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/mlnchkdv/pen/MWNXqEE">
  Bootstrap Advanced Example</a> by mlnchkdv (<a href="https://codepen.io/mlnchkdv">@mlnchkdv</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bootstrap Advanced Example</title>
  <!-- Подключаем стили Bootstrap -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

  <!-- Навбар -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <a class="navbar-brand" href="#">MySite</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <a class="nav-link active" href="#">Главная</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">О нас</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Услуги</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Контакты</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Основной контейнер -->
  <div class="container my-4">
    <h1 class="text-center">Добро пожаловать на MySite!</h1>
    <p class="text-center">Исследуйте возможности Bootstrap с разными компонентами</p>

    <!-- Карточки с адаптивной сеткой -->
    <div class="row">
      <div class="col-12 col-md-6 col-lg-4 mb-4">
        <div class="card h-100">
          <img src="https://via.placeholder.com/300x200" class="card-img-top" alt="Image 1">
          <div class="card-body">
            <h5 class="card-title">Карточка 1</h5>
            <p class="card-text">Описание первого элемента, адаптированное для мобильных устройств.</p>
            <a href="#" class="btn btn-primary w-100">Подробнее</a>
          </div>
        </div>
      </div>
      <div class="col-12 col-md-6 col-lg-4 mb-4">
        <div class="card h-100">
          <img src="https://via.placeholder.com/300x200" class="card-img-top" alt="Image 2">
          <div class="card-body">
            <h5 class="card-title">Карточка 2</h5>
            <p class="card-text">Описание второго элемента, демонстрирующее гибкость карточек Bootstrap.</p>
            <button class="btn btn-secondary w-100" data-bs-toggle="modal" data-bs-target="#exampleModal">Подробнее</button>
          </div>
        </div>
      </div>
      <div class="col-12 col-md-6 col-lg-4 mb-4">
        <div class="card h-100">
          <img src="https://via.placeholder.com/300x200" class="card-img-top" alt="Image 3">
          <div class="card-body">
            <h5 class="card-title">Карточка 3</h5>
            <p class="card-text">Еще один пример карточки с кнопкой перехода.</p>
            <a href="#" class="btn btn-success w-100">Перейти</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Модальное окно -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Подробнее о Карточке 2</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            Здесь вы можете узнать больше информации о втором элементе. Модальные окна помогают выделить ключевые данные.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Форма обратной связи -->
    <div class="card mt-4">
      <div class="card-body">
        <h5 class="card-title">Свяжитесь с нами</h5>
        <form>
          <div class="mb-3">
            <label for="name" class="form-label">Ваше имя</label>
            <input type="text" class="form-control" id="name" placeholder="Введите ваше имя">
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Электронная почта</label>
            <input type="email" class="form-control" id="email" placeholder="Введите вашу почту">
          </div>
          <div class="mb-3">
            <label for="message" class="form-label">Сообщение</label>
            <textarea class="form-control" id="message" rows="3" placeholder="Введите сообщение"></textarea>
          </div>
          <button type="submit" class="btn btn-primary w-100">Отправить</button>
        </form>
      </div>
    </div>
  </div>

  <!-- Подключаем скрипты Bootstrap для работы интерактивных компонентов -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### Описание кода

1. **Навбар** — адаптивная панель навигации, которая автоматически превращается в «кнопку-бургер» на небольших экранах. Кнопка позволяет развернуть меню на мобильных устройствах.
2. **Сетка с карточками** — карточки размещены с использованием адаптивных колонок. На мобильных устройствах они отображаются в одну колонку (`col-12`), на средних экранах в две (`col-md-6`), а на больших — в три (`col-lg-4`).
3. **Модальное окно** — открывается при нажатии на кнопку во второй карточке. Оно помогает показывать больше информации без перегрузки интерфейса.
4. **Форма** — включает поля для имени, почты и сообщения и размещена в карточке. Поля и кнопка заполняют всю ширину для удобства на мобильных устройствах.

### Примечания

- Весь контент автоматически адаптируется под размеры экрана, обеспечивая удобство на любых устройствах.
- Пример можно использовать как основу для вашего проекта и добавлять или модифицировать компоненты по необходимости.