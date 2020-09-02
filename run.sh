echo "running on $(python --version) Python version" 
export CWD=$HOME/Bureau/SIN/eatwas-back-end
rm $CWD/db.sqlite3
export SECRET_JWT_KEY=" JWT PASSWORD"
export GREENPEACE_PATH=$CWD/greenpeace.xlsx
export CIQUAL_PATH=$CWD/ciqual.xlsx
export GMAIL_PASSWORD="GMAIL PASSWORD"
export HTML_LOCATION=$CWD/api/templates/

python $CWD/api/main.py

# If you want to run with gunicorn :
# gunicorn main:init_api --bind 0.0.0.0:8080 --worker-class aiohttp.GunicornWebWorker &> $HOME/log
