#!/usr/bin/python3

with open('demo_file.txt', encoding="utf-8") as f1:
    # f1.read()
    all_lines = f1.readline()
    print(all_lines)
