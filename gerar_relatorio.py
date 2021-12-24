import os


def main():
    os.system('jupyter nbconvert --execute --to pdf --no-input DataScience\Kapitalo\Relatório.ipynb')

if __name__ == '__main__':
    main()