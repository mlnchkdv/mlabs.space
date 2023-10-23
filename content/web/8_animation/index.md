---
weight: 1
title: CSS-Анимации
description: Анимации в web при помощи Transitions, Animations и Motion Path
author: MLabs
authorLink: null
date: 2023-09-03T14:48:57.920Z
lastmod: null
slug: animation
categories:
  - WEB
math: true
lightgallery: true
toc:
  auto: false
draft: false
---

До появления CSS3 при слове «анимация» верстальщиков бросало в холодный пот. А всё потому, что в те времена сделать качественную и красивую анимацию было не тривиальной задачей. CSS этого делать не умел, поэтому все анимации делались на JavaScript. Нужно было перелопатить кучу форумов, найти таких же товарищей по несчастью, потратить уйму времени на разработку, а в итоге услышать от дизайнера: «Ладно, сойдет и так». И когда наконец вышел CSS3, фейерверки не прекращались до утра, а шампанское лилось рекой. Это был знаменательный день для всех web-разработчиков (следующий такой день был, когда Microsoft объявила о прекращении поддержки Internet Explorer). С приходом CSS3 многие ранее сложные задачи превратились в простые и приятные для работы.

## CSS transitions

CSS transitions позволяют сделать изменения CSS-свойств плавно и в течение некоторого времени. Таким образом, вы получаете возможность контролировать процесс перехода элемента от одного состояния к другому. Начнем с простейшего примера и продолжим дальше.

При наведении курсора на квадрат плавно изменяется цвет фона.

<iframe height="265" scrolling="no" title="Exapmple transitions css" src="https://codepen.io/ruslan_khomiak/embed/bBvdMp/?height=265&amp;theme-id=0&amp;default-tab=css,result&amp;embed-version=2" frameborder="no" allowtransparency="true" allowfullscreen="true" style="width: 732px;"></iframe>

Теперь подробнее рассмотрим, как управлять переходами в CSS. У нас на вооружении есть всего 5 свойств, которые позволяют контролировать transition-анимацию:

-   `transition-property;`
-   `transition-duration;`
-   `transition-timing-function;`
-   `transition-delay;`
-   `transition;`

**transition-property** — указывает список свойств, которые будут анимироваться; свойства, которые здесь не указаны, будут изменяться обычным образом. Можно анимировать все свойства для конкретного элемента, указав значение `all`. Если вы не указали ни одного свойства, то по умолчанию используется значение `all`.

Пример:

```css
transition-property: width;
```

**transition-duration** — задаёт значение продолжительности анимации, время можно указывать в секундах или миллисекундах.

Пример:

```css
transition-duration: 1s;
```

**transition-timing-function** — временная функция, указывает точки ускорения и замедления за определенный период времени для контроля изменения скорости анимации. Проще говоря, с помощью этого свойства можно указать поведение для анимации. Например, мы можем ускорить анимацию в начале и замедлить в конце, либо наоборот. Для того, чтобы задать процесс анимации используются кривые Безье. Вообще, `transition-timing-function` позволяет сделать очень много разных поведений для анимаций, это целая тема для статьи, поэтому здесь мы не будем углубляться.

Пример:

```css
transition-timing-function: cubic-bezier(0, 0, 1, 1);
```

**transition-delay** — задаёт задержку времени до начала анимации, можно указывать в секундах или миллисекундах.

Пример:

```css
transition-delay: 500ms;
```

**transition** — это общее свойство, которое позволяет перечислить первые четыре свойства в порядке: `property`, `duration`, `timing-function`, `delay`.

Пример:

```css
transition: background-color 1s cubic-bezier(0, 0, 1, 1) 500ms;
```

У нас получилась вот такая простая анимация: при наведении мышкой на квадрат изменяется ширина; продолжительность анимации одна секунда; анимация воспроизводится по линейной функции; задержка перед началом анимации 500 миллисекунд.

<iframe height="265" scrolling="no" title="Animation CSS" src="https://codepen.io/ruslan_khomiak/embed/eBLPbY/?height=265&amp;theme-id=0&amp;default-tab=css,result&amp;embed-version=2" frameborder="no" allowtransparency="true" allowfullscreen="true" style="width: 732px;"></iframe>

С помощью CSS `transitions` можно анимировать почти все свойства и создавать много интересных, красивых, функциональных и даже сложных анимаций, которые будут дополнять и улучшать ваш проект. Например, вот такой Material-FAB на чистом CSS, используя `transitions`:

<iframe height="376" scrolling="no" title="Material fab Pure CSS" src="https://codepen.io/ruslan_khomiak/embed/QGmwMP/?height=376&amp;theme-id=0&amp;default-tab=css,result&amp;embed-version=2" frameborder="no" allowtransparency="true" allowfullscreen="true" style="width: 732px;"></iframe>

## CSS animations

CSS animations позволяют делать более сложные анимации, нежели CSS transitions. Весь секрет в `@keyframes`. Правило `@keyframes` позволяет создавать анимацию с помощью набора ключевых кадров, то есть описывает состояние объекта в определенный момент времени. Давайте рассмотрим простой пример.

Наш круг ожил и он как будто пульсирует.

<iframe height="265" scrolling="no" title="Circle Pulsing Animated" src="https://codepen.io/ruslan_khomiak/embed/ObooMV/?height=265&amp;theme-id=0&amp;default-tab=css,result&amp;embed-version=2" frameborder="no" allowtransparency="true" allowfullscreen="true" style="width: 732px;"></iframe>

Есть 9 свойств, которые позволяют контролировать CSS animations:

-   `animation-name;`
-   `animation-duration;`
-   `animation-timing-function;`
-   `animation-delay;`
-   `animation-iteration-count;`
-   `animation-direction;`
-   `animation-play-state;`
-   `animation-fill-mode;`
-   `animation;`

**animation-name** — здесь указывается имя анимации, которое связывает правило `@keyframes` с селектором.

Пример:

```css
animation-name: my-animation;
```

```css
@keyframes my-animation {
    0%   { opacity: 0; }
    100% { opacity: 1; }
}
```

**animation-iteration-count** — задаёт количество повторов анимации, значение по умолчанию `1`. Значение `infinite` означает, что анимация будет проигрываться бесконечно.

Пример:

```css
animation-iteration-count: 2;
```

**animation-direction** — задаёт направление анимации.

Пример:

```css
animation-direction: reverse;
```

**animation-play-state** — данное свойство управляет остановкой и проигрыванием анимации. Есть два значения, `running` (анимация проигрывается, по умолчанию) и `paused` (останавливает анимацию).

Пример:

```css
animation-play-state: paused;
```

**animation-fill-mode** — устанавливает, какие CSS-свойства будут приминены к объекту до или после анимации. Может принимать такие значения:

-   `none` — анимируемые CSS-свойства применятся к объекту только во время воспроизведения анимации, по окончании объект возвращается в исходное состояние;
-   `forwards` — анимируемые CSS-свойства применятся к объекту по окончании воспроизведения анимации;
-   `backwards` — анимируемые CSS-свойства применятся к объекту до начала воспроизведения анимации;
-   `both` — анимируемые CSS-свойства применятся к объекту и до начала, и после окончания воспроизведения анимации;

Пример:

```css
animation-fill-mode: backwards;
```

Свойства **animation-duration**, **animation-timing-function**, **animation-delay** работают так же, как аналогичные свойства в CSS `transitions`, о которых я писал раньше, поэтому не буду повторяться.

С помощью animations CSS можно создавать довольно сложные анимации без использования JavaScript. Яркий пример — это лоадеры, то есть элементы, которые показывают, что на вашей страничке что-то загружается. Вот несколько примеров:

<iframe height="254" scrolling="no" title="Loaders Pure CSS" src="https://codepen.io/ruslan_khomiak/embed/MbqWaK/?height=254&amp;theme-id=0&amp;default-tab=css,result&amp;embed-version=2" frameborder="no" allowtransparency="true" allowfullscreen="true" style="width: 732px;"></iframe>

## Motion Path Module

Motion Path Module CSS позволяет создавать движение объектов по контуру через специальное свойство `motion-path`. Раньше такую анимацию можно было сделать только с помощью SVG или сложных скриптов.

В этой спецификаии есть 3 свойства:

-   `motion-path;`
-   `motion-offset;`
-   `motion-rotation;`

**motion-path** — это свойство позволяет указать точки(координаты) по которым будет двигаться объект. Синтаксис такой же как у SVG-атрибута `path`.

Пример:

```css
motion-path: path('M 235,323 Q 412,440 365,615 Q 400,300 670,240 L 870,340 L 975,535 Q 730,600 630,535 z');
```

**motion-offset** — это свойство приводит объект в движение от начальной точки до конечной. Оно принимает либо двойное значение длины, либо проценты. Чтобы объект начал двигаться, нужно определить анимацию, которая будет идти от `0` до `100%`.

Пример:

```css
@keyframes airplane-fly {
    0%   { motion-offset: 0; }
    100% { motion-offset: 100%; }
}
```

**motion-rotation** — это свойство позволяет указать, какой стороной вперед будет двигаться объект. Можно указать `auto`, `reverse` или свое значение в градусах (`'-45deg'`, `'30deg'` и т.д).

Пример:

```css
motion-rotation: auto;
```

<iframe height="600" style="width: 100%;" scrolling="no" title="Motion Path CSS" src="https://codepen.io/ruslan_khomiak/embed/preview/RoMRjR?default-tab=html%2Cresult&editable=true" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/ruslan_khomiak/pen/RoMRjR">
  Motion Path CSS</a> by ruslan_khomiak (<a href="https://codepen.io/ruslan_khomiak">@ruslan_khomiak</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>