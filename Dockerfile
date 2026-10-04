FROM python:3.12-slim
#bnst5dm Python 3.12-slim ka base image w e5trna slim la2naha a5f mn python el kamla
WORKDIR /app
#bn7dd /app ka working directory da5l el container

COPY requirements.txt .
#han3ml copy ll requirements.txt mn build context ll /app gwa el image fa tb2a /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
# Benesabet kol el dependencies el matlooba lel application
# --no-cache-dir beye2allel el malafat el mo2a2ata gheir el daroreya gowa el image

COPY . .
#han3ml copy l ba2y files el project mn host(my laptop) to /app eli hwa container

EXPOSE 8000
#bn3ln el application da5l el container byst5dm port 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
#y3ny docker by2ol ana 5lst build ll image w lma 7d y3ml run ll container 
# abd2 sha8l el app b est5dam el amr dh
# 0.0.0.0 allows Uvicorn to accept connections from outside the container on port 8000.
