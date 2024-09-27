#! /usr/bin/sh

for file in $(ls src/*.py | grep -v "__")
do
  file=$(basename "$file" .py)
  echo "traitement : $file"
  python3 -m pydoc "src.$file" | sed -E \
    -e "s/^ {8}([a-zA-Z])/### \1/" \
    -e "s/^ {4}([a-zA-Z])/## \1/" \
    -e "s/^([a-zA-Z])/# \1/" \
    -e "s/^  */ /g" \
    -e "s/^ \|/>/" \
    > "doc/$file.md"
  echo "    $(du -sb doc/$file.md)"
done