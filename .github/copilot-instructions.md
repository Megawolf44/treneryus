# Copilot Instructions for obumov_python

## Что это за проект
Учебный репозиторий с небольшими, самодостаточными Python-скриптами — каждая программа это «урок»: краткая теория в начале файла (тройная строка), затем наглядные примеры и демонстрации (часто с `input()`). В каталоге `avtokliker/` находятся Windows-специфичные примеры автоматизации (см. `avtokliker/.github/copilot-instructions.md`).

## Большая картина (Why) 🔍
- Цель: понятная демонстрация базовых концептов Python (типы, списки, циклы, словари) через читаемые, запускаемые примеры.
- Структура: набор отдельных файлов-уроков (например `lesson.py`, `lists.py`, `cikl.py`, `struc_dann.py`, `slov_funkc.py`, `povtorenie_1go_modul.py`) и один вспомогательный подмодуль `avtokliker/`.

## Что нужно знать сразу (Key patterns) ✅
- Локаль/язык: **все комментарии, docstring и пользовательские переменные должны быть на русском**.
- Header: теория размещается в начале файла в тройной строке `'''...'''` — объяснить «почему» до кода.
- Примеры: рабочие примеры часто делаются как демонстрации; показывайте вызов и результат (`a.append(1)` → `print(a)`).
- Уровни примеров: для контрольных структур предпочитают 3 уровня сложности (Simple / Medium / Complex).
- Импортируемые функции: оборачивайте демонстрации в `if __name__ == '__main__'`.

## Запуск, зависимости и отладка 🛠️
- Запуск: `python <file>.py` (Windows: PowerShell recommended). Многие файлы используют `input()` — для CI добавьте альтернативный non-interactive пример.
- Зависимости: верхний уровень репозитория не требует внешних пакетов. `avtokliker/` использует `ahk` (указано в `avtokliker/.github/copilot-instructions.md`) — create/activate `.venv` and `pip install ahk` or `ahk[binary]`.
- Тесты: нет глобальной тестовой базы. Если добавляете тесты, use `pytest`, place them under `tests/`, and skip Windows-only automation tests with markers (e.g. `@pytest.mark.skipif(os.name != 'nt', reason='Windows only')`).

## Integration points & gotchas ⚠️
- `avtokliker/` interacts with OS input devices — automation moves cursor, registers hotkeys, may need elevated rights; always add `--dry-run`/`--simulate` and clear safety notes when adding examples.
- Avoid destructive examples (broad `taskkill` usage). Preserve explicit safety comments found in `avtokliker/klicer.py` and `.venv/example.py`.
- Preserve Russian comments and non-ASCII text when editing files — they are intentional teaching artifacts.

## Files to inspect first 📁
- `lesson.py`, `lists.py`, `cikl.py`, `struc_dann.py`, `slov_funkc.py`, `povtorenie_1go_modul.py` — canonical lesson patterns.
- `avtokliker/klicer.py` and `avtokliker/.venv/example.py` — Windows automation demos and safety patterns.
- `avtokliker/.github/copilot-instructions.md` — project-specific automation guidance.

## PR checklist (short) ✅
- Комментарии и docstrings на русском
- В header присутствует тройная теоретическая строка
- Демонстрации показывают явный `print()`-вывод
- Для демонстраций добавлен `if __name__ == '__main__'` блок при добавлении импортируемых функций
- Не сломать существующие интерактивные примеры; предпочитайте добавить новый файл, а не массово рефакторить
- Для изменений, затрагивающих платформу/зависимости: указать шаги установки и требуемые права в PR
- Для автоматизации: добавить `--dry-run`/`--simulate`, документировать риск

---

Если что-то неясно (например, нужен формат примера для автоматизированного теста или предпочтение оформления), скажите — уточню и допишу инструкцию.
