# # Python image
# FROM python:3.10-slim

# # RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*
# # working directory
# WORKDIR /app

# # Copy project files
# COPY . .

# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # COPY wait-for-it.sh /wait-for-it.sh
# # RUN chmod +x /wait-for-it.sh
# COPY wait-for-it.sh /usr/local/bin/wait-for-it
# RUN chmod +x /usr/local/bin/wait-for-it

# # Expose Flask port
# EXPOSE 5000

# # command to run the app
# CMD ["python", "run.py"]



FROM python:3.10.11

# Set working directory
WORKDIR /product_store

# Copy application files
COPY ./app/ ./app/
COPY run.py .
COPY wait-for-it.sh /usr/local/bin/wait-for-it
RUN chmod +x /usr/local/bin/wait-for-it

# Install application dependencies
RUN pip install --no-cache-dir -r app/requirements.txt

# Add and set permissions for wait-for-it script

# Expose application port
EXPOSE 5000

ENV DATABASE_URL=mysql+pymysql://brad:brad_steve@db:3306/product_store

# Use CMD to run the application
#CMD ["python", "run.py", "--host=0.0.0.0"]
CMD ["sh", "-c", "wait-for-it db:3306 -- python run.py"]

# To run with env var
# docker run -d -p 5000:5000 \
#   -e DATABASE_URL="mysql+pymysql://brad:brad_steve@db:3306/product_store" \
#   bradesteve/product-store-backend





