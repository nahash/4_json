# Prettify JSON

Вывод содержимого файла в формате json в удобочитаемом виде.

# Quickstart

Example of script launch on Linux, Python 3.5:
Параметр -i/--indent задает отступ при выводе, по умолчанию 2

```#!bash

$ python pprint_json.py <path to file> [ -i 2 ]
...
{
    "Cells": {
      "Name": "Соната-М",
      "PublicPhone": [
        {
          "PublicPhone": "(905) 791-87-13"
        }
      ],
      "IsNetObject": "нет",
      "AdmArea": "Северо-Восточный административный округ",
      "ClarificationOfWorkingHours": null,
      "TypeService": "реализация продовольственных товаров",
      "Address": "Алтуфьевское шоссе, дом 72",
      "geoData": {
        "type": "Point",
        "coordinates": [
          37.58803599964753,
          55.89020100016689
        ]
      },
      "District": "район Бибирево",
      "global_id": 14937274,
      "OperatingCompany": null,
      "WorkingHours": [
        {
          "DayOfWeek": "понедельник",
          "Hours": "09:00-22:00"
        },
        {
          "DayOfWeek": "вторник",
          "Hours": "09:00-22:00"
        },
        {
          "DayOfWeek": "среда",
          "Hours": "09:00-22:00"
        },
        {
          "DayOfWeek": "четверг",
          "Hours": "09:00-22:00"
        },
        {
          "DayOfWeek": "пятница",
          "Hours": "09:00-22:00"
        },
        {
          "DayOfWeek": "суббота",
          "Hours": "09:00-22:00"
        },
        {
          "DayOfWeek": "воскресенье",
          "Hours": "09:00-22:00"
        }
      ]
    },
    "Number": 3,
    "Id": "a16c8154-09d8-4207-8e13-cb8db654e95c"
  }
  ...
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
