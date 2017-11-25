import csv
import os
import sys

IDX_CSVFILE = 1
IDX_FILENAME = 0
IDX_CONTENT = 1
IDX_TAB_TRIGGER = 2
IDX_SCOPE = 3
VALID_NUM_OF_ARGS = 2
VALID_NUM_OF_COLUMNS = 4


def generate_snippet_from_csv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    header = next(reader) # ヘッダーのスキップ
    for row in reader:
        if len(row) != VALID_NUM_OF_COLUMNS:
            print('error: wrong format csv file')
            sys.exit()

        write_down(row[IDX_FILENAME], row[IDX_CONTENT], row[IDX_TAB_TRIGGER], row[IDX_SCOPE])
    f.close()


def write_down(filename, content, tab_trigger, scope):
    sublime_snippet_path = os.getenv('SUBLIME_SNIPPET_PATH', '')
    if sublime_snippet_path == '': # 実行前に環境変数「SUBLIME_SNIPPET_PATH」の設定が必要
        print('error: set environment variable "SUBLIME_SNIPPET_PATH"')
        sys.exit()

    suffix = '.sublime-snippet'
    f = open(sublime_snippet_path + filename + suffix, 'w')
    f.write(f'<snippet>\n\
    <content><![CDATA[\n\
{content}\n\
]]></content>\n\
    <tabTrigger>{tab_trigger}</tabTrigger>\n\
    <scope>source.{scope}</scope>\n\
</snippet>')
    f.close()


if __name__ == '__main__':
    args = sys.argv
    if len(args) == VALID_NUM_OF_ARGS:
        generate_snippet_from_csv(args[IDX_CSVFILE])
    else:
        print('usage: python sublime_snippet_generator.py [csv]')
