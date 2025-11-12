import argparse
import os


def check_repository_mode(mode):
    if mode not in ['W', 'R']:
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description="Визуализация графа зависимостей для менеджера пакетов")
    parser.add_argument("--package_name", required=True, help="Имя анализируемого пакета")
    parser.add_argument("--repo_url", required=True,
                        help="URL-адрес репозитория или путь к файлу тестового репозитория")
    parser.add_argument("--repo_mode", required=True, help="Режим работы с тестовым репозиторием (W/R)")
    parser.add_argument("--output_file", required=True, help="Имя сгенерированного файла с изображением графа")
    parser.add_argument("--ascii_tree", action='store_true', help="Режим вывода зависимостей в формате ASCII-дерева")
    parser.add_argument("--filter_substr", help="Подстрока для фильтрации пакетов")


    args = parser.parse_args()

    print("Параметры конфигурации:")
    print(f"Имя пакета: {args.package_name}")
    print(f"URL репозитория или путь к файлу: {args.repo_url}")
    print(f"Режим работы с репозиторием: {args.repo_mode}")
    print(f"Имя файла для изображения графа: {args.output_file}")
    print(f"Режим вывода в формате ASCII-дерева: {'Да' if args.ascii_tree else 'Нет'}")
    if args.filter_substr:
        print(f"Подстрока для фильтрации пакетов: {args.filter_substr}")
    else:
        print("Подстрока для фильтрации пакетов: Не задана")

    if not check_repository_mode(args.repo_mode):
        print("Ошибка: Некорректный режим работы с репозиторием")
        return

    if not os.path.exists(args.repo_url):
        print(f"Ошибка: Неверный путь или URL репозитория: {args.repo_url}")
        return

    print("Конфигурация успешно загружена!")


if __name__ == "__main__":
    main()
