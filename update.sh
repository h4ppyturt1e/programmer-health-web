#!/bin/bash

function report_result() {
    # Gets the return value `$?` of the last command and reports success or not
    if [ $? -eq 0 ]; then
        echo -e "Success."
    else
        echo -e "\nSomething went wrong! Bailing..."
        exit 1
    fi
}

# venv
echo -e "\n*** Activating the python virtual environment for this script..."
OS=$(uname -a | cut -c1-5)
report_result
if [[ $OS =~ "Linux" ]]; then
    echo "Making adjustments due to bad choice of operating system"
    source venv/bin/activate
else
    source venv/Scripts/activate
fi
report_result
echo -e "Using: $(which python)"

# pip install
echo -e "\n*** Installing latest Python requirements...\n"
python -m pip install -r requirements.txt
report_result

# remove db
echo -e "\n*** Attempting to delete the old database...\n"
rm src/db.sqlite3
if [ $? -eq 0 ]; then
    echo -e "Found and deleted."
fi
# If file isn't found then attempt to continue anyway, as it might no exist, or maybe was already deleted.

# new db
echo -e "\n*** Attempting to initialize a new database...\n"
python src/manage.py makemigrations
python src/manage.py migrate
report_result

echo -e "\n*** Attempting to populate the database with fake information.\n"
src/manage.py populate_db

# Let the user know that the setup has completed.
echo -e "\nUpdate completed successfully. Have a time!"