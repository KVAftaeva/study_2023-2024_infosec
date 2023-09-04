---
## Front matter
title: "Отчет по лабораторной работе №1"
subtitle: "Дисциплина: Математическое моделирование"
author: "Выполнила: Афтаева Ксения Васильевна"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Создание репозитория курса на github.com на основе шаблона. Установка необходимого ПО. Ознакомление с основными возможностями разметки Markdown. Написание отчета с использованием Markdown.

# Задание

1. Создать репозиторий курса на github.com на основе шаблона и соглашений о наименовании, описанных на странице курса.
2. Установить необходимые для дальнейшей работы программы (pandoc, texlive и т.д.).
3. Написать отчет с использованием Markdown.

# Теоретическое введение
В ходе данного курса мы будем работать с **репозиторием** и выгружать результаты своей работы на github. **Репозиторий или проект GIT** включает в себя полный набор файлов и папок, связанных с проектом, а также журнал изменений каждого файла. Журнал файла представлен в виде моментальных снимков на определенные моменты времени. Эти снимки называются фиксациями. Фиксации можно упорядочивать по нескольким линиям разработки, называемым ветвями. Так как GIT — распределенная система управления версиями, репозитории являются автономными единицами и любой пользователь, имеющий копию репозитория, может получать доступ ко всей базе кода и ее истории. С помощью командной строки или других удобных интерфейсов возможны также следующие действия с репозиторием GIT: взаимодействие с журналом, клонирование репозитория, создание ветвей, фиксация, слияние, сравнение изменений в разных версиях кода и многое другое [@key-2].

Для выполнения отчетов в данном курсе мы будем использовать **Markdown** — это облегченный язык разметки с синтаксисом форматирования обычного текста. Несмотря на то, что файлы с разметкой Markdown имеют собственный формат .md или .markdown, они содержат только текст и могут создаваться в любых программах типа Блокнот.  Однако, его можно без проблем конвертировать и в гипертекст, и даже в документ с визуальным оформлением (RTF или DOC) без потери форматирования [@key-3].

В данном отчете я также использую выделение текста, которое **Markdown** позволяет довольно легко сделать. Например, для выделения слова курсивом нужно с обеих сторон обрамить текст символами "*" или "_". Для выделения жирным необходимо поставить по два таких символа с каждой стороны. 

# Выполнение лабораторной работы



# Выводы

Я создала репозиторий курса на github.com на основе шаблона. Установила необходимое ПО. Ознакомилась с основными возможностями разметки Markdown. Написала отчет с использованием Markdown.

# Список литературы{.unnumbered}

::: {#refs}
:::
