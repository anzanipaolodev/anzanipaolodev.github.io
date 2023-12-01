#!/usr/bin/env python3
import argparse
import os
import sys

parser = argparse.ArgumentParser(
    prog='notes')

parser.add_argument('filename')
parser.add_argument('folder')

def update_notes(html_content, filenames, markers=['<!-- BEGIN_NOTES -->', '<!-- END_NOTES -->']):
    start_marker_index = html_content.index(markers[0])
    end_marker_index = html_content.index(markers[1])

    current_list = html_content[start_marker_index+len(markers[0]):end_marker_index]

    new_list = '\n'
    for filename in filenames:
        list_item = f"<li><a href=\"notes/{filename}\">{filename}</a></li>\n"
        new_list += list_item

    updated_html_data = html_content.replace(current_list, new_list)
    return updated_html_data

if __name__ == "__main__":
    args = parser.parse_args()

    filenames = os.listdir(args.folder)

    with open(args.filename, 'r') as f:
        html_data = f.read()
        updated_html = update_notes(html_data, filenames)
        f.close()

    with open(args.filename, 'w') as f:
        f.write(updated_html)
        f.close()

    sys.exit(0)
