---
weight: 1
title: Оформление текста
description: Оформление текста при помощи CSS
author: MLabs
authorLink: null
date: 2023-09-06T14:48:57.920Z
lastmod: null
slug: text_style
categories:
  - WEB
math: true
lightgallery: true
toc:
  auto: false
draft: false
---

У любого текстового элемента есть свои стили по умолчанию. Заголовки крупные и жирные, текст в абзацах нормального размера и начертания, а ссылки обычно синие и подчёркнутые снизу.

Каждый из этих элементов можно стилизовать по-своему, например, поменять размер, начертание или цвет. Давайте посмотрим, как это сделать.

## Сменить шрифт

Чтобы изменить шрифт элемента, используйте CSS-свойство `font-family`:

```css
body {
  font-family: 'Roboto', Arial, sans-serif;
}
```

Первым указывается шрифт, который вы хотите добавить. После него через запятую идут альтернативные шрифты. Например, если на компьютере у посетителя сайта не установлен шрифт Roboto, браузер использует шрифт Arial.

## Изменить цвет и размер текста

Цвет текста задаётся с помощью свойства [`color`](https://htmlacademy.ru/blog/css/color). Оно принимает значения в различных форматах: можно написать название цвета (`red`, `blue`), шестнадцатеричное значение (`#ff0000`, `#00f`) или функцию `rgb()`, чтобы задать [цвет](https://htmlacademy.ru/blog/css/color-formats) с помощью трёх чисел.

```css
p {
  color: red; /* Красный с помощью слов */
  color: #ff0000; /* Красный с помощью HEX */
  color: rgb(1.0,0.0,0.0); /* Красный с помощью rgb() */
}
```

Размер текста меняется свойством `font-size`. Оно принимает значения в пикселях (`px`), процентах (`%`) и других единицах измерения.

```css
h1 {
  font-size: 24px;
}
```

<iframe allowfullscreen="true" allowpaymentrequest="true" allowtransparency="true" class="cp_embed_iframe " frameborder="0" height="300" width="100%" name="cp_embed_1" scrolling="no" src="https://codepen.io/feizerr/embed/ZEqVWay?height=300&amp;theme-id=light&amp;default-tab=css%2Cresult&amp;slug-hash=ZEqVWay&amp;editable=true&amp;user=feizerr&amp;name=cp_embed_1" title="CodePen Embed" loading="lazy" id="cp_embed_ZEqVWay" style="box-sizing: inherit; overflow: hidden; display: block;"></iframe>

## Добавить жирность

Свойство `font-weight` задаёт жирность текста. Оно принимает два вида значений.

**Численные:** от `100` до `900`. Например, `400` — обычный шрифт, а `700` — полужирный.

**Ключевые слова:** `normal` — обычный шрифт, `bold` — полужирный, `bolder` — жирнее, чем текущий, `lighter` — менее жирный шрифт по сравнению с текущим.

```css
p {
  font-weight: bold; /* Полужирный с помощью ключевого слова */
  font-weight: 700; /* Полужирный с помощью численного значения */
}
```

<iframe allowfullscreen="true" allowpaymentrequest="true" allowtransparency="true" class="cp_embed_iframe " frameborder="0" height="300" width="100%" name="cp_embed_2" scrolling="no" src="https://codepen.io/feizerr/embed/Jjmwrrv?height=300&amp;theme-id=light&amp;default-tab=css%2Cresult&amp;slug-hash=Jjmwrrv&amp;editable=true&amp;user=feizerr&amp;name=cp_embed_2" title="CodePen Embed" loading="lazy" id="cp_embed_Jjmwrrv" style="box-sizing: inherit; overflow: hidden; display: block;"></iframe>

## Сделать текст курсивным

Для этого есть свойство `font-style`. По умолчанию у него стоит значение `normal`, то есть текст обычный, без курсива. Чтобы поменять начертание, используйте:

- `italic` — делает текст курсивным;
- `oblique` — делает текст наклонным.

```css
p {
  font-style: italic;
}
```

Оба значения создают похожий эффект — текст выглядит курсивным, но есть и разница. Если очень упростить, то `italic` и `oblique` немного отличаются в начертании. А ещё не у всех шрифтов есть специальная курсивная версия. В таких случаях `oblique` делает текст похожим на курсив.

<iframe allowfullscreen="true" allowpaymentrequest="true" allowtransparency="true" class="cp_embed_iframe " frameborder="0" height="300" width="100%" name="cp_embed_3" scrolling="no" src="https://codepen.io/feizerr/embed/eYPbGVE?height=300&amp;theme-id=light&amp;default-tab=css%2Cresult&amp;slug-hash=eYPbGVE&amp;editable=true&amp;user=feizerr&amp;name=cp_embed_3" title="CodePen Embed" loading="lazy" id="cp_embed_eYPbGVE" style="box-sizing: inherit; overflow: hidden; display: block;"></iframe>

## Преобразовать текст

Свойство `text-transform` меняет регистр текста. Оно принимает значения:

- `none` — без изменений, значение по умолчанию;
- `uppercase` — все буквы становятся прописными;
- `lowercase` — все буквы становятся строчными;
- `capitalize` — первая буква каждого слова находится в верхнем регистре.

```css
p {
  text-transform: uppercase;
}
```

<iframe allowfullscreen="true" allowpaymentrequest="true" allowtransparency="true" class="cp_embed_iframe " frameborder="0" height="300" width="100%" name="cp_embed_4" scrolling="no" src="https://codepen.io/feizerr/embed/LYgMzmJ?height=300&amp;theme-id=light&amp;default-tab=css%2Cresult&amp;slug-hash=LYgMzmJ&amp;editable=true&amp;user=feizerr&amp;name=cp_embed_4" title="CodePen Embed" loading="lazy" id="cp_embed_LYgMzmJ" style="box-sizing: inherit; overflow: hidden; display: block;"></iframe>

## Добавить подчёркивание

Свойство [`text-decoration`](https://htmlacademy.ru/blog/css/text-decoration) добавляет тексту декоративные эффекты:

- `overline` создаёт линию над текстом,
- `line-through` делает текст зачёркнутым,
- `underline` добавляет подчёркивание.

```css
p {
  text-decoration: overline;
}
```

По умолчанию у свойства стоит значение `none` — без оформления.

<iframe allowfullscreen="true" allowpaymentrequest="true" allowtransparency="true" class="cp_embed_iframe " frameborder="0" height="300" width="100%" name="cp_embed_5" scrolling="no" src="https://codepen.io/feizerr/embed/QWZzqBK?height=300&amp;theme-id=light&amp;default-tab=css%2Cresult&amp;slug-hash=QWZzqBK&amp;editable=true&amp;user=feizerr&amp;name=cp_embed_5" title="CodePen Embed" loading="lazy" id="cp_embed_QWZzqBK" style="box-sizing: inherit; overflow: hidden; display: block;"></iframe>

## Создать тень

Свойство `text-shadow` добавляет тексту тень. Оно принимает значение в таком формате:

```css
text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5)
/*смещение по горизонтали, смещение по вертикали, радиус размытия, цвет тени */
```

<iframe allowfullscreen="true" allowpaymentrequest="true" allowtransparency="true" class="cp_embed_iframe " frameborder="0" height="300" width="100%" name="cp_embed_6" scrolling="no" src="https://codepen.io/feizerr/embed/yLRGzxb?height=300&amp;theme-id=light&amp;default-tab=css%2Cresult&amp;slug-hash=yLRGzxb&amp;editable=true&amp;user=feizerr&amp;name=cp_embed_6" title="CodePen Embed" loading="lazy" id="cp_embed_yLRGzxb" style="box-sizing: inherit; overflow: hidden; display: block;"></iframe>

## Выровнять текст

Свойство `text-align` выравнивает текст по горизонтали. Оно принимает значения:

- `left` — влево;
- `right` — вправо;
- `center` — по центру;
- `justify` — выравнивание по ширине.

<iframe allowfullscreen="true" allowpaymentrequest="true" allowtransparency="true" class="cp_embed_iframe " frameborder="0" height="300" width="100%" name="cp_embed_7" scrolling="no" src="https://codepen.io/feizerr/embed/MWPZELv?height=300&amp;theme-id=light&amp;default-tab=css%2Cresult&amp;slug-hash=MWPZELv&amp;editable=true&amp;user=feizerr&amp;name=cp_embed_7" title="CodePen Embed" loading="lazy" id="cp_embed_MWPZELv" style="box-sizing: inherit; overflow: hidden; display: block;"></iframe>

## Изменить высоту строки и межбуквенное расстояние

Свойство `line-height` устанавливает высоту строки, указывая множитель относительно размера шрифта. Свойство `letter-spacing` управляет расстоянием между символами.

```css
p {
  line-height: 1.5;
  letter-spacing: 2px;
}
```

<iframe allowfullscreen="true" allowpaymentrequest="true" allowtransparency="true" class="cp_embed_iframe " frameborder="0" height="300" width="100%" name="cp_embed_8" scrolling="no" src="https://codepen.io/feizerr/embed/ExdGwzp?height=300&amp;theme-id=light&amp;default-tab=css%2Cresult&amp;slug-hash=ExdGwzp&amp;editable=true&amp;user=feizerr&amp;name=cp_embed_8" title="CodePen Embed" loading="lazy" id="cp_embed_ExdGwzp" style="box-sizing: inherit; overflow: hidden; display: block;"></iframe>

## Нюансы

- У некоторых шрифтов нет жирного и курсивного варианта.
- Свойство `text-shadow` делает текст эффектным, но слишком насыщенные тени могут усложнить чтение текста или создать плохой контраст.
- Слишком большое или маленькое значение `line-height` и `letter-spacing` может нарушить интервалы между буквами и строками.
- При изменении размера шрифта (`font-size`) следует учитывать, что очень мелкий и крупный текст может плохо отображаться или стать нечитабельным.

## Рекомендации

**Тестируйте вёрстку**. Проверяйте, как шрифты отображаются на разных устройствах и браузерах. Некоторые шрифты могут отображаться по-разному на разных платформах.

**Используйте стили осторожно**. Смена регистра, курсив и жирный текст помогают выделить важный контент, расставляют акценты в тексте. Используйте их умеренно, потому что крупные фрагменты текста, написанного капсом или курсивом, лишь отвлекают пользователя. Акценты теряются, и текст выглядит неаккуратно.

**Помните о доступности**. Используйте подходящие значения `font-weight` — слишком мелкий или крупный текст плохо читается. Подбирайте контрастные цвета для текстов.

**Используйте несколько шрифтов**. Некоторые шрифты могут быть недоступны, поэтому важно указывать альтернативные варианты.

**Соблюдайте авторское право**. У каждого шрифта есть лицензия, которая описывает, в каких случаях можно использовать шрифт, а в каких нельзя. Например, какие-то варианты нельзя использовать в коммерческих проектах, а какие-то предназначены только для веба или печати. Поэтому нужно внимательно читать лицензию перед загрузкой понравившегося шрифта — вдруг он не подходит под ваши цели.