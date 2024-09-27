#! /usr/bin/sh

python3 -m unittest discover src/tests

if [ $? -ne 0 ]
then
    echo "IS_BETA=true" >> "$GITHUB_ENV"
    echo "Tests echoués, ce sera une version BETA"
fi

exit 0